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

# Configurar el diseño de la página para ser más amplio
st.set_page_config(layout="wide")

# Leer datos desde el archivo Excel
df = pd.read_excel('Vista_Detalles_Pedidos_V1.xlsx')


# Estilo CSS para tarjetas con bordes redondeados, borde verde y sombra
st.markdown(
    """
    <style>
    .card {
        background: white;  /* Fondo blanco */
        border-radius: 15px;  /* Bordes redondeados */
        border: 2px solid limegreen;  /* Borde verde fluorescente */
        box-shadow: 2px 2px 12px rgba(0, 255, 0, 0.2);  /* Sombra con tono verde */
        padding: 20px;  /* Espacio interno */
        text-align: center;  /* Texto centrado */
        margin: 10px;  /* Espacio externo */
        color:black;
        font-size: 19px; /* Tamaño de la letra */
        font-weight: bold; /* Letra negrita */
        color: darkblue; /* Color de la letra */
        transition: all 0.3s ease; /* Transición suave para los cambios de estilo */
        animation: latido 1s infinite; /* Aplica la animación de latido al pasar el cursor */
    }
    
    .card:hover {
        background-color: darkslategray; /* Fondo más oscuro al pasar el cursor */
        color: white; /* Texto blanco al pasar el cursor */
        transform: scale(1.05); /* Aumentar ligeramente el tamaño al pasar el cursor */
        box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.3); /* Mayor sombra para el efecto de elevación */
    }

    @keyframes latido {
        0%, 100% {
            transform: scale(1); /* Sin cambios al inicio y final de la animación */
        }
        50% {
            transform: scale(1.1); /* Aumenta el tamaño a mitad de la animación */
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Título y subtítulo
st.markdown("<h1 style='text-align: center;'>📊 Análisis de Datos de Pedidos y Entregas con Python 📊</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4cd137;'>Creado por: Ing. Juancito Pena</h3>", unsafe_allow_html=True)


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
        f"<div class='card'>📦 Total Pedidos<br><strong>{suma_total_pedidos:,.0f}</strong></div>",
        unsafe_allow_html=True
    )

# Tarjeta para la suma total de cantidad vendida con emoji
with col2:
    st.markdown(
        f"<div class='card'>📊 Total Cantidad<br><strong>{suma_cantidad_vendida:,.0f}</strong></div>",
        unsafe_allow_html=True
    )

# Tarjeta para la suma de ingresos totales con símbolo de moneda y emoji
with col3:
    st.markdown(
        f"<div class='card'>💰 Ingresos Totales<br><strong>${suma_ingresos_totales:,.2f}</strong></div>",
        unsafe_allow_html=True
    )

# Tarjeta para el costo total con símbolo de moneda y emoji
with col4:
    st.markdown(
        f"<div class='card'>💸 Costo Total<br><strong>${suma_costo_total:,.2f}</strong></div>",
        unsafe_allow_html=True
    )

# Tarjeta para el margen con símbolo de moneda y emoji
with col5:
    st.markdown(
        f"<div class='card'>💹 Margen<br><strong>${suma_margen:,.2f}</strong></div>",
        unsafe_allow_html=True
    )

# Tarjeta para el porcentaje de margen con emoji y formato de porcentaje
with col6:
    st.markdown(
        f"<div class='card'>📈 % Margen<br><strong>{suma_porcentaje_margen:,.2f}%</strong></div>",
        unsafe_allow_html=True
    )

# Agregar un expander para segmentadores
with st.expander("Filtros"):
    clientes = st.multiselect("Seleccione Clientes", df['Cliente'].unique(), default=df['Cliente'].unique())
    vendedores = st.multiselect("Seleccione Vendedores", df['Vendedor'].unique(), default=df['Vendedor'].unique())
    distribuidores = st.multiselect("Seleccione Distribuidores", df['Distribuidor'].unique(), default=df['Distribuidor'].unique())
    ciudades = st.multiselect("Seleccione Ciudades", df['Ciudad'].unique(), default=df['Ciudad'].unique())
    estados = st.multiselect("Seleccione Estados", df['estado'].unique(), default=df['estado'].unique())
    
    
# Aplicar filtros a los datos
filtered_df = df[
    (df['Cliente'].isin(clientes)) & 
    (df['Vendedor'].isin(vendedores)) & 
    (df['Distribuidor'].isin(distribuidores)) & 
    (df['Ciudad'].isin(ciudades)) &
    (df['estado'].isin(estados))
]

# Crear gráficos para el dashboard

# Sección 1: Gráficos por Cliente y por Vendedor
col1, col2 = st.columns(2)

with col1:
    st.subheader("👥 Ingreso por Cliente")
    ingreso_cliente = filtered_df.groupby("Cliente")["Ingreso Total"].sum().sort_values()
    st.bar_chart(ingreso_cliente)

with col2:
    st.subheader("👤 Ingreso por Vendedor")
    ingreso_vendedor = filtered_df.groupby("Vendedor")["Ingreso Total"].sum().sort_values()
    st.bar_chart(ingreso_vendedor)

# Sección 2: Ingreso por Distribuidor y por Producto
col3, col4 = st.columns(2)

with col3:
    st.subheader("🛒 Ingreso por Distribuidor")
    ingreso_distribuidor = filtered_df.groupby("Distribuidor")["Ingreso Total"].sum().sort_values()
    st.bar_chart(ingreso_distribuidor)

with col4:
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
    
    

import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# Agregar CSS para centrar el contenido
st.markdown(
    """
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;  # Asegúrate de que el contenedor tenga una altura definida
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Subtítulo para el mapa
st.subheader("🗺️ Mapa de Geolocalización")

# Crear el mapa con Folium
mapa = folium.Map(location=[18.486057, -69.931212], zoom_start=12)

# Selector para distribuidor con un `key` único para evitar duplicados
distribuidores = st.multiselect("Seleccione Distribuidores", df['Distribuidor'].unique(), default=df['Distribuidor'].unique(), key='unique_distribuidores')

# Filtrar datos según el distribuidor seleccionado
filtered_df = df[df['Distribuidor'].isin(distribuidores)]

# Agregar marcadores con colores según el estado
estado_colores = {
    "Entrega Exacta en Lugar": "green",
    "Dentro del Rango de 30 Metros": "orange",
    "Fuera del Rango de 30 Metros": "red"
}

# Agregar marcadores al mapa basados en el DataFrame filtrado
for _, fila in filtered_df.iterrows():
    latitud = fila['Latitud_Cliente']
    longitud = fila['Longitud_Cliente']
    estado = fila['estado']

    color = estado_colores[estado]

    tooltip_text = (
        f"Cliente: {fila['Cliente']}<br>"
        f"Distribuidor: {fila['Distribuidor']}<br>"
        f"Estado: {estado}<br>"
        f"Ingreso Total: {fila.get('Ingreso Total', 'N/A')}"
    )

    folium.Marker(
        location=[latitud, longitud],
        tooltip=tooltip_text,
        icon=folium.Icon(color=color, icon='info-sign')
    ).add_to(mapa)

# Usar CSS para centrar el mapa
st.markdown("<div class='centered'>", unsafe_allow_html=True)
st_folium(mapa, width=1500, height=600)  # Ajusta el ancho y altura según necesites
st.markdown("</div>", unsafe_allow_html=True)




# Pie de página
footer_html = """
<div style='text-align: center; color: lime; font-size: 18px; font-weight: bold;'>
  <br>
  <a href='https://www.youtube.com/@JuancitoPenaV' target='_blank' style='font-size: 18px;'>🔴 YouTube</a> | 
  <a href='https://www.linkedin.com/in/juancitope%C3%B1a/' target='_blank' style='font-size: 18px;'>🔵 LinkedIn</a> | 
  <a href='https://github.com/JUANCITOPENA/Analisis_Datos_Pedidos_Entregas_Python' target='_blank' style='font-size: 18px;'>⚫ GitHub</a>
  <br><br>
  <h3>© 2023 Advisertecnology - Todos los derechos reservados | <a href='https://advisertecnology.com/' target='_blank'>www.advisertecnology.com</a></h3>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)



# Instrucciones para ejecutar el dashboard
# Desde la consola, en la carpeta de tu proyecto, ejecuta: `streamlit run Dashboard.py`
