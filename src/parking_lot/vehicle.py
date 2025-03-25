from abc import ABC
from enum import Enum


class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcyle"
    TRUCK = "Truck"


class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type: VehicleType) -> None:
        self._license_plate = license_plate
        self._vehicle_type = vehicle_type

    @property
    def vehicle_type(self) -> VehicleType:
        return self._vehicle_type

    @property
    def license_plate(self) -> str:
        return self._license_plate

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self._license_plate == other._license_plate


class Car(Vehicle):
    def __init__(self, license_plate: str) -> None:
        super().__init__(
            license_plate=license_plate,
            vehicle_type=VehicleType.CAR,
        )


class Motorcycle(Vehicle):
    def __init__(self, license_plate: str) -> None:
        super().__init__(
            license_plate=license_plate,
            vehicle_type=VehicleType.MOTORCYCLE,
        )


class Truck(Vehicle):
    def __init__(self, license_plate: str) -> None:
        super().__init__(
            license_plate=license_plate,
            vehicle_type=VehicleType.TRUCK,
        )
