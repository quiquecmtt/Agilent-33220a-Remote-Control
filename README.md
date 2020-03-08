# Agilent-33220a-Remote-Control
Python Script que permite controlar el generador de señales AGILENT 33220a desde una computadora, utilizando el módulo pyvisa.

## Descarga
```sh
$ git clone https://github.com/Quik-e/Agilent-33220a-Remote-Control.git
```

## Instalación necesaria
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
## Como llamar a las funciones
```python
instrument = agi.connect_device()
```
Conecta la computadora con el dispositivo, en necesario para comenzar la comunicación entre ambos

```python
instrument.load_signal(funcion)
```
Carga la función (vector unidimensional) en el instrumento y lo guarda en la memoria volátil. Esto hace que se borre la función si se apaga el instrumento o si se vuelve a llamar a la función de esta manera.

```python
instrument.load_signal(funcion,"nombre_guardado")
```
Carga la función (vector unidimensional) en el instrumento en la memoria con el nombre nombre_guardado, permitiendo apagar el instrumento y que la función pueda ser utilizada cuando vuelva a prenderse.

```python
instrument.output_signal("VOLATILE",1,1000,0.5)
```
Selecciona la señal guardada en la memoria volátil a ser transmitida por el generador de señales, con una amplitud de 1v, frecuencia de 1kHz y un offset de 0.5v.

```python
instrument.output_af("nombre_guardado",1,1000,0.5)
```
Selecciona la señal a ser transmitida por el generador de señales, con una amplitud de 1v, frecuencia de 1kHz y un offset de 0.5v. Si la señal no se encuentra en la memoria (no se encuentra coincidencia con nombre_guardado), se mostrará el catálogo con los nombre de las señales disponibles.

```python
instrument.af_attributes("nombre_funcion")
```
Muestra atributos de la función nombre_funcion.

```python
instrument.erase_af("nombre_funcion")
```
Elimina de la memoria la función que tenga el nombre nombre_funcion.

```python
instrument.catalog()
```
Muestra las funciones arbitrarias disponibles en la memoria del generador de señales.

```python
instrument.display_text("Hola mundo")
```
Muestra Hola mundo en la pantalla del generador de señales.

```python
instrument.display_text("Hola mundo",3)
```
Muestra Hola mundo en la pantalla del generador de señales por tres segundos y después lo borra.

```python
instrument.output_on()
```
Enciende el output del instrumento.

```python
instrument.output_off()
```
Apaga el output del instrumento.


