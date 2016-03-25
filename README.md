# raspbot
Robot Framework pybot extension to raspberry pi to show test results with leds

#Requirements
* Python 3.x
* Pip packages: [check requirements.txt](requirements.txt)
* Raspberry Pi
** Tested on Raspberry Pi 2

# Installation
* Install python3 and pip
* Clone this repository
* Run command `cd <path_to_repository> 6& pip install -r requirements.txt`

# Setup

GPIO:

* Green led output in PIN 38
* Red led output in PIN 40

#Usage

Run command `python raspbot.py <pybot_args>`

If tests are passing, green led is lit, otherwise red led is lit.
