from ReadFromExcelClass import readingCell

x = readingCell("D:\Training\Python_Selenium_Training\PythonSeleniumTrainingGaurav\Module_9\TestData.xlsx")
print(x.readColumByIndex("Sheet1", 4, 2).value)
print(x.getRowCount("Sheet1"))
print(x.getColCount("Sheet1"))
x.writeByColIndex("Sheet1", 4 , 3, "Learning Python", "D:\Training\Python_Selenium_Training\PythonSeleniumTrainingGaurav\Module_9\TestData.xlsx")