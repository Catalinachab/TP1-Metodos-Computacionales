# Proyecto de Implementación del Algoritmo PageRank

## Introducción

En este proyecto, nos embarcamos en la implementación del famoso algoritmo PageRank, utilizado por Google para ordenar páginas web según su importancia o relevancia en los resultados de búsqueda. A través de métodos computacionales, exploramos cómo este algoritmo puede aplicarse no solo a la web, sino también a otros dominios, como la evaluación del impacto de trabajos científicos.

## Descripción del Algoritmo PageRank

PageRank, desarrollado por Sergey Brin y Lawrence Page en 1998, no se limitó a contar simplemente la cantidad de enlaces que apuntan a una página web, sino que consideró la calidad de esos enlaces. En esencia, PageRank se basó en el siguiente mecanismo:

1. Un estudiante lee trabajos científicos o páginas web.
2. Decide aleatoriamente si sigue leyendo alguno de los trabajos citados o continúa con otro trabajo disponible.
3. La probabilidad de seguir un enlace citado se determinó por un parámetro \( d \) (generalmente establecido en 0.85 en la práctica).
4. Con el tiempo, los trabajos más citados y citantes se consideraron más relevantes e importantes.

## Implementación del Proyecto

El algoritmo PageRank se basa en cálculos matriciales complejos que involucran la multiplicación de matrices. En particular, en nuestro proyecto, nos enfocamos en el uso de matrices ralas (matrices dispersas) para representar las conexiones entre trabajos científicos. Las matrices ralas son especialmente útiles en este contexto debido a que las referencias entre trabajos científicos pueden generar matrices con muchos ceros debido a la baja conectividad entre los elementos. Utilizar matrices ralas nos permitió optimizar el uso de memoria y mejorar el rendimiento de los cálculos de PageRank.

1. **Clase MatrizRala en Python**: Implementamos una clase que maneja matrices ralas, es decir, matrices donde la mayoría de los elementos son cero. Esta clase ofrece métodos para indexación, suma, resta, multiplicación por un escalar y producto matricial.

2. **Método de Gauss-Jordan para Matrices Ralas**: Implementamos este método para resolver sistemas de ecuaciones lineales en matrices ralas, lo cual fue esencial para el cálculo de PageRank.

3. **Aplicación del Algoritmo PageRank**: Utilizamos nuestro código para calcular el PageRank en diferentes contextos. Por ejemplo, evaluamos la relevancia e impacto de trabajos científicos basándonos en citas entre ellos.


## Objetivos y Resultados Esperados

Este proyecto nos ayudó a entender el algoritmo PageRank en profundidad y a aplicar conceptos de estructuras de datos como matrices ralas y métodos numéricos como Gauss-Jordan. Al final del proyecto, obtuvimos una herramienta poderosa para evaluar la relevancia y el impacto en diferentes dominios, lo cual es valioso no solo en la web, sino también en campos como la ciencia y la investigación académica.

---




