import sys
import time
import datetime
import pydantic


start_time = datetime.datetime.now()


while True:
    print("\n--- Інформація ---")
    print("Версія Python:", sys.version)
    print("hello")
    print("Версія pydantic:", pydantic.__version__)
    print("Час старту програми:", start_time)

    time.sleep(2)
