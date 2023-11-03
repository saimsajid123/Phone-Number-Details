import phonenumbers
from phonenumbers import timezone,geocoder,carrier

phonenum=input("Enter Your Phone Number With +__ eg if u r from pakistan then use +92 = ")
phone=phonenumbers.parse(phonenum)
time=timezone.time_zones_for_number(phone)
geo=geocoder.description_for_number(phone,"en")
car=carrier.name_for_number(phone,"en")

print(phone)
print(time)
print(geo)
print(car)
