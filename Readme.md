# Introducción

Este proyecto corresponde al módulo de Recuento de votos de Agora@US 2017/18 del grupo 1.

# Miembros del equipo

-Pablo Roldán Sánchez ([@Roldans](https://github.com/Roldans))  

-Ernesto de Tovar Vázquez ([@ernestodtv](https://github.com/ernestodtv))  

-Arturo Ronda Lucena([@ernestodtv](https://github.com/ernestodtv))  

-Álvaro Acha Burgos([@Alvachbur](https://github.com/Alvachbur))  

-Francisco Javier Huertas Vera([@jimdrix93](https://github.com/jimdrix93))  

-Javier Rodríguez Martín([@Javrd](https://github.com/Javrd))  

# Organización del repositorio

Existen dos ramas principales, "develop" y "master". Sobre la rama *develop* se realizarán todos los cambios en el proyecto durante el desarrollo de la aplicación,
 La rama *master* contendrá sólo versiones que se consideren estables, y por lo tanto es la que debería ser usada por el equipo de integración para realizar la integración de el recuento de votos.


# Instalación y uso
Para instalar y usar este servicio hay que usar uno de los tres métodos descritos a continuación, exclutenyes entre sí. El único método que proporciona acceso a la base de datos que proporcionó integración es el de docker-compose.

## Docker-compose
```
docker-compose up
```
O si se prefiere dejar en segundo plano:
```
docker-compose up -d
```
Se puede acceder desde http://localhost:52007/recvotes/{pollID}.

## Docker
Para poder usarlo habría que ejecutar a parte la base de datos de integración.
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
Una vez configurada la base de datos externa, se podría acceder desde http://localhost:52007/recvotes/{pollID}.

## Bare Metal
Para poder usarlo habría que ejecutar a parte la base de datos de integración.
### Instalación de python 3
```
sudo apt-get install python3
```
Introducir contraseña de sudo
### Comprobar instalación correcta de Python3->
Escribir en la terminal:
```
python
```
Se abrira la consola de python
Para salir de la misma esbribir 
```
exit()
```

### Instalación de pip
```
python get-pip.py
```
En caso de resultar en un error:
Este error que nos puede aparecer tiene como causa una incorrecta adicion de paquetes de python luego
```
sudo apt-get install python-pip
```
Si este error persiste: 
```
python get-pip.py --user
python get-pip.py --no-index --find-links=/local/copies
```
Como opcion adicional upgradear el "existente":  
```
pip install -U pip
```
### Instalar dependencias
```
pip install --no-cache-dir -r requirements.txt
```

### Iniciar servidor

```
python manage.py runserver
```

Una vez configurada la base de datos externa, se podría acceder desde http://localhost:8000/recvotes/{pollID}.