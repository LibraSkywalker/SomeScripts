from util import *
import numpy
import time 
import math
import argparse
import os
import itchat

startX,startY = 715, 400# press the ready button

def getBonus():
	time.sleep(50)
	capture("log1")
	while not waitFor("BONUS"):
		time.sleep(0.05)
	
	for i in range(2):
		click(startX,startY)
	time.sleep(2.5)
	for i in range(2):
		click(startX,startY)
	cnt = 0
	capture("log2")
	while (not waitFor("FIRE") and waitFor("SPIRIT")):
		time.sleep(0.1)
		cnt += 1
		if (cnt > 20) :
			click(startX,startY)
			cnt = 0
			
def capture(name):
	img = controller.screenshot(region=(0, 0, 1920, 540))
	img.save(name+".jpg")
	itchat.send_image(name+".jpg", toUserName='filehelper')
	
parser = argparse.ArgumentParser()
parser.add_argument("-r","--rounds",help="input rounds")
args = parser.parse_args()

if args.rounds:
	rounds = int(args.rounds)
else :
	rounds = 199


itchat.auto_login(enableCmdQR=True,hotReload=True)
user = itchat.search_friends(name='hua')[0]['UserName']
#user = "filehelper"
log = open("log.txt","w+")
	
print("script running for",rounds,"rounds")
print("script running for",rounds,"rounds",file = log)
itchat.send("script running for "+str(rounds)+" rounds", toUserName='filehelper')

for i in range(rounds):
	print("time:",time.strftime("%H:%M:%S", time.localtime()),"\tremaining ",rounds - i," rounds")
	print("time:",time.strftime("%H:%M:%S", time.localtime()),"\tremaining ",rounds - i," rounds",file = log)
	itchat.send("time:"+time.strftime("%H:%M:%S", time.localtime())+"\tremaining "+str(rounds - i)+" rounds", toUserName=user)
	
	click(startX,startY)
	click(startX,startY)
	getBonus()
exitGame()