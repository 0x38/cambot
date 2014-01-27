import RPi.GPIO as io
io.setmode(io.BCM)
 
in1_pin = 4
in2_pin = 17
in3_pin = 22
in4_pin = 23
enable_pin = 18
 
io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)

io.setup(in3_pin, io.OUT)
io.setup(in4_pin, io.OUT)

io.setup(enable_pin, io.OUT)

def forward():
    io.output(in1_pin, True)
    io.output(in2_pin, False)
    io.output(in3_pin, True)
    io.output(in4_pin, False)
    io.output(enable_pin, True)

def left():
    io.output(in1_pin, False)
    io.output(in2_pin, True)
    io.output(in3_pin, True)
    io.output(in4_pin, False)
    io.output(enable_pin, True)

def right():
    io.output(in1_pin, True)
    io.output(in2_pin, False)
    io.output(in3_pin, False)
    io.output(in4_pin, True)
    io.output(enable_pin, True)

def back():
    io.output(in1_pin, False)
    io.output(in2_pin, True)
    io.output(in3_pin, False)
    io.output(in4_pin, True)
    io.output(enable_pin, True)

def stop():
    io.output(enable_pin, False)
 
#while True:
#    cmd = raw_input("Command, f, l, r,b, s")
#    direction = cmd[0]
#    if direction == "f":
#        forward()
#    elif direction == "l": 
#        left()
#    elif direction == "r":
#        right()
#    elif direction == "b":
#        back()
#    else :
#        stop()
