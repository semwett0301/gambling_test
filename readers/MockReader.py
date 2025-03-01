from pathlib import Path

from readers.ReadersInterface import ReaderInterface


class MockReader(ReaderInterface):
    def __init__(self, directory):
        self._directory = directory

        self._file_list = [f.name for f in Path(directory).iterdir() if f.is_file()]
        self._file_list.sort()

        self._counter = 0

    def get_screenshot(self):
        result_file = f"{self._directory}/{self._file_list[self._counter]}" if self._counter < len(self._file_list) else None
        self._counter += 1

        return result_file