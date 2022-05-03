valor_veiculo = float(input())
sexo = str(input())
idade = int(input())

if sexo == "M" and idade <= 24:
    premio = valor_veiculo*0.10
elif sexo == "M" and 25 <= idade <= 33:
    premio = (valor_veiculo*0.10)*0.90
elif sexo == "M" and idade > 33:
    premio = (valor_veiculo*0.10)*0.80
elif sexo == "F" and idade <= 24:
    premio = ((valor_veiculo)*0.10)*0.95
elif sexo == "F" and 25 <= idade <= 33:
    premio = ((valor_veiculo)*0.10)*0.80
else:
    premio = ((valor_veiculo)*0.10)*0.65
    
print(f'{premio:.2f}')