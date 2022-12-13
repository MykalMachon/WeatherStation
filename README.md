# Weather Station
a software suite to measure and utilize weather data at my apartment 🏔️🌡️

## Architecture

### Hardware and infrastructure
This will run on a [Raspberry Pi 3b](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) with a [Sense HAT add-on board](https://www.raspberrypi.com/products/sense-hat/) sitting in my appartment. That said, any Raspberry Pi with a 40 pin GPIO layout will work. 

### Software
- The pi will be running the standard 32-bit version of RaspbianOS. 
- A python program will collect temperature, pressure, humidity, and compass information and write it to a SQLlite database (short-running, CRON triggered).
- A node.js server will host a website that will display current and historical statistics about the temperature. 
- There *may* be a setup script that automates the install process for all of this. 
