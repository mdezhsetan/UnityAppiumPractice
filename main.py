from setupdriver import create_driver


driver = create_driver(port=4723)
driver.switch_to.context('UNITY')
print(driver.page_source)
