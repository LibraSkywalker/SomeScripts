from util import *


entranceX, entranceY = 880, 480
startX, startY = 700, 440
#startX, startY = 500, 440
endX,endY = 39,79
confirmX,comfirmY = 586,326

def drag_to(direction):
	for i in range(2) :
		leftX, leftY = indistinct_position(random.randint(30, 50), random.randint(180,220))
		rightX, rightY = indistinct_position(random.randint(890, 910), random.randint(180,220)) 
		if direction :
			controller.moveTo(leftX,leftY, 0.3, controller.easeInOutQuad)
			time.sleep(random.uniform(0.18,0.25))
			controller.dragTo(rightX, rightY, 0.3 , controller.easeInOutQuad)
			time.sleep(random.uniform(0.18,0.25))
			
		else :
			controller.moveTo(rightX, rightY, 0.3, controller.easeInOutQuad)
			time.sleep(random.uniform(0.18,0.25))
			controller.dragTo(leftX,leftY, 0.3 , controller.easeInOutQuad)
			time.sleep(random.uniform(0.18,0.25))
		found_monster,_ = findTarget([30,40])
		if (found_monster or checkScene() != BATTLEFIELD) :
			return
		
			
def outerzone() :
	click(entranceX,entranceY)
	waitFor(ENGAGINGGATE)
	return checkScene()

def engaginggate() :
	click(startX,startY)	
	waitFor(BATTLEFIELD)
	return checkScene()
	
	
def fight() :
	if (not waitFor(BONUS)):
		return checkScene()
		
def bonus() :
	click(startX,startY)
	click(startX,startY)
	time.sleep(1.5)
	click(startX,startY)
	click(startX,startY)
	while not waitFor(BATTLEFIELD) :
		click(startX,startY)
	
def battlefield(depth):
	if depth == 3 :
		click(endX,endY)
		click(confirmX,comfirmY)
		waitFor(OUTERZONE)
		return checkScene()
	
	found_monster,position = findTarget([30,40])
	print(position)
	if (found_monster) :
		click(position[0],position[1])
		waitFor(FIGHT) 
		return checkScene()
	else :
		drag_to(depth % 2)
		if (checkScene() != BATTLEFIELD):
			return checkScene()
		return battlefield(depth + 1)

def main():
	now = checkScene()
	
	while (True):
		if (now == OUTERZONE) :
			now = outerzone()
		elif (now == ENGAGINGGATE) :
			now = engaginggate()
		elif (now == BATTLEFIELD) :
			now = battlefield(0)
		elif (now == FIGHT) :
			now = fight()
		elif (now == BONUS) :
			now = bonus()
		elif (now == INVITATION1 or now == INVITATION2):
			cancel_invitation()
			now = checkScene()
		else :
			time.sleep(0.1)
			now = checkScene()

	while(True):
		now = checkScene()
	
main()