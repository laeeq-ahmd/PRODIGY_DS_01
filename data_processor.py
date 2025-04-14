import data_loader as dl
import pandas as pd


def process_data(data):
    if data is None:
        print("Data loading failed!")
        exit()

    # Drop missing values
    if data.isna().sum().sum() > 0:
        data = data.dropna()

    # Pattern to match
    pattern = r'^Population ages (\d{2}-\d{2}|80 and above), (male|female)$'

    # Check which rows match
    match_mask = data["Indicator Name"].str.match(pattern, na=False)
    
    # Filter and extract the info
    filtered_data = data[match_mask].copy()
    filtered_data[["Age_Group", "Gender"]] = filtered_data["Indicator Name"].str.extract(pattern)

    filtered_data = filtered_data[filtered_data["Age_Group"] != "15-64"]
    # Convert Value to numeric
    filtered_data["Value"] = pd.to_numeric(filtered_data["Value"])

    # Group and display
    grouped = filtered_data.groupby(["Age_Group", "Gender"], as_index=False)["Value"].sum()
    return grouped