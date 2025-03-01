import os

import settings
from listeners.JsonWriterListener import AnalyzerWriterListener
from readers.MockReader import MockReader
from readers.ScreenshotReader import ScreenshotReader
from services.AnalyzerService import AnalyzerService

current_result = None

if __name__ == "__main__":
    # Creating the files
    os.makedirs(settings.RESULT_DIR, exist_ok=True)
    os.makedirs(settings.SCREEN_DIR, exist_ok=True)
    os.system(f"touch {settings.JSON_PATH}")

    # Reader define
    # reader = MockReader("./data/screenshots/2025-03-01_21-53-49")
    reader = ScreenshotReader()

    # Create analyzer with reader and listeners
    analyzer_service = AnalyzerService(reader)
    analyzer_service.add_listener(AnalyzerWriterListener(settings.JSON_PATH))

    # Start analyze process
    analyzer_service.analyze()




