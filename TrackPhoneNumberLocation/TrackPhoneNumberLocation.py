import phonenumbers
from phonenumbers import geocoder

#code to fetch the location of the phone number
from TrackPhoneNumberLocation.Phonenumber import number
ch_number = phonenumbers.parse(number, "CA")
print(geocoder.description_for_number(ch_number, "en"))
#code to fetch the carrier information of the phone number
from phonenumbers import carrier, is_valid_number
service_number = phonenumbers.parse(number, "CA")
try:
    if is_valid_number(service_number):
        carrier_name = carrier.name_for_number(service_number, "en")
        print(carrier_name or "No carrier information available")
    else:
        print("The Phone number is not valid")
except Exception as e:
    print(f"An error occurred",e)
