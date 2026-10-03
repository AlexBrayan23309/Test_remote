import streamlit as st

st.title("Conversor de temperatura")

modo = st.radio("Convertir de:", ["Fahrenheit a Celsius", "Celsius a Fahrenheit", "Kelvin a Celsius", "Celsius a Kelvin"])
valor = st.number_input("Ingresa el valor a convertir:", value = 0.0)

if modo == "Fahrenheit a Celsius":
    resultado = (valor - 32) * 5/9
    st.success(f"**{round(resultado, 2)} °C**")
    st.caption(f"{valor} °F equivalen a {round(resultado, 2)} °C")
elif modo == "Celsius a Fahrenheit":
    resultado = (valor * 9/5) + 32
    st.success(f"**{round(resultado, 2)} °F**")
    st.caption(f"{valor} °C equivalen a {round(resultado, 2)} °F")
elif modo == "Kelvin a Celsius":
    resultado = valor - 273.15
    st.success(f"**{round(resultado, 2)} °C**")
    st.caption(f"{valor} K equivalen a {round(resultado, 2)} °C")
elif modo == "Celsius a Kelvin":
    resultado = valor + 273.15
    st.success(f"**{round(resultado, 2)} K**")
    st.caption(f"{valor} °C equivalen a {round(resultado, 2)} K")

st.caption("Desarrollado por [Alex Brayan] - [900000000]")