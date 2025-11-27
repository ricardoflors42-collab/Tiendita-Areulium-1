import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


pd.set_option('display.max_columns', None)
sns.set_theme(style="darkgrid")

ruta = './Data/'
clientes = pd.read_excel(f'{ruta}Clientes.xlsx')
Detalle_ventas = pd.read_excel(f'{ruta}Detalle_ventas.xlsx')
Productos = pd.read_excel(f'{ruta}Productos.xlsx')
Ventas = pd.read_excel(f'{ruta}Ventas.xlsx')

Ventas_categorias = (Detalle_ventas.merge(
Productos, on='id_producto'
))

Cantidad = Ventas[['id_cliente', 'nombre_cliente']].groupby(by = 'id_cliente').count()
Cantidad = Cantidad.rename(columns={'nombre_cliente':'Numero_compras'})

Tabla_correlacion = (Ventas.merge(Detalle_ventas, how = 'inner', on = 'id_venta')
                     .merge(Productos, how = 'inner', on = 'id_producto')
                     .merge(clientes, how = 'inner', on = 'id_cliente')
                     .merge(Cantidad, on = 'id_cliente'))
Tabla_correlacion = Tabla_correlacion[['medio_pago', 'cantidad', 'importe', 'precio_unitario_x', 'categoria', 'ciudad', 'Numero_compras']]
diccionario = dict(enumerate(Tabla_correlacion.medio_pago.unique()))
Tabla_correlacion['medio_pago'] = Tabla_correlacion['medio_pago'].replace({valor: clave for clave, valor in diccionario.items()})
diccionario = dict(enumerate(Tabla_correlacion.categoria.unique()))
Tabla_correlacion['categoria'] = Tabla_correlacion['categoria'].replace({valor: clave for clave, valor in diccionario.items()})
diccionario = dict(enumerate(Tabla_correlacion.ciudad.unique()))
Tabla_correlacion['ciudad'] = Tabla_correlacion['ciudad'].replace({valor: clave for clave, valor in diccionario.items()})


def VerTabla(n = 2):
    tablas = {'ventas':Ventas,
              'clientes':clientes,
              'Detalle':Detalle_ventas,
              'Productos':Productos}
    for nombre,tabla in tablas.items():
        print("-"*80)
        print(f"Tabla de {nombre}")
        print("-"*80)
        print(tabla.head(n))

def EstadisticasDescriptivas():
    print("-"*80)
    print(f"Estadisticas descriptivas Cantidaad, precio e importe")
    print("-"*80)
    print(Detalle_ventas[['cantidad', 'precio_unitario', 'importe']].describe())
    print("-"*80)
    print(f"Estadisticas descriptivas cantidad de veces que compra el cliente")
    print("-"*80)
    print(Cantidad.describe())

def PrincipalesGraficas():

    #Grafico de detalle por categoria
    fig, ax = plt.subplots(1,2, figsize = (14,6))
    sns.histplot(data = Ventas_categorias['categoria'], ax = ax[0])
    ax[0].set_title('# Productos comprados por categoria')

    sns.histplot(data=Ventas_categorias,x='categoria',weights='importe',ax = ax[1])
    ax[1].set_title('Importe por categoria')
    plt.savefig('Detalle_por_categoria.png')

    #Grafico de distribucion importe
    sns.displot(Detalle_ventas['importe'], kde = True)
    plt.title('Distribución de importe')
    plt.savefig('Distribuccion_importe.png')

    #Grafico de cantidad de veces que compra el cliente
    sns.displot(data = Cantidad['Numero_compras'], kde = True,discrete = True)
    plt.title('Cantidad de veces que compra el cliente')
    plt.savefig('N_Veces_compra_cliente.png')

def GraficoCorrelacion():
    plt.figure(figsize=(7,7))
    sns.heatmap(Tabla_correlacion.corr(), annot=True, cbar = False)
    plt.savefig('Correlaacion.png')