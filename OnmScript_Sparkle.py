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
		
		click(startX,startY)
		click(startX,startY)
		getBonus()
	
	exitGame()
	print("mission complete")
	print("mission complete",file = log)
	if wechat :
		itchat.send("mission complete", toUserName=user)
main()