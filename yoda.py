import RPi.GPIO as GPIO
import time
from pygame import mixer
from random import randint

RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24
SENSOR_PIR_PIN = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(SENSOR_PIR_PIN, GPIO.IN)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
PWM_FREQ_READ = GPIO.PWM(17, 50)
PWM_FREQ_GREEN = GPIO.PWM(22, 50)
PWM_FREQ_BLUE = GPIO.PWM(24, 50)

yodaQuotes = {
    1: 'amEndeHerrschaft_11.mp3',
    2: 'eatEat_09_6.mp3',
    3: 'furchtwuthass_11_6.mp3',
    4: 'goodMeal_03.mp3',
    5: 'maechtig_06_6.mp3',
    6: 'makingJedis_09.mp3',
    7: 'timeToEat_05_86.mp3',
    8: 'todRaffgier_18_4.mp3',
    9: 'vielzulernen_03_9.mp3',
}

quoteTiming = {
    1: 12,
    2: 10,
    3: 12,
    4: 4,
    5: 7,
    6: 10,
    7: 6,
    8: 19,
    9: 4
}

def motionDetected(channel):
    print('Someone wants candy!')
    PWM_FREQ_GREEN.start(100.0)
    randomAudio = randint(1, 9)
    mixer.music.set_volume(0.5)
    mixer.music.load('./sounds/' + yodaQuotes[randomAudio])
    mixer.music.play()
    time.sleep(quoteTiming[randomAudio])
    PWM_FREQ_GREEN.stop()

try:
    mixer.init(70100) # i had to add strange frequency for the mp3s to play correctly on the pi. normaly they are 44100 Hz
    GPIO.add_event_detect(SENSOR_PIR_PIN, GPIO.RISING, callback=motionDetected)
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    # aborting
    print('aborting...')
    time.sleep(0.5)
    GPIO.cleanup()
