from util import *
import numpy
import time 
import math
import os
import itchat

duration = 25
middleX,middleY = 1420, 130 #ushi mairi curse
time1 = 13 #first round end point
time2 = 23 #second round end point
time3 = 37 #third round end point
startX,startY = 780, 480# press the ready button
loadTime = 3

def round(round_time):
	while not waitFor("ROUNDSTART",["OTHER"]):
		if (checkScene == "OTHER"):
			return
	print("Round",round_time,"is processing")
	print("Round",round_time,"is processing",file = log)
	time.sleep(1.2)
	for i in range(random.randint(5, 7)): #randomize click round
		click(middleX, middleY)
	
	time.sleep(3)

def getBonus():
	while not waitFor("BONUS"):
		time.sleep(0.05)
	
	for i in range(2):
		click(startX,startY)
		click(middleX, middleY)
	time.sleep(2)
	for i in range(2):
		click(startX,startY)
		click(middleX, middleY)
	
def start():
	while (not waitFor("TEAM")):
		time.sleep(0.1)
	click(startX,startY)
	click(startX,startY)
	
rounds,verbose,control,wechat,user = argumentParsing()
log = open("log.txt","w+")
	
def main():


	print("script running for",rounds,"rounds")
	print("script running for",rounds,"rounds",file = log)

	if wechat :
		itchat.send("script running for "+str(rounds)+" rounds", toUserName=user)

	for i in range(rounds):
		print("time:",time.strftime("%H:%M:%S", time.localtime()),"\tremaining ",rounds - i," rounds")
		print("time:",time.strftime("%H:%M:%S", time.localtime()),"\tremaining ",rounds - i," rounds",file = log)
		if wechat :
			itchat.send("time:"+time.strftime("%H:%M:%S", time.localtime())+"\tremaining "+str(rounds - i)+" rounds", toUserName=user)
		
		start()
		
		if control:
			for j in range(3):
				round(j)
		else :
			time.sleep(duration)
		
		getBonus()
	exitGame()
	print("mission complete")
	print("mission complete",file = log)
	if wechat :
		itchat.send("mission complete", toUserName=user)

main()