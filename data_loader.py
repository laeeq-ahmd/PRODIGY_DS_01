import pandas as pd

def load_dataset(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data Successfully Loaded!")
        # print("DataSet Shape:", df.shape)
        print("Missing Value:", data.isna().sum().sum())
        return data
    except FileNotFoundError:
        print("File not found!")
        return None
    except Exception as e:
        print(f"Error {e}")
        return None
