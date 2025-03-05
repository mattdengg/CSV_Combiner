import pandas as pd
import tkinter as tk
from tkinter import filedialog

def combine_csv(files, output_file):
    df_list = [pd.read_csv(file) for file in files]
    combined_df = pd.concat(df_list, ignore_index=True)

    # Save to a new CSV file
    combined_df.to_csv(output_file, index=False)
    print(f"Combined CSV saved as {output_file}")

root = tk.Tk()
root.withdraw()
csv_files = filedialog.askopenfilenames(title="Select CSV files", filetypes=[("CSV files", "*.csv")])


if csv_files:
    output_csv = filedialog.asksaveasfilename(
        title="Save Combined CSV As",
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")]
    )
    if output_csv:
        combine_csv(csv_files, output_csv)