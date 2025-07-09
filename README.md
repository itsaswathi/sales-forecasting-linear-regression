# 📈 Sales Forecasting with Linear Regression

## 🧠 Problem Statement
Businesses often struggle to estimate future sales based on historical performance. This project solves that problem using a Linear Regression model to forecast upcoming sales revenue.

---

## 🎯 Objective
To build a machine learning model using historical sales data to predict future revenue, and to visualize the results both graphically and in tabular form.

---

## 📁 Dataset
- **File**: `sales_data.csv`
- **Columns**:
  - `date`: Date of the transaction
  - `product`: Product name
  - `quantity`: Number of units sold
  - `revenue`: Total revenue from the sale

---

## 📦 Requirements

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## 🚀 How to Run

1. Clone this repository or download the ZIP.
2. Place `sales_data.csv` in the same directory as the Python script.
3. Run the script:

```bash
python sales_forecasting.py
```

4. The script will generate:
   - 📊 `forecast_output.png`: A plot of actual vs predicted sales
   - 📄 `forecast_table.csv`: Forecasted sales for the next 30 days

---

## 📊 Output Preview

### 📈 Forecast Plot:
![Sales Forecast](forecast_output.png)

### 🧾 Sample Forecast Table:

| Date       | Predicted Revenue |
|------------|-------------------|
| 2023-06-30 | 1069.17           |
| 2023-07-01 | 1068.93           |
| 2023-07-02 | 1068.69           |
| ...        | ...               |

---

## 👩‍💻 Author
**Aswathi C D**  
Submitted as part of academic project requirements.

---

## 📬 Contact
For feedback or queries, reach me at:  
📧 aswathi.cd@example.com