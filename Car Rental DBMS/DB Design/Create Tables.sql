CREATE TABLE IF NOT EXISTS Zip_Code_Info (
    Zip_Code               VARCHAR(12) NOT NULL,
    City                   VARCHAR(36),
    State                  VARCHAR(36),
    CONSTRAINT pk_zip_code_info PRIMARY KEY (Zip_Code)
);

CREATE TABLE IF NOT EXISTS Customer (
    CustomerID             VARCHAR(10) NOT NULL,
    Drivers_License_Number VARCHAR(20),
    First_Name             VARCHAR(35),
    Last_Name              VARCHAR(35),
    Street_Address         VARCHAR(35),
    Apartment              VARCHAR(10),
    Zip_Code               VARCHAR(12),
    Phone_Number           VARCHAR(15),
    Email_Address          VARCHAR(100),
    CONSTRAINT pk_customer PRIMARY KEY (CustomerID)
);

CREATE TABLE IF NOT EXISTS Vehicle (
    VehicleID              VARCHAR(10) NOT NULL,
    VIN                    VARCHAR(20),
    Plate_number           VARCHAR(20),
    Model                  VARCHAR(35),
    Make                   VARCHAR(35),
    Year                   INTEGER,
    Mileage                INTEGER,
    Color                  VARCHAR(30),
    Fuel_Type              VARCHAR(20),
    Price_Per_Day          FLOAT,
    Availability           VARCHAR(4),
    CONSTRAINT pk_vehicle PRIMARY KEY (VehicleID)
);

CREATE TABLE IF NOT EXISTS Vehicle_History (
    RecordsID              VARCHAR(10) NOT NULL,
    History_Date           DATE,
    Safety_Status          VARCHAR(50),
    Appraisal_Value        FLOAT,
    Maintenance_History    VARCHAR(255),
    Registration_Number    VARCHAR(20),
    Registration_Expiry_Date DATE,
    Insurance_Number       VARCHAR(20),
    Insurance_Expiry_Date  DATE,
    Inspection_Date        DATE,
    Inspection_Expiry_Date DATE,
    VehicleID              VARCHAR(10),
    CONSTRAINT pk_vehicle_history PRIMARY KEY (RecordsID)
);

CREATE TABLE IF NOT EXISTS Rental_Agreement (
    RentalID               VARCHAR(10) NOT NULL,
    Start_Date             DATE,
    Return_Date            DATE,
    Agreement_Type         VARCHAR(50),
    Status                 VARCHAR(50),
    CustomerID             VARCHAR(10),
    EmployeeID             VARCHAR(10),
    VehicleID              VARCHAR(10),
    CONSTRAINT pk_rental_agreement PRIMARY KEY (RentalID)
);

CREATE TABLE IF NOT EXISTS Payment (
    PaymentID              VARCHAR(10) NOT NULL,
    Gross_Amount           FLOAT,
    Fees                   FLOAT,
    Tax                    FLOAT,
    Deposit                FLOAT,
    Due_Date               DATE,
    Payment_Type           VARCHAR(50),
    Card_Number            VARCHAR(20),
    Card_Holder            VARCHAR(50),
    Card_Zipcode           VARCHAR(12),
    CVV                    VARCHAR(4),
    CustomerID             VARCHAR(10),
    CONSTRAINT pk_payment PRIMARY KEY (PaymentID)
);

CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID             VARCHAR(10) NOT NULL,
    Position               VARCHAR(50),
    First_Name             VARCHAR(35),
    Last_Name              VARCHAR(25),
    Phone_Number           VARCHAR(15),
    Email_Address          VARCHAR(100),
    CONSTRAINT pk_employee PRIMARY KEY (EmployeeID)
);
