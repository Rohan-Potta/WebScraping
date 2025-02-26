import openpyxl

excel = openpyxl.Workbook()

sheet = excel.active
sheet.title = 'MU Faculty Data'

sheet.append(['URL','Name','Profession','Department','Emil-Id','Phone Number'])
