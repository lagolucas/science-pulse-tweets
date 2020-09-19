# science-pulse-tweets
 twitter bot for science pulse project


# Instalação

## Criar uma máquina virtual EC2 na amazon (recomendo t3a.nano)

## Instalar os seguintes itens
### Com yum
`sudo yum install python3`

`sudo yum install python3-dev libpq-dev`


### Com pip3
`pip3 install peewee`

`pip3 install tweepy`

`pip3 install psycopg2-binary`

## clonar o repositório na máquina

## Configurações

### alterar o arquivo config.json.default

Colocar as credenciais corretas de banco e da api do twitter e renomear para config.json

# Uso do bot

## Parâmetros

### start

Na tabela de parametros são necessários parâmetros com o slug `start` para cada lingua que serão construídos os fios no twitter

### end

A mesma regra dos parâmetros `start` vale para os parâmetros `end`

### parametros para tipo de trends

Para cada tipo de trend usada no bot, é necessário um parâmetro com o `body_text` utilizado, isso será referenciado pelo param_id na tabela de fila de tweets

## Tweets

### Fila

No horário programado o robo irá fazer um tweet de início de fio e em seguida varrer a tabela de fila buscando todos os tweets para montar o fio.

Os tweets serão atualizados com `bot_flag = True` depois de ter realizado o tweet.



## A aplicação precisa de um parâmetro para funcionar corretamente

Para execução do script é necessário passar um parâmetro que será comparado a coluna `period_day` do banco de dados, atualmente os parâmetros no banco de dados são `night` ou `morning`, mas podem ser adicionados outros.