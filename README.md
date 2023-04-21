## Hot to fill requirements.txt
```shell
pip3 freeze > requirements.txt
```

## Run app
```shell
uvicorn main:app --reload
```

### Para errores de certificado SSL usar esta libreria
```shell
pip install python-certifi-win32
```
