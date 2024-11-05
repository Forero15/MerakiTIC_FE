import streamlit as st
import requests

def actualizar_departamentos():
    st.header("Actualizar Departamento")
    
    uuid_departamento = st.text_input("Ingresa el UUID del departamento a actualizar:")
    
    # Inicializar variables para los datos del departamento
    nombre_departamento = ""
    
    if st.button("Cargar Datos"):
        try:
            if not uuid_departamento:
                st.warning("Por favor, ingresa un UUID para cargar los datos.")
                return
            
            response = requests.get(f"http://127.0.0.1:8000/departamentos/{uuid_departamento}/")
            if response.status_code == 200:
                departamento = response.json()
                nombre_departamento = departamento.get("nombre_departamento", "")
                st.success("Datos cargados con éxito.")
            else:
                st.error("Error al cargar los datos del departamento. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar cargar los datos: {e}")
    
    nuevo_nombre = st.text_input("Nuevo nombre del departamento:", value=nombre_departamento)
    
    if st.button("Actualizar"):
        try:
            if not uuid_departamento:
                st.warning("Por favor, ingresa un UUID para actualizar el departamento.")
                return
            
            if not nuevo_nombre:
                st.warning("Por favor, ingresa un nuevo nombre para el departamento.")
                return
            
            url = f"http://127.0.0.1:8000/departamentos/{uuid_departamento}/"
            data = {"nombre_departamento": nuevo_nombre}
            response = requests.put(url, json=data)
            
            if response.status_code == 200:
                st.success("Departamento actualizado con éxito.")
            else:
                st.error("Error al actualizar el departamento. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar actualizar el departamento: {e}")
