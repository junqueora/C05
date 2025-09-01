import re

txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#questão 1
q1 = re.search("sonhos", txt)
if q1:
    print("match!")
else:
    print("sem match!")

#questão 2
q2 = []
for match in re.finditer("[a-zA-Zç]*as", txt):
    q2.append(match.group())

print(q2)

#questão 3
q3 = re.sub("maior|grande", "surreal", txt)

print(q3)

#questão 4
q4 = re.search("inspiração", txt)
print(q4.span())

#questão 5
q5 = []
for match in re.finditer("[a-zA-Zçã]{9,}", txt):
    q5.append(match.group())

print(q5)

#questão 6
q6 = re.split(",|[.]", txt)

print(q6)

#questão 7
q7 = []
for match in re.finditer("[a-zA-Zç]*[éÉ][a-zA-Zç]*", txt):
    q7.append(match.group())

print(q7)

#questão 8
q8 = re.sub(",|[.]", "", txt)
q8 = re.split("\\s", q8)

print(len(q8))
