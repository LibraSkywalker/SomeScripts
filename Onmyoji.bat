@echo off&setlocal enabledelayedexpansion
D:
cd D:/Onmyoji/
set /p num="你想打开几个客户端(0-4):"
for /l %%i in (1,1,%num%) do "C:/Program Files/Sandboxie/start" /box:client%%i "C:/Program Files (x86)/Onmyoji/Launch" 
echo 请将客户端调整到合适的大小
echo 1.御魂（双开）
echo 2.御魂（三开）
echo 3.御灵/业原火
echo 4.狗粮
set /p id="你想使用哪个脚本(1-4):"
set /p round="你想刷多少轮(0-999不负责判断上限)"
set wechat=True
set control=True

set /p ctrl="是否需要点怪(y/n)"
if %ctrl% NEQ n goto label
set control=False

:label
set /p wc="是否微信通知(y/n)"
if %wc% NEQ n goto label2
set wechat=False

:label2
set /p user="请输入被通知账号（默认为文件助手）"
if %id%==1 (
	echo 请将界面调整至御魂准备界面，左上角为司机，准备好后请在这里按回车
	pause
	call activate opencv-env
	echo OnmScript.py -r %round% -c !control! -w !wechat! -u %user%
	python OnmScript.py -r %round% -c %control% -w %wechat% -u %user%
	call deactivate
)
if %id%==2 (
	echo 请将界面调整至御魂准备界面，左上角为司机，准备好后请在这里按回车
	pause
	call activate opencv-env
	echo OnmScript_tri.py -r %round% -c !control! -w !wechat! -u %user%
	python OnmScript_tri.py -r %round% -c %control% -w %wechat% -u %user%
	call deactivate
)
if %id%==3 (
	echo 请将界面调整至御魂准备界面，左上角为司机，准备好后请在这里按回车
	pause
	call activate opencv-env
	echo OnmScript_Sparkle.py -r %round% -c !control! -w !wechat! -u %user%
	python OnmScript.py -r %round% -c %control% -w %wechat% -u %user%
	call deactivate
)
if %id%==4 (
	echo 请将界面调整至御魂准备界面，左上角为司机，准备好后请在这里按回车
	pause
	call activate opencv-env
	echo OnmScript_Dogfood.py -r %round% -c !control! -w !wechat! -u %user%
	python OnmScript.py -r %round% -c %control% -w %wechat% -u %user%
	call deactivate
)
pause