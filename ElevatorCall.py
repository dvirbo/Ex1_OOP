class ElevatorCall:
    def __init__(self,
                 strElevatorCall: str,
                 timeStamp: float,
                 sourceOfCall: int,
                 destinationOfCall: int,
                 stateOfElevator: int,
                 idChosenElev: int) -> None:
        self.strElevatorCall = strElevatorCall
        self.timeStamp = timeStamp
        self.sourceOfCall = sourceOfCall
        self.destinationOfCall = destinationOfCall
        self.stateOfElevator = stateOfElevator
        self.idChosenElev = idChosenElev
