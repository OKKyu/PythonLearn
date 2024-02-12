#! python3
# -*- coding:utf-8 -*-
import os
import sys
import openpyxl
from openpyxl.workbook.protection import WorkbookProtection
from openpyxl.worksheet.protection import SheetProtection
'''
  overview: This code is sample of lock/unlock with password.
     https://office54.net/python/excel/excel-openpyxl-protect
'''

try:
    wb = openpyxl.load_workbook("lockbook.xlsx")
except FileNotFoundError as fnfe:
    wb = openpyxl.Workbook()
finally:
    if len(sys.argv) == 2:
        if bool(int(sys.argv[1])) is True:
            # lock workbook
            wb.security = WorkbookProtection(workbookPassword="abce", lockWindows=True, lockStructure=True)
            wb.security.lock_structure = True
            wb.security.set_workbook_password("fffe")
            ws = wb["Sheet"]
            ws.protection.password = "test"
            ws.protection.enable()
        else:
            wb.security = WorkbookProtection(workbookPassword="abce", lockWindows=False, lockStructure=False)
            ws = wb["Sheet"]
            ws.protection.disable()

        wb.save("lockbook.xlsx")

