# API-blog

API de Blog em Flask

Este projeto é uma API de Blog desenvolvida em Flask, oferecendo funcionalidades básicas para o gerenciamento de autores e postagens. A API é construída com o intuito de fornecer uma estrutura sólida que pode ser expandida conforme necessário para atender aos requisitos específicos do seu projeto.

Funcionalidades Principais

Cadastro de Autores:

* Sistema de registro para novos autores no blog.
* Cada autor é representado por um nome, senha e e-mail único.

Cadastro de Postagens:

* Facilita a criação de novas postagens.
* Cada postagem possui um título e está associada a um autor existente.

Autenticação por Token:

* Implementa autenticação de usuários através de tokens JWT.
* Login é necessário para obter um token de acesso, essencial para operações na API.

Leitura de Conteúdo:

* Permite visualizar todas as postagens disponíveis no blog.
* Oferece detalhes específicos de uma postagem através do seu ID.
* Facilita a obtenção de uma lista de todos os autores cadastrados no blog.

Operações de Edição e Exclusão:

* Possui funcionalidades para editar e atualizar informações de postagens existentes.
* Permite a exclusão de postagens indesejadas.
* Facilita a edição de informações relacionadas a autores, como nome, e-mail e senha.
* Oferece a capacidade de excluir autores do sistema.

Como Executar

Instalação de Dependências:
pip install -r requirements.txt

Execução do Servidor:
python main.py

O servidor Flask será executado localmente na porta 7777 por padrão.