#importing the openpyxl library  
import openpyxl  
  
# writing the full raw path of our file  
file_path = "Book1.xlsx"  
  
# Here we are Loading workbook  
workbook = openpyxl.load_workbook(file_path)  
  
# Select active sheet  
sheet = workbook.active  
  
# Printing all rows of the Excel file  
for row in sheet.iter_rows(values_only=True):  
    print(row)  