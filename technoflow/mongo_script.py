from pymongo import MongoClient

# Connect to MongoDB
try:
    client = MongoClient('mongodb://localhost:27017/')
    print("Connected to MongoDB successfully!")
except errors.ConnectionError as e:
    print(f"Could not connect to MongoDB: {e}")
    exit()

# Create (or switch to) a database
db = client['vendors_database']

# Sample data for each type of vendor with place set to 'Coimbatore'
vendors = {
    'plumbers': [
        {'name': 'Jack', 'occupation': 'Plumber', 'phone_no': '123-456-7890', 'place': 'Coimbatore'},
        {'name': 'Jane Smith', 'occupation': 'Plumber', 'phone_no': '123-456-7891', 'place': 'Coimbatore'},
        {'name': 'Jim Brown', 'occupation': 'Plumber', 'phone_no': '123-456-7892', 'place': 'Coimbatore'},
        {'name': 'Jake White', 'occupation': 'Plumber', 'phone_no': '123-456-7893', 'place': 'Coimbatore'},
        {'name': 'Jill Green', 'occupation': 'Plumber', 'phone_no': '123-456-7894', 'place': 'Coimbatore'},
    ],
    'electricians': [
        {'name': 'Ethan Miller', 'occupation': 'Electrician', 'phone_no': '234-567-8901', 'place': 'Coimbatore'},
        {'name': 'Ella Johnson', 'occupation': 'Electrician', 'phone_no': '234-567-8902', 'place': 'Coimbatore'},
        {'name': 'Evan Davis', 'occupation': 'Electrician', 'phone_no': '234-567-8903', 'place': 'Coimbatore'},
        {'name': 'Emily Garcia', 'occupation': 'Electrician', 'phone_no': '234-567-8904', 'place': 'Coimbatore'},
        {'name': 'Eddie Martinez', 'occupation': 'Electrician', 'phone_no': '234-567-8905', 'place': 'Coimbatore'},
    ],
    'carpenters': [
        {'name': 'Carl Young', 'occupation': 'Carpenter', 'phone_no': '345-678-9012', 'place': 'Coimbatore'},
        {'name': 'Cathy Allen', 'occupation': 'Carpenter', 'phone_no': '345-678-9013', 'place': 'Coimbatore'},
        {'name': 'Craig King', 'occupation': 'Carpenter', 'phone_no': '345-678-9014', 'place': 'Coimbatore'},
        {'name': 'Cindy Wright', 'occupation': 'Carpenter', 'phone_no': '345-678-9016', 'place': 'Coimbatore'},
        {'name': 'Chris Scott', 'occupation': 'Carpenter', 'phone_no': '345-678-9016', 'place': 'Coimbatore'},
   
    ],
    'gardeners': [
        {'name': 'George Walker', 'occupation': 'Gardener', 'phone_no': '456-789-0123', 'place': 'Coimbatore'},
        {'name': 'Grace Hall', 'occupation': 'Gardener', 'phone_no': '456-789-0124', 'place': 'Coimbatore'},
        {'name': 'Gordon Allen', 'occupation': 'Gardener', 'phone_no': '456-789-0125', 'place': 'Coimbatore'},
        {'name': 'Gina Young', 'occupation': 'Gardener', 'phone_no': '456-789-0126', 'place': 'Coimbatore'},
        {'name': 'Gary Hernandez', 'occupation': 'Gardener', 'phone_no': '456-789-0127', 'place': 'Coimbatore'},
       
    ],
    'mechanics': [
        {'name': 'Michael Nelson', 'occupation': 'Mechanic', 'phone_no': '567-890-1234', 'place': 'Coimbatore'},
        {'name': 'Megan Carter', 'occupation': 'Mechanic', 'phone_no': '567-890-1235', 'place': 'Coimbatore'},
        {'name': 'Martin Mitchell', 'occupation': 'Mechanic', 'phone_no': '567-890-1236', 'place': 'Coimbatore'},
        {'name': 'Mia Perez', 'occupation': 'Mechanic', 'phone_no': '567-890-1237', 'place': 'Coimbatore'},
        {'name': 'Mark Roberts', 'occupation': 'Mechanic', 'phone_no': '567-890-1238', 'place': 'Coimbatore'},
       
    ],
    'home_cleaners': [
        {'name': 'Hannah Clark', 'occupation': 'Home Cleaner', 'phone_no': '678-901-2345', 'place': 'Coimbatore'},
        {'name': 'Henry Lewis', 'occupation': 'Home Cleaner', 'phone_no': '678-901-2346', 'place': 'Coimbatore'},
        {'name': 'Hazel Robinson', 'occupation': 'Home Cleaner', 'phone_no': '678-901-2347', 'place': 'Coimbatore'},
        {'name': 'Hector Walker', 'occupation': 'Home Cleaner', 'phone_no': '678-901-2348', 'place': 'Coimbatore'},
        {'name': 'Hailey Young', 'occupation': 'Home Cleaner', 'phone_no': '678-901-2349', 'place': 'Coimbatore'},
     
    ],
    'painters': [
        {'name': 'Peter Nelson', 'occupation': 'Painter', 'phone_no': '789-012-3456', 'place': 'Coimbatore'},
        {'name': 'Paula Carter', 'occupation': 'Painter', 'phone_no': '789-012-3457', 'place': 'Coimbatore'},
        {'name': 'Patrick Mitchell', 'occupation': 'Painter', 'phone_no': '789-012-3458', 'place': 'Coimbatore'},
        {'name': 'Penelope Perez', 'occupation': 'Painter', 'phone_no': '789-012-3459', 'place': 'Coimbatore'},
        {'name': 'Paul Roberts', 'occupation': 'Painter', 'phone_no': '789-012-3460', 'place': 'Coimbatore'},
    ]
}

# Insert data into the MongoDB database
try:
    for occupation, people in vendors.items():
        collection = db[occupation]
        collection.insert_many(people)
    print("Data inserted successfully!")
except errors.PyMongoError as e:
    print(f"An error occurred: {e}")
