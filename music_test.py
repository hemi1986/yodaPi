from pygame import mixer # Load the required library
from random import randint
import time

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

mixer.init(70100)
randomAudio = randint(1, 9);
mixer.music.load('./sounds/' + yodaQuotes[randomAudio])
mixer.music.play()
time.sleep(quoteTiming[randomAudio])
print('ende')
exit()

while 1:
    pass