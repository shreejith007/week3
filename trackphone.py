import geocoder


import phonenumbers
ch_number1=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number1,"en"))