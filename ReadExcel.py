import pandas as pd      
# Specify the correct file path  
file_path = r"Book1.xlsx"  
  
tpointtech = pd.read_excel(file_path, engine='openpyxl')  
  
print(tpointtech)  