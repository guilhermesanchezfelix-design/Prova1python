#-- Calculdora de lanche--
valor_lanche = float(input("qual o valor do lanche?"))
if valor_lanche <= 10.00:
   print("preço justo")
elif 10.01 <= valor_lanche <= 20.00:
   print("esta ficando caro!")
else:
   print("muito caro, melhor levar de casa!")