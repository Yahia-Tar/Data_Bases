ALTER TABLE Customer
   ADD CONSTRAINT fk_customer_zipcode_info
     FOREIGN KEY (Zip_Code) 
        REFERENCES Zip_Code_Info (Zip_Code);

ALTER TABLE Vehicle_History
   ADD CONSTRAINT fk_vehicle_history_vehicle
     FOREIGN KEY (VehicleID) 
        REFERENCES Vehicle (VehicleID);

ALTER TABLE Rental_Agreement
   ADD CONSTRAINT fk_rental_agreement_customer
     FOREIGN KEY (CustomerID) 
        REFERENCES Customer (CustomerID);

ALTER TABLE Rental_Agreement
   ADD CONSTRAINT fk_rental_agreement_employee
     FOREIGN KEY (EmployeeID) 
        REFERENCES Employee (EmployeeID);

ALTER TABLE Rental_Agreement
   ADD CONSTRAINT fk_rental_agreement_vehicle
     FOREIGN KEY (VehicleID) 
        REFERENCES Vehicle (VehicleID);

ALTER TABLE Payment
   ADD CONSTRAINT fk_payment_customer
     FOREIGN KEY (CustomerID) 
        REFERENCES Customer (CustomerID);
