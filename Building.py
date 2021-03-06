from Elevator import Elevator


class Building:
    def __init__(self, minFloor: int, maxFloor: int, elevators: list) -> None:
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.elevators = []
        for elevator in elevators:
            elv = Elevator(elevator['_id'],
                           elevator['_speed'],
                           elevator['_minFloor'],
                           elevator['_maxFloor'],
                           elevator['_closeTime'],
                           elevator['_openTime'],
                           elevator['_startTime'],
                           elevator['_stopTime']
                           )
            self.elevators.append(elv)

