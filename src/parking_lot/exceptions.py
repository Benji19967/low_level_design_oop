class NoMoreFreeSpotsError(Exception):
    """
    There are no more free spots
    """

    pass


class WrongVehicleTypeError(Exception):
    """
    Wrong vehicle type
    """

    pass


class SpotIsOccupiedError(Exception):
    """
    Spot is already occupied
    """

    pass


class VehicleNotFoundError(Exception):
    """
    Vehicle not found
    """

    pass
