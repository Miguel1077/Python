nombre = input("ingrese su nombre")
edad = int(input("ingrese su edad"))
ciudad = input("cual es su ciudad")
horas_trabajadas = float(input("cuantas horas trabajo"))
salario_base =int(input("valor hora"))
horas_extra = float(input("Ingrese las horas extra trabajadas: "))
valor_hora_extra = float(input("Ingrese el valor por hora extra: "))

salario_base_total = horas_trabajadas * salario_base
salario_extra = horas_extra * valor_hora_extra
salario_total = salario_base_total + salario_extra
