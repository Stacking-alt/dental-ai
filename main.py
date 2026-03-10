import os
from dotenv import load_dotenv
from retell import Retell

load_dotenv()

# Initialize the Retell client
client = Retell(api_key=os.getenv("cal_live_b13d38df3fefbe5f1798604a270895ed"))

def create_call(to_number):
    try:
        call = client.call.create_phone_call(
            from_number="+1234567890", # Your Retell/Twilio number
            to_number=to_number,
            agent_id=os.getenv("4965348")
        )
        print(f"Call initiated successfully: {call.call_id}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # You can trigger a test call here
    print("Smile 4 U AI Receptionist is active.")