__author__ = 'jjauhiainen'
import RPi.GPIO as GPIO
from robot import run_cli, run
from utils.formatter import convert_int, convert_bool
import time
import sys
class RasBot(object):
    red_led = None
    green_led = None
    auto_mode = True
    def __init__(self, red_led=40, green_led=38):
        self.red_led = convert_int(red_led)
        self.green_led = convert_int(green_led)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.red_led, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.green_led, GPIO.OUT, initial=GPIO.LOW)

    def run(self, *args):
        res = None
        #try:
        pybot_args = "".join(args[0])
        res = run(pybot_args)
        if self.auto_mode:
            if res != 0:
                GPIO.output(self.red_led, GPIO.HIGH)
                time.sleep(15)
                GPIO.output(self.red_led, GPIO.LOW)
        else:
            if res != 0:
                GPIO.output(self.red_led, GPIO.HIGH)
            ack = input("Press enter to confirm that you've seen the result, disable this message with setting auto_mode=True")
            if res != 0:
                GPIO.output(self.red_led, GPIO.LOW)
        GPIO.cleanup()

    def set_auto_mode(self, val):
        self.auto_mode = convert_bool(val)



def main():
    auto_mode = False
    print(sys.argv)
    if 'auto_mode' in sys.argv:
        auto_mode = True
        sys.argv.remove('auto_mode')
    pybot_args = sys.argv[1:]
    raspbot = RasBot()
    raspbot.set_auto_mode(auto_mode)
    raspbot.run(pybot_args)


if __name__ == "__main__":
    main()
