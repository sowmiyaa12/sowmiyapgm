def camel1(word):
import re
return ''.join(x.capitalizer()or',' for x in word.aplit(','))
print(camel1(input('enter the string'))
