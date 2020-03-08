# Agilent-33220a-Remote-Control
Python Script que permite controlar el generador de señales AGILENT 33220a desde una computadora, utilizando el módulo pyvisa.

## Instalación
Se utilizó [Python 3](https://www.python.org/) con los módulos pyvisa, numpy y matplotlib. Para instalar los módulos se utilizó el administrador de paquetes [pip](https://pypi.org/project/pip/).
### En Windows
```sh
> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
> python get-pip.py
```
### En Ubuntu
```sh
$ sudo apt install python3-venv python3-pip
```
Para descargar los módulos:
```sh
$ pip3 install numpy matplotlib pyvisa
```
## Contenidos
* [agilent33220a.py](https://github.com/Quik-e/Agilent-33220a-Remote-Control/blob/master/agilent33220a.py) contiene la clase del instrumento, donde se pueden encontrar sus funciones y sus características.
* [agilent33220a_test.py](https://github.com/Quik-e/Agilent-33220a-Remote-Control/blob/master/agilent33220a_test.py) es un script en el que se puede mostrar el procedimiento para utilizar el instrumento.
* [arbitraryfunctions.py](https://github.com/Quik-e/Agilent-33220a-Remote-Control/blob/master/arbitraryfunctions.py) contiene dos funciones arbitrarias que creé como muestra.
* [33220_user_guide.pdf](https://github.com/Quik-e/Agilent-33220a-Remote-Control/blob/master/33220_user_guide.pdf) manual de usuario en el que me basé para realizar las funciones, puede ser útil si alguien desea relizar sus propias funciones y mejorar el código.
