@echo off&setlocal enabledelayedexpansion
D:
cd D:/Onmyoji/
set /p num="����򿪼����ͻ���(0-4):"
for /l %%i in (1,1,%num%) do "C:/Program Files/Sandboxie/start" /box:client%%i "C:/Program Files (x86)/Onmyoji/Launch" 
echo �뽫�ͻ��˵��������ʵĴ�С
echo 1.���꣨˫����
echo 2.���꣨������
echo 3.����/ҵԭ��
echo 4.����
set /p id="����ʹ���ĸ��ű�(1-4):"
set /p round="����ˢ������(0-999�������ж�����)"
set wechat=True
set control=True

set /p ctrl="�Ƿ���Ҫ���(y/n)"
if %ctrl% NEQ n goto label
set control=False

:label
set /p wc="�Ƿ�΢��֪ͨ(y/n)"
if %wc% NEQ n goto label2
set wechat=False

:label2
set /p user="�����뱻֪ͨ�˺ţ�Ĭ��Ϊ�ļ����֣�"
if %id%==1 (
	echo �뽫�������������׼�����棬���Ͻ�Ϊ˾����׼���ú��������ﰴ�س�
	pause
	call activate opencv-env
	echo OnmScript.py -r %round% -c !control! -w !wechat! -u %user%
	python OnmScript.py -r %round% -c %control% -w %wechat% -u %user%
	call deactivate
)
if %id%==2 (
	echo �뽫�������������׼�����棬���Ͻ�Ϊ˾����׼���ú��������ﰴ�س�
	pause
	call activate opencv-env
	echo OnmScript_tri.py -r %round% -c !control! -w !wechat! -u %user%
	python OnmScript_tri.py -r %round% -c %control% -w %wechat% -u %user%
	call deactivate
)
if %id%==3 (
	echo �뽫�������������׼�����棬���Ͻ�Ϊ˾����׼���ú��������ﰴ�س�
	pause
	call activate opencv-env
	echo OnmScript_Sparkle.py -r %round% -c !control! -w !wechat! -u %user%
	python OnmScript.py -r %round% -c %control% -w %wechat% -u %user%
	call deactivate
)
if %id%==4 (
	echo �뽫�������������׼�����棬���Ͻ�Ϊ˾����׼���ú��������ﰴ�س�
	pause
	call activate opencv-env
	echo OnmScript_Dogfood.py -r %round% -c !control! -w !wechat! -u %user%
	python OnmScript.py -r %round% -c %control% -w %wechat% -u %user%
	call deactivate
)
pause