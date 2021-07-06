# Documentation

## Raspberry prerequisites

`pip3 install adafruit-blinka`

`pip3 install adafruit-circuitpython-mcp3xxx`

`pip3 install adafruit-circuitpython-ssd1306`

`pip3 install pillow`

## Switches

     LCK    SGN
    I X I  I X I 
    I   I  I   I     [BUTTON]
    I   I  I   I
    
 `LCK`: up == off, down == on
 
 `SGN`: up == analog, down == digital
 
# Display header

`SDA CLK 3V GND [o]`
 
## Input/Output

|             |          |     |    |     | LED  | LED  |
|-------------|----------|-----|----|-----|------|------|
| **TRANSITOR** | GND      | GND | 3V | ch0 | Tube | FL   |
|             | e_tape B | GND | 3v | ch1 | GND  | FDR+ |