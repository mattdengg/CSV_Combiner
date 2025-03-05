import pandas as pd
import tkinter as tk
from tkinter import filedialog

def combine_csv(files, output_file):
    # Read and combine all CSV files
    df_list = [pd.read_csv(file) for file in files]
    combined_df = pd.concat(df_list, ignore_index=True)

    # Ensure the 'date' column is in datetime format and sort
    if 'date' in combined_df.columns:
        combined_df['date'] = pd.to_datetime(combined_df['date'], errors='coerce')
        combined_df = combined_df.sort_values(by='date')

    # Save to a new CSV file
    combined_df.to_csv(output_file, index=False)
    print(f"Combined CSV saved as {output_file}")

# Open file dialog to select CSV files
root = tk.Tk()
root.withdraw()  # Hide the root window
csv_files = filedialog.askopenfilenames(title="Select CSV files", filetypes=[("CSV files", "*.csv")])

if csv_files:
    output_csv = filedialog.asksaveasfilename(title="Save Combined CSV As", defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if output_csv:
        combine_csv(csv_files, output_csv)
