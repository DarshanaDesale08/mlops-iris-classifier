from datetime import timedelta

from feast import Entity, FeatureView, FeatureService, Field, FileSource
from feast.types import Float32, Int64, String


# Entity
sample = Entity(
    name="sample_id",
    join_keys=["sample_id"],
)


# Data Source
iris_source = FileSource(
    name="iris_source",
    path="data/iris_features.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
)


# Feature View 1: Original Iris Measurements
iris_measurements_fv = FeatureView(
    name="iris_measurements",
    entities=[sample],
    schema=[
        Field(name="sepal length (cm)", dtype=Float32),
        Field(name="sepal width (cm)", dtype=Float32),
        Field(name="petal length (cm)", dtype=Float32),
        Field(name="petal width (cm)", dtype=Float32),
        Field(name="species", dtype=String),
    ],
    source=iris_source,
    ttl=timedelta(days=3650),
)


# Feature View 2: Engineered Features
iris_engineered_fv = FeatureView(
    name="iris_engineered_features",
    entities=[sample],
    schema=[
        Field(name="sepal_area", dtype=Float32),
        Field(name="petal_area", dtype=Float32),
        Field(name="sepal_to_petal_length_ratio", dtype=Float32),
        Field(name="petal_length_bin", dtype=String),
    ],
    source=iris_source,
    ttl=timedelta(days=3650),
)


# Feature Service
iris_feature_service = FeatureService(
    name="iris_feature_service",
    features=[
        iris_measurements_fv,
        iris_engineered_fv,
    ],
)