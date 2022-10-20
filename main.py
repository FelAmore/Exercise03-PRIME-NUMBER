# Exercise03 PRIME NUMBER
#
def isPrime(num):
    for i in range (2, num):
        if num%i == 0:
            return False
    else:
        return True

num = int(input('Enter an integer: '))
print(isPrime(num))

