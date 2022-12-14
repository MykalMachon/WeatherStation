# Weather Station
a software suite to measure and utilize weather data at my apartment 🏔️🌡️

## Architecture

### Hardware and infrastructure
This will run on a [Raspberry Pi 3b](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) with a [Sense HAT add-on board](https://www.raspberrypi.com/products/sense-hat/) sitting in my appartment. That said, any Raspberry Pi with a 40 pin GPIO layout will work. 

### Software
- The pi will be running the standard 32-bit version of RaspbianOS. 
- A python program will collect temperature, pressure, humidity, and compass information and write it to a SQLlite database (short-running, CRON triggered).
- A python/flask program will provide access to data via a simple API server.
- An Astro website will query the python/flask API and make the stats all pretty. 
- There *may* be a setup script that automates the install process for all of this. 

## Design choices
This section will discuss a few intentional design choices I've made for the project.

### Containerless
I've intentionally decided not to use docker or this project. I *love* me some containers, but given the performance constraints of a RPI 3, I figured it was not a great idea to run 3-4 relatively heavy processes on the little guy. 

### Multiple microservices
I've never done much work with the "microservice" architecture outside of a few small projects at work and figured this would be a fun opportunity. 
I also wanted to experiment with multiple tech stacks, and saw this as a fun way to do that. 
