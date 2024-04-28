# 📊 Dashboard de Análisis de Pedidos y Entregas con Python 📊

## 🌟 Introducción 🌟
Bienvenido a este proyecto de análisis de datos de pedidos y entregas. El objetivo es crear un dashboard interactivo en Python utilizando Streamlit para visualizar y analizar datos de pedidos y entregas, proporcionando información valiosa para la toma de decisiones y la mejora de procesos.

## 🔍 Planteamiento del Problema 🔍
En muchas empresas, los procesos de pedidos y entregas son fundamentales para el éxito del negocio. Sin embargo, estos procesos a menudo generan grandes cantidades de datos que pueden ser difíciles de interpretar y analizar. Los problemas comunes incluyen retrasos en entregas, altos costos operativos, y baja satisfacción del cliente debido a la falta de visibilidad y control.

## 💡 Solución 💡
Para abordar estos problemas, hemos desarrollado un dashboard interactivo que permite analizar datos de pedidos y entregas de manera visual y dinámica. Con este dashboard, puedes aplicar filtros, visualizar gráficos, y obtener información relevante para tomar decisiones informadas y mejorar la eficiencia operativa.

## 📊 Recursos utilizados como datos📊

Para el análisis de datos de pedidos y entregas, utilizamos un archivo Excel llamado `Vista_Detalles_Pedidos_V1.xlsx`. Este dataset es una vista generada a partir de una base de datos que contiene información detallada sobre pedidos, clientes, productos, vendedores, y más.

Los datos contenidos en el archivo Excel incluyen las siguientes columnas:

- **NoPedido**: Número de identificación del pedido.
- **Fecha Pedido**: Fecha en que se realizó el pedido.
- **Vendedor**: Nombre del vendedor responsable del pedido.
- **Teléfono Vendedor**: Número de contacto del vendedor.
- **Cliente**: Nombre del cliente que realizó el pedido.
- **Teléfono Cliente**: Número de contacto del cliente.
- **Ciudad**: Ciudad o localidad del cliente.
- **Latitud_Cliente y Longitud_Cliente**: Coordenadas geográficas del cliente.
- **Distribuidor**: Nombre del distribuidor a cargo de la entrega.
- **Producto**: Descripción del producto pedido.
- **Fecha Depacho**: Fecha de despacho o entrega del pedido.
- **Latitud_Despacho y Longitud_Despacho**: Coordenadas geográficas de donde se hizo la entrega.
- **Teléfono Distribuidor**: Número de contacto del distribuidor.
- **Distancia Metros**: Distancia entre el cliente y el punto de entrega.
- **Estado**: Estado de la entrega (por ejemplo, "Entrega Exacta en Lugar", "Dentro del Rango de 30 Metros", "Fuera del Rango de 30 Metros").
- **Total de Pedidos**: Cantidad total de pedidos realizados.
- **Cantidad Vendida**: Cantidad de productos vendidos en el pedido.
- **Costo Total**: Costo total de los productos vendidos.
- **Ingreso Total**: Ingresos generados por los pedidos.
- **Diferencia**: Diferencia entre el costo total y el ingreso total.
- **Margen y % Margen**: Margen bruto y porcentaje de margen en relación con los ingresos.

---

## 🛠️ Tecnologías Utilizadas 🛠️
Para construir este dashboard, utilizamos las siguientes tecnologías y herramientas:
- **Python**: Lenguaje de programación principal.
- **Streamlit**: Framework para crear aplicaciones web interactivas.
- **Pandas**: Biblioteca para análisis y manipulación de datos.
- **Matplotlib y Seaborn**: Bibliotecas para visualización de datos.
- **Folium**: Biblioteca para crear mapas interactivos.
- **Visual Studio Code**: Entorno de desarrollo integrado (IDE) para el desarrollo del proyecto.

## 📋 Instalación y Configuración 📋
Sigue estos pasos para instalar y configurar el proyecto en tu entorno local:

1. **Clonar el repositorio** desde GitHub:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git

---
## Crear y activar un entorno virtual para mantener las dependencias aisladas:

python -m venv mi_entorno
source mi_entorno/bin/activate  # Para Linux/macOS
mi_entorno\Scripts\activate  # Para Windows

### Instalar las dependencias necesarias:

pip install streamlit pandas matplotlib seaborn folium openpyxl

### Ejecutar el dashboard:


streamlit run Dashboard.py

## 📊 Diseño del Dashboard 📊

El dashboard está compuesto por varias secciones y gráficos para el análisis de datos de pedidos y entregas:

- **Gráficos de Barra**: Visualiza los ingresos por cliente, vendedor, distribuidor y producto. Estos gráficos proporcionan información clara y comparativa.
- **Gráfico Circular por Estado**: Muestra la distribución por estado con colores personalizados: 
  - Verde para "Entrega Exacta".
  - Amarillo para "Dentro del Rango de 30 Metros".
  - Rojo para "Fuera del Rango de 30 Metros".
- **Gráfico de Líneas por Fechas**: Analiza el ingreso total a lo largo del tiempo, permitiendo identificar tendencias.
- **Mapa de Geolocalización**: Muestra la ubicación de los clientes y las entregas. Los puntos del mapa están coloreados según el estado de la entrega.

---

## 🏷️ Licencia 🏷️

Este proyecto está licenciado bajo la Licencia MIT. Puedes usar, copiar, modificar y distribuir el código con libertad, siempre que mantengas esta licencia y des el crédito correspondiente.

---

## ⭐ Contribuciones y Soporte ⭐

Las contribuciones al proyecto son bienvenidas. Si encuentras errores, tienes ideas para mejorar, o deseas contribuir, no dudes en abrir un issue o un pull request en GitHub. Recuerda dar una estrella al repositorio si te resulta útil y compartirlo con otros.

---

## 📣 Sígueme en Redes Sociales 📣

Si te gustó este proyecto, te invito a seguirme en estas plataformas:

- [YouTube](#) 
- [GitHub](#)
- [LinkedIn](#)
- [Blog](#)

---

## 🚀 Ejecución del Dashboard 🚀

Para ejecutar el dashboard, sigue estos pasos:

1. Abre una terminal o consola en la carpeta donde clonaste el repositorio.
2. Activa tu entorno virtual.
3. Ejecuta el comando: `streamlit run Dashboard.py`.
4. Abre tu navegador para ver el dashboard en acción.

---

Esperamos que este proyecto te sea útil para comprender mejor el análisis de datos de pedidos y entregas. Gracias por tu interés, y no dudes en contribuir y compartir el proyecto. 🚀

