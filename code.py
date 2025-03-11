import board
import digitalio
import asyncio
import keypad
import usb_hid

from adafruit_hid.keyboard import Keyboard

import default_config

try:
    import config

    print("config.py found, merging with default_config.py")
    config_keys = ["keys", "value_when_pressed", "pull", "interval", "led_pin"]
    for config_key in config_keys:
        if not hasattr(config, config_key):
            setattr(config, config_key, getattr(default_config, config_key))
except ImportError:
    print("No config.py found, using default_config.py")
    config = default_config

# For pins that only have a single keycode assigned (not a list of keycodes),
# wrap the keycode value into a list to unify the configuration.
config.keys = [
    (key[0], [key[1]]) if not isinstance(key[1], list) else key for key in config.keys
]

help()
print('board "{}": {}'.format(board.board_id, dir(board)))
print()

keyboard = Keyboard(usb_hid.devices)

pins = tuple(map(lambda key_config: key_config[0], config.keys))
pull = config.pull
interval = config.interval
if config.led_pin is not None:
    led = digitalio.DigitalInOut(config.led_pin)
    led.switch_to_output(value=False)
else:
    led = None

print("Current configuration:")
print("Keys:", config.keys)
print("Pin value when presses:", config.value_when_pressed)
print("Use internal pull-up/pull-down resistors:", pull)
print("Maximum poll interval:", interval)
print("Digital LED output pin:", config.led_pin if hasattr(config, "led_pin") else None)


async def blink(led):
    async def blink_internal():
        led.value = True
        await asyncio.sleep(0.05)
        led.value = False

    asyncio.create_task(blink_internal())


async def main():
    with keypad.Keys(
        pins, value_when_pressed=config.value_when_pressed, pull=pull, interval=interval
    ) as keys:
        while True:
            event = keys.events.get()
            if event:
                keycodes = config.keys[event.key_number][1]
                if event.pressed:
                    if led is not None:
                        await blink(led)
                    print("key(s) {} pressed".format(keycodes))
                    keyboard.press(*keycodes)
                elif event.released:
                    if led is not None:
                        await blink(led)
                    print("key(s) {} released".format(keycodes))
                    keyboard.release(*keycodes)
            await asyncio.sleep(0)


asyncio.run(main())
