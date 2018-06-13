# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

numb_name = [2, 3, 5, 7, 8, 9, 15, 82, 63, 800, 89, -25, -5846]
for item in numb_name:
    if item < 5:
        print item


#Part II
# Take two lists, say for example these two:
#b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
print"________"
m = [1, 2, 15, 5, 8, 9, 10, 7]
l = [7, 8, 13, 14, 20, 45, 9, 10]

for item in m:
    for item_l in l:
        if item == item_l:
            print item


#Part III
# Take a list, say for example this one:


# and write a program that replaces all “a” with “*”.

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
print "______"
counter = 0
for item in d:
    if item == "a":
        d[counter] = "*"
    counter = counter + 1
print d







#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.

dog = raw_input("Please enter a word:")
L = []
L2 = []
for letter in dog:
    L.append(letter)
    L2.append(letter)
print L
L2.reverse()
print L2




