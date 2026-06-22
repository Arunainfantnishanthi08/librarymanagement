import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
stock = "AAPL"
data = yf.download(stock, period="6mo")

# Fix multi-index issue (VERY IMPORTANT)
data.columns = data.columns.get_level_values(0)

# Drop missing values
data = data.dropna()

# Ensure numeric
for col in ["Open", "High", "Low", "Close", "Volume"]:
    data[col] = pd.to_numeric(data[col], errors="coerce")

data = data.dropna()

# FEATURES (MUST BE 2D)
X = data[["Open", "High", "Low", "Volume"]]

# TARGET (MUST BE 1D)
y = data["Close"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

print("Training successful ✔")