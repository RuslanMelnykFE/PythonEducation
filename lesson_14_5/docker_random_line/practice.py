import time

from random import randint
from settings import settings


while True:
    random_len = randint(settings.min_len, settings.max_len)
    line = ""

    for i in range(random_len):
        line += str(settings.symbol)

    print(line)

    time.sleep(settings.delay)
