from parking_spot import ParkingSpot
from vehicle import Car, Motorcycle, Truck, VehicleType

from parking_lot import Level, ParkingLot

if __name__ == "__main__":
    levels = [
        Level(
            floor=0,
            parking_spots=[
                ParkingSpot(spot_number=0, vehicle_type=VehicleType.CAR),
                ParkingSpot(spot_number=1, vehicle_type=VehicleType.CAR),
                ParkingSpot(spot_number=2, vehicle_type=VehicleType.MOTORCYCLE),
                ParkingSpot(spot_number=3, vehicle_type=VehicleType.MOTORCYCLE),
                ParkingSpot(spot_number=4, vehicle_type=VehicleType.TRUCK),
            ],
        ),
        Level(
            floor=1,
            parking_spots=[
                ParkingSpot(spot_number=0, vehicle_type=VehicleType.CAR),
                ParkingSpot(spot_number=1, vehicle_type=VehicleType.CAR),
                ParkingSpot(spot_number=2, vehicle_type=VehicleType.TRUCK),
                ParkingSpot(spot_number=3, vehicle_type=VehicleType.TRUCK),
                ParkingSpot(spot_number=4, vehicle_type=VehicleType.TRUCK),
            ],
        ),
    ]
    parking_lot = ParkingLot(levels=levels)
    parking_lot = ParkingLot(levels=levels)
    parking_lot.display_availability()
    parking_lot.park_vehicle(vehicle=Car(license_plate="HJKHS"))
    parking_lot.park_vehicle(vehicle=Car(license_plate="POSGH"))
    parking_lot.park_vehicle(vehicle=Truck(license_plate="HJKHL"))
    parking_lot.park_vehicle(vehicle=Truck(license_plate="TYUIQ"))
    parking_lot.park_vehicle(vehicle=Motorcycle(license_plate="JKOIO"))
    parking_lot.park_vehicle(vehicle=Motorcycle(license_plate="YUIOA"))
    parking_lot.unpark_vehicle(vehicle=Car(license_plate="POSGH"))
    parking_lot.display_availability()
