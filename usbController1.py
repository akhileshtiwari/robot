import evdev

controller = None
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)
    if device.name == 'PC Game Controller':
        controller = evdev.InputDevice(device.path)

for event in controller.read_loop():
    if event.type == 1 or event.type == 3:
        print("type:",event.type," code:", event.code," value:", event.value)
    #print(" end ")
    #if event.type == evdev.ecodes.EV_KEY:
     #   print(evdev.categorize(event))
    #else:
     #   print(event)