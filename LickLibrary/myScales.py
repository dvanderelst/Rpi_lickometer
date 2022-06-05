from LickLibrary import hx711
from LickLibrary import Settings
import time


# Place nothing on the scale, run the calibration.py and record the output. That is the offset.
# Place a known weight like 1kg(1000g) on the scale, record the output as w.
# Calculate the ratio
# ratio = (w - offset) / known weight

class myScales:
    def __init__(self):
        self.scale1 = hx711.HX711(dout=Settings.dout_pin1, pd_sck=Settings.pd_sck_pin1)
        self.scale2 = hx711.HX711(dout=Settings.dout_pin2, pd_sck=Settings.pd_sck_pin2)

    def calibrate(self, scale_nr=1, calibration_weight=355):
        if scale_nr == 1: scale = self.scale1
        if scale_nr == 2: scale = self.scale2

        scale.set_offset(0)
        scale.set_scale(1)

        print('Remove weight from scale')
        time.sleep(3)
        offset = scale.get_grams()

        print('place calibration weight of', calibration_weight, 'grams')
        time.sleep(3)
        w = scale.get_grams()

        ratio = (w - offset) / calibration_weight
        print('---- Results:')
        print('w', w)
        print('ratio', ratio)
        line1 = "offset%s = %.5f" % (scale_nr, offset)
        line2 = "ratio%s = %.5f" % (scale_nr, ratio)

        scale.set_offset(offset)
        scale.set_scale(ratio)
        test_measurement = scale.get_grams()

        print('Test Measurement:', test_measurement)
        print('-----')
        print('Add this code to Settings.py:')
        print(line1)
        print(line2)

    def measure(self, repeats=1):
        self.scale1.set_offset(Settings.offset1)
        self.scale1.set_scale(Settings.ratio1)

        self.scale2.set_offset(Settings.offset2)
        self.scale2.set_scale(Settings.ratio2)

        w1 = self.scale1.get_grams(repeats)
        w2 = self.scale2.get_grams(repeats)
        return w1, w2
