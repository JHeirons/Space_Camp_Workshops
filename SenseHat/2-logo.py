from sense_emu import SenseHat

sense = SenseHat()

def logo():
    G = (0, 255, 0)
    B = (0, 0, 255)
    W = (0, 0, 0)
    O = (255, 255, 255)
    logo = [
    O, O, O, O, O, O, O, O,  
    O, O, W, W, O, O, O, O,
    O, O, W, W, O, O, O, O,
    O, G, W, W, G, B, O, O,
    W, W, W, W, G, G, B, O,
    B, G, W, W, W, B, O, B,
    O, B, B, B, B, O, O, O,
    O, O, G, W, O, O, O, O,
    ]
    return logo

while True:
    sense.set_pixels(logo())