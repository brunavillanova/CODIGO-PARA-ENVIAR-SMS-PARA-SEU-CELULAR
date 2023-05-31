# CODIGO-PARA-ENVIAR-SMS-PARA-SEU-CELULAR
import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf21bf1698e6e2c90e5c9a31336d1d2f6"
# Your Auth Token from twilio.com/console
auth_token  = "0d0cbe133b826587a712c7a555d0b509"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
        to="seu numero celular",
        from_="+numero que o twilio disponibiliza",
        body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
    print(message.sid)