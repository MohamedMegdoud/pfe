import pandas as pd

# === Replace this with your actual file path ===
raw_file_path = 'adni_full.raw'
csv_file_path = 'converted_file.csv'

# === Try reading the file with pandas ===
try:
    # If your file is whitespace or tab delimited
    df = pd.read_csv(raw_file_path, delim_whitespace=True, header=None)

    # Optional: Assign column names manually if needed
    # df.columns = ['col1', 'col2', 'col3', ...]

    # Save as CSV
    df.to_csv(csv_file_path, index=False)
    print(f"Converted '{raw_file_path}' to '{csv_file_path}' successfully!")

except Exception as e:
    print("Error reading the .raw file:", e)