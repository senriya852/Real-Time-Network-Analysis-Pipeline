import pandas as pd

# Read the CSV file and perform the necessary transformations
df = pd.read_csv("merged_data.csv")

# Clean and transform the 'proto' column, then create binary columns
df['proto'] = df['proto'].str.strip().str.lower()
df['tcp'] = df['proto'].apply(lambda x: 1 if x == 'tcp' else 0)
df['icmp'] = df['proto'].apply(lambda x: 1 if x == 'icmp' else 0)

# Clean and transform the 'state' column, then create binary columns
df['state'] = df['state'].str.strip().str.lower()
df['INT'] = df['state'].apply(lambda x: 1 if x == 'int' else 0)
df['RST'] = df['state'].apply(lambda x: 1 if x == 'rst' else 0)

# Replace NaN values with zero or mean
# Replace NaN with zero
# df.fillna(0, inplace=True)
df=df.drop('proto', axis=1)
df=df.drop('state', axis=1)
# Replace NaN with mean
df.isnull().sum()


# Save the DataFrame to a new CSV file
output_filename = "processed_data_final12.csv"
df.to_csv(output_filename, index=False)  # Use index=False to avoid writing the row index to the CSV file

print(f"DataFrame saved to {output_filename}")

