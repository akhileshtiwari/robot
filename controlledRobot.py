import evdev
from gpiozero import Robot
import time

myRob = Robot(left=(7,8), right=(9,10))

controller = None
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    if device.name == 'PC Game Controller':
        controller = evdev.InputDevice(device.path)

for event in controller.read_loop():
    if event.type == 3:
        if event.code == 1: # Up and Down arrows
            if event.value == 0:
                print("Robot go forward:")
                myRob.forward()
            elif event.value == 255:
                print("Robot go backward")
                myRob.backward()
            else :
                print("Robot stopped")
                myRob.stop()
        if event.code == 0:
            if event.value == 0:
                print("Robot go left")
                myRob.left()
            if event.value == 255:
                print("Robot turn right")
                myRob.right()
            if event.value == 128:
                print("Robot no horizontal")
                myRob.stop()