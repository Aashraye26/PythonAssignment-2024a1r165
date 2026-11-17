# Food Rescue and Surplus Donation Coordination System

# Question 1: Record One Donation and Estimate Meal Support

donor_name = input("Enter donor name: ")
food_category = input("Enter food category: ")
quantity_kg = float(input("Enter quantity in kilograms: "))
remaining_hours = int(input("Enter remaining hours before consumption: "))

donor_name = donor_name.strip().title()
food_category = food_category.strip().title()

print("\n--- Data Type Information ---")
print("Quantity data type:", type(quantity_kg))
print("Remaining hours data type:", type(remaining_hours))

meal_size_kg = 0.40
estimated_meals = int(quantity_kg // meal_size_kg)

print("\n--- Food Donation Summary ---")
print("Donor Name:", donor_name)
print("Food Category:", food_category)
print("Quantity:", quantity_kg, "kg")
print("Remaining Time:", remaining_hours, "hours")
print("Estimated Complete Meals:", estimated_meals)


# Question 2: Process Multiple Donations

donations = []
food_categories = set()

critical_count = 0
priority_count = 0
normal_count = 0

meal_size_kg = 0.40

print("===== FOOD RESCUE AND SURPLUS DONATION SYSTEM =====")
print("Enter DONE as donor name to finish entering donations.\n")

while True:

    donor_name = input("Enter donor name (or DONE): ").strip()

    if donor_name.upper() == "DONE":
        break

    food_category = input("Enter food category: ").strip()

    quantity_kg = float(input("Enter quantity in kilograms: "))
    remaining_hours = int(input("Enter remaining hours: "))

    if quantity_kg <= 0 or remaining_hours <= 0:
        print("\nInvalid donation! Quantity and remaining hours must be positive.")
        print("Please enter the next donation.\n")
        continue

    donor_name = donor_name.title()
    food_category = food_category.title()

    if remaining_hours <= 4:
        priority = "CRITICAL"
        critical_count += 1

    elif remaining_hours <= 12:
        priority = "PRIORITY"
        priority_count += 1

    else:
        priority = "NORMAL"
        normal_count += 1

    estimated_meals = int(quantity_kg // meal_size_kg)

    # Store donation as a dictionary
    donation = {
        "donor_name": donor_name,
        "food_category": food_category,
        "quantity_kg": quantity_kg,
        "remaining_hours": remaining_hours,
        "priority": priority,
        "estimated_meals": estimated_meals
    }

    donations.append(donation)
    food_categories.add(food_category)

    print("Donation recorded successfully!")
    print("Pickup Priority:", priority)
    print("Estimated Meals:", estimated_meals)
    print()

print("\n========== DONATION SUMMARY ==========")

if len(donations) == 0:
    print("No valid donations were recorded.")

else:
    total_quantity = 0
    total_meals = 0

    for donation in donations:
        total_quantity += donation["quantity_kg"]
        total_meals += donation["estimated_meals"]

    print("Total Valid Donations:", len(donations))
    print("Total Food Quantity:", total_quantity, "kg")
    print("Total Estimated Meals:", total_meals)

    print("\nPriority Statistics:")
    print("CRITICAL Donations:", critical_count)
    print("PRIORITY Donations:", priority_count)
    print("NORMAL Donations:", normal_count)

    print("\nUnique Food Categories:")
    for category in sorted(food_categories):
        print("-", category)

    print("\nRecorded Donations:")
    for donation in donations:
        print(
            donation["donor_name"],
            "|", donation["food_category"],
            "|", donation["quantity_kg"], "kg",
            "|", donation["priority"]
        )

print("\n===== APPLICATION ENDED =====")

# Question 3: Object-Oriented Programming

class FoodDonation:


    organization_name = "Community Food Rescue"

    def __init__(self, donation_id, donor_name, food_category,
                 quantity_kg, hours_to_expiry):

        self.donation_id = donation_id
        self.donor_name = donor_name
        self.food_category = food_category
        self.quantity_kg = quantity_kg
        self.hours_to_expiry = hours_to_expiry

    def estimated_meals(self):
        meal_size_kg = 0.40
        return int(self.quantity_kg / meal_size_kg)

    def priority_level(self):

        if self.hours_to_expiry <= 4:
            return "CRITICAL"

        elif self.hours_to_expiry <= 12:
            return "PRIORITY"

        else:
            return "NORMAL"

    def display_summary(self):

        print("\n--- Donation Summary ---")
        print("Organization:", FoodDonation.organization_name)
        print("Donation ID:", self.donation_id)
        print("Donor Name:", self.donor_name)
        print("Food Category:", self.food_category)
        print("Quantity:", self.quantity_kg, "kg")
        print("Remaining Hours:", self.hours_to_expiry)
        print("Estimated Meals:", self.estimated_meals())
        print("Pickup Priority:", self.priority_level())

    def __str__(self):

        return (
            f"Donation ID: {self.donation_id} | "
            f"Donor: {self.donor_name} | "
            f"Category: {self.food_category} | "
            f"Priority: {self.priority_level()}"
        )



donation1 = FoodDonation(
    101, "Green Oven Bakery", "Baked Food", 8.5, 3
)

donation2 = FoodDonation(
    102, "Fresh Mart", "Vegetables", 12.0, 8
)

print("===== FOOD RESCUE SYSTEM =====")

donation1.display_summary()
donation2.display_summary()

# Display concise object descriptions
print("\n--- Object Descriptions ---")
print(donation1)
print(donation2)


# Question 4: Functions and Modules

import time

from rescue_utils import (
    calculate_meals,
    classify_priority,
    summarize_donations
)

class FoodDonation:

    organization_name = "Community Food Rescue"

    def __init__(self, donation_id, donor_name, food_category,
                 quantity_kg, hours_to_expiry):

        self.donation_id = donation_id
        self.donor_name = donor_name.strip().title()
        self.food_category = food_category.strip().title()
        self.quantity_kg = quantity_kg
        self.hours_to_expiry = hours_to_expiry

    def estimated_meals(self, meal_size_kg=0.40):
        return calculate_meals(
            self.quantity_kg,
            meal_size_kg=meal_size_kg
        )

    def priority_level(self):
        return classify_priority(self.hours_to_expiry)

    def display_summary(self):

        print("\nDonation ID:", self.donation_id)
        print("Donor:", self.donor_name)
        print("Category:", self.food_category)
        print("Quantity:", self.quantity_kg, "kg")
        print("Estimated Meals:", self.estimated_meals())
        print("Priority:", self.priority_level())

    def __str__(self):

        return (
            f"ID: {self.donation_id} | "
            f"Donor: {self.donor_name} | "
            f"Category: {self.food_category} | "
            f"Priority: {self.priority_level()}"
        )

donations = []
donation_id = 101

print("===== FOOD RESCUE AND SURPLUS DONATION SYSTEM =====")
print("Enter DONE as donor name to finish.\n")

while True:

    donor_name = input("Enter donor name (or DONE): ").strip()

    if donor_name.upper() == "DONE":
        break

    food_category = input("Enter food category: ").strip()
    quantity_kg = float(input("Enter quantity in kg: "))
    hours_to_expiry = int(input("Enter remaining hours: "))

    # Validate donation
    if quantity_kg <= 0 or hours_to_expiry <= 0:
        print("Invalid donation! Values must be positive.\n")
        continue

    donation = FoodDonation(
        donation_id,
        donor_name,
        food_category,
        quantity_kg,
        hours_to_expiry
    )

    donations.append(donation)
    donation_id += 1

    print("Donation recorded successfully!")
    print("Pickup Priority:", donation.priority_level())
    print()


print("\n===== FINAL DONATION REPORT =====")

start_time = time.time()

sorted_donations = sorted(
    donations,
    key=lambda donation: donation.hours_to_expiry
)

summary = summarize_donations(
    donations,
    meal_size_kg=0.40
)

end_time = time.time()

print("\nDonations Sorted by Urgency:")

for donation in sorted_donations:
    print(donation)

print("\nTotal Donations:", summary["total_donations"])
print("Total Quantity:", summary["total_quantity"], "kg")
print("Total Estimated Meals:", summary["total_meals"])

print("\nPriority Counts:")

for priority, count in summary["priority_counts"].items():
    print(priority, ":", count)

print("\nUnique Food Categories:")

for category in sorted(summary["food_categories"]):
    print("-", category)

processing_time = end_time - start_time

print("\nReport Processing Time:",
      format(processing_time, ".6f"), "seconds")

print("\n===== APPLICATION ENDED =====")

# Question 5: File Handling and Exception Handling

import time

from rescue_utils import (
    calculate_meals,
    classify_priority,
    summarize_donations,
    save_donation,
    load_donations
)


class FoodDonation:
    organization_name = "Community Food Rescue"

    def __init__(self, donation_id, donor_name, food_category,
                 quantity_kg, hours_to_expiry):
        self.donation_id = donation_id
        self.donor_name = donor_name.strip().title()
        self.food_category = food_category.strip().title()
        self.quantity_kg = quantity_kg
        self.hours_to_expiry = hours_to_expiry

    def estimated_meals(self, meal_size_kg=0.40):
        return calculate_meals(
            self.quantity_kg,
            meal_size_kg=meal_size_kg
        )

    def priority_level(self):
        return classify_priority(self.hours_to_expiry)

    def display_summary(self):
        print("\nDonation ID:", self.donation_id)
        print("Donor:", self.donor_name)
        print("Category:", self.food_category)
        print("Quantity:", self.quantity_kg, "kg")
        print("Estimated Meals:", self.estimated_meals())
        print("Priority:", self.priority_level())

    def __str__(self):
        return (
            f"ID: {self.donation_id} | "
            f"Donor: {self.donor_name} | "
            f"Category: {self.food_category} | "
            f"Priority: {self.priority_level()}"
        )


donations = []
donation_id = 101

print("===== FOOD RESCUE AND SURPLUS DONATION SYSTEM =====")

try:
    previous_records = load_donations()
    print("Previous records found:", len(previous_records))

except FileNotFoundError:
    print("No previous records found. A new file will be created.")

print("\nEnter DONE as donor name to finish.\n")

while True:
    donor_name = input("Enter donor name (or DONE): ").strip()

    if donor_name.upper() == "DONE":
        break

    food_category = input("Enter food category: ").strip()

    
    try:
        quantity_kg = float(input("Enter quantity in kg: "))
        hours_to_expiry = int(input("Enter remaining hours: "))

    except ValueError:
        print("Invalid input! Quantity must be numeric and hours must be an integer.")
        print("Please enter the donation again.\n")
        continue

    if quantity_kg <= 0 or hours_to_expiry <= 0:
        print("Invalid donation! Values must be positive.\n")
        continue

    donation = FoodDonation(
        donation_id,
        donor_name,
        food_category,
        quantity_kg,
        hours_to_expiry
    )

    donations.append(donation)
    donation_id += 1

    save_donation(donation)

    print("Donation recorded and saved successfully!")
    print("Pickup Priority:", donation.priority_level())
    print()

print("\n===== FINAL DONATION REPORT =====")

start_time = time.time()

sorted_donations = sorted(
    donations,
    key=lambda donation: donation.hours_to_expiry
)

summary = summarize_donations(donations)

end_time = time.time()

print("\nDonations Sorted by Urgency:")
for donation in sorted_donations:
    print(donation)

print("\nTotal Donations:", summary["total_donations"])
print("Total Quantity:", summary["total_quantity"], "kg")
print("Total Estimated Meals:", summary["total_meals"])

print("\nPriority Counts:")
for priority, count in summary["priority_counts"].items():
    print(priority, ":", count)

print("\nUnique Food Categories:")
for category in sorted(summary["food_categories"]):
    print("-", category)

print(
    "\nReport Processing Time:",
    format(end_time - start_time, ".6f"),
    "seconds"
)

print("\n===== SAVED DONATION RECORDS =====")

try:
    saved_records = load_donations()

    if len(saved_records) == 0:
        print("No valid saved records found.")

    else:
        for record in saved_records:
            print(
                "ID:", record["donation_id"],
                "| Donor:", record["donor_name"],
                "| Category:", record["food_category"],
                "| Quantity:", record["quantity_kg"], "kg",
                "| Remaining Hours:", record["hours_to_expiry"]
            )

except FileNotFoundError:
    print("Error: Donation records file was not found.")

print("\n===== APPLICATION ENDED =====")
