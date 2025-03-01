from typing import Optional, Annotated

from pydantic import BaseModel, Field

class AnalyzeReport(BaseModel):
    speed: float
    accuracy: float
    is_winning: Optional[bool]

    def to_object(self):
        return {
            "speed": self.speed,
            "accuracy": self.accuracy,
            "is_winning": self.is_winning,
        }

AnalyzeReportRequired = Annotated[AnalyzeReport, Field(...)]
