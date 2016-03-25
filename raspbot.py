__author__ = 'jjauhiainen'
import RPi.GPIO as GPIO
from robot import run_cli
from utils.formatter import convert_int
import time
class RasBot(object):
    red_led = None
    green_led = None

    def __init__(self, red_led=40, green_led=38):
        self.red_led = convert_int(red_led)
        self.green_led = convert_int(green_led)
        GPIO.setmode(GPIO.BOARD)
        GPIO(self.red_led, GPIO.OUT, initial=GPIO.LOW)
        GPIO(self.green_led, GPIO.OUT, initial=GPIO.LOW)

    def run(self):
        GPIO.output(self.red_led, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(self.red_led, GPIO.LOW)


def main():
    raspbot = RasBot()
    raspbot.run()


if __name__ == "__main__":
    main()
