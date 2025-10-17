# Integrantes
1. Ricardo Flores ve
2. Andrés Guzmán
3. 
# Tema

# Problema
La tienda necesita un anlisis sobre los clientes y las ventas de los productos, la tienda quiere diseñar una estartegia para incrementar sus ventas y fidelizar sus clientes. 
# Solución
1. Normalizar la bases de datos.
2. Definir criterios de segmentación de clientes. (High client, low client, smart client)
3. Variables a emplear (frecuencia de compra, importe, productos comprados, edad)
# Dataset
*Productos*
- Atributo | Tipo de dato | Escala de medición
- id_producto | Int | 
- nombre_producto | strings | 
- categoria | strings |
- precio_unitario | float |

*Clientes*
- Atributo | Tipo de dato | Escala de medición
- id_cliente | int |
- nombre_cliente | strings
- email | strings |
- ciudad | strings |
- fecha_alta | date |

 *Ventas*
 - Atributo | Tipo de dato | Escala de medición
 - id_venta | int |
 - fecha	| date | 
 - id_cliente	| int |
 - nombre_cliente	| strings |
 - apellido_cliente	| strings |
 - email | strings | 
 - medio_pago | strings

 *Detalle_ventas*
 - id_venta | int
 - id_producto | int
 - nombre_producto | string
 - cantidad | int |
 - precio_unitario |	float
 - importe | float |
 
# Pseudocodigo
# Diagrama del programa
