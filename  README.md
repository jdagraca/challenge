<h1> Challenge </h1>

### Requisitos:
- Python 3.8+
- Docker Compose 

### Instalar Dependenicas 

```
pip install -r requeriments.txt
```

### Instanciar MongoDB con Docker Compose

```
docker-compose up -d
```

### Poblar DB con datos de Prueba

```
python poblar_db.py

```

### Ejecutar Proceco de Pagos

```
python main.py
```
### Test

```
python -m unittest discover -s test/
```





