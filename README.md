# Air Quality Monitoring System

This Python script is designed to run on a Raspberry Pi Zero W 2, and is for monitoring air quality and carbon dioxide (CO2) levels using an MH-Z19 sensor and sending the collected data to the Adafruit IO platform.

## Prerequisites

- Python 3.x
- [Adafruit_IO](https://github.com/adafruit/Adafruit_IO_Python) library
- [mh-z19](https://github.com/UedaTakeyuki/mh-z19) library

## Installation

1. Install the required libraries using the following commands:
   ```
   pip install Adafruit_IO
   pip install mh-z19
   ```

2. I'm using the Nova PM sensor. Make sure your PM sensor is connected to your system via a serial port (e.g., `/dev/ttyUSB0`). Adjust the `ser = serial.Serial('/dev/ttyUSB0')` line if your PM sensor is connected to a different serial port.

3. In this example, the MH-Z19c co2 sensor is connected using pwm. If you wish to connect it using UART, the code will have to be adjusted accordingly.

4. Set up an account on [Adafruit IO](https://io.adafruit.com/) and obtain your Adafruit IO key and username.

5. Update the `adafruit_key` and `adafruit_username` variables in the script with your Adafruit IO key and username:
   ```python
   # Set Adafruit IO key here
   adafruit_key = 'your_adafruit_io_key'

   # Set Adafruit IO username here
   adafruit_username = 'your_adafruit_io_username'
   ```

6. Create the feeds in Adafruit for the cooresponding data. In this example, there is a feed for co2 measurements with key co2, a feed for pm2.5 with key air-quality-pm-two-five, and a feed for pm10 with key air-quality-pm-ten.

## Usage

Run the script using the following command:
```
python main.py
```

The script will continuously read data from the MH-Z19 sensor and send the PM2.5, PM10, and CO2 measurements to your Adafruit IO dashboard every 30 seconds.

## Troubleshooting

If you encounter any issues while running the script, check the following:

- Ensure the MH-Z19 sensor is properly connected to your system.
- Confirm the correct serial port is specified in the script (`ser = serial.Serial('/dev/ttyUSB0')`).
- Verify that the Adafruit IO key and username are correctly set in the script.

## Notes

- The script uses the `mh_z19` library for reading CO2 measurements from the MH-Z19 sensor.
- The PM2.5 and PM10 measurements are obtained from a connected sensor through the specified serial port.

Feel free to modify the script according to your specific hardware setup or data reporting requirements.
