import random
year = int(input("Please enter the model year of your choice: "))
make = int(input("Please enter the maker of the vehicke: "))
model = input("Please enter the model of the vehicle: ")

letter_a = chr(random.randint(65,90))
letter_b = chr(random.randint(65,90))
letter_c = chr(random.randint(65,90))

digits = random.randint(1000, 9999)

license_plate = letter_a +letter_b +letter_c + digits

car = {
    'Year': year,
    'Make': make,
    'Model': model,
    'Plate': license_plate
}

print(f'The licensce plate for your {car["Year"]} {car["Make"]} is {car["Plate]}"]}')