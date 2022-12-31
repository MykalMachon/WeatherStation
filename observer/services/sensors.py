from sense_hat import SenseHat

def get_sensor_data():
  sense = SenseHat()
  
  return {
    "t_hum": sense.get_temperature(),
    "t_pres": sense.get_temperature_from_pressure(),
    "hum": sense.get_humidity(),
    "pres": sense.get_pressure() 
  }


