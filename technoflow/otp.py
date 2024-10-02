import nexmo
import random

# Function to generate OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP via Nexmo
def send_otp_sms(receiver_number, otp):
    client = nexmo.Client(key='your_api_key', secret='your_api_secret')
    
    from_number = 'your_nexmo_number'  # Your Nexmo virtual number
    message = f"Your OTP is: {otp}"
    
    try:
        response = client.send_message({
            'from': from_number,
            'to': receiver_number,
            'text': message,
        })
        message = response['messages'][0]
        if message['status'] == '0':
            print("OTP sent successfully!")
        else:
            print(f"Error: {message['error-text']}")
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
if __name__ == "__main__":
    receiver_number = input("Enter your phone number (+countrycode): ")
    otp = generate_otp()
    send_otp_sms(receiver_number, otp)
