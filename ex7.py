sir = input("Dati un sir de caractere: ")
print(sir)

a = 0
for i in sir:
    a = sir.count('A')
print("a) Numărul de apariții a caracterului „A”: ", a)

print("b) şirul obţinut prin substituirea caracterului ’A’ prin caracterul ’*’")
sir1 = sir
print(sir1.replace('A', '*'))

print("c) şirul obţinut prin radierea din şirul S a tuturor apariţiilor caracterului ’B’")
sir2 = sir
print(sir2.replace('B', ''))

c = 0
for i in sir:
    c = sir.count('MA')
print("d) numărul de apariţii ale silabei MA în şirul S:", c)

print("e) şirul obţinut prin substituirea tuturor apariţiilor în şirul S a silabei MA prin silaba TA")
print(sir.replace('MA', 'TA'))

print("f) şirul obţinut prin radierea din şirul S a tuturor apariţiilor silabei TO")
print(sir.replace('TO', ''))

print("g) scrierea inversă a şirului S")
sir3 = sir
print(sir3[::-1])

print("h) true dacă şirul S este palindrom şi false în caz contrar")
if sir == sir[::-1]:
    print('true')
else: print('false')

print("i) şirul obţinut prin transformarea tuturor literelor mici din componenţa şirului S în litere mari")
print(sir.upper())

print("j) şirul obţinut prin transformarea primei litere a fiecăruia dintre cuvintele din componenţa şirului S în literă mare")
print(sir.title())

print("k) şirul obţinut prin sortarea în ordine alfabetică a caracterelor din şirul S")
sir = sorted(sir)
sir = "".join(sir)
print(sir)