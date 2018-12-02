import gpiozero

led_pins = [4,17,24,25,18,23,27,22]

leds = []

for i in led_pins:
    leds.append(gpiozero.LED(i))

def show_binary(leds, number):
    for i in leds:
        i.off()
    if number > 2**len(leds)-1:
        return
    else:
        for i in range(1,len(leds)+1,1):
            if number%(2**i) != 0:
                number -= number%(2**i)
                leds[i-1].on()

number = 0
while True:
    number += 1
    if number > 255:
        number = 0
    show_binary(leds,number)
    time.sleep(1)
