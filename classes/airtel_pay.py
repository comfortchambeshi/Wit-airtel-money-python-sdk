import requests
import json
import uuid

from pin import Pin


class AirtelPay():
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
    #Airtel money bearer token

    #Link check
    url_prefix = "https://openapiuat.airtel.africa"
    if environment_mode == "production":
      url_prefix = "https://openapi.airtel.africa"
    print(url_prefix)  
    def token():
        



        url = ""+AirtelPay.url_prefix+"/auth/oauth2/token"

        payload = json.dumps({
          "client_id": ""+str(AirtelPay.client_id)+"",
          "client_secret": ""+str(AirtelPay.client_secret)+"",
          "grant_type": "client_credentials"
        })
        headers = {
          'client_id': ''+str(AirtelPay.client_id)+'',
          'client_secret': ''+str(AirtelPay.client_secret)+'',
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        jsondata = response.json()
        return jsondata


    #Request to pay
    def pay(phone_number, amount, currency, country, txn):
       url = ""+str(AirtelPay.url_prefix)+"/merchant/v1/payments/"

       #Slice phone number
       slicedphone = phone_number[0].strip('0') + phone_number[1:]

       payload = json.dumps({
       "reference": "Referece for transactions",
       "subscriber": {
         "country": country,
         "currency": currency,
         "msisdn": slicedphone
       },
       "transaction": {
         "amount": amount,
         "country": country,
         "currency": currency,
         "id": txn
       }
     })
       headers = {
       'X-Country': country,
       'X-Currency': currency,
       'Accept': '*/*',
       'Authorization': 'Bearer '+AirtelPay.token()["access_token"]+' ',
       'Content-Type': 'application/json'
     }

       response = requests.request("POST", url, headers=headers, data=payload)
       jsondata = response.json()
       context = {"status":response.status_code, "jsondata":jsondata}
       return context

    #Veridy transaction
    def verify_transaction(txn):
       url = ""+str(AirtelPay.url_prefix)+"/standard/v1/payments/"+str(txn)+""

       payload = json.dumps({
       
     })
       headers = {
       'X-Country': ''+str(AirtelPay.x_country)+'',
       'X-Currency': ''+str(AirtelPay.x_currency)+'',
       'Accept': '*/*',
       'Accept': '*/*',
       'Authorization': 'Bearer '+AirtelPay.token()["access_token"]+' ',
       'Content-Type': 'application/json'
     }

       response = requests.request("GET", url, headers=headers, data=payload)
       jsondata = response.json()
       context = {"status":response.text, "jsondata":jsondata}
       return context

    #Airtel money balance
    def airtelbalance():
           url = ""+str(AirtelPay.url_prefix)+"/standard/v1/users/balance"

           payload = ""
           headers = {
             'X-Country': ''+str(AirtelPay.x_country)+'',
             'X-Currency': ''+str(AirtelPay.x_currency)+'',
             'Accept': '*/*',
             'Authorization': 'Bearer '+AirtelPay.token()["access_token"]+' ',
             'Cookie': 'SERVERID=s116'
           }

           response = requests.request("GET", url, headers=headers, data=payload)
           jsondata = response.json()
           return jsondata
    def transfermoney(phone_number, amount):
          #Get pin
          pin = Pin.get_pin()["pin"]
          #UUID V4 generator
          uuidgen = str(uuid.uuid4().hex[:20])
          url = ""+str(AirtelPay.url_prefix)+"/standard/v1/disbursements/"

          payload = json.dumps({


            "charges": {
          "service": 1
        },
          "payee": {
            "msisdn": phone_number
          },
          "reference": "Pay",
          "pin": ""+str(pin)+"",
          "transaction": {
            "charge": 1,
            "amount": amount,
            "id": uuidgen
          }
        

           
           
          })
          headers = {
            'X-Country': ''+str(AirtelPay.x_country)+'',
            'X-Currency': ''+str(AirtelPay.x_currency)+'',
            'Accept': '*/*',
            'Authorization': 'Bearer '+AirtelPay.token()["access_token"]+'',
            'Content-Type': 'application/json',
            'Cookie': 'SERVERID=s116'
          }

          response = requests.request("POST", url, headers=headers, data=payload)
          data = {"data":response.json(), "txn":uuidgen}
          return data
        



      
