import RPi.GPIO as GPIO
import time
import random
import logging
FORMAT = '[%(asctime)s]-[%(funcName)s]-[%(levelname)s] - %(message)s'
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT
)


def turnOnAndOff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)
    logging.info("LED ON")
    GPIO.output(18, True)
    time.sleep(2)
    logging.info("LED OFF")
    GPIO.output(18, False)
    pass  # end turnOnAndOff()


def flashLoop():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)
    DELAYED_SECONDS = 1
    while True:
        GPIO.output(18, True)
        logging.info("LED ON")
        time.sleep(DELAYED_SECONDS)
        GPIO.output(18, False)
        logging.info("LED OFF")
        time.sleep(DELAYED_SECONDS)
        pass  # end while
    pass  # end flashLoop()


def randomFlashLoop():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)
    DELAYED_SECONDS = 1
    FLASH_STATE = [True, False]
    while True:
        state = random.choice(FLASH_STATE)
        if state == True:
            GPIO.output(18, state)
            logging.info("LED ON")
            time.sleep(DELAYED_SECONDS)
            pass  # end if
        else:
            GPIO.output(18, state)
            logging.info("LED OFF")
            time.sleep(DELAYED_SECONDS)
            pass  # end else
        pass  # end while
    pass  # end randomFlashLoop()


if __name__ == "__main__":
    # turnOnAndOff()
    # flashLoop()
    randomFlashLoop()
    pass
