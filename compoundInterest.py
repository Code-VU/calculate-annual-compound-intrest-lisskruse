def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundIntrest()
# This first 3 lines are provided for you
    def interest(principal,rate,time):
        amount = principal*((1+rate/100)**time)
        return(amount-principal)
        
    client_one_principal = float(input("Principle (amount): "))
    client_one_time =      float(input("Time:               "))
    client_one_rate =      float(input("Rate:               "))
    print("Compound Interest: "+str(round(interest(client_one_principal,client_one_rate,client_one_time),1)))
    print ("---")
    client_two_principal = float(input("Principle (amount): "))
    client_two_time =      float(input("Time:               "))
    client_two_rate =      float(input("Rate:               "))
    print("Compound Interest: "+str(round(interest(client_two_principal,client_two_rate,client_two_time),2)))
    print ("---")
    client_three_principal = float(input("Principle (amount): "))
    client_three_time =      float(input("Time:               "))
    client_three_rate =      float(input("Rate:               "))
    print("Compound Interest: "+str(round(interest(client_three_principal,client_three_rate,client_three_time),1)))

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN

#calculateCompoundInterest()
