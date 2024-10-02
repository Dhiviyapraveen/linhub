from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['login_database']
collection = db['customer_details']

def submit_details(data_list):
    results = []
    for data in data_list:
        name = data.get('name')
        phone_number = data.get('phone_number')
        address = data.get('address')
        pincode = data.get('pincode')

        if not name or not phone_number or not address or not pincode:
            results.append({'error': 'All fields are required!'})
            continue

        # Create a document to insert into MongoDB
        customer_details = {
            'name': name,
            'phone_number': phone_number,
            'address': address,
            'pincode': pincode
        }

        try:
            # Insert the document into the collection
            collection.insert_one(customer_details)
            results.append({'message': f'Details for {name} submitted successfully!'})
        except Exception as e:
            results.append({'error': f'Error submitting details for {name}: {str(e)}'})

    return results

# Example data list
data_list = [
    {
        'name': 'John Doe',
        'phone_number': '9997896356',
        'address': '123 Main Street, Coimbatore',
        'pincode': '641202'
    },
    {
        'name': 'Harshini',
        'phone_number': '9876543210',
        'address': '456 Elm Street, Coimbatore',
        'pincode': '600001'
    },
      {
        'name': 'Dhiviya',
        'phone_number': '9876543210',
        'address': '456 Elm Street, Coimbatore',
        'pincode': '600001'
    },
      {
        'name': 'Angu',
        'phone_number': '9876543210',
        'address': '456 Elm Street, Coimbatore',
        'pincode': '600001'
    }
]

# Call the function to submit details
results = submit_details(data_list)
for result in results:
    print(result)
