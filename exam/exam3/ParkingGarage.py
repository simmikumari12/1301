class ParkingGarage:
    def __init__(self, parking_levels):
        
        
        self.parking_levels = parking_levels

    def get_total_spaces(self):
       

        total_spaces = {'Normal': 0, 'Compact': 0, 'Oversize': 0}
        for level in self.parking_levels:
            for vehicle_type, spaces in level.get_total_spaces().items():
                total_spaces[vehicle_type] += spaces
        return total_spaces

    def get_remaining_spaces(self):
        
        
    
        remaining_spaces = {'Normal': 0, 'Compact': 0, 'Oversize': 0}
        for level in self.parking_levels:
            for vehicle_type, spaces in level.get_remaining_spaces().items():
                remaining_spaces[vehicle_type] += spaces
        return remaining_spaces

    def find_vehicle(self, license_plate):
        

        for idx, level in enumerate(self.parking_levels, start=1):
            if level.find_vehicle(license_plate):
                print(f"Vehicle with license plate {license_plate} is parked on level {idx}.")
                return
        print(f"No vehicle with license plate {license_plate} found in the parking garage.")

    def add_vehicle(self, vehicle):
        
        for idx, level in enumerate(self.parking_levels, start=1):
            if level.add_vehicle(vehicle):
                print(f"Vehicle with license plate {vehicle.get_license_plate()} was added to level {idx}.")
                return
        print(f"No available space for vehicle with license plate {vehicle.get_license_plate()}.")

    def remove_vehicle(self, license_plate):