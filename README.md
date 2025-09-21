# Discounted Cash Flow (DCF) Analysis with Monte Carlo Simulations

## Overview
This project created in Python, was built on the concept of discounted cash flows I learned in managerial accounting. The model takes inputs about the details of a potential investment, then calculates the discounted cash flow along with the return for the next best option (opportunity cost of capital) and compares them using the Net Present Value technique. Also, a Monte Carlo simulation is generated to analyze the range of outcomes, making the model more usable in real-world conditions with fluctuating inputs.

---

## Key Features
- **DCF Calculation**: Takes cash flows and growth or decline of cash flows, calculates the discounted cash flow for the investment and compares it to the opportunity cost of capital.
- **Monte Carlo Simulation**: Models thousands of potential scenarios for cash flow growth and discount rates to get a range of possible outcomes more realistic to real-world applications.
- **Visualizations**:
  - Comparison of DCF vs. opportunity cost.
  - Histograms and charts of NPV distributions for the Monte Carlo simulation.
  - Mean and likelihood of investment having a positive NPV.
- **User Input**: A GUI built with Tkinter allows customization of key inputs like initial investment, discount rate, and cash flow growth.

---

## Skills Demonstrated
- **Python Programming**: Data manipulation with Pandas and Numpy, visualization with Matplotlib, and GUI creation with Tkinter.
- **Financial Modeling**: Application of DCF and Monte Carlo simulations to analyze investment risks and returns.
- **Data Visualization**: Clear and actionable charts for decision-making.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib
- **GUI Framework**: Tkinter

---

## Example
- **Potential Investment**: Say you're considering an investment of $100,000 that will last 15 periods with cash flows of $12,000 per period that will grow at 10% per period. The next best option may be a risk-free interest rate of 5%. When this is plotted using the program created, we see the investment will outperform the risk-free rate over the 15 periods. The NPV (Investment - Discount rate) = $134345.85
- **Monte Carlo**: When we generate the Monte Carlo simulation for this investment, we see the NPV will be positive in about 71% of situations. In accounting, we are taught that a positive NPV means an investment makes sense. So Monte Carlo helps us analyze a range of possible outcomes to see the likelihood of different possibilities. 

---

## How to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Killy-H/Discounted-Cash-Flow-Analysis.git
   cd Discounted-Cash-Flow-Analysis
