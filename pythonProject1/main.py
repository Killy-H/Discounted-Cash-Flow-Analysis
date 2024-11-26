from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.options.display.float_format = '{:,.2f}'.format

def plot_dcf_vs_oppcost():

    initiat_investment = int(initial_investment_entry.get())
    expected_cash_flow = int(initial_cashflow_entry.get())
    growth_rate = float(cash_flow_growth_entry.get())
    discount_rate = float(discount_rate_entry.get())
    periods = int(periods_entry.get())

    investment_df = pd.DataFrame({"Periods": pd.Series(range(periods + 1)),
                           "Cash_Flows": [0] + [expected_cash_flow * (1 + growth_rate) ** period for period in pd.Series(range(periods))],
                           "Capital_Oppertunity_Cost": [initiat_investment * (1 + discount_rate) ** period for period in pd.Series(range(periods + 1))],
                           })

    dcf_val = 0
    dcf_list = []
    for index, row in investment_df.iterrows():
        period = row["Periods"]
        cash_flow = row["Cash_Flows"]
        dcf_list.append(cash_flow / (1 + discount_rate) ** period)
        dcf_val += cash_flow / (1 + discount_rate) ** period
    investment_df["DCF"] = np.array(dcf_list).cumsum() + initiat_investment

    investment_df["Net_Present_Value"] = investment_df["DCF"] - investment_df["Capital_Oppertunity_Cost"]

    final_dcf = "{:.2f}".format(investment_df["DCF"].iloc[-1])
    final_oppcost = "{:.2f}".format(investment_df["Capital_Oppertunity_Cost"].iloc[-1])
    final_npv = "{:.2f}".format(investment_df["Net_Present_Value"].iloc[-1])

    plt.figure(figsize=(10, 8), dpi=120)
    plt.title(f"Investment Cash Flow vs Opportunity Cost After {periods} Periods")
    plt.xlabel("Periods", fontsize=12)
    plt.ylabel("Total Investment Value", fontsize=12)

    bar_colors = np.where(investment_df["Net_Present_Value"] >= 0.001, "green", "red")
    if (investment_df["Net_Present_Value"] > 0).any():
        #npv_positive = investment_df[investment_df["Net_Present_Value"] > 0]["Periods"].iloc[0]
        positive_periods = investment_df[investment_df["Net_Present_Value"] > 0]["Periods"]
        positive_npvs = investment_df[investment_df["Net_Present_Value"] > 0]["DCF"]
        positive_oppcost = investment_df[investment_df["Net_Present_Value"] > 0]["Capital_Oppertunity_Cost"]


    ax = plt.gca()

    ax.plot(investment_df["Periods"], investment_df["DCF"], marker="o", color="blue", label="Investment ROR")
    ax.plot(investment_df["Periods"], investment_df["Capital_Oppertunity_Cost"], color="red", label="Oppertunity Cost of Capital")
    ax.axhline(initiat_investment, color="green", linestyle="dashed", label="Initial Investment")
    ax.bar(investment_df["Periods"], investment_df["Net_Present_Value"], color=bar_colors, label="Net Present Value", alpha=0.7)
    if (investment_df["Net_Present_Value"] >= 0.001).any():
        #ax.axvline(npv_positive, color="black", linestyle="dashed", label="NPV Positive = Investment Makes Sense")
        ax.fill_between(positive_periods, positive_npvs, positive_oppcost, color="grey", alpha=0.5, label="Additional Return Above Baseline")

    plt.text(8, -0.5, f"DCF After {periods} Periods: {final_dcf}\nNPV After {periods} Periods: {final_npv}\nOppertunity Cost After {periods} Periods: {final_oppcost}",
             fontsize=12, color="black", va="center", bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))

    plt.legend()
    plt.show()


