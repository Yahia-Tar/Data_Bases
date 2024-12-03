import os
import csv
import random
from datetime import datetime, timedelta

# Define your target directory
output_directory = "./"

# Ensure the directory exists
os.makedirs(output_directory, exist_ok=True)

# List of realistic first and last names
first_names = ["John", "Emily", "Michael", "Sarah", "David", "Jessica", "Daniel", "Emma", "Matthew", "Sophia"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def random_phone():
    return f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"

def random_email(first_name, last_name):
    domains = ["gmail.com", "yahoo.com", "outlook.com"]
    return f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"

def generate_csv_files():
    # Define ranges and data
    makes_models = {
        "Toyota": ["Camry", "Corolla", "RAV4"],
        "Ford": ["F-150", "Escape", "Mustang"],
        "Honda": ["Civic", "Accord", "CR-V"],
        "Tesla": ["Model S", "Model 3", "Model X"],
    }
    fuel_types = ["Gasoline", "Diesel", "Electric", "Hybrid"]
    colors = ["Red", "Blue", "Black", "White", "Silver"]
    statuses = ["Active", "Inactive"]
    cities_states = [
        ("New York", "NY"),
        ("Los Angeles", "CA"),
        ("Chicago", "IL"),
        ("Houston", "TX"),
        ("Phoenix", "AZ"),
    ]
    positions = ["Manager", "Salesperson", "Mechanic"]

    # Generate Zip_Code_Info.csv
    zip_codes = list(range(10000, 10010))
    with open(os.path.join(output_directory, 'Zip_Code_Info.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Zip_Code", "City", "State"])
        for zip_code in zip_codes:
            city, state = random.choice(cities_states)
            writer.writerow([zip_code, city, state])

    # Generate Customer.csv
    with open(os.path.join(output_directory, 'Customer.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["CustomerID", "Drivers_License_Number", "First_Name", "Last_Name", "Street_Address", "Apartment", "Zip_Code", "Phone_Number", "Email_Address"])
        for customer_id in range(1, 101):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            writer.writerow([
                customer_id,
                f"DL{random.randint(100000, 999999)}",
                first_name,
                last_name,
                f"{random.randint(1, 9999)} Main St",
                random.choice(["Apt 1", "Apt 2", "Suite 3", None]),
                random.choice(zip_codes),
                random_phone(),
                random_email(first_name, last_name),
            ])

    # Generate Employee.csv
    with open(os.path.join(output_directory, 'Employee.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["EmployeeID", "Position", "First_Name", "Last_Name", "Phone_Number", "Email_Address"])
        for employee_id in range(1, 21):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            writer.writerow([
                employee_id,
                random.choice(positions),
                first_name,
                last_name,
                random_phone(),
                random_email(first_name, last_name),
            ])

    # Generate Vehicle.csv
    with open(os.path.join(output_directory, 'Vehicle.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["VehicleID", "VIN", "Plate_number", "Model", "Make", "Year", "Mileage", "Color", "Fuel_Type", "Price_Per_Day", "Availability"])
        for vehicle_id in range(1, 51):
            make = random.choice(list(makes_models.keys()))
            model = random.choice(makes_models[make])
            writer.writerow([
                vehicle_id,
                f"VIN{random.randint(100000, 999999)}",
                f"PLATE{random.randint(1000, 9999)}",
                model,
                make,
                random.randint(2000, 2023),
                random.randint(10000, 200000),
                random.choice(colors),
                random.choice(fuel_types),
                round(random.uniform(20, 200), 2),
                random.choice(["Yes", "No"]),
            ])

    # Generate Vehicle_History.csv
    with open(os.path.join(output_directory, 'Vehicle_History.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["RecordsID", "History_Date", "Safety_Status", "Appraisal_Value", "Maintenance_History", "Registration_Number", "Registration_Expiry_Date", "Insurance_Number", "Insurance_Expiry_Date", "Inspection_Date", "Inspection_Expiry_Date", "VehicleID"])
        for record_id in range(1, 101):
            writer.writerow([
                record_id,
                random_date(datetime(2010, 1, 1), datetime(2024, 1, 1)).strftime('%Y-%m-%d'),
                random.choice(statuses),
                random.randint(5000, 50000),
                f"Service{random.randint(1, 10)}",
                f"REG{random.randint(10000, 99999)}",
                random_date(datetime(2024, 1, 1), datetime(2026, 1, 1)).strftime('%Y-%m-%d'),
                f"INS{random.randint(10000, 99999)}",
                random_date(datetime(2024, 1, 1), datetime(2026, 1, 1)).strftime('%Y-%m-%d'),
                random_date(datetime(2023, 1, 1), datetime(2024, 1, 1)).strftime('%Y-%m-%d'),
                random_date(datetime(2024, 1, 1), datetime(2025, 1, 1)).strftime('%Y-%m-%d'),
                random.randint(1, 50),
            ])

    # Generate Rental_Agreement.csv
    with open(os.path.join(output_directory, 'Rental_Agreement.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["RentalID", "Start_Date", "Return_Date", "Agreement_Type", "Status", "CustomerID", "EmployeeID", "VehicleID"])
        for rental_id in range(1, 101):
            start_date = random_date(datetime(2023, 1, 1), datetime(2023, 12, 1))
            return_date = start_date + timedelta(days=random.randint(1, 30))
            writer.writerow([
                rental_id,
                start_date.strftime('%Y-%m-%d'),
                return_date.strftime('%Y-%m-%d'),
                random.choice(["Daily", "Weekly", "Monthly"]),
                random.choice(statuses),
                random.randint(1, 100),
                random.randint(1, 20),
                random.randint(1, 50),
            ])

    # Generate Payment.csv
    with open(os.path.join(output_directory, 'Payment.csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["PaymentID", "Gross_Amount", "Fees", "Tax", "Deposit", "Due_Date", "Payment_Type", "Card_Number", "Card_Holder", "Card_Zipcode", "CVV", "CustomerID"])
        for payment_id in range(1, 101):
            customer_id = random.randint(1, 100)  # Ensure the CustomerID matches the Customer table
            card_zipcode = random.choice(zip_codes)  # Ensure the Card_Zipcode matches Zip_Code_Info
            card_holder_first = random.choice(first_names)
            card_holder_last = random.choice(last_names)
            writer.writerow([
                payment_id,
                round(random.uniform(100, 1000), 2),
                round(random.uniform(10, 50), 2),
                round(random.uniform(5, 20), 2),
                round(random.uniform(50, 200), 2),
                random_date(datetime(2023, 1, 1), datetime(2023, 12, 1)).strftime('%Y-%m-%d'),
                random.choice(["Credit", "Debit", "Cash"]),
                f"{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}",
                f"{card_holder_first} {card_holder_last}",
                card_zipcode,
                random.randint(100, 999),
                customer_id,
            ])


# Generate the CSV files
generate_csv_files()
