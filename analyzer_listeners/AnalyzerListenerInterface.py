from abc import ABC, abstractmethod

from dto.AnalyzeReport import AnalyzeReportRequired


class AnalyzerListenerInterface(ABC):
    @abstractmethod
    def update_report(self, report: AnalyzeReportRequired):
        pass

