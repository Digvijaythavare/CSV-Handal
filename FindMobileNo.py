import re

with open('Rawdata.txt', 'r') as file:
    data = file.read()

    mobile_numbers = re.findall("[6-9]{1}[0-9]{9}", data)
    print("Mobile Numbers Found:", mobile_numbers)