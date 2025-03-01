import json

from analyzer_listeners.AnalyzerListenerInterface import AnalyzerListenerInterface
from dto.AnalyzeReport import AnalyzeReportRequired

class AnalyzerWriterListener(AnalyzerListenerInterface):
    def __init__(self, file_path):
        self._file = open(file_path, "a")

    def update_report(self, report: AnalyzeReportRequired):
        self._file.write(json.dumps(report.to_object(), ensure_ascii=False) + '\n')
        self._file.flush()

    def __del__(self):
        self._file.close()
