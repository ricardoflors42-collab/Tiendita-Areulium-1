# Integrantes
1. Ricardo Flores ven
2. Andrés Guzmán col
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
Atributo | Tipo de dato | Escala de medición | Identificadores
-|-|-|-
id_producto | Int | intervalo | PK
nombre_producto | strings | nominal | 
categoria | strings | nominal |
precio_unitario | float | razón |

*Clientes*
Atributo | Tipo de dato | Escala de medición | Identificadores
-|-|-|-
id_cliente | int | intervalo | PK
nombre_cliente | strings | nominal | 
email | strings | nominal | 
ciudad | strings | nominal |
fecha_alta | date | intervalo |

 *Ventas*
Atributo | Tipo de dato | Escala de medición | Identificadores
-|-|-|-
 id_venta | int | intervalo | FK
 fecha	| date | intervalo |
 id_cliente	| int | intervalo | FK 
 nombre_cliente	| strings | nominal | 
 apellido_cliente	| strings | nominal | 
 email | strings | nominal |
 medio_pago | strings | nominal |

 *Detalle_ventas*
Atributo | Tipo de dato | Escala de medición | Identificadores
-|-|-|-
id_venta | int | intervalo | PK
id_producto | int | intervalo | FK
nombre_producto | string | nominal |
cantidad | int | razón |
precio_unitario |	float | razón |
importe | float | razón | 
 
# Pseudocodigo
# Diagrama del programa
