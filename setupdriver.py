from appium.webdriver import webdriver


def create_driver(port):
    desired_capabilities = {
        "deviceName": "Mahshad's A52",
        "udid": "RZ8T11EEMNJ",
        'automationName': 'UiAutomator2',
        "platformName": "Android",
        "platformVersion": "12",
        'altUnityHost': 'localhost',
        'altUnityPort': 13000,
        "app": 'C:\\Users\\Mahshad\\Desktop\\Project\\UnityAppiumWorkshop.apk',
    }
    return webdriver.Remote('http://localhost:{0}'.format(port), desired_capabilities)