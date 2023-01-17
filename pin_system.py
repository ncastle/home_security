import time
import explorerhat as ehat
import picture


# Lists for correct PIN and empty list to add current input to
correct_pin = [1, 2, 3, 4]
pin = []
pic_number = 0


def add_to_pin(channel, event):
    if channel > 4:  # only use channels 1-4 on explorer hat
        return
    if event == 'press':
        global pin
        pin.append(channel)
        ehat.light[channel-1].on()  # Blink corresponding LED
        time.sleep(0.05)
        ehat.light[channel-1].off()

# try, except, finally to run code and catch exceptions


def door_switch():
    print('activated')


while True:
    print('waiting for entry...')
    if not ehat.input.one.read():
        print('starting pin system')
        break

try:
    attempts = 0
    while True:
        print('Enter the pin for access!')
        while len(pin) < 4:  # Keep adding until 4 digits added
            ehat.touch.pressed(add_to_pin)
            time.sleep(0.05)
        if pin == correct_pin:  # Pin is correct, access granted
            print('PIN correct')
            for i in range(5):
                print(i)
                ehat.output.one.on()
                time.sleep(0.1)
                ehat.output.one.off()
                time.sleep(0.1)
        else:  # Pin is incorrect, increment attempts, display message
            attempts += 1
            if (attempts < 3):
                print('PIN incorect, try again')
                for i in range(5):
                    ehat.output.two.on()
                    time.sleep(0.1)
                    ehat.output.two.off()
                    time.sleep(0.1)
            else:  # Failed 3 times, so take picture of intruder
                print('Too many attempts, intruder!')
                picture.take_picture('intruder', pic_number)
                pic_number += 1
                attempts = 0
        pin = []

except KeyboardInterrupt:
    print('Ending program')

# except Exception:
#     print('Some error occurred!')
