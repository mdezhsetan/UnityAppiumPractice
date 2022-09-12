from appium import webdriver


def create_driver(port):
    desired_capabilities = {
        "deviceName": "Mahshad A52",
        "udid": "RZ8T11EEMNJ",
        'automationName': 'UiAutomator2',
        "platformName": "Android",
        "platformVersion": "12",
        'altUnityHost': 'localhost',
        'altUnityPort': 13000,
        'newCommandTimeout': 0,
        "app": 'C:\\Users\\Mahshad\\Desktop\\build_apk\\Am.apk',
    }
    return webdriver.Remote(command_executor='http://localhost:{0}'.format(port), desired_capabilities=desired_capabilities)