## 2017.2 - meRepresenta - Rest API


<p align="justify">&emsp;&emsp;A API do software possui um repositório destinado a ela. Este pode ser acessado no endereço a seguir:
[meRepresenta](https://github.com/fga-gpp-mds/2017.2-DepuTinder)</p>

### Instalação

<p align="justify">&emsp;&emsp;Para instalar todas as dependências necessárias do projeto, rode o seguinte comando:</p>

```
pip install -r requirements.txt
```

<p align="justify">&emsp;&emsp;Para que seja possível a utilização da API, é preciso executar o makemigrations. Este comando é necessário para criação de novas migrações relacionadas às models:</p>

```
python3 manage.py makemigrations
```

<p align="justify">&emsp;&emsp;Para que essas migrações possam ser manipuladas, tanto na aplicação de novas quando no exclusão das existentes, é necessário executar o comando:</p>

```
python3 manage.py migrate
```

<p align="justify">&emsp;&emsp;Para executar a API é fundamental o seguinte comando: </p>

```
python3 manage.py runserver
```

<p align="justify">&emsp;&emsp;Para acessar o servidor gerado no comando anterior, basta acessar [localhost:8000](http://localhost:8000/)</p>
