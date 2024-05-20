import pandas as pd
import os

def merge_csv_files_columnwise(folder_path, output_filename):
    merged_data = pd.DataFrame()
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(folder_path, filename)
            df = pd.read_csv(filepath)
            df.fillna(0, inplace=True)  # Replace NaN values with 0
            column_name = filename.split(".")[0]  # Extract column name from filename
            merged_data[column_name] = df.iloc[:, 0]  # Assuming single-column CSV files

    # Dump the merged data to a CSV file on the device
    merged_data.to_csv(output_filename, index=False)

# Example usage:
folder_path = "./"  # Replace with the actual path to your folder
output_filename = "merged_data.csv"  # Choose a filename for the output
merge_csv_files_columnwise(folder_path, output_filename)
