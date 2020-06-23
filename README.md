# INTERPOLACIÓN DE FUNCIONES POR MEDIO DE POLINOMIOS DE LAGRANGE
Este repositorio contiene un programa para hallar, matemáticamente, un punto f(x) de una función a partir de parejas de datos conocidos, es decir, (x, f(x)), esto por medio del método de interpolación por Polinomios de Lagrange, además, el programa permite mostrar algunos otros detalles matemáticos, como el polinomio de aproximación y la gráfica de este.

# Pre-requisitos
Para poder ejecutar la aplicación, se necesita que el equipo tenga instalados los siguientes programas:
•	Algún editor de texto para lenguaje Python (Spyder, VS Code, etc)
•	Digia Qt SDK o en efecto PyQt.

# Instalación y Ejecución
1.	Descargar los archivos contenidos en la carpeta “IP-Lagrange” o hacer una copia de esta, por medio de Git, a la base de datos del equipo.
2.	Abrir el archivo .py con el editor de texto.
3.	Dar clic en la pestaña de opciones “Debug” y escoger la opción “Run without debugging”

# Modo de Uso
1.	Ingresar una pareja de datos conocida (x, f(x)) en las casillas “Datos en X” y “Datos en Y”, respectivamente.
2.	Dar clic en el botón “Siguiente Valor”. Se eliminarán de las casillas los datos ingresados.
3.	Se procede a realizar nuevamente el paso 1 y 2 hasta que se hayan ingresado todas las parejas de datos conocidas (las casillas en donde se escribieron tales datos deben quedar en blanco).
4.	Ingresar el dato x, correspondiente al f(x) a desconocido, en la casilla de “Punto a evaluar”.
5.	Activar las casillas referentes a:
•	“Gráfica” si se quiere que se muestre la gráfica del polinomio de aproximación.
•	“Polinomio expandido” si se quiere que se muestre el polinomio no simplificado.
•	“Lista de datos” si se quiere que se muestre la lista de datos completa y ordenada.
6.	Dar clic en el botón “Calcular”.
7.	Enseguida, en la casilla “Polinomio” se muestra el polinomio de aproximación simplificado; en la casilla “Evaluación” se muestra el valor de f(x) que se deseaba hallar.
8.	En caso que se quiera encontrar un nuevo valor se deben realizar nuevamente todos los pasos dados.

# Construido con
•	VS Code – Editor de Texto
•	Qt Designer – Diseño de Aplicación

# Autores
•	Juan Torres - JuanTorres1911
•	Andrés Alvarez - Andrs18
