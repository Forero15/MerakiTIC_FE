import streamlit as st
import requests

def actualizar_ciudades():
    st.header("Actualizar Ciudad")
    
    uuid_ciudad = st.text_input("Ingresa el UUID de la ciudad a actualizar:")
    
    # Inicializar variables para los datos de la ciudad
    nombre_ciudad = ""
    departamento_id = ""
    
    if st.button("Cargar Datos"):
        try:
            if not uuid_ciudad:
                st.warning("Por favor, ingresa un UUID para cargar los datos.")
                return
            
            response = requests.get(f"http://127.0.0.1:8000/ciudades/{uuid_ciudad}/")
            if response.status_code == 200:
                ciudad = response.json()
                nombre_ciudad = ciudad.get("nombre_ciudad", "")
                departamento_id = ciudad.get("departamento_id", "")
                st.success("Datos cargados con éxito.")
            else:
                st.error("Error al cargar los datos de la ciudad. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar cargar los datos: {e}")
    
    nuevo_nombre = st.text_input("Nuevo nombre de la ciudad:", value=nombre_ciudad)
    nuevo_departamento_id = st.text_input("Nuevo ID de departamento:", value=departamento_id)
    
    if st.button("Actualizar"):
        try:
            if not uuid_ciudad:
                st.warning("Por favor, ingresa un UUID para actualizar la ciudad.")
                return
            
            if not nuevo_nombre or not nuevo_departamento_id:
                st.warning("Por favor, ingresa un nuevo nombre y un nuevo ID de departamento para la ciudad.")
                return
            
            url = f"http://127.0.0.1:8000/ciudades/{uuid_ciudad}/"
            data = {
                "nombre_ciudad": nuevo_nombre,
                "departamento_id": nuevo_departamento_id
            }
            response = requests.put(url, json=data)
            
            if response.status_code == 200:
                st.success("Ciudad actualizada con éxito.")
            else:
                st.error("Error al actualizar la ciudad. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar actualizar la ciudad: {e}")
