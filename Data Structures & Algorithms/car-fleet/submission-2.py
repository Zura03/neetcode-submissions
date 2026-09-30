class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps=[(p,s) for p,s in zip(position,speed)]
        fleets=0
        currtime=0
        for dist,speed in sorted(ps,reverse=True):
            desttime=float((target-dist))/speed
            if currtime<desttime:
                fleets+=1
                currtime=desttime
        return fleets