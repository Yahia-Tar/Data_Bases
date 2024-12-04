# Vehicle History Relation
**Relation:**  
`Vehicle_History(RecordsID(Key), History_Date, Safety_Status, Appraisal_Value, Maintenance_History, Registration_Number, Registration_Expiry_Date, Insurance_Number, Insurance_Expiry_Date, Inspection_Date, Inspection_Expiry_Date, VehicleID(FK))`

- **KEY:** RecordsID  
- **Functional Dependencies:**  
  - FD1: RecordsID -> History_Date, Safety_Status, Appraisal_Value, Maintenance_History, Registration_Number, Registration_Expiry_Date, Insurance_Number, Insurance_Expiry_Date, Inspection_Date, Inspection_Expiry_Date, VehicleID(FK)  
- **Normalization:**  
  - 1NF: Meets the definition of a relation  
  - 2NF: No partial key dependencies  
  - 3NF: No transitive dependencies  

---

# Vehicle Relation
**Relation:**  
`Vehicle(VehicleID(Key), VIN, Plate_number, Model, Make, Year, Mileage, Color, Fuel_Type, Price_Per_Day, Availability)`

- **KEY:** VehicleID  
- **Alternate Key:** VIN, Plate_number  
- **Functional Dependencies:**  
  - FD1: VehicleID -> VIN, Plate_number, Model, Make, Year, Mileage, Color, Fuel_Type, Price_Per_Day, Availability  
- **Normalization:**  
  - 1NF: Meets the definition of a relation  
  - 2NF: No partial key dependencies  
  - 3NF: No transitive dependencies  

---

# Rental Agreement Relation
**Relation:**  
`Rental_Agreement(RentalID(Key), Start_Date, Return_Date, Agreement_Type, Status, CustomerID(FK), EmployeeID(FK), VehicleID(FK))`

- **KEY:** RentalID  
- **Functional Dependencies:**  
  - FD1: RentalID -> Start_Date, Return_Date, Agreement_Type, Status, CustomerID(FK), EmployeeID(FK), VehicleID(FK)  
- **Normalization:**  
  - 1NF: Meets the definition of a relation  
  - 2NF: No partial key dependencies  
  - 3NF: No transitive dependencies  

---

# Customer Relation
**Relation:**  
`Customer(CustomerID(Key), Drivers_License_Number, First_Name, Last_Name, Street_Address, Apartment, City, State, Zip_Code, Phone_Number, Email_Address)`

- **KEY:** CustomerID  
- **Alternate Key:** Drivers_License_Number  
- **Functional Dependencies:**  
  - FD1: CustomerID -> Drivers_License_Number, First_Name, Last_Name, Street_Address, Apartment, City, State, Zip_Code, Phone_Number, Email_Address  
  - FD2: Zip_Code -> City, State  
- **Normalization:**  
  - 1NF: Meets the definition of a relation  
  - 2NF: No partial key dependencies  
  - 3NF: Transitive dependency exists:  
    - CustomerID -> Drivers_License_Number, First_Name, Last_Name, Street_Address, Apartment, City, State, Zip_Code, Phone_Number, Email_Address  
    - Zip_Code -> City, State  
  - **Solution:** Create a new relation `Zip_Code_Info`.

**Updated Relations:**  
1. `Customer(CustomerID(Key), Drivers_License_Number, First_Name, Last_Name, Street_Address, Apartment, Zip_Code(FK), Phone_Number, Email_Address)`  
2. `Zip_Code_Info(Zip_Code(Key), City, State)`

---

# Payment Relation
**Relation:**  
`Payment(PaymentID(Key), Gross_Amount, Fees, Tax, Total, Deposit, Balance, Due_Date, Payment_Type, Card_Number, Card_Holder, Card_Zipcode, CVV, CustomerID(FK))`

- **KEY:** PaymentID  
- **Alternate Key:** Card_Number  
- **Functional Dependencies:**  
  - FD1: PaymentID -> Gross_Amount, Fees, Tax, Total, Deposit, Balance, Due_Date, Payment_Type, Card_Number, Card_Holder, Card_Zipcode, CVV, CustomerID(FK)  
  - FD2: Gross_Amount, Fees, Tax -> Total  
  - FD3: Total, Deposit -> Balance  
- **Normalization:**  
  - 1NF: Meets the definition of a relation  
  - 2NF: No partial key dependencies  
  - 3NF: Transitive dependency exists:  
    - PaymentID -> Gross_Amount, Fees, Tax, Total, Deposit, Balance, Due_Date, Payment_Type, Card_Number, Card_Holder, Card_Zipcode, CVV, CustomerID(FK)  
    - Gross_Amount, Fees, Tax -> Total  
    - Total, Deposit -> Balance  
  - **Solution:** Drop the `Deposit` and `Balance` attributes as they can be calculated through queries.

**Updated Relation:**  
`Payment(PaymentID(Key), Gross_Amount, Fees, Tax, Due_Date, Payment_Type, Card_Number, Card_Holder, Card_Zipcode, CVV, CustomerID(FK))`

---

# Employee Relation
**Relation:**  
`Employee(EmployeeID(Key), Position, First_Name, Last_Name, Phone_Number, Email_Address)`

- **KEY:** EmployeeID  
- **Functional Dependencies:**  
  - FD1: EmployeeID -> Position, First_Name, Last_Name, Phone_Number, Email_Address  
- **Normalization:**  
  - 1NF: Meets the definition of a relation  
  - 2NF: No partial key dependencies  
  - 3NF: No transitive dependencies
