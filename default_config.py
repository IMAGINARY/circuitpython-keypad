import board
from adafruit_hid.keycode import Keycode

# List of (pin, keycode) or (pin, [keycode1, keycode2, ...]) pairs that define
# the mapping between pins on the board and the keycodes that are sent through USB
keys = [
    (board.GP0, Keycode.LEFT_ARROW),
    (board.GP1, Keycode.RIGHT_ARROW),
    (board.GP2, [Keycode.SHIFT, Keycode.R]),
]

# True if the pin reads high when the key is pressed.
# False if the pin reads low (is grounded) when the key is pressed.
# All the pins must be connected in the same way.
value_when_pressed = False

# True if an internal pull-up or pull-down should be enabled on each pin.
# A pull-up will be used if value_when_pressed is False; a pull-down will be used if it is True.
# If an external pull is already provided for all the pins, you can set pull to False.
# However, enabling an internal pull when an external one is already present is not a problem;
# it simply uses slightly more current.
# Optional (default: true);
pull = True

# Scan keys no more often than interval to allow for debouncing. interval is in float seconds.
# Optional (default: 0.02)
interval = 0.02

# Digital pin to be used as output to signal that a key event has been sent.
# Set to None to disable.
led_pin = board.LED
