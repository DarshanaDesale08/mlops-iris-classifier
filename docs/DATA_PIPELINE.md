\# Data Pipeline



\## Pipeline Stages



| Stage | Purpose | Input | Output |

|---|---|---|---|

| Collect | Obtain raw Iris data | sklearn Iris dataset | `iris\_raw.csv` |

| Preprocess | Clean data | `iris\_raw.csv` | `iris\_preprocessed.csv` |

| Feature Engineering | Create useful features | `iris\_preprocessed.csv` | `iris\_features.csv` |

| Validate | Check schema, nulls and ranges | `iris\_features.csv` | Validation result |



\## Pipeline Flow



Collect

↓

Preprocess

↓

Feature Engineering

↓

Validate

