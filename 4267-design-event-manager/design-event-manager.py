from heapq import *

class EventManager:
    def __init__(self, events: list[list[int]]):
        self.heap = []
        self.active = {}

        for eventid, priority in events:
            heappush(self.heap, (-priority, eventid))
            self.active[eventid] = priority
        
    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.active[eventId] = newPriority
        heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.heap:
            neg_priority, eventid = heappop(self.heap)
            priority = -neg_priority

            if eventid in self.active and self.active[eventid] == priority:
                del self.active[eventid]
                return eventid

        return -1