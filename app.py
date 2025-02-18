import pandas as pd  

def merge_databases(file1, file2, output_file):  
    # Read the two CSV files into DataFrames  
    df1 = pd.read_csv(file1)  
    df2 = pd.read_csv(file2)  
    
    # Merge the DataFrames on a common column, e.g., 'id'  
    merged_df = pd.merge(df1, df2, on='id', how='outer')  
    
    # Save the merged DataFrame to a new CSV file  
    merged_df.to_csv(output_file, index=False)  

# Example usage  
merge_databases('database1.csv', 'database2.csv', 'merged_database.csv')
