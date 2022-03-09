# A four-digit integer is given. Find the sum of even digits in it.

# Create a variable "var_int" and assign it a four-digit integer value.

# Create a variable "sum_even" and assign it 0.

# Find the sum of the even digits in the variable "var_int".

var_int = 1184
sum_even = 0
x1 = var_int % 10
var_int //= 10
sum_even += (x1 + 1) % 2 * x1

x2 = var_int % 10
var_int //= 10
sum_even += (x2 + 1) % 2 * x2

x3 = var_int % 10
var_int //= 10
sum_even += (x3 + 1) % 2 * x3

x4 = var_int % 10
var_int //= 10
sum_even += (x4 + 1) % 2 * x4

print(sum_even)