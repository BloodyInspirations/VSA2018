current_number = 1
previous_number = 0
X = int(raw_input("Enter a number."))

next_number = (previous_number + current_number)

for numb in range(0, X):
    print next_number
    previous_number = current_number
    current_number = next_number
    next_number = (previous_number + current_number)



X = int(raw_input("Enter a number."))
print X * X
