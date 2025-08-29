# Student Performance Analysis

## Description
Analyze student performance data to understand scores and factors affecting them.

## Dataset
- File: `Student_performance`


## Preprocessing
- Reading files (.csv , .xlsx , .json , .db )
-Drop unnecessary columns
- Convert columns to correct data types
- Fill missing values (Categorical → mode, Numerical → median)

## Usage
```python
import pandas as pd

df = pd.read_csv("Student_performance.csv")
# Continue with other preprocessing steps
