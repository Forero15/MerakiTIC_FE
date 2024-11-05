import streamlit as st
import requests

def actualizar_usuarios():
    st.header("Actualizar Usuario")
    
    uuid_usuario = st.text_input("Ingresa el UUID del usuario a actualizar:")
    
    # Inicializar variables para los datos del usuario
    nombre = ""
    cedula = ""
    correo = ""
    celular = ""
    
    if st.button("Cargar Datos"):
        try:
            if not uuid_usuario:
                st.warning("Por favor, ingresa un UUID para cargar los datos.")
                return
            
            response = requests.get(f"http://127.0.0.1:8000/usuarios/{uuid_usuario}/")
            if response.status_code == 200:
                usuario = response.json()
                nombre = usuario.get("nombre", "")
                cedula = usuario.get("cedula", "")
                correo = usuario.get("correo", "")
                celular = usuario.get("celular", "")
                st.success("Datos cargados con éxito.")
            else:
                st.error("Error al cargar los datos del usuario. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar cargar los datos: {e}")
    
    nuevo_nombre = st.text_input("Nuevo nombre:", value=nombre)
    nuevo_cedula = st.text_input("Nueva cédula:", value=cedula)
    nuevo_correo = st.text_input("Nuevo correo electrónico:", value=correo)
    nuevo_celular = st.text_input("Nuevo número de celular:", value=celular)
    
    if st.button("Actualizar"):
        try:
            if not uuid_usuario:
                st.warning("Por favor, ingresa un UUID para actualizar el usuario.")
                return
            
            if not nuevo_nombre or not nuevo_cedula or not nuevo_correo or not nuevo_celular:
                st.warning("Por favor, completa todos los campos para actualizar el usuario.")
                return
            
            url = f"http://127.0.0.1:8000/usuarios/{uuid_usuario}/"
            data = {
                "nombre": nuevo_nombre,
                "cedula": nuevo_cedula,
                "correo": nuevo_correo,
                "celular": nuevo_celular
            }
            response = requests.put(url, json=data)
            
            if response.status_code == 200:
                st.success("Usuario actualizado con éxito.")
            else:
                st.error("Error al actualizar el usuario. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar actualizar el usuario: {e}")
