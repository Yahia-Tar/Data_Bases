\copy zip_code_info FROM './Zip_Code_Info.csv' WITH CSV HEADER;

\copy customer FROM './Customer.csv' WITH CSV HEADER;

\copy employee FROM './Employee.csv' WITH CSV HEADER;

\copy vehicle FROM './Vehicle.csv' WITH CSV HEADER;

\copy vehicle_history FROM './Vehicle_History.csv' WITH CSV HEADER;

\copy rental_agreement FROM './Rental_Agreement.csv' WITH CSV HEADER;

\copy payment FROM './Payment.csv' WITH CSV HEADER;
