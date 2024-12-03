# Relationship Sentences
One Vehicle_ History MUST BE (1) Recorded with ONE (1) Vehicle
One Vehicle MAY BE (0) Documented with MANY (*) Vehicle_History

One Vehicle MUST BE(1) Rented by (1) Rental_Agreement 
One Rental_Agreement MAY BE (0) Tied to MANY (*) Vehicle 

One Rental Agreement MUST BE (1) Created by ONE (1) Employee 
One Employee MAY BE (0) Approving  MANY (*) Rental Agreement 

One Rental_Agreement MUST BE (1) Booked by ONE (1) Customer
One Customer MAY BE (0) Booking MANY (*)  Rental_Agreement 

One Customer MAY BE (0) Making MANY (*) Payments
One Payment MUST BE (1) Made by ONE(1) Customer 

# Initial Set Of Relations
Vehicle_History(RecordsID(Key), History_Date, Safety_Status, Appraisal_Value, Maintenance_History, Registration_Number, Registration_Expiry_Date, Insurance_Number, Insurance_Expiry_Date, Inspection_Date, Inspection_Expiry_Date, VehicleID(FK)))

Vehicle(VehicleID(Key), VIN, Plate_number, Model, Make, Year, Mileage, Color, Fuel_Type, Price_Per_Day, Availability)

Rental_Agreement(Rental ID(Key), Start_Date, Return_Date, Agreement_Type, Status, CustomerID(FK), EmployeeID(FK),VehicleID(FK))

Customer(CustomerID(Key), Drivers_License_Number, First_Name, Last_Name, Street_Address, Apartment, City, State, Zip_Code, Phone_Number, Email_Adress)

Payment(PaymentID(Key), Gross_Amount, Fees, Tax, Total, Deposit, Balance, Due_Date, Payment_Type, Card_Number, Card_Holder, Card_Zipcode, CVV, CustomerID(FK))

Employee(EmployeeID(Key), Positon, First_Name, Last_Name, Phone_Number, Email_Address)
