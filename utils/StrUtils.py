import re
from typing import Optional


class StrUtils:
    @staticmethod
    def find_float(match_pattern: str, match_str: str) -> Optional[float]:
        matcher = re.search(match_pattern, match_str)
        try:
            return float(matcher.group(1).replace(',', ''))
        except:
            return None
