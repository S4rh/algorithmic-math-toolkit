from algorithms import gcd, lcm, is_even

a = int(input("First number: "))
b = int(input("Second number: "))

print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))

number = int(input("Enter a number: "))

print("Even:", is_even(number))