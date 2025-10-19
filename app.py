import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="Biofarmers", page_icon="🌽")
ARCHIVO = "productos.csv"

# Cargar productos si existe el archivo
if "productos" not in st.session_state:
    if os.path.exists(ARCHIVO):
        st.session_state["productos"] = pd.read_csv(ARCHIVO).to_dict("records")
    else:
        st.session_state["products"] = []


# Título e introducción
st.title("🌾 Biofarmers")
st.write("Conecta directamente a campesinos y compradores para reducir el desperdicio de alimentos.")

# Formulario para agregar productos
with st.form("add_product"):
    nombre = st.text_input("name of producto")
    cantidad = st.number_input("available quantity (kg)", min_value=1)
    precio = st.number_input("Price for kg (COP)", min_value=100)
    productor = st.text_input("name of product")
    submit = st.form_submit_button("add product")

    if submit:
        nuevo = {
            "nombre": name,
            "cantidad": quantity,
            "precio": price,
            "productor": product
        }
        st.session_state["products"].append(nuevo)
        st.success(f"✅ Product '{name}' agregado correctamente")
 # 🔥 Guardar productos en CSV para persistencia
        pd.DataFrame(st.session_state["products"]).to_csv(ARCHIVO, index=False)
# Mostrar productos registrados
st.subheader("📦 available Products")
if len(st.session_state["products"]) == 0:
    st.info("Aún no hay productos registrados.")
else:
    for p in st.session_state["products"]:
        st.write(f"**{p['name']}** - {p['quantity']} kg - ${p['price']} COP/kg - 👨‍🌾 {p['product']}")
if submit:
    nuevo = {
        "nombre": name,
        "cantidad": quantity,
        "precio": price,
        "productor": product
    }
    st.session_state["products"].append(nuevo)
    pd.DataFrame(st.session_state["products"]).to_csv(ARCHIVO, index=False)  # 💾 Guarda el archivo
    st.success(f"✅ Producto '{name}' agregado correctamente")
