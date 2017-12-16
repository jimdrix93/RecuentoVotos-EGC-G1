# Recuento de votos

Para ejecutar el servidor puede optar por una de estas tres alternativas:

## Bare Metal
Se necesita tener instalado Python 2.7 y pip
### Instalar dependencias
```
pip install --no-cache-dir -r requirements.txt
```

### Iniciar servidor

```
python manage.py runserver
```

Se puede acceder desde http://localhost:8000/recuento/.

## Docker

### Construir imagen
```
docker build -t recuentovotos-egc-g1
```
### Iniciar servidor
```
docker run -p 52007:8000 recuentovotos-egc-g1
```
O si se prefiere dejar en segundo plano:
```
docker run -p 52007:8000 -d recuentovotos-egc-g1
```
Se puede acceder desde http://localhost:52007/recuento/.

## Docker-compose
```
docker-compose up
```
O si se prefiere dejar en segundo plano:
```
docker-compose up -d
```
Se puede acceder desde http://localhost:52007/recuento/.