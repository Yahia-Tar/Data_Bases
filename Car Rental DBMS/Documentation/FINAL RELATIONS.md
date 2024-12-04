# Final Set of Relations

**Vehicle History Relation:**  
`Vehicle_History(RecordsID(Key), History_Date, Safety_Status, Appraisal_Value, Maintenance_History, Registration_Number, Registration_Expiry_Date, Insurance_Number, Insurance_Expiry_Date, Inspection_Date, Inspection_Expiry_Date, VehicleID(FK))`

**Vehicle Relation:**  
`Vehicle(VehicleID(Key), VIN, Plate_number, Model, Make, Year, Mileage, Color, Fuel_Type, Price_Per_Day, Availability)`

**Rental Agreement Relation:**  
`Rental_Agreement(RentalID(Key), Start_Date, Return_Date, Agreement_Type, Status, CustomerID(FK), EmployeeID(FK), VehicleID(FK))`

**Customer Relation:**  
`Customer(CustomerID(Key), Drivers_License_Number, First_Name, Last_Name, Street_Address, Apartment, Zip_Code(FK), Phone_Number, Email_Address)`

**Zip Code Info Relation:**  
`Zip_Code_Info(Zip_Code(Key), City, State)`

**Payment Relation:**  
`Payment(PaymentID(Key), Gross_Amount, Fees, Tax, Deposit, Due_Date, Payment_Type, Card_Number, Card_Holder, Card_Zipcode, CVV, CustomerID(FK))`

**Employee Relation:**  
`Employee(EmployeeID(Key), Position, First_Name, Last_Name, Phone_Number, Email_Address)`
