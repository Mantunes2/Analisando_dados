#Importando bibioteca
import pandas as pd

#Criando os dados
name = input('Nome: ')
idade = int(input('Idade: '))
gen = input('Genêro: ')
setor = input('Setor: ')
salario = float(input('Salário: '))
data = {
    'Nome': [name],
    'Idade': [idade],
    'Genêro': [gen],
    'Setor': [setor],
    'Salário (R$)': [salario]
}

df = pd.DataFrame(data=data) #Inserindo os dados na tabela
df.head() #Chamando o elemento de visualização de dados
