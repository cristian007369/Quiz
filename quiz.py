# Programa para aplicar los operadpres aritmeticos 
print("------------------------------------")
print("----------------Quiz----------------")
print("------------------------------------")
# imput 
n= int(input("Digite el valor de x: "))
# Processing
a=n//100
b=n%100
c=b//10
d=b%10
e=a+c*10+d*100
# output
print("-----------------------------------------------")
print("------------------ RESULTADOS -----------------")
print("-----------------------------------------------")
print("Nümero invertido: " + str(e))