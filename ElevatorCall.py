class ElevatorCall:
    def __init__(self, strElevatorCall: str, timeStamp: float, sourceOfCall: int, destinationOfCall: int,
                 stateOfElevator: int,
                 idChosenElev: int) -> None:
        self.strElevatorCall = strElevatorCall
        self.timeStamp = timeStamp
        self.sourceOfCall = sourceOfCall
        self.destinationOfCall = destinationOfCall
        self.stateOfElevator = stateOfElevator
        self.idChosenElev = idChosenElev
        self.direction = direction(self)


def direction(self):
    if self.destinationOfCall - self.sourceOfCall > 0:
        return 1
    else:
        return -1

def __str__(self) -> str:
        return f'''ElevatorCall : {self.strElevatorCall},timeStamp : {self.timeStamp} 
sourceOfCall : {self.sourceOfCall},destinationOfCall : {self.destinationOfCall}
stateOfElevator : {self.stateOfElevator},idChosenElev : {self.idChosenElev}'''

def __repr__(self) -> str:
        return f'''ElevatorCall : {self.strElevatorCall},timeStamp : {self.timeStamp}
sourceOfCall : {self.sourceOfCall},destinationOfCall : {self.destinationOfCall}
stateOfElevator : {self.stateOfElevator},idChosenElev : {self.idChosenElev}'''
