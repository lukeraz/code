from math import radians, sin, cos, tan
ag = float(input("insira um angulo: "))
seno = sin(radians(ag))
cosseno = cos(radians(ag))
tangente = tan(radians(ag))
print(f"O angulo de {ag} tem o seno de {seno :.2f}")
print(f"O angulo de {ag} tem o cosseno de {cosseno :.2f}")
print(f"O angulo de {ag} tem o tangente de {tangente :.2f}")