import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="BIOFARMERS", page_icon="🌽")
ARCHIVO = "productos.csv"

# Cargar productos si existe el archivo
if "productos" not in st.session_state:
    if os.path.exists(ARCHIVO):
        st.session_state["products"] = pd.read_csv(ARCHIVO).to_dict("records")
    else:
        st.session_state["products"] = []


# Título e introducción
st.title("🌾 BIOFARMERS")
st.write("Conecta directamente a campesinos y compradores para reducir el desperdicio de alimentos.")

# Formulario para agregar productos
with st.form("agregar_product"):
    nombre = st.text_input("Name of product")
    cantidad = st.number_input("available quantity  (kg)", min_value=1)
    precio = st.number_input("Price for kg (COP)", min_value=100)
    productor = st.text_input("Name of productor")
    submit = st.form_submit_button("Add producto")

    if submit:
        nuevo = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
            "productor": productor
        }
        st.session_state["products"].append(nuevo)
        st.success(f"✅ Producto '{nombre}' agregado correctamente")
 # 🔥 Guardar productos en CSV para persistencia
        pd.DataFrame(st.session_state["products"]).to_csv(ARCHIVO, index=False)
# Mostrar productos registrados
st.subheader("📦 Productos disponibles")
if len(st.session_state["products"]) == 0:
    st.info("Aún no hay productos registrados.")
else:
    for p in st.session_state["products"]:
        st.write(f"**{p['nombre']}** - {p['cantidad']} kg - ${p['precio']} COP/kg - 👨‍🌾 {p['productor']}")
if submit:
    nuevo = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
        "productor": productor
    }
    st.session_state["products"].append(nuevo)
    pd.DataFrame(st.session_state["productos"]).to_csv(ARCHIVO, index=False)  # 💾 Guarda el archivo
    st.success(f"✅ Producto '{nombre}' agregado correctamente")
