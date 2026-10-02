import streamlit as st

st.title("Conversor de temperatura")

modo = st.radio("Selecciona el modo de conversión:", ("Fahrenheit a Celsius", "Celsius a Fahrenheit", "Kelvin a Celsius", "Celsius a kelvin"))
valor = st.number_input("Ingresa el valor a convertir:", value = 0.0)

if modo == "Fahrenheit a Celsius":
    celsius = (valor - 32) * 5/9
    st.write(f"{valor} °F equivalen a {round(celsius, 2)} °C")
elif modo == "Celsius a Fahrenheit":
    fahrenheit = (valor * 9/5) + 32
    st.write(f"{valor} °C equivalen a {round(fahrenheit, 2)} °F")
elif modo == "Kelvin a Celsius":
    celsius = valor - 273.15
    st.write(f"{valor} K equivalen a {round(celsius, 2)} °C")
elif modo == "Celsius a kelvin":
    kelvin = valor + 273.15
    st.write(f"{valor} °C equivalen a {round(kelvin, 2)} K")
