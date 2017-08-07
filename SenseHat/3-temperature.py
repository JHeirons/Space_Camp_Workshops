from sense_emu import SenseHat

sense = SenseHat()

while True:
    temp = sense.temp
    sense.show_message(str(temp))
    print(temp)