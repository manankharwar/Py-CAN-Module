import xlwt
import xlrd
from xlwt import Workbook
from xlutils.copy import copy
import datetime
import time

class excel:

    def __init__(self, name):
        #Formatting of datetime function
        dateStr = str(datetime.datetime.now())
        self.date = dateStr[0:10]
        self.time = dateStr[11:]
        self.saveName = name

        # Try opening existing .xls fire
        try:
            tempWB = xlrd.open_workbook(self.saveName+".xls",formatting_info=True)
            self.wb = copy(tempWB)
            self.sheet = self.wb.get_sheet(0)

        except:
            #Create workbook and initialize the header rows
            self.wb = Workbook()
            self.sheet = self.wb.add_sheet("Sheet 1")

            self.sheet.write(0,0,"Date")
            self.sheet.write(0,1,"Time")
            self.sheet.write(0,2,"Message ID")
            self.sheet.write(0,3,"Channel Sent to")
            self.sheet.write(0,4,"Data")

            self.saveName = name
            self.wb.save(self.saveName+".xls")


    def addRow(self, msgId, chan, data):
        currRow = self.getCurrentRow()
        self.sheet.write(currRow,0,self.date)
        self.sheet.write(currRow,1,self.time)
        self.sheet.write(currRow,2,msgId)
        self.sheet.write(currRow,3,chan)
        self.sheet.write(currRow,4,data)
        self.wb.save(self.saveName+".xls")

    def getCurrentRow(self):
        w = xlrd.open_workbook(self.saveName + ".xls")
        return w.sheet_by_index(0).nrows

    def readRows(self):
        workbook = xlrd.open_workbook(self.saveName+".xls")
        s1 = workbook.sheet_by_index(0)

        for rowNum in range(s1.nrows):
            print(s1.row_values(rowNum))
