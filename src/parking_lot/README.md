# Parking lot

https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/parking-lot.md

## Requirements

1. The parking lot should have multiple levels, each level with a certain number of parking spots.
2. The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.
3. Each parking spot should be able to accommodate a specific type of vehicle.
4. The system should assign a parking spot to a vehicle upon entry and release it when the vehicle exits.
5. The system should track the availability of parking spots and provide real-time information to customers.
6. The system should handle multiple entry and exit points and support concurrent access.

## Things to remember

1. Create SINGLETON for classes that should only be used once
2. Create base class for vehicle, then you can create Car, Truck, ... objects and add functionality to them if needed
3. Add identifiers for Vehicles (eg. license plate), Level (eg. floor number) to be able to uniquely identify them
    - Helps for 
        - displaying objects
        - searching / finding objects
4. When you use exceptions for control flow, don't forge to `return` on successful paths