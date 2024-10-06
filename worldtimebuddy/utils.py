import os
from typing import List

def get_major_tz_from_env() -> List[str]:
    try:
        major_time_zones = os.environ.get("MAJOR_TIMEZONES", None)
        return list(major_time_zones[1:len(major_time_zones) - 1].split(','))
    except:
        return []