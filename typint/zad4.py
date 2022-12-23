s = "A python script"
print(s[0])
print(s[2])
print(s[2:7])
print(s[:8])
print(s[8:])

message = 'Document "cv.doc" was printed on printer: XEROX'
print(message.find(':'))
print(message[42:])

print(message.find('"'))
print(message[message.find('"')+1:])
tmp = message[message.find('"')+1:]
print(tmp[:tmp.find('"')])

q = 'THE EYES'
print(q[0:3]+q[5]+q[3]+q[7]+q[4]+q[6])

q= 'a gentleman'
print(q[3]+q[6]+q[7]+q[2]+q[0]+q[4]+q[5]+q[1]+q[8]+q[9:])

text = 'THE MORSE CODE'
print(text[1:3]+text[6]+text[8]+text[9]+text[10:12]+text[4]+text[13]+text[9]+text[12]+text[5]+text[0]+text[7])

#zadania pt 2

nr = 43
wynik = (nr*5+50)*20+1022-2001
print(wynik)

absense = 0.85
gpa = 3.5
work = False

passvar = absense > 0.8 and gpa >= 3.0 or work
print(passvar)

absense = 0.85
gpa = 3.5
work = False

passvar = absense > 0.8 and gpa >= 3.0 and work
print(passvar)

absense = 0.4
gpa = 2.5
work = True
passvar = absense > 0.8 and gpa >= 3.0 or work
print(passvar)



