from exceptions import NoMoreFreeSpotsError, VehicleNotFoundError
from parking_spot import ParkingSpot
from vehicle import Vehicle


class Level:

    DEFAULT_NUMBER_OF_SPOTS = 10

    def __init__(
        self, floor: int, parking_spots: list[ParkingSpot] | None = None
    ) -> None:
        self._floor = floor
        self._parking_spots = parking_spots or [
            ParkingSpot(i) for i in range(self.DEFAULT_NUMBER_OF_SPOTS)
        ]

    @property
    def num_spots(self) -> int:
        return len(self._parking_spots)

    def park_vehicle(self, vehicle: Vehicle) -> None:
        for spot in self._parking_spots:
            if spot.is_available_for_vehicle(vehicle=vehicle):
                spot.park_vehicle(vehicle=vehicle)
                return
        raise NoMoreFreeSpotsError

    def unpark_vehicle(self, vehicle: Vehicle) -> None:
        for spot in self._parking_spots:
            if spot.parked_vehicle == vehicle:
                spot.unpark_vehicle()
                return
        raise VehicleNotFoundError

    def display_availability(self) -> None:
        print("Level {self.floor} availability:")
        for spot in self._parking_spots:
            spot.display_availability()


class ParkingLot:

    _instance = None

    def __init__(self, levels: list[Level]) -> None:
        if ParkingLot._instance is not None:
            raise Exception("Instance already exists")
        ParkingLot._instance = self
        self._levels = levels

    @property
    def capacity(self) -> int:
        return sum(level.num_spots for level in self._levels)

    def park_vehicle(self, vehicle: Vehicle) -> None:
        for level in self._levels:
            try:
                level.park_vehicle(vehicle=vehicle)
                return
            except NoMoreFreeSpotsError:
                continue
        raise NoMoreFreeSpotsError

    def unpark_vehicle(self, vehicle: Vehicle) -> None:
        for level in self._levels:
            try:
                level.unpark_vehicle(vehicle=vehicle)
                return
            except VehicleNotFoundError:
                continue
        raise VehicleNotFoundError

    def display_availability(self) -> None:
        print("Parking lot availability:")
        for level in self._levels:
            level.display_availability()
