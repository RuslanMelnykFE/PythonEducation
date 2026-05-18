import time

from random import randint
from settings import settings


while True:
    random_len = randint(settings.min_len, settings.max_len)
    line = settings.symbol * random_len

    print(line)

    time.sleep(settings.delay)
