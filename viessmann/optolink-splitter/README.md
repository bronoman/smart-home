# Content
This section contains the key config files needed to read out parameters from a Viessmann Vitotronic 200 (KW2) 
- `settings_ini.py` - is the core settings file of the optolink-splitter
- `poll_list.py` - this file contains my initial findings of parameters which have been confirmed on a running system via user menu and display outputs, pull requests welcome

# Addl. setup Notes
## Optolink Splitter
[https://github.com/philippoo66/optolink-splitter](https://github.com/philippoo66/optolink-splitter?tab=readme-ov-file#desktop_computerhardware-requirements)

Cable, available in Germany via TGA Shop (reliable, very fast drop-ship directly from Viessmann)

[https://tga-shop.de/Viessmann-Anschlussleitung-USB-Optolink-7856059/70058-7856059](https://tga-shop.de/Viessmann-Anschlussleitung-USB-Optolink-7856059/70058-7856059)

## Setup Instructions
best instructions:
[https://www.rustimation.eu/index.php/category/iot/viessmann-ohne-api/](https://www.rustimation.eu/index.php/category/iot/viessmann-ohne-api/)

note: this is running in a virtual environment:

[https://github.com/philippoo66/optolink-splitter/wiki/510-error:-externally‐managed‐environment-‐‐-venv](https://github.com/philippoo66/optolink-splitter/wiki/510-error:-externally%E2%80%90managed%E2%80%90environment-%E2%80%90%E2%80%90-venv)

## Protocol background
https://github.com/openv/openv/wiki/Protokoll-KW

## MQTT
MQTT is used to transfer information from the Optolink Splitter to openHAB

Mosquito Instructions:
[https://www.elektronik-kompendium.de/sites/raspberry-pi/2709041.htm](https://www.elektronik-kompendium.de/sites/raspberry-pi/2709041.htm)
