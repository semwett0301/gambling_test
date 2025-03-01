from typing import Optional

from listeners.AnalyzerListenerInterface import AnalyzerListenerInterface
from dto.AnalyzeReport import AnalyzeReport, AnalyzeReportRequired
from readers.ReadersInterface import ReaderInterface
from utils.CvUtils import CvUtils
from utils.StrUtils import StrUtils


def _extract_params(text: str):
    speed = StrUtils.find_float("speed:\s*([\d.]+)", text)
    accuracy = StrUtils.find_float("accuracy:\s*([\d.]+)", text)
    total_score = StrUtils.find_float("total score:\s*([\d,]+)", text)

    return speed, accuracy, total_score


# Vocabulary that defines winnings
_WINNING_MAP: dict[str, bool] = {
    "you won": True,
    "you ranked 2nd": False
}

def _extract_winning(text: str) -> Optional[bool]:
    for key, value in _WINNING_MAP.items():
        if key in text:
            return value

    return None


class AnalyzerService:
    def __init__(self, reader: ReaderInterface):
        self._listeners: list[AnalyzerListenerInterface] = []
        self._reader: ReaderInterface = reader
        self._current_report: Optional[AnalyzeReport] = None

    def add_listener(self, listener: AnalyzerListenerInterface):
        self._listeners.append(listener)

    def remove_listener(self, listener: AnalyzerListenerInterface):
        self._listeners.remove(listener)

    def set_reader(self, reader: ReaderInterface):
        self._reader = reader

    def analyze(self):
        screenshot_filename = self._reader.get_screenshot()

        while screenshot_filename:
            text = CvUtils.extract_text(screenshot_filename)

            self._analyse_score(text)
            self._check_winnings(text)

            if self._current_report and self._current_report.is_winning is not None:
                self._update_listeners(self._current_report)
                self._current_report = None

            screenshot_filename = self._reader.get_screenshot()

    def _update_listeners(self, report: AnalyzeReportRequired):
        for listener in self._listeners:
            listener.update_report(report)

    def _check_winnings(self, text):
        is_winning = _extract_winning(text)

        if is_winning is not None and self._current_report is not None:
            self._current_report.is_winning = is_winning

    def _analyse_score(self, text):
        speed, accuracy, total_score = _extract_params(text)

        if speed and accuracy and total_score > 0:
            self._current_report = AnalyzeReport(speed=speed, accuracy=accuracy, is_winning=None)
