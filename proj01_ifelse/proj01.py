# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


# If you complete extensions, describe your extensions here!


print "Hello there!"
your_name = raw_input("What is your name?")
date_of_grad = raw_input("What grade are you in?")

print your_name + ", you will graduate in" + str(12 - int(date_of_grad)) + "years."


print "Hi!"
your_name = raw_input("What is your name?")
your_name = your_name[0].upper() + your_name[1:100].lower()
print your_name


print "Hello!"
your_name = raw_input("What is your name?")
your_name = your_name[0:2].lower() + your_name[2].upper() + your_name[3:].lower()
print your_name



print "Hey there!"
birth_month = int(raw_input("What is your birth month in a number?"))
birth_day = int(raw_input("What is the date of when you were born?[Number]"))
date_current = 11
month_current = 6
if birth_month >= month_current:
    print "Your birthday is in" + str(birth_month - month_current)
elif month_current >= birth_month:
    print "Your birthday is in" + str(12-(month_current - birth_month))
print "months"
print '/'
if birth_day >= date_current:
    print str(birth_day - date_current)
elif date_current >= birth_day:
    print str(30-(date_current - birth_day))
print "days."

















