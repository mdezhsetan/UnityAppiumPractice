echo "adb command ... "
adb forward tcp:13000 tcp:13000

echo "Starting Appium ..."
appium
sleep 10
ps -ef|grep appium