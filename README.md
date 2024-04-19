Phone Number Carrier Details

**Intro:**
This Python script utilizes the `phonenumbers` library to parse a given phone number and retrieve the carrier's name associated with it. 
It's coded to work with international phone numbers and requires the appropriate country code to be provided in the code.

**Main tasks/functions:**
- **Phone Number Parsing**: Parses the input phone number using the `phonenumbers` library.
- **Carrier Information Retrieval**: Fetches the carrier name for the parsed phone number.
- **International Support**: Can handle phone numbers from various countries by specifying the country code.

**HOw to Run:**
1. Install the `phonenumbers` library using `pip install phonenumbers`.
2. Run the script in a PyCharm.
3. Enter the phone number and the country code
4. The script will print the location and carrier name associated with the phone number.


**Code snippet:**
from phonenumbers import carrier, parse

number = "YourPhoneNumberHere"  # Replace with the actual phone number
service_number = parse(number, "US")  # Replace "US" with the appropriate country code
carrier_name = carrier.name_for_number(service_number, "en")
print(carrier_name)
