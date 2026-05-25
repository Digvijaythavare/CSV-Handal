import csv    
    
data = [    
    {'Name': 'Lucy', 'Age': 30},  # 'City' is missing    
    {'Name': 'Peter', 'Age': 25, 'City': 'Miami'}    
]    
    
with open('dict-missing-fields.csv', 'w', newline='') as file:    
    fieldnames = ['Name', 'Age', 'City']    

    writer = csv.DictWriter(file, fieldnames=fieldnames, restval='N/A') 
       
    writer.writeheader()    
    writer.writerows(data)    
