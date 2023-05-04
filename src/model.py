import pandas as pd

## Function to load the engineered dataset
def load_engineered_data(data_path, chunksize=10000):
    chunks = []
    for chunk in pd.read_csv(data_path, chunksize=chunksize, low_memory=False):
        chunks.append(chunk)
    data = pd.concat(chunks, axis=0)
    return data

data_path = "../data/engineered_data.csv"
data = load_engineered_data(data_path)

data_path = "../data/engineered_data.csv"
data = load_engineered_data(data_path)

from sklearn.model_selection import train_test_split

# Separate the features (X) and the target variable (y)
X = data.drop(['UnitPrice'], axis=1)
y = data['UnitPrice']

# Split the data into a training set (80%) and a testing set (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Initialize the RandomForestRegressor model
model = RandomForestRegressor(random_state=42)

# Train the model using the training data
model.fit(X_train, y_train)

# Evaluate the model on the testing data
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean squared error:", mse)

from sklearn.model_selection import GridSearchCV

# Define the hyperparameters to be tuned
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Initialize the GridSearchCV
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, scoring='neg_mean_squared_error', verbose=2, n_jobs=-1)

# Fit the GridSearchCV to the training data
grid_search.fit(X_train, y_train)

# Get the best hyperparameters
best_params = grid_search.best_params_
print("Best hyperparameters:", best_params)

# Train the model with the best hyperparameters
best_model = RandomForestRegressor(**best_params, random_state=42)
best_model.fit(X_train, y_train)

# Evaluate the model with the best hyperparameters on the testing data
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean squared error (best model):", mse)