# Load plate numbers
# Mondays, Wednesdays and Fridays for odd plates
# Tuesdays, Thurdays and Saturdays for enven plates
# Sundays for all plates
car_plates = ["AB1234", "CD5678", "EF901", "GH234", "JK567", "LM8901"]
odd_days = ["MO", "WE", "FR"]
even_days = ["TU", "TH", "SA"]
pass_list = []
today = input("Enter day of week (SUnday to SAturday): ")
for plate in car_plates:
    last_digit = int(plate[-1])
    if today in odd_days and last_digit % 2 != 0:
        pass_list.append(plate)
    elif today in even_days and last_digit % 2 == 0:
        pass_list.append(plate)
    elif today == "SU":
        pass_list.append(plate)
print(pass_list)
