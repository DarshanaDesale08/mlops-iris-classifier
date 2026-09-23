import pandas as pd
from feast import FeatureStore

# Connect to Feast repository
store = FeatureStore(repo_path=".")

# Load the offline feature data
df = pd.read_parquet("data/iris_features.parquet")

# Select 5 entities with event timestamps
entity_df = df[["sample_id", "event_timestamp"]].head(5)

# Define features from your actual Feature Views
features = [
    "iris_measurements:sepal length (cm)",
    "iris_measurements:sepal width (cm)",
    "iris_measurements:petal length (cm)",
    "iris_measurements:petal width (cm)",
    "iris_engineered_features:sepal_area",
    "iris_engineered_features:petal_area",
    "iris_engineered_features:sepal_to_petal_length_ratio",
    "iris_engineered_features:petal_length_bin",
]

# Retrieve historical features
historical_features = store.get_historical_features(
    entity_df=entity_df,
    features=features
).to_df()

# Display results
print("Historical Features:")
print(historical_features)

print("Shape:", historical_features.shape)