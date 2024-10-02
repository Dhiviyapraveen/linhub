from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['login_database']
collection = db['vendor_details']

def store_vendor_details(data):
    name = data.get('name')
    business_plan = data.get('business_plan')
    working_address = data.get('working_address')
    pincode = data.get('pincode')
    aadhar_number = data.get('aadhar_number')
    phone_number = data.get('phone_number')

    if not name or not business_plan or not working_address or not pincode or not aadhar_number or not phone_number:
        return {'error': 'All fields are required!'}, 400

    # Create a document to insert into MongoDB
    vendor_details = {
        'name': name,
        'business_plan': business_plan,
        'working_address': working_address,
        'pincode': pincode,
        'aadhar_number': aadhar_number,
        'phone_number': phone_number
    }

    try:
        # Insert the document into the collection
        collection.insert_one(vendor_details)
        return {'message': 'Vendor details stored successfully!'}, 200
    except Exception as e:
        return {'error': str(e)}, 500

data_entries = [
    {'name': 'Jack', 'business_plan': 'Plumber', 'working_address': '123 Main Street,coimbatore', 'pincode': '', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'Evan Devas', 'business_plan': 'Electrician', 'working_address': '789 Oak Street,coimbatore', 'pincode': '67890', 'aadhar_number': '567890123456', 'phone_number': '4567890123'},
    {'name': 'Carl Young', 'business_plan': 'Carpenter', 'working_address': '123 Main Street,coimbatore', 'pincode': '12345', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'Gina Young', 'business_plan': 'Gardener', 'working_address': '123 Main Street,coimbatore', 'pincode': '12345', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'Ethan Miller', 'business_plan': 'Electrician', 'working_address': '123 Main Street,coimbatore', 'pincode': '12345', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'Ella Johnson', 'business_plan': 'Electrician', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '1234567890'},
    {'name': 'Jill Green', 'business_plan': 'Plumber', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '1234567890'},
    {'name': 'Jim Brown', 'business_plan': 'Plumber', 'working_address': '789 Oak Street,coimbatore', 'pincode': '67890', 'aadhar_number': '567890123456', 'phone_number': '9876548990'},
    {'name': 'Cyndy Write', 'business_plan': 'Carpenter', 'working_address': '123 Main Street,coimbatore', 'pincode': '12345', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'Hannah Clark', 'business_plan': 'Home Cleaner', 'working_address': '123 Main Street,coimbatore', 'pincode': '12345', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'Henry Lewis', 'business_plan': 'Home Cleaner', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '1234567890'},
    {'name': 'Emily Garcia', 'business_plan': 'Electrician', 'working_address': '123 Main Street,coimbatore', 'pincode': '12345', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'Eddie Martinez', 'business_plan': 'Electrician', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '1234567890'},
    {'name': 'Hazel Robinson', 'business_plan': 'Home Cleaner', 'working_address': '789 Oak Street,coimbatore', 'pincode': '67890', 'aadhar_number': '567890123456', 'phone_number': '4567890123'},
    {'name': 'Cathy Allen', 'business_plan': 'Carpenter', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '1234567890'},
    {'name': 'Craig King', 'business_plan': 'Carpenter', 'working_address': '789 Oak Street,coimbatore', 'pincode': '67890', 'aadhar_number': '567890123456', 'phone_number': '4567890123'},
    {'name': 'Jake White', 'business_plan': 'Plumber', 'working_address': '123 Main Street,coimbatore', 'pincode': '12345', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'George Walker', 'business_plan': 'Gardener', 'working_address': '123 Main Street,coimbatore', 'pincode': '12345', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'Chris Scott', 'business_plan': 'Carpenter', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '1234567890'},
    {'name': 'Martin Mitchell', 'business_plan': 'Mechanic', 'working_address': '789 Oak Street,coimbatore', 'pincode': '67890', 'aadhar_number': '567890123456', 'phone_number': '4567890123'},
    {'name': 'Mia Perez', 'business_plan': 'Mechanic', 'working_address': '123 Main Street,coimbatore', 'pincode': '12345', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'Grace Haul', 'business_plan': 'Gardener', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '1234567890'},
    {'name': 'Gardon Allen', 'business_plan': 'Gardener', 'working_address': '789 Oak Street,coimbatore', 'pincode': '67890', 'aadhar_number': '567890123456', 'phone_number': '4567890123'},
  
    {'name': 'Gary Hernandez', 'business_plan': 'Gardener', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '1234567890'},
    {'name': 'Penelope Perez', 'business_plan': 'Painter', 'working_address': '123 Main Street,coimbatore', 'pincode': '12345', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'Michael Nelson', 'business_plan': 'Mechanic', 'working_address': '123 Main Street,coimbatore', 'pincode': '12345', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'Megan Carter', 'business_plan': 'Mechanic', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '1234567890'},

    {'name': 'Mark Roberts', 'business_plan': 'Mechanic', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '1234567890'},
    

    {'name': 'Hector Walker', 'business_plan': 'Home Cleaner', 'working_address': '123 Main Street,coimbatore', 'pincode': '12345', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'Hailey Young', 'business_plan': 'Home Cleaner', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '1234567890'},
    {'name': 'Jane Smith', 'business_plan': 'Plumber', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '9863874868'},
    {'name': 'Peter Nelson', 'business_plan': 'Painter', 'working_address': '123 Main Street,coimbatore', 'pincode': '12345', 'aadhar_number': '123456789012', 'phone_number': '9876543210'},
    {'name': 'Paula Carter', 'business_plan': 'Painter', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '1234567890'},
    {'name': 'Patrick Mitchell', 'business_plan': 'Painter', 'working_address': '789 Oak Street,coimbatore', 'pincode': '67890', 'aadhar_number': '567890123456', 'phone_number': '4567890123'},

    {'name': 'Paul Roberts', 'business_plan': 'Painter', 'working_address': '456 Elm Street,coimbatore', 'pincode': '54321', 'aadhar_number': '098765432109', 'phone_number': '1234567890'},
  
]

# Iterate over each data entry and store it
for data_entry in data_entries:
    response, status_code = store_vendor_details(data_entry)
    print(response, status_code)
