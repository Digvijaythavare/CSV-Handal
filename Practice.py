import os 
import csv

data = [
    {'Name': 'John', 'Age': 20, 'City': 'Hyderabad'},
    {'Name': 'Sachin', 'Age': 21, 'City': 'Pune'},
    {'Name': 'Lucy', 'Age': 40, 'City': 'New York'},
    {'Name': 'Aman', 'Age': 23, 'City': 'Delhi'},
    {'Name': 'Priya', 'Age': 22, 'City': 'Mumbai'},
    {'Name': 'Rohit', 'Age': 25, 'City': 'Chennai'},
    {'Name': 'Sneha', 'Age': 24, 'City': 'Bangalore'},
    {'Name': 'Karan', 'Age': 26, 'City': 'Jaipur'},
    {'Name': 'Neha', 'Age': 21, 'City': 'Pune'},
    {'Name': 'Vikas', 'Age': 27, 'City': 'Lucknow'}
]

File_Name = input("Enter the file name with extension: ")


with open('write.csv','w',newline='') as file:
    writer = csv.DictWriter(file,fieldnames=['Name','Age','City'])

    writer.writeheader() # write the header row to the CSV file
    writer.writerows(data) # write the data rows to the CSV file


