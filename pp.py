import requests
import json
import time

# --- Configuration ---

# 1. UPDATED: Using the actual Formspree endpoint URL provided by the user.
FORMSPREE_URL = "https://formspree.io/f/xyznjyjj"

# 2. UPDATED: Define the data you want to submit, matching your form fields.
# Formspree uses the keys you provide here as the field names in the email/dashboard.
FORM_DATA = {
    # Key names below are simplified from the form labels for best practice.
    "your_name": "Alexander Hamilton",
    "email_address": "alex.hamilton@us-treasury.gov",
    "phone_number": "555-0101",
    "admin_challenge": "Managing too many scattered documents and needing better version control.",
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
}

# --- Submission Logic ---

def submit_to_formspree(url, data):
    """
    Submits data to the Formspree URL using the requests library, ensuring 
    the data is sent as a valid JSON object.
    """
    
    # 1. Define the necessary headers for a JSON submission.
    # The 'Accept' header tells Formspree that we expect a JSON response.
    # The 'Content-Type' header is CRITICAL; it tells Formspree the body is JSON.
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    
    print(f"Attempting to submit data to: {url}")
    print(f"Data to be sent (as Python dict): {data}")

    try:
        # Use the 'json' parameter in requests.post. 
        # This automatically sets the Content-Type header and uses json.dumps(data) 
        # to correctly serialize the Python dictionary into a JSON string body.
        response = requests.post(url, headers=headers, json=data)

        # Check if the request was successful (HTTP status code 200-299)
        if response.ok:
            print("\n✅ Success! Formspree submission successful.")
            print(f"Status Code: {response.status_code}")
            print("Check your Formspree dashboard for the new entry.")
        else:
            # If Formspree returns an error (like a 400 Bad Request)
            print("\n❌ Error! Formspree submission failed.")
            print(f"Status Code: {response.status_code}")
            
            # Formspree often returns the specific error message in the response text
            try:
                error_response = response.json()
                print(f"Formspree Error Details (JSON): {error_response}")
            except json.JSONDecodeError:
                print(f"Raw Response Text: {response.text}")
            
            print("\nPossible causes for failure:")
            print("- The data keys might violate any custom validations you set in Formspree.")
            print("- If using an @-prefixed field (e.g., '_replyto'), ensure it contains a valid email format.")

    except requests.exceptions.RequestException as e:
        print(f"\n🛑 A network error occurred: {e}")

if __name__ == "__main__":
    submit_to_formspree(FORMSPREE_URL, FORM_DATA)

