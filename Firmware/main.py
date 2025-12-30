import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.extensions.encoder import RotaryEncoder

keyboard = KMKKeyboard()

# ------------------------
# Keys (Direct GPIO -> GND)
# Layout:
# K1 K2 K3
# K4 K5 K6
# ------------------------
keyboard.matrix = KeysScanner(
    pins=[
        board.D2,    # Top-left
        board.D10,   # Top-middle
        board.D4,    # Top-right
        board.D0,    # Bottom-left
        board.D3,    # Bottom-middle
        board.D1,    # Bottom-right
    ],
    value_when_pressed=False,
)

# Change these to whatever you want later
keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E,
        KC.A, KC.S, KC.D,
    ]
]

# ------------------------
# Rotary Encoder (EC11)
# A -> GP27
# B -> GP26
# SW -> GP28
# ------------------------
encoder = RotaryEncoder(
    clk=board.GP27,   # A
    dt=board.GP26,    # B
    sw=board.GP28,    # Push button
    value_when_pressed=False,
)

encoder.keymap = {
    "clockwise": KC.VOLU,
    "counter_clockwise": KC.VOLD,
    "pressed": KC.MUTE,
}

keyboard.extensions.append(encoder)

# ------------------------
# Start Keyboard
# ------------------------
if __name__ == "__main__":
    keyboard.go()
