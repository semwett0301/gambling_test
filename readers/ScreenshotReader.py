import os
import time

from readers.ReadersInterface import ReaderInterface
from datetime import datetime
import settings


class ScreenshotReader(ReaderInterface):
    def get_screenshot(self) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{settings.SCREEN_DIR}/screenshot_{timestamp}.png"

        os.system("adb shell screencap -p /sdcard/screen.png")
        os.system(f"adb pull /sdcard/screen.png {filename}")
        os.system("adb shell rm /sdcard/screen.png")

        print(f"Screenshot saved: {filename}", flush=True)

        # To create a gap between attempts
        time.sleep(1)

        return filename