from picamera import PiCamera
from time import sleep

def main():
    camera = PiCamera()
    camera.rotation = 180 # Flip camera preview 180 degrees
    camera.start_preview()
    sleep(5)
    camera.stop_preview()
    pass

if __name__ == "__main__":
    main()
    pass