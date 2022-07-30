# only the function answer is here not the whole code


import requests
def getPhoneNumbers(country, phoneNumber):
    # Write your code here
    url = "https://jsonmock.hackerrank.com/api/countries?name=" + country
    response = requests.get(url)
    res = response.json()
    data = res["data"]
    if not data:
        return -1
    codes = data[0]["callingCodes"]
    if len(codes) > 1:
        code = codes[-1]
    else:
        code = codes[0]
    return "+"+code+" "+phoneNumber