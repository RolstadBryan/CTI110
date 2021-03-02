user_int = int(input('Enter integer (32 - 126):\n'))

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
float = float(input('Enter float:\n'))
character = input('Enter character:\n')
string = input('Enter string:\n')
print(user_int,float,character,string)
# FIXME (2): Output the four values in reverse
print(string,character,float,user_int)
# FIXME (3): Convert the integer to a characer, and output that character
convert = chr(user_int)
print(user_int,'converted to a character is',convert)