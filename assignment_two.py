## even number 
print("Even Number with for loop")
for num in range(1, 30):
        if num % 2 == 0 :
            print(num)

print("EvenNumber with while loop")
i=1
while(i < 30):
    if i % 2 == 0 :
        print(i)
    i=i + 1

## odd numbers
print("ood number with for loop")
for num in range(1,32):
        if num % 2 !=0 :
            print(num)

print("odd number with while loop")
i=1
while(i< 30 ):
    if i % 2 != 0 :
        print(i)
    i = i + 1
##

def aquireCustomer(initialAmount):
    print(" initial Amount :", initialAmount, "GHC")
    marketing = 0.25 * initialAmount
    print(" Marketing cost :", marketing, "GHC")
    #rest =initialAmount - marketing
    otherOperation = 0.50 * initialAmount
    print(" Other Operation cost :", otherOperation, "GHC")
    numberCustomers = (0.25*initialAmount)/5
    print(" Number of Customers :", numberCustomers)


print("   Ahmed Capstone Financial Statement   ")
aquireCustomer(50000)