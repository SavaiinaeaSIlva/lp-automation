import requests
import json

# Configuration for the Formspree endpoint
# This is the endpoint provided: https://formspree.io/f/xkgqzdqe
FORMSPREE_URL = "https://formspree.io/f/xkgqzdqe"

# Data to be submitted.
# Keys MUST match the 'name' attributes you set on your HTML form fields.
# We are using the names 'name', '_replyto', 'phone', and 'challenge'
# as per the suggested HTML fixes in the previous response.
FORM_DATA = {
    "name": "Python Automated Test",
    "_replyto": "python-test@example.com", # Formspree uses _replyto for the sender email
    "phone": "555-123-4567",
    "challenge": "I need help with automating lead qualification and scheduling.",
    "_subject": "New Lead: Automated Submission Test" # Optional Formspree field to customize the email subject
}

def submit_form_to_formspree(url: str, data: dict):
    """
    Submits the specified data to the Formspree endpoint via an HTTP POST request.

    Args:
        url (str): The Formspree endpoint URL.
        data (dict): A dictionary containing form field names and their values.
    """
    print(f"Submitting data to: {url}")
    print(f"Data payload: {json.dumps(data, indent=2)}")
    
    # Send the POST request
    try:
        # Formspree expects form data, so we use the 'data' parameter for requests
        response = requests.post(url, data=data)
        
        # Check the response status code
        if response.status_code == 200:
            print("\n✅ SUCCESS: Form submitted successfully!")
            print("Check your email associated with the Formspree endpoint for the submission.")
        elif response.status_code == 302:
            print("\n✅ SUCCESS (Redirect): Form submitted successfully!")
            print("Formspree often responds with a 302 redirect after submission.")
            print("Check your email associated with the Formspree endpoint for the submission.")
        else:
            print(f"\n❌ FAILURE: Submission failed with status code {response.status_code}")
            print(f"Response text: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"\n❌ ERROR: An error occurred during the HTTP request: {e}")

if __name__ == "__main__":
    # Ensure you have the 'requests' library installed: pip install requests
    submit_form_to_formspree(FORMSPREE_URL, FORM_DATA)
