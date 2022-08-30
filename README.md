# CircuitPython Keypad

This project simplifies the creation of custom USB HID keyboards.

## Hardware requirements

- A
  [microcontroller board compatible with CircuitPython](https://circuitpython.org/downloads).
- Hardware buttons or any electrical component that can close and open an
  electrical connection.
- Some wires and connectors to connect the buttons to the board.

## Installation

- Download [CircuitPython 7.x](https://circuitpython.org) and flash it to your
  board (CircuitPython versions higher than 7.x may also work, but compatibility
  is not guaranteed). Your board will now appear as a USB mass storage device
  called `CIRCUITPY` volume.
- Download the
  [Adafruit CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle)
  compatible with your CircuitPython version, extract it and copy the
  `adafruit_hid`, `asyncio` and `adafruit_ticks` modules into the `lib` folder
  of the `CIRCUITPY` volume.
- Copy the `.py` files form this folder onto the `CIRCUITPY` volume.
- Customize the `config.py` file according to your board and needs, e.g. assign
  your board's GPIO pins to keystrokes.

## Debugging

The device outputs diagnostic messages to the serial console offered by your
board.

## Credits

Developed by Christian Stussak for IMAGINARY gGmbH.

## License

Copyright 2022 IMAGINARY gGmbH

Licensed under the MIT license (see the [`LICENSE`](LICENSE) file).