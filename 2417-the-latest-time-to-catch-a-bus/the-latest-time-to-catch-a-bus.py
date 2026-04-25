class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        pass_index=0
        latest=0
        pass_set=set(passengers)
        for bus in buses:
            count=0
            while pass_index<len(passengers) and passengers[pass_index]<=bus and count<capacity:
                count+=1
                pass_index+=1

            if count<capacity:
                latest=bus
            else:
                latest=passengers[pass_index-1]-1
            while latest in pass_set:
                latest-=1
            
        return latest