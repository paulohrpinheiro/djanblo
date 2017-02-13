# djanblo

Welcome to the djanblo!

Djanblo é um gerenciador de blog escrito em Python com framework Django, criado para ser um dos critérios de avaliação para uma vaga de emprego.

![djanblo blog](djanblo.png)
> Logo by [RoboHash](https://robohash.org/)

## Especificação

Desenvolver um sistema de blog usando Python e Django:

- [x] o sistema deve ter uma home page que mostre as postagens, da mais recente a mais antiga, paginadas, 10 postagens por página
- [x] deve existir um sistema de login para que os administradores possam cadastrar novas postagens
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

Crie um usuário:

    ./manage createsuperuser

e acesse, pelo browser, o endereço:

[http://127.0.0.1:8080](http://127.0.0.1:8080)

## Admin

Para administrar usuários e posts (operações CRUD), acesse o endereço:

[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## API

Há uma API, que responde pelos seguintes recursos:

### [http://127.0.0.1:8080/api](http://127.0.0.1:8080/api)

É o ponto de entrada. Retona um código de resposta HTTP 200:

    ➤ curl -i http://127.0.0.1:8000/api                                                                      
    HTTP/1.0 200 OK
    Date: Mon, 13 Feb 2017 09:59:56 GMT
    Server: WSGIServer/0.2 CPython/3.5.2
    X-Frame-Options: SAMEORIGIN
    Content-Type: application/json
    {"post_content": "http://127.0.0.1:8000/api/posts/{path}", "message": "", "posts_listing": "http://127.0.0.│[13/Feb/2017 09:59:42] "GET /api HTTP/1.1" 200 146
    1:8000/api/posts", "status": "success"}

### [http://127.0.0.1:8080/api/posts](http://127.0.0.1:8080/api/posts)

Gera uma lista com todos os posts. Retorna um código de resposta HTTP 200:

    ➤ curl -i http://127.0.0.1:8000/api/posts
    HTTP/1.0 200 OK
    Date: Mon, 13 Feb 2017 10:10:21 GMT
    Server: WSGIServer/0.2 CPython/3.5.2
    Content-Type: application/json
    X-Frame-Options: SAMEORIGIN
    
    {"message": "", "posts_count": 96, "status": "success", "posts": [{"link": "http://127.0.0.1:8000/post/voluptate-consequatur-quibusdam-voluptas-similique-pariatur-labore", "path": "voluptate-consequatur-quibusdam-voluptas-similique-pariatur-labore", "ref": "http://127.0.0.1:8000/api/posts/voluptate-consequatur-quibusdam-voluptas-similique-pariatur-labore", "title": "Voluptate consequatur quibusdam voluptas similique pariatur labore.", "author": "arag\u00e3oalexandre", "publication_date": "2017-02-11T17:17:09.150Z", "subject": "Soluta illum blanditiis saepe hic dolorem nesciunt eaque suscipit adipisci commodi quaerat reiciendis illum."}, {"link": "http://127.0.0.1:8000/post/non-natus-est-nam-culpa-nemo-consequatur", "path": "non-natus-est-nam-culpa-nemo-consequatur", "ref": "http://127.0.0.1:8000/api/posts/non-natus-est-nam-culpa-nemo-consequatur", "title": "Non natus est nam culpa nemo consequatur.", "author": "silveiradaniela", "publication_date": "2017-02-11T17:07:09.600Z", "subject": "Odio eveniet repellat minima quae quia quos incidunt officia facilis fugit expedita cum similique incidunt sit architecto esse perferendis nihil animi quia voluptate laboriosam."}, 
    ... suppressed output ...

A estrutura desse retorno é similar a:

{
    "status": "success|fail"
    "message": "empty in success or a error message",
    "posts_count": "número total de posts retornados",
    "posts": {
        "title": "título do post",
        "subject": "pequena explicação sobre o conteúdo do post",
        "author": "username de quem publicou",
        "path": "prefixo da URL que identifica unicamente o post corrente",
        "publication_date": "data da publicação",
        "link": "endereço WEB",
        "ref": "endereço para buscar o post corrente pela API",
    }
}

### [http://127.0.0.1:8080/api/posts/{path}](http://127.0.0.1:8080/api/posts/{path})

Devolve um post em específico, dado o seu `path` (veja mais abaixo uma explicação sobre o modelo de dados usado). Tem o retorno HTTP 200, caso encontre o `path` solicitado:

    ➤ curl -i http://127.0.0.1:8000/api/posts/voluptate-consequatur-quibusdam-voluptas-similique-pariatur-labore
    HTTP/1.0 200 OK
    Date: Mon, 13 Feb 2017 10:13:18 GMT
    Server: WSGIServer/0.2 CPython/3.5.2
    Content-Type: application/json
    X-Frame-Options: SAMEORIGIN
    
    {"message": "", "status": "success", "post": {"link": "http://127.0.0.1:8000/post/voluptate-consequatur-quibusdam-voluptas-similique-pariatur-labore", "path": "voluptate-consequatur-quibusdam-voluptas-similique-pariatur-labore", "ref": "http://127.0.0.1:8000/api/posts/voluptate-consequatur-quibusdam-voluptas-similique-pariatur-labore", "title": "Voluptate consequatur quibusdam voluptas similique pariatur labore.", "author": "arag\u00e3oalexandre", "publication_date": "2017-02-11T17:17:09.150Z", "content": "Ipsa iure recusandae inventore odio. Ipsa ullam nulla rem molestias eligendi. Enim earum odit ex fugiat maiores alias id magni. Occaecati laudantium ad consequuntur odit repellendus quasi.\nDistinctio dolorem reprehenderit excepturi non delectus. Exercitationem sit aliquam tenetur eligendi expedita recusandae. Accusantium labore exercitationem nulla architecto. Odit qui vitae molestiae. Nulla nisi dolore recusandae tenetur mollitia inventore debitis quo.\nEligendi quod eligendi hic nesciunt nesciunt explicabo dolor. Voluptas voluptatem odit alias earum laboriosam aut itaque ipsa. Occaecati rem commodi dolorum voluptatem fugit ab consequatur. Accusantium provident ex magni.\nDolor odio voluptatem corporis praesentium dignissimos similique neque ratione. Numquam voluptatibus voluptates dolore fugiat quaerat dolores reprehenderit. Nesciunt provident rerum iste dolorem. Quidem totam magni dolor harum nulla. Fugit et occaecati quis nulla laboriosam molestiae ullam.\nDelectus ipsam voluptatum consequatur tempore ipsa deserunt. Beatae error placeat dolorem exercitationem. Earum sit ratione architecto nostrum incidunt a. Eos hic delectus odio minima.", "subject": "Soluta illum blanditiis saepe hic dolorem nesciunt eaque suscipit adipisci commodi quaerat reiciendis illum."}}

Caso seja requisitado um post com `path` inexistente uma saída similar a essa é gerada (com retorno HTTP 404):

    ➤ curl -i http://127.0.0.1:8000/api/posts/inexistent                                                        
    HTTP/1.0 404 Not Found
    Date: Mon, 13 Feb 2017 10:14:24 GMT
    Server: WSGIServer/0.2 CPython/3.5.2
    Content-Type: application/json
    X-Frame-Options: SAMEORIGIN
    
    {"message": "The required post path not exist.", "status": "fail"}
    
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