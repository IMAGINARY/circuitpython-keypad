# CircuitPython Keypad

This project simplifies the creation of custom USB HID keyboards.

## Hardware requirements

- A
  [microcontroller board compatible with CircuitPython](https://circuitpython.org/downloads).
- Hardware buttons or any electrical component that can close and open an
  electrical connection.
- Some wires and connectors to connect the buttons to the board.

## Installation

Download [CircuitPython 9.x](https://circuitpython.org) and flash it to your
board (CircuitPython versions higher than 9.x may also work, but compatibility
is not guaranteed). Your board will now appear as a USB mass storage device
called `CIRCUITPY` volume.

### Dependencies

This project requires the CircuitPython packages listed in the `requirements.txt` file.
These packages can be manually extracted from the
[Adafruit CircuitPython library bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle)
and copied to the `lib` folder of the `CIRCUITPY` volume.
However, it is recommended to use the `circup` tool via the `uv` package manager to install
(and update) the dependencies automatically:

```bash
uvx circup install -r requirements.txt
```

### Source code

Copy the contents of this folder to the `CIRCUITPY` volume:

```bash
cp -r * /path/to/CIRCUITPY
```

The project should now be running on your board using the default configuration.

## Configuration

The file `default_config.py` contains the default configuration of the project.
You can customize the configuration by creating a `config.py` file next to `default_config.py`.
It is recommended to copy the default configuration and modify it according to your needs.

See the `default_config.py` file for a detailed description of the available configuration options.

## Development

This project uses the `uv` package manager to manage development dependencies:

```bash
uv sync
```

Automatic code formatting and linting can be achieved by running

```bash
uvx ruff format
```

respectively

```bash
uvx ruff check
```

## Debugging

The device outputs diagnostic messages to the serial console offered by your
board.

## Credits

Developed by Christian Stussak for IMAGINARY gGmbH.

## License

Copyright 2022 IMAGINARY gGmbH

Licensed under the MIT license (see the [`LICENSE`](LICENSE) file).
