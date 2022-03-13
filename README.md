# MORSE CODE TRANSLATOR

Este projeto tem como objetivo a criação de um site que permite ao usuário traduzir um código morse baseado na tabela de tradução abaixo:

![Tabela](https://raw.githubusercontent.com/RafaelGruhn/morse_code/master/flaskr/static/table_morse_translator.png)

## Modo de uso [ambiente de desenvolvimento]

Tendo o `Docker e Docker Compose` previamente instalado em sua máquina, na raíz do projeto execute `docker-compose up --build`
O comando irá subir a aplicação em um container docker e você poderá acessá-la no link: [http://0.0.0.0:8000](http://0.0.0.0:8000)

Exemplo de requisição simples para o endpoint de descriptografia: `curl -X POST -H "Content-Type: application/json" -d '{"message": "--- .-.. .-"}' 0.0.0.0:8000/decrypt_morse`
Resultado esperado: "OLA"

## Endpoints da Aplicação
* `/`: Métodos permitidos (`GET`)
* `/decrypt_morse`: Meétodos permitidos (`POST`)

## Tecnologias Empregadas

* Frontend baseado na stack HTML + Boostrap
* Backend desenvolvido em Phython Flask
* Ambiente totalmente dockerizado
* Cache implementado utilizando o Redis
* Workflows de CI para análize de código estático utilizando actions próprias escritas em Github Actions 

## Implementações Futuras

* Adição de testes e workflow de execução de testes
* Adição de cadastro de usuários
* Limitação de uso da API por cota de usuário autenticado e anônimo
* Documentação do swagger da api
* Tradução do código Morse por palavra adicionada (atualmente todo o código é retraduzido)
* Implentação de HPA baseado no consumo de recursos
* Adição de fila com RabbitMQ para o endpoint da API
* Adição de rotina de Stress Test
* Utilização de um Compressor para o Javascript
* Adição de Nginx ou outra solução para pegar expor os arquivos estáticos sem passar pela aplicação
