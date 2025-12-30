import requests
currency_url = "https://api.frankfurter.app/2023-01-01"

data = requests.get(currency_url)
print(data)

if data.status_code==200:
    #Conbverting the data into json
    mydata = data.json()

    user_input = int(input("Enter Amount in Euro:-"))
    to_change = input("Enter Currency Code you want to Change:-")
    if to_change in mydata['rates'].keys():
        converted_amount = user_input*mydata['rates'][to_change]
        print("Converted Amount = ",converted_amount)
else:
    print("Unable to Retrive the Data Please Try Again")