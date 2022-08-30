import board
import digitalio
import asyncio
import keypad
import usb_hid

from adafruit_hid.keyboard import Keyboard

import config

help()
print('board "{}": {}'.format(board.board_id, dir(board)))
print()

keyboard = Keyboard(usb_hid.devices)

pins = tuple(map(lambda key_config: key_config[0], config.keys))
pull = config.pull if hasattr(config, "pull") else True
interval = config.interval if hasattr(config, "interval") else 0.02
if hasattr(config, "led_pin"):
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
                keycode = config.keys[event.key_number][1]
                if event.pressed:
                    if led is not None:
                        await blink(led)
                    print("key {} pressed".format(keycode))
                    keyboard.press(keycode)
                elif event.released:
                    if led is not None:
                        await blink(led)
                    print("key {} released".format(keycode))
                    keyboard.release(keycode)
            await asyncio.sleep(0)


asyncio.run(main())
