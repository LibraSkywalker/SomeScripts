import pyautogui as controller
import argparse
import random
import numpy
import cv2
import csv
import time 
import math
import itchat
import os

interval = 10
threshold = 25

def indistinct_position(x,y): #randomize click point
	deltaX =  random.randint(-interval, interval)
	deltaY =  random.randint(-interval, interval)
	return x + deltaX , y + deltaY

def click(x,y):
	latency = random.uniform(0.18, 0.25) #randomize latency
	controller.moveTo(x, y, latency, controller.easeInOutQuad)
	controller.doubleClick(indistinct_position(x, y))
	return latency	

def dist(x,y):
	return (abs(x[0]-y[0]) + abs(x[1]-y[1]) + abs(x[2] - y[2]))
	
def capture(name):
	img = controller.screenshot(name+".jpg")
	itchat.send_image(name+".jpg", toUserName='filehelper')

def checkScene(verbose = False):
	img = controller.screenshot(region=(0, 0, 1920, 540))
	for i in range(scene_num):
		hit,_ = findTarget(feature[i], img)
		if (hit) :
			if verbose :
				print(scene_name[i])
			return scene_name[i]
	if verbose :
		print("OTHER")
	return "OTHER"

def clearInvitation(verbose = False):
	img = controller.screenshot()
	result,position	= findMultiTarget(feature[-3:],img)
	if result:
		click(position[0],position[1])
	
def exitGame():
	print('mission complete, close the client in 5 seconds')
	time.sleep(5)
	os.system('"C:\Program Files\Sandboxie\Start.exe"  /terminate_all')

def findMultiTarget(data, img = None ):
	if (img is None):
		img = controller.screenshot()
	if len(data) == 2 :
		data = data + [0,0,0]
	image = cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.2,20,param1=50,param2=40,minRadius=data[0][0],maxRadius=data[0][1])
	if circles is None:
		return False,(0,0)
	
	circles = numpy.uint16(numpy.around(circles))
	#print(circles,data)
	for i in range(len(data)):
		for circle in circles[0]:
			if dist(data[i][2:],list(circle)) < threshold:
				return True,data[i][2:]
	return False,[0,0,0]
	
def findTarget(data, img = None ):
	if (img is None):
		img = controller.screenshot()
	if len(data) == 2 :
		data = data + [0,0,0]
	image = cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.2,20,param1=50,param2=40,minRadius=data[0],maxRadius=data[1])
	if circles is None:
		return False,(0,0)
	
	circles = numpy.uint16(numpy.around(circles))
	#print(circles,data)
	if data[2:] != [0,0,0]:
		for circle in circles[0]:
			if dist(data[2:],list(circle)) < threshold:
				return True,data[2:]
		return False,data[2:]
	else :
		return True,circles[0][0]

def allReady():
	print("waiting for teamates")
	time.sleep(0.1)
	img = controller.screenshot(region=(0, 0, 1920, 1080))
	hit,_=findTarget([20,30,655,187,22],img)
	return hit

def argumentParsing():
	parser = argparse.ArgumentParser()
	parser.add_argument("-r","--rounds",help="input rounds")
	parser.add_argument("-v","--verbose",help="show some debug log")
	parser.add_argument("-c","--control",help="need some extra auxiliary")
	parser.add_argument("-w","--wechat",help="sending message to wechat")
	parser.add_argument("-u","--user",help="wechat user nickname")
	args = parser.parse_args()

	if args.rounds:
		rounds = int(args.rounds)
	else :
		rounds = 199
		
	verbose = args.verbose == str(True)
	wechat = args.wechat == str(True)
	control = args.control == str(True)
	if wechat :
		itchat.auto_login(enableCmdQR=True,hotReload=True)
		if args.user == "nouser":
			user = "filehelper"
		else :
			user = itchat.search_friends(name=args.user)[0]['UserName']
	print(rounds,verbose,control,wechat,user)
	return rounds,verbose,control,wechat,user

def waitFor(scene,retry = []):
	retry = retry 
	print("waiting for",scene)
	clearInvitation()
	now = checkScene()
	cnt = 0
	while (cnt < 10 and now != scene) :
		if (now in retry) :
			return False
		clearInvitation()
		now = checkScene()
		cnt += 1
	if cnt < 10 :
		print("Getting into",scene)
		return True
	else :
		return False
		
scene_name = []
feature = []
data = csv.reader(open('data.csv'))
next(data)
for line in data :
	print(line)
	scene_name.append(line[0])
	feature.append(list(map(int,line[1:])))
scene_num = len(scene_name) - 4
print(scene_name)
print(feature)