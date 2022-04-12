# Importando a biblioteca
import pandas as pd

# Tratando os dados
uri = r'/content/esus-vepi.LeitoOcupacao_2022.csv'
tabela = pd.read_csv(uri)
tabela = tabela.drop(columns=['Unnamed: 0', '_id', 'origem', '_p_usuario', 'excluido', '_created_at'])
tabela = tabela.rename(columns={'_updated_at': 'atualizado'})
tabela_test = tabela.fillna(0)

# Salvando os dados tratados em outro arquivo.
tabela_test.to_csv('novos_dados.csv')
