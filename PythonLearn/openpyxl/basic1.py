#!python3
# -*- coding:utf-8 -*-

'''
  overview:
    Sample of Accessing cells in workbook by openpyxl.
'''

import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string

wbname = "example.xlsx"

# reading workbook
wb = openpyxl.load_workbook(wbname)

# Search worksheet names in workbook.
print(wb.get_sheet_names)
print(wb.worksheets)

# Get a worksheet from workbook by sheet name.
sheet = wb.get_sheet_by_name("Sheet1")
# You can get sheet by way below.
#sheet = wb['Sheet1']

# Getting one cell in worksheet.
cell = sheet["A1"]
print(str(cell.coordinate) + "  value:" + str(cell.value) + ",row:" + str(cell.row) + ",col:" + str(cell.column) + ",coordinate:" + str(cell.coordinate))
cell = sheet["B2"]
print(str(cell.coordinate) + "  value:" + str(cell.value) + ",row:" + str(cell.row) + ",col:" + str(cell.column) + ",coordinate:" + str(cell.coordinate))
print("Cell's attributes" + str(dir(cell)))

# Getting one cell by row number and column number.
cell = sheet.cell(row=2, column=1)
print(str(cell.coordinate) + "  value:" + str(cell.value) + ",row:" + str(cell.row) + ",col:" + str(cell.column) + ",coordinate:" + str(cell.coordinate))

#Converting from column number to column letter.
print("Column what has index 3 is " + get_column_letter(3))

#Converting from column letter to column number. There are ok either lowercase and uppercase.
print("Column C's index is " + str(column_index_from_string("C")))
print("Column c's index is " + str(column_index_from_string("c")))

# Getting two or more cells in worksheet.
# It return 2 dimensional tuple. [row][column]
rows = sheet["A1":"C3"]
for row in rows:
    print(row[0].coordinate + " " + str(row[0].value) + "  ", end="")
    print(row[1].coordinate + " " + str(row[1].value) + "  ", end="")
    print(row[2].coordinate + " " + str(row[2].value) + "  ")
    
# Access specific column or row.
cols = tuple(sheet.columns)
for item in cols[1]:
    print(item.value)
