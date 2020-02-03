from configparser import ConfigParser
config = ConfigParser()
z=config.read("D:\Training\Python_Selenium_Training\PythonSeleniumTrainingGaurav\Module_9\config.properties")
z=config.sections()
print(z)

