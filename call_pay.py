from classes.airtel_pay import AirtelPay

#Request pay
#pay = AirtelPay.pay("0972927679", "1", "ZMW", "ZM", "random-02345678")
#print(pay["jsondata"])


#Verify/check transaction status
#verify = AirtelPay.verify_transaction("random-02345678")
#trans = verify["jsondata"]["data"]["transaction"]["status"]

#print(verify["jsondata"])
#if trans == "TF":
#    print("Your transactio was failed!")

#if trans == "TS":
#    print("Transaction was successful!")

#if trans == "TP":
#    print("Your transaction is pending!")    


#Disburse funds
transfer = AirtelPay.transfermoney("0972927679", "5")
print(transfer)
