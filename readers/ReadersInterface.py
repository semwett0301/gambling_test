from abc import ABC, abstractmethod
from typing import Optional


class ReaderInterface(ABC):
    @abstractmethod
    def get_screenshot(self) -> Optional[str]:
        pass