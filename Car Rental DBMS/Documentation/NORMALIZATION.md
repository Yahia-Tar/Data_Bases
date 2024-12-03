# Vehicle History Relation
Vehicle_History(RecordsID(Key), History_Date, Safety_Status, Appraisal_Value, Maintenance_History, Registration_Number, Registration_Expiry_Date, Insurance_Number, Insurance_Expiry_Date, Inspection_Date, Inspection_Expiry_Date, VehicleID(FK)))
KEY: RecordsID
FD1: RecordsID ->History_Date, Safety_Status, Appraisal_Value, Maintenance_History, Registration_Number, Registration_Expiry_Date, Insurance_Number, Insurance_Expiry_Date, Inspection_Date, Inspection_Expiry_Date, VehicleID(FK)
1NF: Meets the definition of a relation
2NF: No partial Key dependencies
3NF: No Transitive dependencies

Vehicle Relation
Vehicle(VehicleID(Key), VIN, Plate_number, Model, Make, Year, Mileage, Color, Fuel_Type, Price_Per_Day, Availability)
KEY: VehicleID
ALT KEY: VIN, PLATE(Treat like any other attribute)
FD1: VehicleID ->VIN, Plate_number, Model, Make, Year, Mileage, Color, Fuel_Type, Price_Per_Day, Availability)
1NF: Meets the definition of a relation
2NF: No partial Key dependencies
3NF: 3NF: No Transitive dependencies

# Rental Agreement Relation
Rental_Agreement(Rental ID(Key), Start_Date, Return_Date, Agreement_Type, Status, CustomerID(FK), EmployeeID(FK),VehicleID(FK))
KEY: RentalID
FD1: RentalID -> Start_Date, Return_Date, Agreement_Type, Status, CustomerID(FK), EmployeeID(FK),VehicleID(FK))
1NF: Meets the definition of a relation
2NF: No partial Key dependencies
3NF: No Transitive dependencies

# Customer Relation
Customer(CustomerID(Key), Drivers_License_Number, First_Name, Last_Name, Street_Address, Apartment, City, State, Zip_Code, Phone_Number, Email_Adress)
KEY:CustomerID
ALT KEY: Drivers_License_Number(Treat like any other attribute)
FD1: CustomerID-> Drivers_License_Number, First_Name, Last_Name, Street_Address, Apartment, City, State, Zip_Code, Phone_Number, Email_Adress
FD2:Zip_Code -> City, State
1NF: Meets the definition of a relation
2NF: No partial Key dependencies
3NF: Transitive dependency exists: 
-CustomerID-> Drivers_License_Number, First_Name, Last_Name, Street_Address, Apartment, City, State, Zip_Code, Phone_Number, Email_Adress
-Zip_Code -> City, State
Solution: Create a new relation called Zip_Code_Info that stores zip code as key, city, and state.

Customer(CustomerID(Key), Drivers_License_Number, First_Name, Last_Name, Street_Address, Apartment,Zip_Code(FK), Phone_Number, Email_Adress)
KEY:CustomerID
ALT KEY: Drivers_License_Number(Treat like any other attribute)
FD1:CustomerID-> Drivers_License_Number, First_Name, Last_Name, Street_Address, Apartment,Zip_Code, Phone_Number, Email_Adress)
1NF: Meets the definition of a relation
2NF: No partial Key dependencies
3NF: No transitive dependencies

Zip_Code_Info(Zip_Code(Key), City, State)
Key:Zip_Code
FD1:Zip_Code -> City,State
1NF: Meets the definition of a relation
2NF: No partial Key dependencies
3NF: No transitive dependencies

# Payment Relation
Payment(PaymentID(Key), Gross_Amount, Fees, Tax, Total, Deposit, Balance, Due_Date, Payment_Type, Card_Number, Card_Holder, Card_Zipcode, CVV, CustomerID(FK))
KEY:PaymentID
ALT KEY: Card_Number(Treat like any other attribute)
FD1: PaymentID -> Gross_Amount, Fees, Tax, Total, Deposit, Balance, Due_Date, Payment_Type, Card_Number, Card_Holder, Card_Zipcode, CVV, CustomerID(FK))
FD2: Gross_Amount, Fees, Tax -> Total
FD3:Total, Deposit -> Balance
1NF: Meets the definition of a relation
2NF: No partial Key dependencies
3NF: Transitive dependency exists: 
-PaymentID -> Gross_Amount, Fees, Tax, Total, Deposit, Balance, Due_Date, Payment_Type, Card_Number, Card_Holder, Card_Zipcode, CVV, CustomerID(FK))
-Gross_Amount, Fees, Tax -> Total
-Total, Deposit -> Balance
Solution: Drop the Deposit total and balance attribute due to both attributes being able to be calculated through simple queries and do not require storage.

Payment(PaymentID(Key), Gross_Amount, Fees, Tax, Deposit, Due_Date, Payment_Type, Card_Number, Card_Holder, Card_Zipcode, CVV, CustomerID(FK))
KEY:PaymentID
ALT KEY: Card_Number(Treat like any other attribute)
FD1:PaymentID ->  Gross_Amount, Fees, Tax, Deposit,, Due_Date, Payment_Type, Card_Number, Card_Holder, Card_Zipcode, CVV, CustomerID(FK))
1NF: Meets the definition of a relation
2NF: No partial Key dependencies
3NF: No Transitive dependencies


# Employee Relation
Employee(EmployeeID(Key), Positon, First_Name, Last_Name, Phone_Number, Email_Address)
Key:EmployeeID
FD1:EmployeeID -> Position, First_Name, Last_Name, Phone_Number, Email_Address
1NF: Meets the definition of a relation
2NF: No partial Key dependencies
3NF: No Transitive dependencies
