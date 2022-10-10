from string import hexdigits
import streamlit as st
import datetime
import time
import pandas as pd
import numpy as np
import altair as alt
# Título
st.title('My First Streamlit app')

# Encabezado
st.header("Segunda línea")

# Markdown
st.markdown("Texto normal")

# Texto éxito 
st.success("Lograste hacer tu aplicación")

# Texto error
st.error("Oops ocurrió un error")

# Texto advertencia
st.warning("Parámetros incorrectos")

# Texto Info
st.info("Aviso, parámetros necesarios")

# Excepción
st.exception("Error ")

# Ayuda - documentación de python
st.help(list)

# Escribir
b = 5
st.write("Texto ejemplo")

st.write(b)

# Media

# Imágenes
st.image("https://images.unsplash.com/photo-1661961111247-e218f67d1cd2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1172&q=80")

# Video
st.video("keyboard.mp4")

# Checkbox
st.checkbox("Agregar archivos multimedia")

# Radio button
st.radio("Opciones", ("Opción1", "Opción 2"))

# Select boxes
selected_item = st.selectbox("Opciones ", [1,2,3])
st.write(selected_item)

# Componentes de entrada 
st.header("Componentes de entrada")

# Slider
rango = st.slider("Selecciona el rango:", 1,5)
st.write(rango)

# Botones
if st.button("clicked"):
    st.write("Botón presionado")


# Entrada de texto
info = st.text_input("Ingrese texto", "Ingrese texto...")

# Contraseña
info = st.text_input("Ingrese texto", type="password")

# Área de texto
texto = st.text_area("Ingresar Texto", height= 250)

# Fechas
hoy = st.date_input("Hoy:", datetime.datetime.now())

# Mostrar json
st.json({
    "nombre": "Luis",
    "apellido": "Román",
    "pasatiempo": "Jugar videojuegos"
})

# Mostrar código
st.code("import streamlit")

with st.expander("Clic para expandir:", expanded= False):
    st.code("import streamlit")

# Subir arcahivos

data = st.file_uploader("Subir Imágen", type=["jpg", "JPEG"])

# Spinner - carga
with st.spinner('cargando'):
    time.sleep(5)
    st.success('Done!')

# Barra lateral
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

df1 = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df1)  # Same as st.write(df)

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)


my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)


with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

