atext='This is a text.'
print(atext.endswith('ext'))
print(atext.upper())
#isupper sprawdza czy tekst jest napisany wyłącznie dużymi literami
print(atext.upper().isupper())
print(atext.find('is'))
print(atext.find('is',3))
#replace wymaga tego samego typu;
print(atext.replace('a','4'))
print(atext.split(' '))
number = '100'
print(number.isdigit())
print(number.isdecimal())
#sprawdza czy w zmiennej znaki to litery
print(number.isalpha())
#sprawdza czy napis jest alfanumeryczny
print(number.isalnum())

#zadania
quote='A good programmer is someone who always looks both ways before crossing a one-way street'
print(quote.upper())
print(quote.lower())
print(quote.endswith('street'))
print(quote.upper().isupper())
print(quote.find('one'))
print(quote.replace('one', '1'))
print(quote.replace('one', '1').replace('both', '2'))
print(quote.split(' '))
print(quote.isdigit())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())