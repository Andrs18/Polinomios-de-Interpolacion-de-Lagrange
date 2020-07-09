# POLINOMIOS DE INTERPOLACIÓN DE LAGRANGE
Muchas veces, tanto en las matemáticas como en algunas ramas de las ciencias, se necesitan realizar aproximaciones de datos en alguna investigación en particular, por lo tanto, existen diferentes métodos y herramientas de interpolación que permiten encontrar un valor f(x) correspondiente a un x particular con tan solo conocer algunas parejas de datos, asimismo, para dichos procesos es necesario encontrar previamente una función que aproxime los datos conocidos.
Consulte el siguiente link para saber más sobre métodos de interpolación de datos: https://www.uv.es/~diaz/mn/node37.html
En este caso, el proyecto se enfoca en desarrollar el método denominado “Polinomios de Interpolación de Lagrange”. Se desarrolla la aplicación de tal manera que, además de hallar el valor f(x) que se quiere, proporciona también la lista de datos final y la función polinómica con su correspondiente gráfica.


## Instalación

### Prerrequisitos
Librerías necesarias:
• sympy
• numpy
• matplotlib
• PyQt5
• sys

### Procedimiento
Para una exitosa instalación se deben seguir los siguietes pasos:
1. Descargar el repositorio por medio de "Code" y luego en la opción "Download ZIP", esto desde https://github.com/Andrs18/Polinomios-de-Interpolacion-de-Lagrange
2. Diríjase a la carpeta donde descargó dicho archivo y extraiga la carpeta "Archivos_Finales".
3. Ejecute el archivo "Proyecto.py".


## Modo de Uso
El programa presenta dos maneras iniciales para su ejecución:
#### •	“Manual”:
1.	Ingresar una pareja de datos conocida (x, f(x)) en las casillas “Datos en X” y “Datos en Y”, respectivamente.
2.	Dar clic en el botón “Siguiente Valor” (se eliminarán visualmente los datos ingresados).
3.	Se procede a realizar nuevamente el paso 1 y 2 hasta que se hayan ingresado todas las parejas de datos conocidas (las casillas en donde se escribieron tales datos deben quedar en blanco).
Saltar al paso 4.

![3](https://user-images.githubusercontent.com/66414813/87029058-36b7c800-c1a5-11ea-9b23-4770cc3a528f.gif)

#### •	“Directa”:
Nota: Se debe tener un archivo .xlsx con los datos en ordenados en columnas. Por ejemplo:

![Captura](https://user-images.githubusercontent.com/66414813/87030587-71226480-c1a7-11ea-9e71-e9466a5eb326.JPG)

1.	Dar clic en el botón “Importar Archivo”.
2.	Buscar y seleccionar el archivo .xlsx
3.	Seleccionar la hoja para trabajar y las columnas “x” y “y” conocidas.
Saltar al paso 4.

![4](https://user-images.githubusercontent.com/66414813/87029231-71216500-c1a5-11ea-9f3c-828b8434dc0d.gif)

4.	Ingresar el dato x, correspondiente al f(x) a desconocido, en la casilla de “Punto a evaluar”.
5.	Dar clic en el botón “Calcular”.
Enseguida, en la casilla “Polinomio” se muestra el polinomio de aproximación simplificado; en la casilla “Evaluación” se muestra el valor de f(x) que se deseaba hallar.
6.	(Opcional) Activar las casillas referentes a:
•	“Gráfica” si se quiere que se muestre la gráfica del polinomio de aproximación.
•	“Polinomio expandido” si se quiere que se muestre el polinomio no simplificado.
•	“Lista de datos” si se quiere que se muestre la lista de datos completa y ordenada.
7.	En caso que se quiera encontrar un nuevo valor: dar clic en el botón “Limpiar” y realizar todos los pasos enunciados nuevamente.
![5](https://user-images.githubusercontent.com/66414813/87029263-80a0ae00-c1a5-11ea-9819-fd5ab96ff131.gif)


## Contribución
Para alguna posible recomendación o mejora al programa, favor poner en contacto con los creadores por medio de Github.

## Construido con
•	Python

## Autores
•	Juan Torres - JuanTorres1911
•	Andrés Alvarez - Andrs18

## Agradecimientos
• Profesor Ricardo Amezquita Orozco
• Compañeros del curso de "Programación e Introducción a Métodos Numéricos"
• Universidad Nacional de Colombia
• Comunidad Python
