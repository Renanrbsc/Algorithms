"""
Pagamento exigido pelo total de metros cúbicos de água ao encher uma piscina.
"""

preco_m3 = float(input("Informe o custo (R$) por metro cúbico de agua:"))

print("Informe as dimensões da piscina:")
Lar = float(input("Largura [metros]:"))
Comp = float(input("Comprimento [metros]:"))
Alt = float(input("Altura [metros]:"))

vol = Lar * Comp * Alt

print("As dimensoes da piscina são Largura x Comprimento x Altura: ")
print(str(Lar) + "x" + str(Comp) + "x" + str(Alt) + ' m3' + '\n')
print("Volume de agua " + str(vol) + " m3")
print("Valor a pagar R$/" + str(preco_m3 * vol) + "\n")
