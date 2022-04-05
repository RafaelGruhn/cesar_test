# MORSE CODE TRANSLATOR

Este projeto tem como objetivo a criação de um site que permite ao usuário traduzir um código morse baseado na tabela de tradução abaixo:

![Tabela](https://github.com/RafaelGruhn/morse_code/blob/master/flaskr/static/table_morse_translator.png?raw=true)

O objetivo deste projeto é criar uma ferramenta simples e escalonável que permita ao usuário converter textos escritos utilizando o `Código Morse` em textos utilizando o sistema de escrita padrão

Como a solução em sí é muito simples foi utilizado o Framework Flask para o desenvolvimento do Backend, por ser muito rápido e minimalista, além de que é extremamente recomendado para projetos desse tipo.
Para aliviar o processamento da mensagem foi utilizado o Redis como sistema de armazenamento de cache, removendo então a necessidade do servidor fazer a decodificação no caso desse processamento já ter sido feito recentemente.
Não achei necessário separar a aplicação em Frontend e Backend por ela ser muito simples e ter poucas telas, então utilizei o Boostrap e outros plugins para facilitar a interação com o usuário.
Utilizei WebSocket para criar uma conexão direta entre o frontend e backend, permitindo assim uma comunicação assíncrona e reativa o que melhora a experiência do usuário.

## Modo de uso [ambiente de desenvolvimento]

Tendo o `Docker e Docker Compose` previamente instalado em sua máquina, na raíz do projeto execute `docker-compose up --build`
O comando irá subir a aplicação em um container docker e você poderá acessá-la no link: [http://0.0.0.0:8000](http://0.0.0.0:8000)

Exemplo de requisição simples para o endpoint de descriptografia: `curl -X POST -H "Content-Type: application/json" -d '{"message": "--- .-.. .-"}' 0.0.0.0:8000/decrypt_morse`
Resultado esperado: "OLA"

## Executando em Modo Produtivo

Para rodar em ambiente produtivo execute: `docker-compose -f docker-compose.yml -f docker-compose.prd up --build`

## Endpoints da Aplicação
* `/`: Métodos permitidos (`GET`)
* `/decrypt_morse`: Métodos permitidos (`POST`)

## Tecnologias Empregadas

* Frontend baseado na stack HTML + Boostrap
* Backend desenvolvido em Phython Flask
* Ambiente totalmente dockerizado
* Cache implementado utilizando o Redis
* Workflows de CI para análize de código estático utilizando actions próprias escritas em Github Actions 

## Implementações Futuras

* Adição de mecanismo para fazer o processo inverso da descriptografia do código Morse (insere texto e tranforma em Morse)
* Adição de testes e workflow de execução de testes
* Adição de balanceador de carga para múltiplos workers com gunicorn
* Adição de cadastro de usuários
* Limitação de uso da API por cota de usuário autenticado e anônimo
* Documentação do swagger da api
* Tradução do código Morse por palavra adicionada (atualmente todo o código é retraduzido)
* Implentação de HPA baseado no consumo de recursos
* Adição de fila com RabbitMQ para o endpoint da API
* Adição de rotina de Stress Test
* Utilização de um Compressor para o Javascript
* Adição de Nginx ou outra solução para expor os arquivos estáticos sem passar pela aplicação
* Melhoria dos logs da aplicação
