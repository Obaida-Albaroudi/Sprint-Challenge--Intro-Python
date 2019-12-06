# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    print("Base Class Vehicle")
    pass

class FlightVehicle(Vehicle):
    print("Vehicle -> FlightVehicle")
    pass

class GroundVehicle(Vehicle):
    print("Vehicle -> GroundVehicle")
    pass

class Starship(FlightVehicle):
    print("Vehicle -> FlightVehicle ->Starship")
    pass

class Car(GroundVehicle):
    print("Vehicle -> GroundVehicle -> Car")
    pass

class Motorcycle(GroundVehicle):
    print("Vehicle -> GroundVehicle -> Motorcycle")
    pass