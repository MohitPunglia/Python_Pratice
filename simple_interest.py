"""
A = P(1 + rt)

Where:

A = Total Accrued Amount (principal + interest)
P = Principal Amount
I = Interest Amount
r = Rate of Interest per year in decimal; r = R/100
R = Rate of Interest per year as a percent; R = r * 100
t = Time Period involved in months or years
From the base formula, A = P(1 + rt) derived from A = P + I and since I = Prt then A = P + I becomes A = P + Prt which can be rewritten as A = P(1 + rt)
"""

def simple_interest(principal,interest,duration):
    #amount=principal + interest
    #si=principal(1+interest*duration)
    si=(principal*interest*duration)/100
    print("Simple Interest : ",si)
    amount = principal+ si
    print("Simple Interest : ",amount)

simple_interest(100,4,5)
