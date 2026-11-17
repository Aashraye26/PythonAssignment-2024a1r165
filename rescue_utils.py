
# rescue_utils.py
# Utility functions for Food Rescue System

def calculate_meals(quantity_kg, meal_size_kg=0.40):
    return int(quantity_kg / meal_size_kg)


def classify_priority(hours_to_expiry):
    if hours_to_expiry <= 4:
        return "CRITICAL"
    elif hours_to_expiry <= 12:
        return "PRIORITY"
    else:
        return "NORMAL"


def summarize_donations(donations, meal_size_kg=0.40):
    total_quantity = 0
    total_meals = 0

    priority_counts = {
        "CRITICAL": 0,
        "PRIORITY": 0,
        "NORMAL": 0
    }

    food_categories = set()

    for donation in donations:
        total_quantity += donation.quantity_kg
        total_meals += calculate_meals(
            donation.quantity_kg,
            meal_size_kg=meal_size_kg
        )

        priority = classify_priority(donation.hours_to_expiry)
        priority_counts[priority] += 1
        food_categories.add(donation.food_category)

    return {
        "total_donations": len(donations),
        "total_quantity": total_quantity,
        "total_meals": total_meals,
        "priority_counts": priority_counts,
        "food_categories": food_categories
    }


# Save one accepted donation to a text file
def save_donation(donation, filename="rescue_records.txt"):
    with open(filename, "a") as file:
        record = (
            f"{donation.donation_id}|"
            f"{donation.donor_name}|"
            f"{donation.food_category}|"
            f"{donation.quantity_kg}|"
            f"{donation.hours_to_expiry}\n"
        )
        file.write(record)


# Read donation records from the text file
def load_donations(filename="rescue_records.txt"):
    records = []

    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            fields = line.strip().split("|")

            # Each record must contain exactly five fields
            if len(fields) != 5:
                print(
                    f"Malformed record on line {line_number}. "
                    "Record skipped."
                )
                continue

            try:
                record = {
                    "donation_id": int(fields[0]),
                    "donor_name": fields[1],
                    "food_category": fields[2],
                    "quantity_kg": float(fields[3]),
                    "hours_to_expiry": int(fields[4])
                }

                records.append(record)

            except ValueError:
                print(
                    f"Invalid data on line {line_number}. "
                    "Record skipped."
                )

    return records
