import pandas as pd  
# specify the path of the CSV file  
file_path = "open.csv"  
# Read the file  
data = pd.read_csv(file_path, low_memory=False)      
# Output the number of rows  
print("Total rows: {0}".format(len(data)))      
# Print the list of column headers  
print(list(data.columns))  