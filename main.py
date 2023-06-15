import requests
from credenciais import nome, email, cpf


def requisicao_post_api(nome: str, email: str, cpf: str) -> str:
    ''' Essa função faz uma requisição POST para a API, 
        passando os parâmetros nome, email e cpf.
        Ex: requisicao_pos_api('nome-completo-sem-espaco', \
                                'seu-email@gmail.com', \
                                '000.111.222-33')
    '''

    url = f'https://cosmic-backbone-386318.rj.r.appspot.com/hashCodeServer?nome={nome}&email={email}&cpf={cpf}'
    resposta = requests.post(url)
    if resposta.status_code == 200:
        msg_resposta = resposta.json()
        codigo_hash = msg_resposta["hashCode"]
        pergunta = msg_resposta["pergunta"]

        print(f'\nRCódigo Hash: {codigo_hash}\n\nPergunta: {pergunta}')
    else:
        print('Erro na requisição:', resposta.status_code)


def custo_total_compra(valor_qtd_menor_que_uma_duzia: int, valor_qtd_maior_que_uma_duzia: int) -> str:
    ''' Essa função faz calculo de custo total de maçãs, ler o input(quantidade) e 
        recebe os parâmetros de valor_unitario_menor_que_uma_duzia e 
        valor_unitario_maior_que_uma_duzia.
        Ex: custo_total_compra(1.30, 1.00)
    '''

    quantidade = int(input('\nDigite a quantidade de maçãs: '))
    if quantidade < 12:
        custo_total_compra = quantidade * valor_qtd_menor_que_uma_duzia
        custo_total_compra = (
            f'R$ {custo_total_compra:,.2f}').replace('.', ',')
    else:
        custo_total_compra = quantidade * valor_qtd_maior_que_uma_duzia
        custo_total_compra = (
            f'R$ {custo_total_compra:,.2f}').replace('.', ',')

    print(f'\nCusto total da compra: {custo_total_compra}\n')


if __name__ == '__main__':
    requisicao_post_api(nome, email, cpf)
    custo_total_compra(1.30, 1.00)
