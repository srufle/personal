#!/usr/bin/env python
prob = 2019
base = 16
digit_length = 5
current_digit = 0
possible_digits = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}
print("We will convert " + str(prob) + " to base " + str(base))

print("")
print("Take the prob value and compare to base raised to a power until denominator is greater then prob value")
for n in range(digit_length):
    denominator = pow(base, n)
    print("denominator='" + str(denominator) + "'")
    if denominator > prob:
        current_digit = n - 1
        print("choosing base to the power of '" +
              str(current_digit) + "' as our largest value")
        break

curr_val = prob
while curr_val > 0:
    curr_denominator = pow(base, current_digit)
    ans = curr_val//curr_denominator
    if possible_digits.get(ans) is not None:
        ans_as_str = possible_digits[ans]
    else:
        ans_as_str = str(ans)
    print("Digit " + str(current_digit + 1) + " is " + ans_as_str)
    curr_val = curr_val - (ans * curr_denominator)
    print(str(curr_val) + " remains")
    current_digit = current_digit - 1

print("Done!!")
