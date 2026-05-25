import xlsxwriter  
# here we are mentioning the full path where we want to save the file  
file_path = "hwllo.xlsx"  
# Create workbook at the specified location  
workbook = xlsxwriter.Workbook(file_path)  
worksheet = workbook.add_worksheet()  
  
# Write values  
worksheet.write('A1', 'Hello..')  
worksheet.write('B1', 'T')  
worksheet.write('C1', 'Point')  
worksheet.write('D1', 'Tech')  
worksheet.write('E1', 'Pvt Ltd')  
  
# Close (save) workbook  
workbook.close()  