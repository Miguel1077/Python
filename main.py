nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
ciudad = input("cual es su ciudad: ")
horas_trabajadas = float(input("cuantas horas trabajo: "))
salario_base =int(input("valor hora: "))
horas_extra = float(input("Ingrese las horas extra trabajadas: "))
valor_hora_extra = float(input("Ingrese el valor por hora extra: "))

salario_base_total = horas_trabajadas * salario_base
salario_extra = horas_extra * valor_hora_extra
salario_total = salario_base_total + salario_extra


print("\nColilla de Pago")
print("Nombre: {}".format(nombre))
print("Edad: {}".format(edad))
print("Ciudad: {}".format(ciudad))
print("Horas Trabajadas: {}".format(horas_trabajadas))
print("Salario Base por Hora: ${}".format(salario_base))
print("Salario Base Total: ${}".format(salario_base_total))
print("Horas Extra: {}".format(horas_extra))
print("Valor Hora Extra: ${}".format(valor_hora_extra))
print("Salario por Horas Extra: ${}".format(salario_extra))
print("Salario Total: ${}".format(salario_total))