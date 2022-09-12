from setupdriver import create_driver

driver = create_driver(4723)
print("Connected to Appium")
driver.switch_to.context('UNITY')
print("Switched to Unity")
var = driver.page_source