def gen_monte_carlo():
    initiat_investment = int(initial_investment_entry.get())
    expected_cash_flow = int(initial_cashflow_entry.get())
    growth_rate = float(cash_flow_growth_entry.get())
    discount_rate = float(discount_rate_entry.get())
    periods = int(periods_entry.get())
    stdev = float(stdev_entry.get())


    varied_growth_rate = np.random.normal(loc=growth_rate, scale=stdev, size=1000)
    varied_discount_rate = np.random.normal(loc=discount_rate, scale=stdev, size=1000)
    varied_inital_cashflow = np.random.normal(loc=expected_cash_flow, scale=stdev, size=1000)

    varied_investment_df = pd.DataFrame({
         "Discounted_Cash_Flows": [initiat_investment + sum(
          varied_inital_cashflow[i] * (1 + varied_growth_rate[i]) ** period / (1 + varied_discount_rate[i]) ** period for period in range(1, periods + 1)) for i in range(1000)],
            "Oppertunity_Cost": [initiat_investment * (1 + varied_discount_rate[i]) ** periods for i in range(1000)]
        })

    varied_investment_df["Net_Present_Value"] = varied_investment_df["Discounted_Cash_Flows"] - \
                                                varied_investment_df["Oppertunity_Cost"]


    npv = varied_investment_df["Net_Present_Value"]

    npv_positive = varied_investment_df[varied_investment_df["Net_Present_Value"] >= 0].index[0]
    npv_mean = varied_investment_df["Net_Present_Value"].mean()
    npv_mean_index = varied_investment_df.iloc[(varied_investment_df["Net_Present_Value"] - npv_mean).abs().idxmin()].iloc[-1]
    positive_percent = len(varied_investment_df[varied_investment_df["Net_Present_Value"] >= 0]) / len(varied_investment_df["Net_Present_Value"])

    plt.figure(figsize=(10, 8), dpi=120)
    plt.title("Distribution of NPV")
    plt.xlabel("NPV", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)

    ax = plt.gca()

    ax.hist(x=npv, bins=30, edgecolor="black")
    ax.axvline(npv_positive, color="green", linestyle="dashed",
               label=f"NPV Positive = Investment Makes Sense\nNPV Positive in {'{:.2f}'.format(100 * positive_percent)}% of Simulations")
    ax.axvline(npv_mean_index, color="red", linestyle="dashed", label=f"NPV Mean: {'{:.2f}'.format(npv_mean)}")

    plt.legend()
    plt.show()



window = Tk()
window.title("Investment Details")
window.config(padx=25, pady=25)

canvas = Canvas(width=200, height=10)
canvas.grid(column=1, row=0)

initial_investment = Label(text="Initial Investment:")
initial_investment.grid(column=0, row=1)
initial_investment_entry = Entry(width=21)
initial_investment_entry.grid(column=1, row=1)

initial_cashflow = Label(text="Initial Cash Flow:")
initial_cashflow.grid(column=0, row=2)
initial_cashflow_entry = Entry(width=21)
initial_cashflow_entry.grid(column=1, row=2)

cash_flow_growth = Label(text="Cash Flow Growth or Decline Rate:")
cash_flow_growth.grid(column=0, row=3)
cash_flow_growth_entry = Entry(width=21)
cash_flow_growth_entry.grid(column=1, row=3)

discount_rate = Label(text="Discount Rate:")
discount_rate.grid(column=0, row=4)
discount_rate_entry = Entry(width=21)
discount_rate_entry.grid(column=1, row=4)

periods = Label(text="Periods:")
periods.grid(column=0, row=5)
periods_entry = Entry(width=21)
periods_entry.grid(column=1, row=5)

stdev = Label(text="Stdev for MC Simulation:")
stdev.grid(column=0, row=6)
stdev_entry = Entry(width=21)
stdev_entry.grid(column=1, row=6)

dcf_vs_opp = Button(text="Plot DCF vs Opportunity Cost", command=plot_dcf_vs_oppcost)
dcf_vs_opp.grid(column=0, row=7, columnspan=2)

monte_carlo = Button(text="Generate NPV Monte Carlo Simulation", command=gen_monte_carlo)
monte_carlo.grid(column=0, row=8, columnspan=2)

window.mainloop()
