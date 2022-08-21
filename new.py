# --> It represent a one line comment in python 

'''
It represent a multi-line comment
We can write any thing here
'''

a = 5   #here, a is a variable which stores/holds integer type value i.e 5
naam = "Kasmi"   #here, naam is a variable which stores/holds string type value i.e "Kasmi"

# And in python string are always inside single or double quotes: 
# For example: "kasmi"   OR   'kasmi'

# creation of function and calling of function

'''
syntax:

#creating function 
def function_name():
    # you can do any thing here
    return ...... something

#calling function
function_name()

'''

# example:

#creating function
def duita_num_joda():
    sum = 3+5
    print(sum)
    return sum

#calling function with their name
duita_num_joda()

# taking input from user:
# my_name=input("Please enter your name-->: ")
# print("Ma sanga stored bhako value yei ho-->",my_name)


f_name=input("Your first name:-->")
l_name=input("Your second name:-->")

def full_name_generator(first_name,second_name):
    full_name = f"{first_name} {second_name}"
    return full_name

print("Your full name is:", full_name_generator(f_name,l_name))


#string formatting
# print("My-1 name-2 is-3 abc-4 def-5")

phone_num = 984551
print(f"Your phone number is {phone_num}")

first =1 
second =2 
third =3
four =4
fifth = 5

print(f"My-{first} name-{second} is-{third} abc-{four} def-{fifth}")


# len function
length_of_this = len("Education")
print(length_of_this)