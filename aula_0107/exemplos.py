import re

txt = "Os melhores engenheiros são do Brasil"

x = re.search("^Os.*Brasil$", txt)

if x:
    print("string aprovada na regex")
else:
    print("string rejeitada na regex")
