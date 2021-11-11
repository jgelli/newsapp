## Para executar o projeto:
1. Criar virtualenv:
```
$ python3 -m venv env
```
ou
```
$ virtualenv --python=python3 env
```

2. "Entrar" na nova env:
```
$ source env/bin/activate
```
ou
```
$ . env/bin/activate
```

3. Instalar dependências:
```
(env) $ pip install -r requirements.txt
```

4. Rodar servidor:

é necessário entrar na paste "newsapp"
```
(env) $ cd newsapp/
```

depois rodar o servidor
```
(env) $ python manage.py runserver 0.0.0.0:8000
```

## Acessando o site:

Basta ir no navegador e digitar: localhost:8000