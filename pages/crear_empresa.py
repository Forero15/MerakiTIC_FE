import streamlit as st
import requests

def crear_empresa():
    st.header("Crear Empresa")
    
    # Campos para ingresar los datos de la empresa
    nombre_empresa = st.text_input("Nombre de la empresa:")
    email = st.text_input("Email:")
    nit = st.text_input("NIT:")
    numero_contacto = st.text_input("Número de contacto:")
    sede = st.text_input("Sede:")
    
    if st.button("Crear Empresa"):
        empresa_data = {
            "nombre_empresa": nombre_empresa,
            "email": email,
            "nit": nit,
            "numero_contacto": numero_contacto,
            "sede": sede
        }
        
        try:
            response = requests.post("http://127.0.0.1:8000/empresas/", json=empresa_data)
            if response.status_code == 201:
                st.success("Empresa creada exitosamente.")
            else:
                st.error(f"Error al crear la empresa: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar crear la empresa: {e}")