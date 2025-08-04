
#  Type casting means converting one data type to another data type 

# Example

Num_str="100"        # This is a string, not a number
print(type(Num_str)) #  <class 'int'>


# Converting string to int

num=int(Num_str)
print(num+50)       # Output: 150
print(type(num))    #Output:<class 'int'>

# Converting int to float

float_num=float(num)
print(float_num+100)
print(type(float_num))  

# Converting float to string

str_num=str(num)
print(str_num)
print(type(str_num))
