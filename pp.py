import requests
import json
import time

# --- Configuration ---

# UPDATED: Using the new Formspree endpoint provided by the user.
FORMSPREE_URL = "https://formspree.io/f/xkgqzdqe"

# 2. Define the data you want to submit.
# These keys should correspond to the fields you want to see in your email/dashboard.
FORM_DATA = {
    "your_name": "Alexander Hamilton - Final Test",
    "email_address": "final.test@example.com",
    "phone_number": "555-0103",
    "admin_challenge": "Testing the script with the newly verified Formspree ID.",
    # You can also use special Formspree fields like _replyto, _subject, etc.
    # "_replyto": "new.test@example.com", 
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
}

# --- Submission Logic ---

def submit_to_formspree(url, data):
    """
    Submits data to the Formspree URL using the requests library, ensuring 
    the data is sent as a valid JSON object.
    """
    
    headers = {
        'Accept': 'application/json',
        # This header is essential for Formspree to process the JSON body.
        'Content-Type': 'application/json', 
    }
    
    print(f"Attempting to submit data to: {url}")
    print(f"Data to be sent (as Python dict): {data}")
    
    # NEW: Show the exact JSON payload being sent
    json_payload = json.dumps(data, indent=4)
    print("\n--- JSON Payload being sent ---")
    print(json_payload)
    print("-------------------------------\n")

    try:
        # requests.post(..., json=data) handles the JSON serialization and content type header
        response = requests.post(url, headers=headers, json=data)

        # Check if the request was successful (HTTP status code 200-299)
        if response.ok:
            print("\n✅ Success! Formspree submission successful.")
            print(f"Status Code: {response.status_code}")
            print("Action Required: Check your Formspree dashboard for the new entry!")
        else:
            # If Formspree returns an error (like a 400 Bad Request)
            print("\n❌ Error! Formspree submission failed.")
            print(f"Status Code: {response.status_code}")
            
            try:
                error_response = response.json()
                print(f"Formspree Error Details (JSON): {error_response}")
            except json.JSONDecodeError:
                print(f"Raw Response Text: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"\n🛑 A network error occurred: {e}")

if __name__ == "__main__":
    if FORMSPREE_URL == "YOUR_NEW_FORMSPREE_ENDPOINT_HERE":
        print("🚨 Please update the FORMSPREE_URL variable with your actual Formspree endpoint before running.")
    else:
        # Run the submission
        submit_to_formspree(FORMSPREE_URL, FORM_DATA)
