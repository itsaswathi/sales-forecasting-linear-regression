
# 📊 Sales Forecasting with Linear Regression

This project demonstrates how to forecast future daily revenue using **Linear Regression**, a fundamental machine learning technique. The project includes data preprocessing, model training, accuracy evaluation, and visual forecasting.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `sales_data.csv` | Simulated sample dataset of daily revenue |
| `forecast_model.py` | Python script for model training, evaluation, and forecasting |
| `forecast_output.png` | Graph comparing actual, predicted, and future forecasted sales |
| `forecast_table.csv` | Predicted revenue for the next 30 days |
| `README.md` | Project overview and explanations (this file) |

---

## 🔧 Project Workflow

1. **Data Preparation**  
   - Reads daily revenue data from `sales_data.csv`
   - Fills missing values (if any) using forward fill
   - Converts dates into numerical format (days since start) for modeling

2. **Modeling with Linear Regression**  
   - Trains a `LinearRegression` model to learn the trend in daily sales
   - Predicts both historical values and forecasts the next 30 days

3. **Model Evaluation**  
   - Evaluates accuracy using three metrics:
     - R² Score: Proportion of variance explained by the model
     - RMSE: Root Mean Squared Error (average prediction error)
     - MAE: Mean Absolute Error (average absolute difference)
   - These are printed directly when the script is run

4. **Visualization**  
   - Plots:
     - Actual sales (blue line)
     - Model's fitted values (orange dashed line)
     - Forecast for next 30 days (green dashed line)

---

## 📈 Output Graph

![Forecast Output](forecast_output.png)

This graph helps visualize how well the model fits the actual data and how it extends into the future.

---

## 📊 Evaluation Metrics (Printed on Run)

| Metric | Description |
|--------|-------------|
| **R² Score** | Indicates how well the model explains the variability in revenue |
| **RMSE** | Measures how far predictions deviate from actual values |
| **MAE** | Measures the average magnitude of errors in predictions |

> Sample output (based on this dataset):  
> R² Score: ~0.94  
> RMSE: ~240  
> MAE: ~180  

---

## 🤔 Why Actual ≠ Predicted?

- **Linear Regression is a simple model** — it fits a straight line through the data.
- **Sales data is often noisy** with irregular spikes, seasonality, and promotions.
- The model learns a general **trend**, not the fluctuations.
- Differences are expected and natural.

> ✅ The key is understanding these differences and evaluating them with metrics, not assuming perfect predictions.

---

## 💡 Suggestions for Improvement

- Use **Polynomial Regression** for non-linear trends
- Try **ARIMA, SARIMA, or Prophet** for time-series modeling with seasonality
- Include external factors like promotions, holidays, or day-of-week

---

## ▶️ How to Run

```bash
pip install pandas numpy matplotlib scikit-learn
python forecast_model.py
```

---

## 🏁 Conclusion

This project is a great starting point for understanding sales forecasting. While it uses a simple model, it lays the foundation for more advanced time-series techniques.

Feel free to ⭐ the repo if you find it useful!
