from algorithms import gcd, lcm, is_even, is_prime

a = int(input("First number: "))
b = int(input("Second number: "))

print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))

number = int(input("Enter a number: "))

print("Even:", is_even(number))

number = int(input("Enter a number to check if it's prime: "))

print("Prime:", is_prime(number))