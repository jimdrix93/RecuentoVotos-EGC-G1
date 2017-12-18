# Introducción

Este proyecto corresponde al módulo de Recuento de votos de Agora@US 2017/18 del grupo 1.

# Miembros del equipo

-Pablo Roldán Sánchez ([@Roldans](https://github.com/Roldans))
-Ernesto de Tovar Vázquez ([@ernestodtv](https://github.com/ernestodtv))
-Arturo Ronda Lucena([@ernestodtv](https://github.com/ernestodtv))
-Álvaro Acha Burgos([@Alvachbur](https://github.com/Alvachbur))
-Francisco Javier Huertas Vera([@Javrd](https://github.com/Javrd))
-Javier Rodriguez Martin([@jimdrix93](https://github.com/jimdrix93))

# Organización del repositorio


# Estructura de la aplicación

#Instalacion
#Instalacion de python 3
```
sudo apt-get install python3
```
Introducir contraseña de sudo
Comprobar instalacion correcta de Python3->
Escribir en la terminal:
```
python
```
Se abrira la consola de python
####Para salir de la misma esbribir 
```
exit()
```

#Instalacion de pip
```
python get-pip.py
```
##En caso de resultar en un error:
Este error que nos puede aparecer tiene como causa una incorrecta adicion de paquetes de python luego
```
sudo apt-get install python-pip
```
##Si este error persiste: 
```
python get-pip.py --user
python get-pip.py --no-index --find-links=/local/copies
```
##Como opcion adicional upgradear el "existente":  
```
pip install -U pip
```

#Instalacion de django
Posicionarte en tu terminal en el directorio definido en el cual vas a trabajar
Instalar django, desde la terminal ejecutar->
```
pip install django==1.11.7
```

##Meter Django en el path
```
 PYTHONPATH=/path/to/django/parent/dir python
  »> import django
```
##Instalar conector mysql, desde la terminal
```
pip install PyMySQL
``` 
([https://pypi.python.org/pypi/PyMySQL])


# Funcionamiento
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