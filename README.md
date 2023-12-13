# Academia

Clone o repositório em seu computador
```
git clone https://github.com/MatheusTG/Academia.git
```

Crie e ative seu ambiente virtual
```
python -m venv venv
venv/Scripts/activate
```

Instale as bibliotecas de requirements.txt
```
pip install -r requirements.txt
```

Em infra/configs/connection.py configure a conexão em self.__connection_string
```
self.__connection_string = 'postgresql://postgres:postgres123@localhost:5432/academia'
```

Por fim execute o arquivo run.py
```
python run.py
```
