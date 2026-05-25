import csv    
# List of rows to write means each row is a list   
rows = [    
    ['Name', 'Age', 'City'],    
    ['Rohan', 22, 'New Delhi'],    
    ['Abhay', 23, 'Noida'],    
    ['Vivek', 24, 'Gurgaon']    
]    
  
with open('write2.csv', 'w', newline='') as file:    
    writer = csv.writer(file)    
    writer.writerows(rows)    
  
# Read and print contents  
with open('writer-output.csv', 'r') as file:  
    reader = csv.reader(file)  
    for row in reader:  
        print(row)  