import streamlit as st
import requests

def crear_usuarios():
    st.header("Crear Usuario")
    
    nombre = st.text_input("Nombre completo:")
    cedula = st.text_input("Cédula:")
    correo = st.text_input("Correo electrónico:")
    celular = st.text_input("Número de celular:")
    contraseña = st.text_input("Contraseña:", type="password")
    
    if st.button("Crear Usuario"):
        if nombre and cedula and correo and celular and contraseña:
            data = {
                "nombre": nombre,
                "cedula": cedula,
                "correo": correo,
                "celular": celular,
                "contraseña": contraseña
            }
            response = requests.post("http://127.0.0.1:8000/usuarios/", json=data)
            if response.status_code == 201:
                st.success("Usuario creado con éxito.")
            else:
                st.error(f"Error al crear el usuario. Código de estado: {response.status_code}")
        else:
            st.warning("Por favor, completa todos los campos.")
