classDiagram
direction BT
class customer {
   varchar(20) drivers_license_number
   varchar(35) first_name
   varchar(35) last_name
   varchar(35) street_address
   varchar(10) apartment
   varchar(12) zip_code
   varchar(15) phone_number
   varchar(100) email_address
   varchar(10) customerid
}
class employee {
   varchar(50) position
   varchar(35) first_name
   varchar(25) last_name
   varchar(15) phone_number
   varchar(100) email_address
   varchar(10) employeeid
}
class payment {
   double precision gross_amount
   double precision fees
   double precision tax
   double precision deposit
   date due_date
   varchar(50) payment_type
   varchar(20) card_number
   varchar(50) card_holder
   varchar(12) card_zipcode
   varchar(4) cvv
   varchar(10) customerid
   varchar(10) paymentid
}
class rental_agreement {
   date start_date
   date return_date
   varchar(50) agreement_type
   varchar(50) status
   varchar(10) customerid
   varchar(10) employeeid
   varchar(10) vehicleid
   varchar(10) rentalid
}
class vehicle {
   varchar(20) vin
   varchar(20) plate_number
   varchar(35) model
   varchar(35) make
   integer year
   integer mileage
   varchar(30) color
   varchar(20) fuel_type
   double precision price_per_day
   varchar(4) availability
   varchar(10) vehicleid
}
class vehicle_history {
   date history_date
   varchar(50) safety_status
   double precision appraisal_value
   varchar(255) maintenance_history
   varchar(20) registration_number
   date registration_expiry_date
   varchar(20) insurance_number
   date insurance_expiry_date
   date inspection_date
   date inspection_expiry_date
   varchar(10) vehicleid
   varchar(10) recordsid
}
class zip_code_info {
   varchar(36) city
   varchar(36) state
   varchar(12) zip_code
}

customer  -->  zip_code_info : zip_code
payment  -->  customer : customerid
rental_agreement  -->  customer : customerid
rental_agreement  -->  employee : employeeid
rental_agreement  -->  vehicle : vehicleid
vehicle_history  -->  vehicle : vehicleid
