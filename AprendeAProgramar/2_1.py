horas = int(input())
precio = int(input())


if horas <= 35:
    salario = horas * precio
else:
    salario = (35*precio) + ((horas - 35) * (1.5*precio))




if salario <= 500:
    impuestos = 0
elif salario <= 900:
    impuestos = (salario - 500) * 0.25
else:
    impuestos = (salario - 900) * 0.45 + 100




SalarioNeto = salario-impuestos
print(SalarioNeto)





