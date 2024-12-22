class ParkingLevel:
    def __init__(self, total_spaces):
        
        
        self.total_spaces = total_spaces  # Total spaces for each vehicle type
        self.remaining_spaces = total_spaces.copy()  # Remaining spaces for each vehicle type
        self.vehicle_list = []  # List of vehicles parked on this level

    def get_total_spaces(self):
        

        return self.total_spaces

    def get_remaining_spaces(self):
        

        return self.remaining_spaces

    def find_vehicle(self, license_plate):
        

        return any(vehicle.get_license_plate() == license_plate for vehicle in self.vehicle_list)

    def add_vehicle(self, vehicle):
       

        vehicle_type = vehicle.get_vehicle_type()
        if self.remaining_spaces.get(vehicle_type, 0) > 0:
            self.vehicle_list.append(vehicle)
            self.remaining_spaces[vehicle_type] -= 1
            return True
        return False

    def remove_vehicle(self, license_plate):
       

        for vehicle in self.vehicle_list:
            if vehicle.get_license_plate() == license_plate:
                self.vehicle_list.remove(vehicle)
                self.remaining_spaces[vehicle.get_vehicle_type()] += 1
                return True
        return False