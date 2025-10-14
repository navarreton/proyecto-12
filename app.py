import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="AgroConecta", page_icon="🌽")
ARCHIVO = "productos.csv"

# Cargar productos si existe el archivo
if "productos" not in st.session_state:
    if os.path.exists(ARCHIVO):
        st.session_state["productos"] = pd.read_csv(ARCHIVO).to_dict("records")
    else:
        st.session_state["productos"] = []
# Inicializar almacenamiento temporal
if "productos" not in st.session_state:
    st.session_state["productos"] = []

# Título e introducción
st.title("🌾 AgroConecta")
st.write("Conecta directamente a campesinos y compradores para reducir el desperdicio de alimentos.")

# Formulario para agregar productos
with st.form("agregar_producto"):
    nombre = st.text_input("Nombre del producto")
    cantidad = st.number_input("Cantidad disponible (kg)", min_value=1)
    precio = st.number_input("Precio por kg (COP)", min_value=100)
    productor = st.text_input("Nombre del productor")
    submit = st.form_submit_button("Agregar producto")

    if submit:
        nuevo = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
            "productor": productor
        }
        st.session_state["productos"].append(nuevo)
        st.success(f"✅ Producto '{nombre}' agregado correctamente")

# Mostrar productos registrados
st.subheader("📦 Productos disponibles")
if len(st.session_state["productos"]) == 0:
    st.info("Aún no hay productos registrados.")
else:
    for p in st.session_state["productos"]:
        st.write(f"**{p['nombre']}** - {p['cantidad']} kg - ${p['precio']} COP/kg - 👨‍🌾 {p['productor']}")
