from util import *

startX,startY = 925,760
cancelX,cancelY = 1410,293
circle = [45,50,442,285,48]
itchat.auto_login(enableCmdQR=True,hotReload=True)
Hang = True
while(Hang):
	time.sleep(1)
	print("not finished yet.")
	click(startX,startY)
	time.sleep(0.5)
	click(cancelX,cancelY)
	success,_=findTarget(circle)
	Hang = not success
user = itchat.search_chatrooms(name='遍地梧桐花～')[0]['UserName']
itchat.send("The Onmyoji server is open!", toUserName = user)
