import streamlit as st

st.title("Conversor de temperatura")
celsius = st.number_input("Grados Celsius (°C): ", value = 0.0)
fahrenheit = (celsius *9/5) + 32
st.write(f"{celsius} °C equivalen a {fahrenheit:.2f} °F")