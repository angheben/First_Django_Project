"""
Para criar um projeto django eu digito o código abaixo no meu terminal:

'django-admin startproject "nome_do_projeto" .'
O . no final é para indicar que o projeto será criado na própria pasta e não em um subdiretório (outra pasta), logo,
recomenda-se criar dessa forma.

Executado esse código será criado um arquivo 'manage.py' na pasta do meu arquivo e uma pasta com o nome que eu dei pro
arquivo

O arquivo manage (gerenciamento) será o arquivo que utilizaremos para executar comandos

Há várias ferramentas de administração, autenticação, segurança entre outras que são todas carregadas nesses arquivos
criados

ROOT_URLCONF = 'django1.url' -> Esse comando diz respeito a rota do meu arquivo
WSGI_APPLICATION = 'django1.wsgi.application' ->


Aula 20)

Para iniciar uma aplicação django, na mesma pasta onde eu criei o projeto django, no terminal eu digito o código
'django-admin startapp "nome_da_aplicação"'

Feito isso será criado um arquivo como nome da aplicação que você deu e dentro dele terá outra pasta chamada migrations
Essa pasta migrations é responsável por realizar migrações dos bancos de dados, ou seja, cada vez que eu altero o meu
banco de dados outra pasta migrations é criada, deixando assim um histórico.

Feito isso no arquivo 'settings' do projeto django eu procuro por INSTALLED_APPS e adiciono na lista o nome da minha
aplicação

Feito isso, em TEMPLATES, na lista de DIR (diretórios) eu adiciono templates

Aula 21)

Qual é a diferença entre uma aplicação Django e um projeto Django?

Quando trabalhamos com o Django Framework devemos levar em conta a forma de trabalho do mesmo que possui um projeto que
engloba o todo e aplicações plugáveis.

Ou seja, em um projeto Django, podemos ter várias aplicações, cada uma com a sua tarefa específica, e estas aplicações
depois de criadas podem ser utilizadas por outros projetos.

Aula 22)

Quando eu adiciono 'templates' na lista DIR da lista TEMPLATES do arquivo settings eu estou indicando que eu terei um
diretório com esse nome que servirá como template, no caso uma página HTML.
"""

