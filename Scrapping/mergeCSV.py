import pandas as pd

def merge_csv_files(csv_files, output_file):
    # Read each CSV file into a DataFrame
    dfs = [pd.read_csv(file) for file in csv_files]
    
    # Concatenate the DataFrames along axis 0 (rows)
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # Write the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file, index=False)
    
    print("CSV files merged successfully!")

if __name__ == "__main__":
    # Specify the paths to the CSV files
    csv_files = ["scrapping_Beauty_Fashion.csv", "scrapping_Diseases_Symptoms.csv", "scrapping_Food.csv"]
    
    # Specify the path for the output merged CSV file
    output_file = "data.csv"
    
    # Merge the CSV files
    merge_csv_files(csv_files, output_file)
