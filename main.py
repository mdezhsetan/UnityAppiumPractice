import time
from altunityrunner import AltUnityDriver, By
import setupdriver as setup




appium_driver = setup.setup_driver(port=4723)
alt_driver = AltUnityDriver()
print("object created")


email_obj.call_component_method("LocalizedText", "SetKey", [email_text])
print("username added")
time.sleep(5)
pass_obj.set_text(pass_text)
# pass_obj.call_component_method("LocalizedText","SetKey",[pass_text])
print("password added")
time.sleep(5)
signin_btn = alt_driver.find_object(By.ID, "16500")
signin_btn.click()
# signin_btn.call_component_method("UnityEngine.UI.Button","Press")
print("clicked")
time.sleep(5)

# actions = TouchAction(appium_driver)
# actions.tap(appium_driver.find_element_by_id("17130"))
# actions.perform()
#


print("End")
# alt_driver.stop()
# appium_driver.quit()
