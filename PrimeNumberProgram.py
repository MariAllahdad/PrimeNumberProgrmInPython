val = int(input('Enter number: '))
i=2
while(i < val):
    if(val % i == 0):
        print('It is not prime No ')
        break
    i+=1

if(i == val):
    print('it is prime number')

elif(val == 1):
    print('It is not prime No ')
