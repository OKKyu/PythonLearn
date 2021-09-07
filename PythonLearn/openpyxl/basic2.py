#!python3
# -*- coding:utf-8 -*-

'''
  overview:
    Sample of updating and saving workbook by openpyxl.
'''

import openpyxl
from openpyxl import styles
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.utils import get_column_letter, column_index_from_string

wbname = "example.xlsx"

#Loading book and sheet.
wb = openpyxl.load_workbook(wbname)
sheet = wb.get_sheet_by_name("Sheet2")

#Get cells so that alternate values.
rows = sheet["A1":"C4"]
cnt = 0
for row in rows:
    for cell in row:
        #Set value
        cell.value = "Me!" + str(cnt)
        
        # Set styles
        cell.font = Font(name="sans cerif", size=20, italic=False, bold=True, color="FF0000")
        cell.alignment = Alignment(horizontal="center")
        
        # instead of border_style, you can write just "style".
        side = Side(border_style="double", color='FF0000')
        side2 = Side(border_style="medium", color='0000FF')
        cell.border = Border(left=side, right=side, top=side, bottom=side, \
                             diagonal=side2, outline=side2, vertical=side2, horizontal=side2 \
                      )
        # Set background color in cell.
        cell.fill = PatternFill(patternType="darkGrid", fgColor="141414", bgColor="090909")
        cnt += 1

#resize height and width.
sheet.row_dimensions[1].height = 30
sheet.column_dimensions["C"].width = 60

wb.save(wbname)