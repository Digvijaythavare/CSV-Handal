import csv  
import pandas as pd  
    
# opening the CSV file  
with open('open.csv', newline='') as file:  
    # using the DictReader() class to convert the content of the file into a dictionary  
    reader = csv.reader(file)  
  
    # printing each row of the table  
    for row in reader:  
        print(row)

print()

# this code of pandas library 

# Reading the CSV file into a DataFrame  
dframe = pd.read_csv('companies.csv')  
  
# Displaying the DataFrame  
print(dframe)            