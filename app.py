import streamlit as st

st.title("Conversor de temperatura")

modo = st.radio("Selecciona el modo de conversión:", ("Fahrenheit a Celsius", "Celsius a Fahrenheit"))
valor = st.number_input("Ingresa el valor a convertir:", value = 0.0)

if modo == "Fahrenheit a Celsius":
    celsius = (valor - 32) * 5/9
    st.write(f"{valor} °F equivalen a {round(celsius, 2)} °C")
else:
    fahrenheit = (valor * 9/5) + 32
    st.write(f"{valor} °C equivalen a {round(fahrenheit, 2)} °F")
