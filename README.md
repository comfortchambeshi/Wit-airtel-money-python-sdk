# Wit Airtel money developer python SDK

### PROJECT REQUIREMENTS
- Airtel money developer account: https://developers.airtel.africa/user/signup
- Airtel money client_id and secrete_key
- Airtel money disbursement pin
- Python 3+

### First step edit environment_mode, x_country, x_currency, client_id and client_secret values from /classes/airtel_pay.py as shown below:

```
    #Main
    x_country = "country_code?"
    x_currency = "currency_code?"
    #Check if sandbox or production
    #Choose either sandbox or production
    environment_mode = "stagging"
    #pin
    disbursement_pin = "your disbursement pin?"

    #Configure keys
    client_id = "client_id?"
    client_secret = "client_secret?"
```

After configuring the above initiliasation steps, then you are ready to collect and disburse the payments. Follow the below instructions.

### REQUEST PAYMENT CALL
To collect or request a payment you kindly need to call the following function
```
from classes.airtel_pay import AirtelPay

#Request pay
pay = AirtelPay.pay("ten_digits_phone_number", "amount", "currency_code", "country_code", "transaction_id")
print(pay["jsondata"])
```

### CHECK/VERIFY TRANSACTION CALL
To check the transaction status or verify, follow the below instructions:
```
from classes.airtel_pay import AirtelPay

#Verify/check transaction status
verify = AirtelPay.verify_transaction("transaction_id")
print(verify)
```


### DISBURSE/TRANSFER THE MONEY
To transfer or disburse money into your mobile money account, follow the below instructions:
ALERT!!!! This calling does not work without the disbursement pin!!! Follow the first instruction to configure your disbursement pin!
```
from classes.airtel_pay import AirtelPay

#Disburse funds
transfer = AirtelPay.transfermoney("airtel_phone_number", "amount")
print(transfer)
```

That's all for this tutorial fam. For personal support/assistance kindly use these details:
- Phone number: +260968793843
- Email: witlevels04@gmail.com

Thank you for your time!


