## Dia 17 - 10/08/2022[  🔙](../../README.md)

- Instalação do Django, programação web

```shell

python -m pip install Django
# versão
python3 -m django --version

# criando o projeto
django-admin startproject desafio21diaspython

# rodar o server
python3 manage.py runserver

# criação de tabelas
python3 manage.py migrate

# criar o super usuário
python3 manage.py createsuperuser

# criar estrutura da aplicação web
# adiciona web no arquivo 'settings.py' em INSTALLED_APPS
python3 manage.py startapp web



# criando uma tela, "Alô Brasil"
# sempre terá início no arquivo views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá Brasil.") 

# criação de rota/caminhos
# 1 - crie um arquivo urls.py dentro do projeto web,
#      -path é o caminho e arquivo de visualização
from . import views

urlpatterns = [
    path('', views.index),
# 2 - incluir esse arquivo ao arquivo urls.py na raiz da aplicação 


```

```shell

# Para configurar o banco de dados, abre o arquivo settings.py(dentro do projeto). O Sqlite vem por padrão, caso queira mudar para o postgresql, você pode usar este código como base. Apesar que ele está configurado com variáveis de ambientes, você pode substitiur por nomes!

# import os
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DATABASE"),
        'USER': os.getenv("DATABASE_USER"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
        'HOST': os.getenv("DATABASE_IP"),
        'PORT': '5432',
    }
}
```

### Fonte de estudos

- Documentação oficial. Disponível em: [https://www.djangoproject.com/community/](https://www.djangoproject.com/community/). Acesso em: 10-08-2022