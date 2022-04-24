"""
https://leetcode.com/problems/design-underground-system/
"""
from typing import Dict, Tuple, List
from statistics import mean
from collections import defaultdict, namedtuple

CheckInInfo = namedtuple('CheckInInfo', ['time', 'station'])


class UndergroundSystem:
    def __init__(self):
        self.check_in_info_by_customer_id: Dict[int, CheckInInfo] = {}
        self.travel_time_by_station_to_station: Dict[Tuple[str, str], List[int]] = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_info_by_customer_id.update({id: CheckInInfo(station=stationName, time=t)})

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_info = self.check_in_info_by_customer_id.pop(id)
        self.travel_time_by_station_to_station[check_in_info.station, stationName].append(t - check_in_info.time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return mean(self.travel_time_by_station_to_station[startStation, endStation])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
