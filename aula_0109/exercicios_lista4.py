import re

txt = "Viver é acalentar sonhos e esperanças, fazendo da fé a nossa inspiração maior. É buscar nas pequenas coisas, um grande motivo para ser feliz"

#questão 1
q1 = re.sub("[a-zA-ZçãéÉ]{6,}", "*", txt)
print(q1)

#questão 2
q2 = []
for match in re.finditer("[a-zA-Zçã]*[áàéèíìóòúùâêîôûÁÀÉÈÍÌÓÒÚÙÂÊÎÔÛ][a-zA-zçã]*", txt):
    q2.append(match.group())

print(q2)

#questão 3
q3 = re.sub("[a-zA-ZçãéÉ]", lambda m: m.group().swapcase(), txt)
print(q3)

#questão 4
q4_sub = re.sub(",|[.]", "", txt)
palavras = re.split("\\s", q4_sub)
q4 = re.search(f"{max(palavras, key=len)}", txt)
print(q4.span())

#questão 5
q5 = []
for match in re.finditer(r"\b[a-zA-ZçãéÉ]{2,6}\b", txt):
    q5.append(match.group())

print(q5)

#questão 6
q6 = re.split("[A-ZÁÀÉÈÍÌÓÒÚÙÂÊÎÔÛ]", txt)
print(q6)

#questão 7
q7 = []
for match in re.finditer("[a-zA-Zçã]*[AEIOUaeiouáàéèíìóòúùâêîôûÁÀÉÈÍÌÓÒÚÙÂÊÎÔÛ][a-zA-zçã]*", txt):
    q7.append(match.group())

print(q7)

#questão 8
q8 = re.sub(",|[.]|\\s", "", txt)
print(len(q8))
