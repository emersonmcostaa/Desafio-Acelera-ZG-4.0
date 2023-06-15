# Desafio - Acelera ZG 4.0  
Repositório com o script do desafio para Estagio na ZG Soluções.
##

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/emersonmcostaa/Desafio-Acelera-ZG-4.0/blob/main/LICENSE) 
##

### Descrição do desafio
Seja bem vind@ a etapa de Desafio, aqui queremos ver como você se sai frente a um problema novo. Siga as orientações e poste o resultado no campo indicado. Iremos avaliar o tempo que levou para resolver a questão com base em sua submissão. Então seja o mais rápido que puder. Boa sorte e mãos a obra!  

Olá, Seja bem vind@ a etapa de Desafio.  
Queremos que você faça uma requisição HTTP para o endereço:  
<"https://cosmic-backbone-386318.rj.r.appspot.com/hashCodeServer?nome=Exemplo&email=XXX@gmail.com&cpf=XXX.XXX.XXX-XX">  
Essa requisição deve ser do tipo POST e deve conter em seus parâmetros as seguintes informações:  

 - Seu nome completo sem espaços,
 - seu e-mail,
 - seu cpf,

Se sua requisição for realizada de forma correta você receberá uma mensagem de sucesso com um código hash e uma pergunta, esse código, a pergunta e a resposta a essa pergunta deverão ser inseridos nos campos destinado a esse fim.  

Além do código, da pergunta e da resposta a pergunta, você deve descrever qual foi sua estratégia para realizar sua essa requisição, compartilhar qualquer dificuldade que tenha passado e caso tenha desenvolvido algum código para realizar essa atividade, pedimos que poste também.  

Para cada um desses itens, há um campo definido a seguir.  

Certifique-se de reservar tempo suficiente para fazer o teste. Caso você saia do teste sem finalizá-lo, o teste será considerado como concluído e você não poderá fazer novamente.  
##

### Output do código:  
![output_Requisição_api](https://github.com/emersonmcostaa/Desafio-Acelera-ZG-4.0/assets/99415850/69013faf-ced1-47ee-9118-06769d02c68b)

### Importante:
Existe um arquivo chamado [`crendiciais.py`](https://github.com/emersonmcostaa/Desafio-Acelera-ZG-4.0/blob/main/credenciais.py) que nele você irá colocar as suas informações, basicamente exitem 3 variaveis dentro dele, que são (nome, email e cpf), o arquivo [`main.py`](https://github.com/emersonmcostaa/Desafio-Acelera-ZG-4.0/blob/main/main.py) precisa delas pra fazer a requisição na API.  
  
Criei essa solução para não deixar essas informações pessoais dentro do código principal.
##

### Tecnologias utilizadas

- __Python__

   _Módulo_ `requests`

## Como executar o projeto

Pré-requisitos: Python 3.6 ou superior

```bash
# clonar repositório
git clone https://github.com/emersonmcostaa/Desafio-Acelera-ZG-4.0

# instalar bibliotecas usadas no projeto
pip install -r requirements.txt

# executar o projeto
python main.py

```

## Autor

Emerson Monteiro da Costa

https://github.com/emersonmcostaa

https://www.linkedin.com/in/emersonmcostaa
