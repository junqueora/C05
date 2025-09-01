import re

txt = "Os melhores engenheiros são do Brasil"

x = re.search("^Os.*Brasil$", txt)

if x:
    print("string aprovada na regex")
else:
    print("string rejeitada na regex")

#findall (retorna uma tupla com os match objects)
txt2 = "oi, seu pai tem boi? foi o que pensei."

x2 = re.findall("oi", txt2)

print(f"matches {x2}")
print(f"quantidade de matches {len(x2)}")

txt3 = "o rato roeu a roupa do rei de roma. que rato danado!"

#search
x3 = re.search("rato", txt3)

if x3:
    print(f"o primeiro rato foi encontrado na posição {x3.start()}")

#span (retorna o intervalo da primeira ocorrência)
x4 = re.search("r[a-z]+o", txt3)

print(x4.span())

#retorna todos os intervalos de ocorrência
for match in re.finditer("r[a-z]+o", txt3): #o finditer irá transformar a string num iterador
    print(match.span())

#group (retorna o primeiro match object)
x5 = re.search("[a-z]*a[a-z]*", txt3)

print(x5.group())

#retorna todos os intervalos de ocorrência
for match in re.finditer("[a-z]*a[a-z]*", txt3): #o finditer irá transformar a string num iterador
    print(match.group())

#split
txt5 = "eu gosto de sorvete de chocolate; meu pai, de creme; meu irmão, de morango."

x6 = re.split(";", txt5)

print(x6)

x7 = re.split("\\s", txt5)

print(x7)

#sub
txt6 = "quando chover, busque pelo arco-íris. quando escurecer, busque pelas estrelas."

x8 = re.sub("quando", "sempre que", txt6)

print(x8)