# djanblo

Welcome to the djanblo!

Djanblo é um gerenciador de blog escrito em Python com framework Django, criado para ser um dos critérios de avaliação para uma vaga de emprego.

![djanblo blog](djanblo.png)
> Logo by [RoboHash](https://robohash.org/)

## Especificação

Desenvolver um sistema de blog usando Python e Django:

- [x] o sistema deve ter uma home page que mostre as postagens, da mais recente a mais antiga, paginadas, 10 postagens por página
- [ ] deve existir um sistema de login para que os administradores possam cadastrar novas postagens
- [x] deve utilizar o framework bootstrap para layout das páginas
- [x] deve existir uma API onde seja possível obter através de GET as postagens do banco
- [x] O código deve ser publicado no github, em uma conta pública

Será avaliado a sua qualidade de código.

## Instalação

baixe o código:

    git clone https://github.com/paulohrpinheiro/djanblo /tmp/djanblo

Crie uma *virtualenv* usando `virtualenvwrapper`:

    mkvirtualenv djanblo

ou, se usando `pyvenv` apenas:

    python3 -m venv /tmp/djanblo-venv
    source /tmp/djanblo-venv/bin/activate

Então instale a s dependências:

    pip install -r requirements.txt

## Uso

Para executar localmente, suba o servidor:

    cd djanblo
    ./manage.py runserver

e acesse, pelo browser, o endereço:

[http://127.0.0.1:8080](http://127.0.0.1:8080)

Há uma API, que responde retorna os seguintes recursos:

### [http://127.0.0.1:8080/api](http://127.0.0.1:8080/api)

É o ponto de entrada

Comando:

### [http://127.0.0.1:8080/api/posts](http://127.0.0.1:8080/api/posts)

Gera uma lista com todos os posts.

### [http://127.0.0.1:8080/api/posts/{path}](http://127.0.0.1:8080/api/posts/{path})

Devolve um post em específico, dado o seu `path` (veja mais abaixo uma explicação sobre o modelo de dados usado).

### Populando

Dados aleatórios podem ser gerados pelo comando:


## Testes automáticos e relatório de cobertura

    cd /tmp/djanblo
    pip install -r requirements.txt
    ./manage.py test

## Colaborando

É recomendável instalar as dependência de desenvolvimento:

    pip install -e requirements-dev.txt

## Modelo de dados

### Modelo `Post`

#### `title`

Título do post.

#### `subject`

Assunto do post, ou uma breve descrição do conteúdo.

#### `content`

É o texto do post.

#### `path`

É um campo de valores únicos e compõe o endereço do post.

#### `pud_date`

Data de inclusão do post. É gerado automaticamente.


#### `Author`

Quem incluiu o post, usa o modelo `User` do Django.


## Considerações gerais

- Assume-se como guia de estilo as regras da [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) e [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/). Para verificação automatizada de conformidade, recomenda-se o [pylint](https://www.pylint.org/), que está nas dependências de desenvolvimento.

- Não foram desenvolvidas configurações diferenciadas para produção, desenvolvimento ou testes. Usa-se uma configuração apenas, com SQLite como banco de dados.

- Stack de desenvolvimento:
    -   [Linux Fedora 25](https://fedoraproject.org/)
    -   [neovim](https://neovim.io/) com configurações geradas pelo [Vim Bootstrap](http://www.vim-bootstrap.com/)
    -   [tmux](https://tmux.github.io/)
    -   [Python 3.5.2](https://docs.python.org/3.5/index.html#)
    -   [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
    -   [ReText](https://github.com/retext-project/retext)
    -   [Git](https://git-scm.com/)!

## Licença

This is a [MIT licensed](LICENSE) project.