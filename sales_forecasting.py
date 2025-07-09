import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

df = pd.read_csv('sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df_daily = df.groupby('date')['revenue'].sum().reset_index()
df_daily['revenue'] = df_daily['revenue'].fillna(method='ffill')
df_daily = df_daily.sort_values('date')
df_daily['days'] = (df_daily['date'] - df_daily['date'].min()).dt.days

X = df_daily[['days']]
y = df_daily['revenue']
model = LinearRegression()
model.fit(X, y)

future_days = 30
last_day = df_daily['days'].max()
future_X = pd.DataFrame({'days': np.arange(last_day + 1, last_day + future_days + 1)})
future_pred = model.predict(future_X)

start_future = df_daily['date'].max() + timedelta(days=1)
future_dates = [start_future + timedelta(days=i) for i in range(future_days)]

plt.figure(figsize=(12, 6))
plt.plot(df_daily['date'], y, label='Actual Sales')
plt.plot(future_dates, future_pred, label='Predicted Sales', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.title('Sales Forecasting with Linear Regression')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('forecast_output.png')
plt.show()

forecast_df = pd.DataFrame({
    'Date': future_dates,
    'Predicted Revenue': future_pred.round(2)
})
forecast_df.to_csv('forecast_table.csv', index=False)