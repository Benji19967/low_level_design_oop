from exceptions import SpotIsOccupiedError, WrongVehicleTypeError
from vehicle import Vehicle, VehicleType


class ParkingSpot:
    def __init__(
        self, spot_number: int, vehicle_type: VehicleType = VehicleType.CAR
    ) -> None:
        self._spot_number = spot_number
        self._vehicle_type = vehicle_type
        self._parked_vehicle: Vehicle | None = None

    @property
    def spot_number(self) -> int:
        return self._spot_number

    @property
    def vehicle_type(self) -> VehicleType:
        return self._vehicle_type

    @property
    def parked_vehicle(self) -> Vehicle | None:
        return self._parked_vehicle

    def is_available(self) -> bool:
        return self._parked_vehicle is None

    def is_available_for_vehicle(self, vehicle: Vehicle) -> bool:
        return self.is_available() and vehicle.vehicle_type == self._vehicle_type

    def park_vehicle(self, vehicle: Vehicle) -> None:
        if not vehicle.vehicle_type == self._vehicle_type:
            raise WrongVehicleTypeError
        if not self.is_available():
            raise SpotIsOccupiedError
        self._parked_vehicle = vehicle

    def unpark_vehicle(self) -> None:
        self._parked_vehicle = None

    def display_availability(self) -> None:
        print(
            f"Spot: {self._spot_number} is {'Available' if self.is_available() else 'Occupied'}"
        )
