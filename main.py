

# simple api use in python
import time

import requests


#creating variables for check
districtId = 770
date = 26 - 0o5 - 2021

#url for api of cowin
URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(
    districtId , date
)

#headers of the api of cowin
header = {
    'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

#function to check whether the slot is available or not

def check_availablity()  :
    counter = 0
    result = requests.request(
        'GET',url = URL , headers=header
    )
    result_json = result.json()
    head_data = result_json["sessions"]

    for each in head_data :
        if ((each["available_capacity"] > 0) & (each["min_age_limit"] == 18)) :
            counter += 1
            print(each["name"])
            print(each["name"])
            print(each["address"])
            print(each["vaccine"])

            return True
    if (counter == 0) :
        print("No Data Center Available")


while (check_availablity() != True) :
    check_availablity()
    time.sleep(5)
    check_availablity()