#!python3
# -*- coding:utf-8 -*-

'''
  overview:
    Sample of setting datavalidation to cell by openpyxl.
    Caution!:
      If formula1 was reffered from other sheet, it will be removed because is not supported.
      Please make sure write pulldown's list in the same sheet as possible.
'''
import sys, os
from pathlib import Path
import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

wbname = "example.xlsx"
wbpath = Path(wbname)

if wbpath.exists == False or wbpath.is_file() == False or wbpath.suffix != ".xlsx" or wbpath.is_mount():
    print("Indicated file is not exists or excel file!")
    sys.exit(1)
    
wb = openpyxl.load_workbook(wbname, keep_links=True, keep_vba=True, read_only=False, data_only=False)
sheet2 = wb["Sheet2"]

#Define datavalidation with type "list"
dv = DataValidation(type="list", formula1="Sheet3!$A$2:$A$5")

#Add can only one cell.
dv.add(sheet2["A8"])

#ranges can set more two cells.
#dv.ranges = "A9 A10"
#ranges can set more two cells.
#dv.ranges = "B8:B10"
# But datavalidation allow to regist only single ranges or add.

#After dv.add or dv.ranges, you need to add datavalidation into sheet.
sheet2.add_data_validation(dv)

wb.save(wbname)
