import time

from settings import settings


while True:
    print("\n--- Інформація ---")
    print("app_name = ", settings.app_name)
    print("filename = ", settings.filename)

    time.sleep(2)
