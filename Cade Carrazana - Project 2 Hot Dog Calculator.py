# Enter the inputs here
number_of_people = int(input("Enter number of people: "))
number_of_hotdogs_per_person = int(input("Enter number of hot dogs: "))

# The assumptions
NUMBER_OF_HOTDOGS_PER_PACKAGE = 10
NUMBER_OF_BUNS_PER_PACKAGE = 8

# Equations
total_number_of_hotdogs = number_of_people * number_of_hotdogs_per_person

number_of_hotdog_packages_needed = total_number_of_hotdogs // NUMBER_OF_HOTDOGS_PER_PACKAGE
number_of_hotdog_buns_needed = total_number_of_hotdogs // NUMBER_OF_BUNS_PER_PACKAGE
number_of_hotdogs_left_over = total_number_of_hotdogs % NUMBER_OF_HOTDOGS_PER_PACKAGE
number_of_hotdog_buns_left_over = total_number_of_hotdogs % NUMBER_OF_BUNS_PER_PACKAGE

# What gets printed after entering the integers
print("Minimum number of packages of hot dogs required =", number_of_hotdog_packages_needed)
print("Minimum number of packages of hot dog buns required =", number_of_hotdog_buns_needed)
print("Number of hot dogs left over =", number_of_hotdogs_left_over)
print("Number of hot dogs buns left over =", number_of_hotdog_buns_left_over)