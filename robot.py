import motor
import keyhandler
import time
import thread

class robostate :
    quit = moving = False
    movetime = time.time()

def stopthread(state):
#    print moving
    while not state.quit :
        #print "time: ", time.time(), " moved:", movetime
#	print moving
        if time.time() > state.movetime + 0.1 :
#                motor.stop()
                state.moving = False
        time.sleep(0.1)

def move(movecall, state):
    state.moving = True
    state.movetime = time.time()
    print "moving at ", time.time(), " movetime ", state.movetime
    movecall()
    time.sleep(0.1)
#    stopthread()

state = robostate()
print "Starting"
thread.start_new_thread(stopthread, (state,))
print "Started"

while not state.quit:
    key = keyhandler.getch()
    print key
    keyNum = ord(key)
    print keyNum
    if keyNum == 65:
	print "up"
        move(motor.forward, state)
    elif keyNum == 66:
        print "down"
        move(motor.back, state)
    elif keyNum == 67:
        print "right"
        move(motor.right, state)
    elif keyNum == 68:
	print "left"
        move(motor.left, state)
    elif key == 'q':
        quit = True
    else :
   	print "press q to quit"
    time.sleep(0.1)

motor.stop()
