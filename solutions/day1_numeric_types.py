# Given an integer number, print its last digit.
x = 7343
print(f'Last digit of {x}:', x % 10)

# Given a three-digit number. Find the sum of its digits.
x = 852
print(f'Sum of digits of {x}:', x // 100 + x // 10 % 10 + x % 10)

# Given any number. Find the sum of its digits.
x = y = 852214463
sum_of_digits = 0
while x:
    sum_of_digits += x % 10  # sum_of_digits = sum_of_digits + last_digit
    x //= 10
print(f'Sum of digits of {y}: {sum_of_digits}')


# Given the integer N - the number of minutes that is passed since midnight -
# how many hours and minutes are displayed on the 24h digital clock?
# The program should print two numbers: the number of hours (between 0 and 23)
# and the number of minutes (between 0 and 59).
# For example, if N = 150, then 150 minutes have passed since midnight -
# i.e. now it's 2:30 am. So the program should print 2 30.
minutes_since_midnight = 150
minutes_in_hour = 60
print('Time on digital clock:',
      minutes_since_midnight // minutes_in_hour,
      minutes_since_midnight % minutes_in_hour)

print('Time on digital clock:', *divmod(minutes_since_midnight, minutes_in_hour))
