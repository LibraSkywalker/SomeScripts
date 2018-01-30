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
lastX,lastY = 780, 1020
loadTime = 0.5
tolerance = 15

def round(round_time):
	cnt = 0
	while not waitFor("ROUNDSTART"):
		cnt += 1
		if (cnt > tolerance * 2):
			return False
	print("Round",round_time,"is processing")
	print("Round",round_time,"is processing",file = log)
	time.sleep(1.2)
	for i in range(random.randint(5, 7)): #randomize click round
		click(middleX, middleY)
	
	time.sleep(1.5)
	return True

def getBonus():
	cnt = 0
	while not waitFor("BONUS"):
		cnt += 1
		if (cnt > tolerance):
			return False
	
	for i in range(2):
		click(startX,startY)
		click(middleX, middleY)
		click(lastX, lastY)
	time.sleep(loadTime)
	for i in range(2):
		click(startX,startY)
		click(middleX, middleY)
		click(lastX, lastY)
	return True
	
def start():
	cnt = 0
	while (not waitFor("TEAM")):
		cnt += 1
		if (cnt > tolerance):
			return False
	while (not allReady()):
		cnt += 1
		if (cnt > tolerance):
			return False
	print("all set!")
	capture("record")
	click(startX,startY)
	click(startX,startY)
	return True
	
rounds,verbose,control,wechat,user = argumentParsing()
log = open("log.txt","w+")
	
def main():

	
	bugFree = True
	print("script running for",rounds,"rounds")
	print("script running for",rounds,"rounds",file = log)

	if wechat :
		itchat.send("script running for "+str(rounds)+" rounds", toUserName=user)

	for i in range(rounds):
		print("time:",time.strftime("%H:%M:%S", time.localtime()),"\tremaining ",rounds - i," rounds")
		print("time:",time.strftime("%H:%M:%S", time.localtime()),"\tremaining ",rounds - i," rounds",file = log)
		if wechat :
			itchat.send("time:"+time.strftime("%H:%M:%S", time.localtime())+"\tremaining "+str(rounds - i)+" rounds", toUserName=user)
		
		bugFree = start()
		if not bugFree:
			break
		if control:
			for j in range(3):
				bugFree = round(j)
				if not bugFree:
					break
		else :
			time.sleep(duration)
		
		bugFree = getBonus()
		if not bugFree :
			break
	if bugFree:
		print("mission complete")
		print("mission complete",file = log)
		if wechat :
			itchat.send("mission complete", toUserName=user)
	else :
		print("some error occured and the game was forced to end.")
		print("some error occured and the game was forced to end.",file = log)
		if wechat :
			itchat.send("some error occured and the game was forced to end.", toUserName=user)
		controller.screenshot('erroropt.png')
		
		
	exitGame()
main()