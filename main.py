from altunityrunner import AltUnityDriver

import setupdriver as setup

appium_driver = setup.setup_driver(port=4723)
alt_driver = AltUnityDriver()
print("object created")


print("End")
# alt_driver.stop()
# appium_driver.quit()
