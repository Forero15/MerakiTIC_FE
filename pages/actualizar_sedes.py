import streamlit as st
import requests

def actualizar_sedes():
    st.header("Actualizar Sede")
    
    uuid_sede = st.text_input("Ingresa el UUID de la sede a actualizar:")
    
    # Inicializar variables para los datos de la sede
    nombre_sede = ""
    email = ""
    numero_contacto = ""
    departamento_id = ""
    ciudad_id = ""
    
    if st.button("Cargar Datos"):
        try:
            if not uuid_sede:
                st.warning("Por favor, ingresa un UUID para cargar los datos.")
                return
            
            response = requests.get(f"http://127.0.0.1:8000/sedes/{uuid_sede}/")
            if response.status_code == 200:
                sede = response.json()
                nombre_sede = sede.get("nombre_sede", "")
                email = sede.get("email", "")
                numero_contacto = sede.get("numero_contacto", "")
                departamento_id = sede.get("departamento_id", "")
                ciudad_id = sede.get("ciudad_id", "")
                st.success("Datos cargados con éxito.")
            else:
                st.error("Error al cargar los datos de la sede. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar cargar los datos: {e}")
    
    nuevo_nombre = st.text_input("Nuevo nombre de la sede:", value=nombre_sede)
    nuevo_email = st.text_input("Nuevo email de la sede:", value=email)
    nuevo_numero_contacto = st.text_input("Nuevo número de contacto:", value=numero_contacto)
    nuevo_departamento_id = st.text_input("Nuevo ID de departamento:", value=departamento_id)
    nuevo_ciudad_id = st.text_input("Nuevo ID de ciudad:", value=ciudad_id)
    
    if st.button("Actualizar"):
        try:
            if not uuid_sede:
                st.warning("Por favor, ingresa un UUID para actualizar la sede.")
                return
            
            if not nuevo_nombre or not nuevo_email or not nuevo_numero_contacto or not nuevo_departamento_id or not nuevo_ciudad_id:
                st.warning("Por favor, completa todos los campos para actualizar la sede.")
                return
            
            url = f"http://127.0.0.1:8000/sedes/{uuid_sede}/"
            data = {
                "nombre_sede": nuevo_nombre,
                "email": nuevo_email,
                "numero_contacto": nuevo_numero_contacto,
                "departamento_id": nuevo_departamento_id,
                "ciudad_id": nuevo_ciudad_id
            }
            response = requests.put(url, json=data)
            
            if response.status_code == 200:
                st.success("Sede actualizada con éxito.")
            else:
                st.error("Error al actualizar la sede. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar actualizar la sede: {e}")
