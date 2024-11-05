import streamlit as st
import requests
import re

def es_correo_valido(correo):
    # Expresión regular para validar el formato del correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None

def actualizar_empresa():
    st.header("Actualizar Empresa")
    
    # Campo para ingresar el UUID de la empresa a actualizar
    uuid_empresa = st.text_input("Ingresa el UUID de la empresa a actualizar:")
    
    # Inicializar variables para los datos de la empresa
    nombre_empresa = ""
    email_empresa = ""
    nit_empresa = ""
    numero_contacto_empresa = ""
    sede_empresa = False
    
    # Botón para cargar los datos actuales
    if st.button("Cargar Datos"):
        try:
            if not uuid_empresa:
                st.warning("Por favor, ingresa un UUID para cargar los datos.")
                return
            
            # Realizar la solicitud GET para obtener los datos actuales
            response = requests.get(f"http://127.0.0.1:8000/empresas/{uuid_empresa}/")
            
            if response.status_code == 200:
                empresa = response.json()
                # Asignar los datos a las variables
                nombre_empresa = empresa.get("nombre_empresa", "")
                email_empresa = empresa.get("email", "")
                nit_empresa = empresa.get("nit", "")
                numero_contacto_empresa = empresa.get("numero_contacto", "")
                sede_empresa = empresa.get("sede", False)
                
                # Mostrar los datos cargados
                st.success("Datos cargados con éxito.")
            else:
                st.error("Error al cargar los datos de la empresa. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar cargar los datos: {e}")
    
    # Campos para los nuevos datos de la empresa
    nuevo_nombre = st.text_input("Nuevo nombre de la empresa:", value=nombre_empresa)
    nuevo_email = st.text_input("Nuevo email de la empresa:", value=email_empresa)
    nuevo_nit = st.text_input("Nuevo NIT de la empresa:", value=nit_empresa)
    nuevo_numero_contacto = st.text_input("Nuevo número de contacto de la empresa:", value=numero_contacto_empresa)
    nueva_sede = st.checkbox("¿Es sede?", value=sede_empresa)
    
    # Botón para actualizar
    if st.button("Actualizar"):
        try:
            # Verificar que se haya ingresado un UUID
            if not uuid_empresa:
                st.warning("Por favor, ingresa un UUID para actualizar la empresa.")
                return
            
            # Validar que el correo electrónico no esté vacío y sea válido
            if not nuevo_email or not es_correo_valido(nuevo_email):
                st.warning("Por favor, ingresa un correo electrónico válido.")
                return
            
            # Construir la URL de actualización
            url = f"http://127.0.0.1:8000/empresas/{uuid_empresa}/"
            data = {
                "nombre_empresa": nuevo_nombre,
                "email": nuevo_email,
                "nit": nuevo_nit,
                "numero_contacto": nuevo_numero_contacto,
                "sede": nueva_sede
            }
            
            # Realizar la solicitud PUT para actualizar la empresa
            response = requests.put(url, json=data)
            
            if response.status_code == 200:
                st.success("Empresa actualizada con éxito.")
            else:
                # Mostrar el mensaje de error detallado
                error_message = response.json().get("detail", "Error desconocido.")
                st.error(f"Error al actualizar la empresa. Código de estado: {response.status_code}. Detalle: {error_message}")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar actualizar la empresa: {e}")