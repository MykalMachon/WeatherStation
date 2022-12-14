# Weather Station

a software suite to measure and utilize weather data at my apartment 🏔️🌡️

## Architecture

### Hardware and infrastructure

This will run on a [Raspberry Pi 3b](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) with a [Sense HAT add-on board](https://www.raspberrypi.com/products/sense-hat/) sitting in my appartment. That said, any Raspberry Pi with a 40 pin GPIO layout will work.

### Software

The Pi will be running the standard 32-bit version of RaspbianOS and a few applications to make this all work. 

| Application | Description                                                | Path          |
|-------------|------------------------------------------------------------|---------------|
| Observer    | Job server: captures weather info and sends notifications. | `./observer/` |
| Meteor      | REST server: provides a REST API for querying data.        | `./meteor/`   |
| Station     | Astro PWA: provides a pretty ui to view weather info.      | `./station/`  |

## Design choices

This section will discuss a few intentional design choices I've made for the project.

### Containerless

I've intentionally decided not to use docker or this project. I *love* me some containers, but given the performance constraints of a RPI 3, I figured it was not a great idea to run 3-4 relatively heavy processes on the little guy.

### Multiple applications

I originally wanted to look into microservices for this project, but after doing some more research it became clear they're sort of impractical for something this small in scale. If you're intersted in microservices, [this video](https://www.youtube.com/watch?v=zzMLg3Ys5vI&) was ultimately what made them "click" for me. Would highly recommend it. 

I've instead opted for a few small, distributed, applications. These are a lot *like* microservices (they server distinct purposes) but are not independently deployable and do suffer from some (albeit, intentional) coupling. Meteor relies on Observer, Station relies on Meteor. If I was to go full microservice for the weather station we would probably end up with 2x more very loosely coupled apps, and a less efficient system overall (see [this great article on excessive loose coupling](https://cedanet.com.au/antipatterns/excessive-loose-coupling.php)). 

By sticking with a few small apps I gain some ease in testing, maintenance, and simplicity that's inheirent in small apps, as well as the benefits in resiliency found in distributed systems. it seems like the right abstraction for this project (right now anyways.)
