# Instalar esta Libreria: pip install streamlit
# Crear el Archivo del Dashboard = Dashboard.py

'''
Crea un entorno virtual: python -m venv mi_entorno
Activa el entorno virtual: mi_entorno\Scripts\activate
Instala seaborn en el entorno virtual:  pip install seaborn
Instalar streamlit: pip install streamlit
Instalar pandas: pip install pandas
Instalar matplotlib: pip install matplotlib
o todo en un solo paso: pip install streamlit pandas matplotlib seaborn

'''

# Instalar librerías necesarias: 
# pip install streamlit seaborn pandas matplotlib openpyxl

# Instalar las librerías necesarias:
# pip install streamlit seaborn pandas matplotlib openpyxl

# Instalar las librerías necesarias

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Librias para El Mapa:

import folium
from streamlit_folium import st_folium

# para crar tablas
import plotly.express as px
import plotly.io as pio
import html
import numpy as np

import folium
from folium.plugins import MarkerCluster  # Importar MarkerCluster
import pandas as pd


# Configurar el diseño de la página para ser más amplio
st.set_page_config(layout="wide")

# Leer datos desde el archivo Excel
df = pd.read_excel('Vista_Detalles_Pedidos_V1.xlsx')


# Inyectar CSS para tarjetas con altura y ancho consistentes
st.markdown(
    """
    <style>
    
      
    .card_kpi {
        background: white;  /* Fondo blanco */
        border-radius: 15px;  /* Bordes redondeados */
        border: 2px solid limegreen;  /* Borde verde */
        box-shadow: 2px 2px 12px rgba(0, 255, 0, 0.2);  /* Sombra sutil */
        padding: 15px;  /* Espacio interno */
        text-align: center;  /* Texto centrado */
        margin: 5px;  /* Reducir el espacio entre tarjetas */
        font-weight: bold;  /* Texto en negrita */
        color: darkblue;  /* Color del texto */
        transition: all 0.3s ease;  /* Transición suave */
        animation: latido 1s infinite;  /* Animación de latido */
        padding-bottom: 15px;  /* Espacio interno solo para abajo */
        flex: 1;  /* Asegurar que todas las tarjetas crezcan por igual */
        height: 90px;  /* Altura fija para mantener consistencia */
    }

    .card_kpi p {
        margin: 0;  /* Eliminar margen para evitar desbordamiento */
        overflow: hidden;  /* Evitar desbordamiento del texto */
        text-overflow: ellipsis;  /* Usar puntos suspensivos si el texto es muy largo */
        white-space: normal;  /* Permitir que el texto se ajuste a múltiples líneas */
        font-size: 16px;  /* Tamaño del texto para párrafos */
    }

    .card-container {
        display: flex;  /* Usar flexbox para la disposición */
        flex-direction: row;  /* Alineación horizontal */
        justify-content: space-between;  /* Espacio uniforme entre tarjetas */
        align-items: stretch;  /* Asegurar misma altura entre tarjetas */
    }


    /* Cambios para pantallas más pequeñas */
    @media (max-width: 768px) {
        .card_kpi {
            font-size: 26px;  /* Tamaño del texto más pequeño */
            padding: 10px;  /* Menos espacio interno */
            height: 105px;  /* Altura fija para mantener consistencia */
        }

        .card_kpi-container {
            flex-direction: column;  /* Cambiar a disposición vertical */
        }
    }

        /* Estilo hover para tarjetas con menor expansión */
    .card_kpi:hover {
        background-color: darkslategray;  /* Fondo más oscuro al pasar el cursor */
        color: white !important;  /* Asegurar prioridad del color */
        transform: scale(1.01);  /* Reducir la expansión al pasar el cursor */
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);  /* Menor sombra */
    }

    /* Animación de latido más lenta */
    @keyframes latido {
        0%, 100% {
            transform: scale(1);  /* Escala normal */
        }
        50% {
            transform: scale(1.05);  /* Menor escala a mitad de la animación */
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)




# Título y subtítulo
st.markdown("<h1 style='text-align: center;'>📈 Conoce tu Negocio: Python y el Análisis de Datos en Retail 📈</h1>", unsafe_allow_html=True)


# Agregar un salto de línea para separar
st.write("")  # Esto crea un espacio adicional

# Agregar una línea horizontal para dividir secciones
st.markdown("<hr>", unsafe_allow_html=True)
###---------------------------------------------------------------------------###

st.markdown(
    """
    <h3 style='text-align: center; color: #4cd137;'>Creado por: Ing. Juancito Pena</h3>
    <p style='text-align: center; color: #3498db; font-size: 16px;'>
        Tecnologías utilizadas: 🐍 Python, 📊 Streamlit, 🖥️ HTML/CSS, 📜 JavaScript, 📁 Git/GitHub, 
        📊 Excel, 💾 SQL Server, 🛠️ Visual Studio Code
    </p>
    """,
    unsafe_allow_html=True
)

# Agregar una línea horizontal para dividir secciones
st.markdown("<hr>", unsafe_allow_html=True)
###---------------------------------------------------------------------------###

# Calcular las sumas totales para las tarjetas
suma_total_pedidos = df["Total de Pedidos"].sum()
suma_cantidad_vendida = df["cantidad_vendida"].sum()
suma_ingresos_totales = df["Ingreso Total"].sum()
suma_costo_total = df["Costo Total"].sum()
suma_margen = df["Margen"].sum()
suma_porcentaje_margen = df["% Margen"].mean()

# Crear tarjetas para mostrar las sumas totales
st.subheader("📉 Indicadores Clave 📉")

# Sección horizontal para las tarjetas
col1, col2, col3, col4, col5, col6 = st.columns(6)
# Tarjeta para la suma total de pedidos con emoji y formato de miles
with col1:
    st.markdown(
        f"<div class='card_kpi'>📦 Total Pedidos<br><strong>{suma_total_pedidos:,.0f}</strong></div>",
        unsafe_allow_html=True
    )

# Tarjeta para la suma total de cantidad vendida con emoji
with col2:
    st.markdown(
        f"<div class='card_kpi'>📊 Total Cantidad<br><strong>{suma_cantidad_vendida:,.0f}</strong></div>",
        unsafe_allow_html=True
    )

# Tarjeta para la suma de ingresos totales con símbolo de moneda y emoji
with col3:
    st.markdown(
        f"<div class='card_kpi'>💰 Ingresos Totales<br><strong>${suma_ingresos_totales:,.2f}</strong></div>",
        unsafe_allow_html=True
    )

# Tarjeta para el costo total con símbolo de moneda y emoji
with col4:
    st.markdown(
        f"<div class='card_kpi'>💸 Costo Total<br><strong>${suma_costo_total:,.2f}</strong></div>",
        unsafe_allow_html=True
    )

# Tarjeta para el margen con símbolo de moneda y emoji
with col5:
    st.markdown(
        f"<div class='card_kpi'>💹 Margen<br><strong>${suma_margen:,.2f}</strong></div>",
        unsafe_allow_html=True
    )

# Tarjeta para el porcentaje de margen con emoji y formato de porcentaje
with col6:
    st.markdown(
        f"<div class='card_kpi'>📈 % Margen<br><strong>{suma_porcentaje_margen:,.2f}%</strong></div>",
        unsafe_allow_html=True
    )

# Agregar un salto de línea para separar
st.write("")  # Esto crea un espacio adicional


# Agregar un expander para segmentadores:

# Función para obtener opciones de selección con "Todos"
def get_multiselect_options(column):
    return ["Todos"] + list(df[column].unique())

# Filtrar el DataFrame según los segmentadores
clientes = df['Cliente'].unique()
vendedores = df['Vendedor'].unique()
distribuidores = df['Distribuidor'].unique()
ciudades = df['Ciudad'].unique()
estados = df['estado'].unique()

# Sección para gráficos por Cliente y Vendedor
with st.expander("Filtro por Cliente y Vendedor"):
    clientes = st.multiselect("Seleccione Clientes", get_multiselect_options("Cliente"), default=["Todos"], key="filtro_cliente")
    vendedores = st.multiselect("Seleccione Vendedores", get_multiselect_options("Vendedor"), default=["Todos"], key="filtro_vendedor")

# Filtrar el DataFrame según los valores seleccionados
filtered_df = df[
    (df['Cliente'].isin(clientes if "Todos" not in clientes else df['Cliente'].unique())) &
    (df['Vendedor'].isin(vendedores if "Todos" not in vendedores else df['Vendedor'].unique()))
]



# Gráficos por Cliente y Vendedor
col1, col2 = st.columns(2)

with col1:
    st.subheader("👥 Ingreso por Cliente")
    ingreso_cliente = filtered_df.groupby("Cliente")["Ingreso Total"].sum().sort_values()
    st.bar_chart(ingreso_cliente)

with col2:
    st.subheader("👤 Ingreso por Vendedor")
    ingreso_vendedor = filtered_df.groupby("Vendedor")["Ingreso Total"].sum().sort_values()
    st.bar_chart(ingreso_vendedor)

# Sección para gráficos por Distribuidor y Producto
with st.expander("Filtro por Distribuidor y Producto"):
    distribuidores = st.multiselect("Seleccione Distribuidores", get_multiselect_options("Distribuidor"), default=["Todos"], key="filtro_distribuidor")
    productos = st.multiselect("Seleccione Productos", get_multiselect_options("Producto"), default=["Todos"], key="filtro_producto")

# Filtrar el DataFrame según los valores seleccionados
filtered_df = df[
    (df['Distribuidor'].isin(distribuidores if "Todos" not in distribuidores else df['Distribuidor'].unique())) &
    (df['Producto'].isin(productos if "Todos" not in productos else df['Producto'].unique()))
]

# Gráficos por Distribuidor y Producto
col1, col2 = st.columns(2)

with col1:
    st.subheader("🛒 Ingreso por Distribuidor")
    ingreso_distribuidor = filtered_df.groupby("Distribuidor")["Ingreso Total"].sum().sort_values()
    st.bar_chart(ingreso_distribuidor)

with col2:
    st.subheader("📈 Ingreso por Producto")
    ingreso_producto = filtered_df.groupby("Producto")["Ingreso Total"].sum().sort_values()
    st.bar_chart(ingreso_producto)
    
    
    

# Sección 3: Gráfico Circular por Estado y Gráfico de Líneas por Fecha
col5, col6 = st.columns(2)

with col5:
    st.subheader("⚖️ Distribución por Estado")
    fig, ax = plt.subplots()

    # Aplicar colores condicionales según el estado
    estado_colores = {
        "Entrega Exacta en Lugar": "gold",
        "Dentro del Rango de 30 Metros": "green",
        "Fuera del Rango de 30 Metros": "red"
    }

    # Fondo transparente para el gráfico
    fig.patch.set_facecolor('none')  # Fondo de la figura
    ax.set_facecolor('none')  # Fondo del eje
    
    estados_unicos = sorted(filtered_df['estado'].unique(), key=lambda x: estado_colores[x])
    
  # Graficar el gráfico circular con colores condicionales y etiquetas blancas
    filtered_df.groupby("estado")["Ingreso Total"].sum().plot.pie(
        autopct=lambda p: f'{p:.1f}%',
        colors=[estado_colores[e] for e in estados_unicos],
        ax=ax,
        textprops={'color': 'white'},  # Configuración de texto blanco
        startangle=90
    )
    st.pyplot(fig)
    
  # Grafica de lineas
  
with col6:
    st.subheader("📅 Ingreso por Fecha")
    ingreso_fecha = filtered_df.groupby("Fecha pedido")["Ingreso Total"].sum()
    st.line_chart(ingreso_fecha)
    

# FIN DE LOS ESTADO Y LINEAS:


###_-----------------------------------------------------------------####

# INICIO SECCION TARJETAS POR PERIODOS

# Inyectar CSS para establecer fondo negro y texto blanco
st.markdown(
    """
    <style>
    /* Estilo para tarjetas con fondo negro y texto blanco */
    .card.animated {
        background-color: #000000;  /* Fondo negro */
        color: #ffffff;  /* Texto blanco */
        padding: 10px;  /* Espacio interno reducido */
        border-radius: 10px;  /* Bordes redondeados */
        border: 1px solid limegreen;  /* Borde verde para contraste */
        box-shadow: 2px 2px 6px rgba(0, 255, 0, 0.2);  /* Sombra sutil */
        font-size: 18px;  /* Tamaño de fuente más pequeño */
        font-weight: bold;  /* Texto en negrita */
        transition: all 0.3s ease;  /* Transición suave */
        text-align: center;  /* Texto centrado */
    }

    /* Cambiar estilo al pasar el cursor sobre la tarjeta */
    .card.animated:hover {
        background-color: #333333;  /* Fondo más claro al pasar el cursor */
        box-shadow: 4px 4px 12px rgba(255, 255, 255, 0.3);  /* Mayor sombra */
    }

    /* Estilo para etiquetas <h4> dentro de .card.animated */
    .card.animated h4 {
        font-size: 18px;  /* Tamaño del texto */
        margin: 5px 0;  /* Reducir margen */
        color: #ffffff !important;  /* Asegurar texto blanco */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Definir función para formato de moneda y cantidad
def format_currency(value):
    return "${:,.2f}".format(value)

def format_quantity(value):
    return "{:,}".format(value)

# Leer el DataFrame
df = pd.read_excel('Vista_Detalles_Pedidos_V1.xlsx')

# Convertir 'Fecha pedido' a tipo datetime
df['Fecha pedido'] = pd.to_datetime(df['Fecha pedido'], errors='coerce')

# Crear intervalos de 3 años (2010 al 2024)
bins = np.arange(2010, 2027, 3)
labels = [f"{start}-{start + 2}" for start in bins[:-1]]

# Añadir una columna para los periodos
df['Periodo'] = pd.cut(df['Fecha pedido'].dt.year, bins=bins, labels=labels, right=False)

# Calcular ingresos y pedidos por período
ingresos_por_periodo = df.groupby('Periodo')['Ingreso Total'].sum()
pedidos_por_periodo = df.groupby('Periodo')['NoPedido'].count()

# Crear secciones de tarjetas para cada período
st.subheader("💹 Ingresos y Pedidos por Período (3 años)")

cols = st.columns(len(ingresos_por_periodo))

# Agregar tarjetas para cada período con el nuevo estilo y animación
for idx, periodo in enumerate(ingresos_por_periodo.index):
    ingreso = ingresos_por_periodo[periodo]
    pedidos = pedidos_por_periodo[periodo]

    with cols[idx]:
        st.markdown(
            f"""
            <div class='card animated'>
                <h4>🗓️Período {periodo}</h4>
                <h4>💰 Ingresos Totales</h4>
                <h4>{format_currency(ingreso)}</h4>
                <h4>📦 Pedidos Totales</h4>
                <h4>{format_quantity(pedidos)}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )      



# FIN SECCION TARJETAS POR PERIODOS

###_-----------------------------------------------------------------####



# INCIIO SECCION GRAFICO POR PERIODOS:

# Asegurarse de que la columna de fechas sea de tipo datetime
df['Fecha pedido'] = pd.to_datetime(df['Fecha pedido'], errors='coerce')

# Extraer el año de la fecha del pedido
df['Año'] = df['Fecha pedido'].dt.year

# Agrupar por año y calcular la suma de ingresos
ingresos_por_ano = df.groupby('Año')['Ingreso Total'].sum().reset_index()

# Agregar un salto de línea para separar
st.write("")  # Esto crea un espacio adicional


# Crear un gráfico de líneas para visualizar la evolución de ingresos por año
st.subheader("🧬 Evolución de Ingresos por Año")

fig = px.line(
    ingresos_por_ano,
    x="Año",
    y="Ingreso Total",
    labels={"Año": "Año", "Ingreso Total": "Ingresos ($)"},
    title="Evolución de Ingresos por Año",
    markers=True,  # Añadir marcadores para mayor visibilidad
    text="Ingreso Total",  # Mostrar el valor de ingresos como texto en cada punto
    color_discrete_sequence=px.colors.qualitative.Set3,  # Cambiar los colores de las líneas
)

# Ajustar el estilo del título y el tamaño del gráfico
fig.update_layout(
    width=800,
    height=400,
    plot_bgcolor="rgba(0,0,0,0)",  # Fondo transparente
    paper_bgcolor="rgba(0,0,0,0)",  # Fondo transparente
    title_font=dict(size=20, color="white"),  # Título en blanco
    legend=dict(
        orientation="h",  # Leyenda horizontal
        xanchor="center",  # Anclar al centro
        x=0.5,  # Ubicación de la leyenda
        y=-0.1,  # Posición de la leyenda (debajo del gráfico)
    ),
    xaxis=dict(showgrid=True, gridcolor="lightgray", zeroline=False),  # Líneas de cuadrícula en el eje X
    yaxis=dict(showgrid=True, gridcolor="lightgray", zeroline=False),  # Líneas de cuadrícula en el eje Y
)

# Ajustar el tamaño de los puntos y mostrar las etiquetas
fig.update_traces(
    marker=dict(size=10),  # Tamaño de los puntos
    textposition="top center",  # Posición de las etiquetas
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig, use_container_width=True)

# FIN SECCION GRAFICO POR PERIODOS:


###_-----------------------------------------------------------------####

# SECCION TARJETAS O CARD POR ESTADO Y Segmentador por estado

# Define colores por estado
estado_colores = {
    "Entrega Exacta en Lugar": "green",
    "Dentro del Rango de 30 Metros": "orange",
    "Fuera del Rango de 30 Metros": "red"
}



# Define formato para valores monetarios
def format_currency(value):
    return "${:,.2f}".format(value)

# Define formato para cantidades
def format_quantity(value):
    return "{:,}".format(value)

# Agregar filtro por estado
estados_seleccionados = st.multiselect(
    "Filtrar por Estado",
    df['estado'].unique(),
    default=df['estado'].unique()
)

# Filtrar datos según los estados seleccionados
tabla_datos_filtrada = df[df['estado'].isin(estados_seleccionados)]

# Verificar si hay datos después de filtrar
if tabla_datos_filtrada.empty:
    st.warning("No hay datos para mostrar según la selección actual.")
else:
    # Calcular ingresos y cantidad de pedidos por estado
    suma_ingresos_por_estado = tabla_datos_filtrada.groupby('estado')['Ingreso Total'].sum()
    cantidad_pedidos_por_estado = tabla_datos_filtrada.groupby('estado')['NoPedido'].count()

    # Mostrar tarjetas con ingresos y cantidad de pedidos por estado
    st.subheader("💵 Suma de Ingresos por Estado y Cantidad de Pedidos")

    col1, col2, col3 = st.columns(3)

    with col1:
        ingreso = suma_ingresos_por_estado.get("Entrega Exacta en Lugar", 0)
        pedidos = cantidad_pedidos_por_estado.get("Entrega Exacta en Lugar", 0)
        st.markdown(
            f"""
            <div style='background-color: {estado_colores["Entrega Exacta en Lugar"]}; 
                        color: white; padding: 20px; border-radius: 10px; 
                        text-align: center;'>
                <h3>💰 Entrega Exacta en Lugar</h3>
                <h2>{format_currency(ingreso)}</h2>
                <h4>📦Pedidos: {format_quantity(pedidos)}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        ingreso = suma_ingresos_por_estado.get("Dentro del Rango de 30 Metros", 0)
        pedidos = cantidad_pedidos_por_estado.get("Dentro del Rango de 30 Metros", 0)
        st.markdown(
            f"""
            <div style='background-color: {estado_colores["Dentro del Rango de 30 Metros"]}; 
                        color: white; padding: 20px; border-radius: 10px; 
                        text-align: center;'>
                <h3>💰Dentro del Rango de 30 Metros</h3>
                <h2>{format_currency(ingreso)}</h2>
                <h4>📦Pedidos: {format_quantity(pedidos)}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        ingreso = suma_ingresos_por_estado.get("Fuera del Rango de 30 Metros", 0)
        pedidos = cantidad_pedidos_por_estado.get("Fuera del Rango de 30 Metros", 0)
        st.markdown(
            f"""
            <div style='background-color: {estado_colores["Fuera del Rango de 30 Metros"]}; 
                        color: white; padding: 20px; border-radius: 10px; 
                        text-align: center;'>
                <h3>💰Fuera del Rango de 30 Metros</h3
                ><h2>{format_currency(ingreso)}</h2>
                <h4>📦Pedidos: {format_quantity(pedidos)}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Agregar un salto de línea para separar
    st.write("")  # Esto crea un espacio adicional

    # Mostrar tabla de pedidos y entregas con formato condicional por estado
    st.subheader("🚚 Tabla de Pedidos y Entregas")
    styled_table = tabla_datos_filtrada[
        ['NoPedido', 'Cliente', 'Vendedor', 'Distribuidor', 'Producto', 'cantidad_vendida', 'Ingreso Total', 'distancia_metros', 'estado']
    ].style.applymap(lambda val: f"color: {estado_colores.get(val, 'black')};", subset=['estado'])

    st.dataframe(styled_table, use_container_width=True)

 
 
 # FIN SECCION TARJETAS O CARD POR ESTADO Y Segmentador por estado
 
 
 
 
 
 ###_-----------------------------------------------------------------####
 
 
 
 
 
 # ININICIO SECCION MAPA INTERACTIVO POR ENTREGAS Y ESTADOS. CLUSTER DINAMICO Y TOOLTIPS
    
# Seccion del Mapa":
# Agregar CSS para centrar el contenido
st.markdown(
    """
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Agregar "Todos" a las listas de opciones
estado_opciones = ["Todos"] + list(df['estado'].unique())
distribuidor_opciones = ["Todos"] + list(df['Distribuidor'].unique())

# Selectbox para Estados con opción "Todos"
estado_seleccionado = st.selectbox(
    "Seleccione Estado",
    options=estado_opciones,
    index=0,  # "Todos" como selección predeterminada
    key='unique_estado'
)

# Selectbox para Distribuidores con opción "Todos"
distribuidor_seleccionado = st.selectbox(
    "Seleccione Distribuidor",
    options=distribuidor_opciones,
    index=0,
    key='unique_distribuidor'
)

# Aplicar lógica para el filtro
if estado_seleccionado == "Todos":
    estados_filtrados = df['estado'].unique()  # Todos los estados
else:
    estados_filtrados = [estado_seleccionado]

if distribuidor_seleccionado == "Todos":
    distribuidores_filtrados = df['Distribuidor'].unique()  # Todos los distribuidores
else:
    distribuidores_filtrados = [distribuidor_seleccionado]

# Filtrar el DataFrame según el estado y distribuidor seleccionados
filtered_df = df[
    (df['estado'].isin(estados_filtrados)) &
    (df['Distribuidor'].isin(distribuidores_filtrados))
]




# Configurar el mapa
mapa = folium.Map(location=[18.486057, -69.931212], zoom_start=12)

# Agregar un MarkerCluster para agrupar marcadores
marker_cluster = MarkerCluster().add_to(mapa)

# Aplicar colores para los estados
estado_colores = {
    "Entrega Exacta en Lugar": "green",
    "Dentro del Rango de 30 Metros": "orange",
    "Fuera del Rango de 30 Metros": "red"
}

# Agregar marcadores al cluster basados en el DataFrame filtrado
for _, fila in filtered_df.iterrows():
    latitud = fila['Latitud_Cliente']
    longitud = fila['Longitud_Cliente']
    estado = fila['estado']

    # Formatear el tooltip para que sea más legible y grande
    tooltip_text = (
        f"<strong>Cliente:</strong> {fila['Cliente']}<br>"
        f"<strong>Distribuidor:</strong> {fila['Distribuidor']}<br>"
        f"<strong>Producto:</strong> {fila['Producto']}<br>"
        f"<strong>Distancia:</strong> {fila['distancia_metros']:.2f} metros<br>"
        f"<strong>Estado:</strong> {estado}<br>"
        f"<strong>Ingreso Total:</strong> ${fila.get('Ingreso Total', 'N/A'):.2f}"
    )

    folium.Marker(
        location=[latitud, longitud],
        tooltip=tooltip_text,
        icon=folium.Icon(color=estado_colores.get(estado, 'blue'), icon='info-sign')
    ).add_to(marker_cluster)

# Mostrar el mapa en Streamlit con tamaño ajustable
st.markdown("<div class='centered'>", unsafe_allow_html=True)
st_folium(mapa, width=1500, height=600, key='unique_mapa')  # Puedes cambiar el tamaño según tus necesidades
st.markdown("</div>", unsafe_allow_html=True)

 # FIN  SECCION MAPA INTERACTIVO POR ENTREGAS Y ESTADOS. CLUSTER DINAMICO Y TOOLTIPS


###---------------------------------------------------------------------------###

# INICIOS DE SECCOPM DE LOS GRAFICOS ADICIONALES DE ENTREGA POR DISTANCIA:

# CSS para centrar el contenido
st.markdown(
    """
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sección para gráficos con dos columnas
st.subheader("📊 Gráficos Adicionales 📊")

col1, col2 = st.columns(2)

# Gráfico de líneas por fecha y estado
with col1:
    st.subheader("💵 Ingresos por Fecha y Estado")

    # Agrupar datos por fecha y estado para obtener los ingresos totales
    df_agg = filtered_df.groupby(["Fecha pedido", "estado"])["Ingreso Total"].sum().reset_index()

    # Gráfico de líneas para mostrar ingresos por estado
    fig = px.line(
        df_agg,
        x="Fecha pedido",
        y="Ingreso Total",
        color="estado",
        labels={"Fecha pedido": "Fecha", "Ingreso Total": "Ingresos ($)"},
        title="Ingresos por Fecha para cada Estado",
        line_shape="linear",
        color_discrete_map={
            "Entrega Exacta en Lugar": "green",
            "Dentro del Rango de 30 Metros": "orange",
            "Fuera del Rango de 30 Metros": "red"
        }  # Aplicar colores consistentes para cada estado
    )

    # Ajustar el tamaño del gráfico y la posición de la leyenda
    fig.update_layout(
        width=700,
        height=450,
        legend=dict(
            orientation="h",
            xanchor="center",
            x=0.5
        )
    )

    st.plotly_chart(fig)

# Gráfico de barras horizontales para la distancia promedio por distribuidor
with col2:
    st.subheader("🗺️ Distancia Promedio por Distribuidor")

    # Calcular la distancia promedio por distribuidor
    df_distancia = filtered_df.groupby("Distribuidor")["distancia_metros"].mean().reset_index()

    # Gráfico de barras horizontales para mostrar la distancia promedio
    fig = px.bar(
        df_distancia,
        x="distancia_metros",
        y="Distribuidor",
        orientation="h",
        labels={"distancia_metros": "Distancia Promedio (m)", "Distribuidor": "Distribuidor"},
        title="Distancia Promedio por Distribuidor"
    )

    # Ajustar el tamaño del gráfico y la posición de la leyenda
    fig.update_layout(
        width=700,
        height=450,
        legend=dict(
            orientation="h",
            xanchor="center",
            x=0.5
        )
    )

    st.plotly_chart(fig)
    
# FIND E LOS GRAFICOS ADICIONALES DE ENTREGA POR DISTANCIA:


###---------------------------------------------------------------------------###


# INICIO DE SECCION TABLA CON ESTADO Y GRAFICO DE DISPERSION:

# Segmentador por estado
estado_seleccionado = st.selectbox(
    "Seleccione Estado para ver el Top 10",
    options=list(df['estado'].unique()),
    index=0  # Puedes cambiar el índice para seleccionar un estado por defecto
)

# Crear una función para obtener el Top 10 por estado
def get_top_10_by_state(df, state):
    # Filtrar por estado y ordenar por distancia
    state_df = df[df['estado'] == state].sort_values(by='distancia_metros')
    # Tomar los primeros 10
    return state_df.head(10)

# Obtener el Top 10 para el estado seleccionado
top_10_df = get_top_10_by_state(df, estado_seleccionado)

# Aplicar colores para formato condicional en la columna 'estado'
estado_colores = {
    "Entrega Exacta en Lugar": "green",
    "Dentro del Rango de 30 Metros": "orange",
    "Fuera del Rango de 30 Metros": "red"
}

# Función para formato condicional
def formato_estado(val):
    color = estado_colores.get(val, 'black')
    return f"color: {color};"

# Mostrar el DataFrame con formato condicional
st.subheader(f"🔝Top 10 por Estado 🏅 : {estado_seleccionado}")
styled_table = top_10_df[
    ['NoPedido', 'Fecha pedido', 'Distribuidor', 'Producto', 'cantidad_vendida', 'Ingreso Total', 'distancia_metros', 'estado']
].style.applymap(formato_estado, subset=['estado'])

st.dataframe(styled_table, use_container_width=True)
# Subtítulo para la nueva sección
# Definir colores por estado
estado_colores = {
    "Entrega Exacta en Lugar": "green",
    "Dentro del Rango de 30 Metros": "yellow",
    "Fuera del Rango de 30 Metros": "red"
}

# Aplicar el color según el estado
df['Color'] = df['estado'].map(estado_colores)

# Gráfico de dispersión por distribuidor y distancia
# Gráfico de dispersión
fig = px.scatter(
    df,
    x="Distribuidor",
    y="distancia_metros",
    color='Color',
    labels={"Distribuidor": "Distribuidor", "distancia_metros": "Distancia (metros)"},
    title="📏🏃‍♂️ Distancia por Distribuidor y Estado 📌🗺️",
    hover_data=["Cliente", "Producto", "Vendedor", "Ingreso Total"]
)

# Ajustar el tamaño del texto del título
fig.update_layout(
    title={
        'text': "📏🏃‍♂️ Distancia por Distribuidor y Estado 📌🗺️",
        'x': 0.5,  # Centrar el título
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 26  # Tamaño del texto
        }
    }
)
# Ajustar el diseño del gráfico
fig.update_layout(
    plot_bgcolor="rgba(0, 0, 0, 0)",  # Fondo transparente
    showlegend=False,  # Ocultar la leyenda si es redundante
)

# Mostrar el gráfico en Streamlit con todo el ancho
st.plotly_chart(fig, use_container_width=True)


# FIN DE TABLA.




    # Agregar un salto de línea para separar
st.write("")  # Esto crea un espacio adicional

###---------------------------------------------------------------------------###


st.markdown(
    """
    
     <p style='text-align: center; color: white; font-size: 30px;'>
       📤 Comparte este reporte:
    </p>
    
    <div style='text-align: center;'>
        <a href='https://twitter.com/intent/tweet?text=¡Mira%20este%20reporte!&url=https%3A%2F%2Fexample.com' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/twitter.png' alt='Twitter' />
        </a>
        <a href='https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fexample.com' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/facebook-new.png' alt='Facebook' />
        </a>
        <a href='https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fexample.com' target='_blank'>
            <img src='https://img.icons8.com/color/48/000000/linkedin.png' alt='LinkedIn' />
        </a>
    </div>
    """,
    unsafe_allow_html=True
)



# Agregar una línea horizontal para dividir secciones
st.markdown("<hr>", unsafe_allow_html=True)
###---------------------------------------------------------------------------###


    # Agregar un salto de línea para separar
st.write("")  # Esto crea un espacio adicional





st.markdown(
    """
    <style>
    @keyframes rotating-border {
        0% {
            background: conic-gradient(red, blue, white, yellow,green);
        }
        100% {
            background: conic-gradient(blue,green, white, yellow, red);
        }
    }

    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        padding-top: 50px;  # Puedes ajustar esto para subir o bajar el margen
        padding-bottom: 50px;  # Y esto para cambiar el margen inferior
    }

    .circular-image {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        overflow: hidden;
        border: 8px solid transparent;
        background: conic-gradient(red, blue, white, yellow);
        animation: rotating-border 4s linear infinite;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .circular-image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    </style>
    
   
    """,
    unsafe_allow_html=True
)

# Agregar una línea horizontal para dividir secciones
st.markdown("<hr>", unsafe_allow_html=True)
###---------------------------------------------------------------------------###



# Definir el estilo CSS para resaltar palabras clave y usar negrita
css_style = """
<style>
.description-quien_soy {
  width: 70%; /* Ocupa el 70% del contenedor */
  color: white; /* Texto blanco */
  background-color: transparent; /* Fondo transparente */
  text-align: center; /* Texto centrado */
  font-size: 18px; /* Tamaño de letra para los párrafos */
  line-height: 1.6; /* Espacio entre líneas para mejorar la legibilidad */
  margin: 0 auto; /* Centrar horizontalmente dentro del contenedor */
  padding: 20px; /* Añadir espacio alrededor del contenido */
}

.description-quien_soy h2 {
  font-size: 30px; /* Tamaño de letra más grande para h2 */
  margin-bottom: 1em; /* Espacio debajo del título */
}

.parrafo {
  margin-bottom: 1.5em; /* Aumentar la separación entre párrafos */
  font-size: 20px; /* Tamaño de letra para los párrafos */
}

.highlight {
  font-weight: bold; /* Texto en negrita */
  color: lime; /* Color verde limón fluorescente */
}
</style>
"""

# Aplicar el estilo CSS
st.markdown(css_style, unsafe_allow_html=True)

# Sección de descripción personal
description_html = """
<div class="description-quien_soy">
  <h2>🤔 ¿Quién Soy? 🇩🇴</h2>
  
 <div class='centered'>
        <div class='circular-image'>
            <img src='https://juancitopena.github.io/PORTAFOLIO_WEB_JPV/imagenes/Juancito-transp.png' alt='Descripción de la imagen' />
        </div>
    </div>
    <br>
  <p class="parrafo">
    🙋 ¡Hola! Mi nombre es <span class="highlight">Juancito Peña V.</span>   💻. Soy un entusiasta del 📊 análisis de datos, las tecnologías, y la programación 💻,
    con más de 15 años de experiencia trabajando, educando, aprendiendo e innovando en sistemas orientados a procesos tecnológicos,
    administrativos, productivos y de marketing. Creo en el poder de la tecnología para mejorar la productividad 🚀, los
    negocios 💼 y la educación 🎓.
  </p>

  <p class="parrafo">
    🎓 Mi formación académica incluye un título en <span class="highlight">Ingeniería en Sistemas y Computación</span> 🎓, una especialidad en <span class="highlight">Desarrollo
    de Software</span> 🛠️, y una maestría en <span class="highlight">Sistemas con mención Gerencial</span>. Recientemente, he iniciado una nueva maestría en
    <span class="highlight">Ciencia de Datos para Negocios (Big Data & Business Analytics)</span> en CEUPE - Centro Europeo de Postgrado CEUPE/CESUMA 📚.
  </p>

  <p class="parrafo">
   🧬 Mis habilidades técnicas incluyen el uso avanzado de herramientas de Business Intelligence como: <span class="highlight">Excel 📊</span>, 
    <span class="highlight">SQL Server 💾</span>, <span class="highlight">Power BI</span>, <span class="highlight">Python</span> 🐍, y Crystal Reports 📊, 
    así como otras herramientas de Desarollo de Software como:  <span class="highlight"> Xamarin, .NET MAUI, C#, .NET Framework</span>, <span class="highlight">HTML</span>, <span class="highlight">CSS</span>, <span class="highlight">JavaScript, Python, PHP, 
    Wordpress, Balsamiq y Figma.</span> y otras herramientas y  Software ERP como: <span class="highlight">SAP HANA,
    Mseller App, Macola, EasySales</span>
  </p>

  <p class="parrafo">
    👷 He trabajado en implementaciones de software 💻, aplicaciones móviles para ventas 📱, almacén, distribución 🚚, así
    como en la creación y generación de reportes 📑, informes 📃, y dashboards para Business Intelligence, con el fin 
    de mejorar la toma de decisiones 🎯 en la empresa.  Desde el planteamiento del problema hasta el lanzamiento, 
    abarcando actividades como 📏 prototipado, 🔍 testing y 🧪 QA, hasta la documentación 📄 y la capacitación del personal 🧑‍🏫
  </p>
  
<p class="parrafo">
    🫡 Soy un guerrero en el mundo laboral, un ejemplo de resiliencia y determinación. Vengo de una familia humilde, 
    con escasos recursos, y he enfrentado mil ⚔️ batallas para llegar a donde estoy. He 🤕 caído muchas veces, pero me he 💪 levantado 
    mil y una, siempre con más fuerza y 🏃 determinación. Amo lo que hago ❤️, y esa pasión me impulsa a seguir adelante incluso
    cuando el camino es difícil.
</p>

<p class="parrafo">
    🤔 Si crees que te puedo ayudar con tus proyectos, no dudes en contactarme a través de mis redes sociales 📱,
    mi correo 📧, o por WhatsApp 💬. Estoy aquí para ayudarte a lograr tus objetivos y a superar cualquier desafío.
</p>





  
</div>
"""

st.markdown(description_html, unsafe_allow_html=True)

# Fin de la sección de descripción personal

# FIN SECCIÓN DE DESCRIPCIÓN PERSONAL

# Agregar una línea horizontal para dividir secciones
st.markdown("<hr>", unsafe_allow_html=True)
###---------------------------------------------------------------------------###


# SECCIÓN DEL PIE DE PÁGINA
footer_html = """

   <p style='text-align: center; color: white; font-size: 20px;'>
       Sígueme en mis Redes Sociales, Comparte y Comenta.
    </p>

    <div style='text-align: center; font-size: 18px; font-weight: bold;'>
      <br>
      <a href='https://www.youtube.com/@JuancitoPenaV' target='_blank' style='font-size: 18px;'>
        <img src='https://img.icons8.com/color/48/000000/youtube-play.png' alt='YouTube' width='24' /> YouTube
      </a> | 
      <a href='https://www.linkedin.com/in/juancitope%C3%B1a/' target='_blank' style='font-size: 18px;'>
        <img src='https://img.icons8.com/color/48/000000/linkedin-circled.png' alt='LinkedIn' width='24' /> LinkedIn
      </a> | 
      <a href='https://github.com/JUANCITOPENA/Analisis_Datos_Pedidos_Entregas_Python' target='_blank' style='font-size: 18px;'>
        <img src='https://img.icons8.com/material-rounded/48/4A90E2/github.png' alt='GitHub' width='24' /> GitHub
      </a> |
      <a href='https://www.instagram.com/' target='_blank' style='font-size: 18px;'>
        <img src='https://img.icons8.com/fluency/48/000000/instagram-new.png' alt='Instagram' width='24' /> Instagram
      </a> | 
      <a href='https://www.facebook.com/' target='_blank' style='font-size: 18px;'>
        <img src='https://img.icons8.com/color/48/000000/facebook-new.png' alt='Facebook' width='24' /> Facebook
      </a> | 
      <a href='https://chat.whatsapp.com/GrzUtfJXvTDFPW1jSa3NWR' target='_blank' style='font-size: 18px;'>
        <img src='https://img.icons8.com/color/48/000000/whatsapp.png' alt='WhatsApp' width='24' /> WhatsApp
      </a> |
      <a href='mailto:juancito.pena@gmail.com' target='_blank' style='font-size: 18px;'>
        <img src='https://cdn.icon-icons.com/icons2/1826/PNG/48/4202011emailgmaillogomailsocialsocialmedia-115677_115624.png' alt='Correo Electrónico' width='24' /> Correo Electrónico
      </a>
      <br><br>
      <h3>© 2023 Advisertecnology - Todos los derechos reservados | 
        <a href='https://advisertecnology.com/' target='_blank' style='font-size: 18px; color: lime;'>www.advisertecnology.com</a>
      </h3>
    </div>
"""

st.markdown(footer_html, unsafe_allow_html=True)

###---------------------------------------------------------------------------###

# Instrucciones para ejecutar el dashboard
# Desde la consola, en la carpeta de tu proyecto, ejecuta: `streamlit run Dashboard.py`
