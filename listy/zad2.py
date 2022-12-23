Tax = (4, 7, 8, 23)
print(Tax[-1]) #ostatni element
print(max(Tax))

#tax.revert()
TaxList = list(Tax)
TaxList.append(30)
NewTax = tuple(TaxList)

print(TaxList)
print(NewTax)

(tax1, tax2, tax3, tax4) = Tax
print(tax1, tax2, tax3, tax4)

#przypisanie z wykorzystaniem tuple
a=1
b=10
(a, b) = (b, a)
print(a, b)

#zadania

lista = ['loyality program', 'client promotion', 'market research']
lista.append('public relations')
print(lista[3])
lista.insert(2,'investor relations')
emailMarketing = lista.copy()
emailMarketing.sort()
onelementl = ['internal communication']
emailMarketing.extend(onelementl)
NewEmail = tuple(emailMarketing)
print(NewEmail)
