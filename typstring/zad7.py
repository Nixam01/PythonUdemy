somethingLikeNumber='1000'
print(somethingLikeNumber)
var = int(somethingLikeNumber) + 1
print(var)
print(type(somethingLikeNumber))
print(type(var))

#zadania

article = '''Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy troupe who created the sketch comedy television show Monty Python's Flying Circus,
 which first aired on the BBC in 1969. Forty-five episodes were made over four series. The Python phenomenon developed from the television series into something larger in scope and influence, 
 including touring stage shows, films, albums, books and musicals.'''
print(article.upper())
print(article.lower().replace('monty', 'flying'))
print(article.split(" "))

print("word python appears "+str(article.lower().count('python'))+" times")
print("to print the \\ you need to put \\ twice \in your text like this: \\\\")
print("The best hits of '80s!!!")