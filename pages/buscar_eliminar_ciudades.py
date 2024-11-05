import streamlit as st
import requests

def buscar_eliminar_ciudades():
    st.header("Buscar y Eliminar Ciudades")
    
    uuid_ciudad = st.text_input("Ingresa el UUID de la ciudad a buscar:")
    nombre_ciudad = st.text_input("Ingresa el nombre de la ciudad a buscar:")
    
    if st.button("Buscar"):
        try:
            if uuid_ciudad:
                response = requests.get(f"http://127.0.0.1:8000/ciudades/{uuid_ciudad}/")
                if response.status_code == 200:
                    ciudad = response.json()
                    st.write(f"**ID**: {ciudad['id']}, **Nombre**: {ciudad['nombre_ciudad']}, **Departamento ID**: {ciudad['departamento_id']}")
                else:
                    st.error("No se encontró la ciudad con ese UUID.")
            elif nombre_ciudad:
                response = requests.get(f"http://127.0.0.1:8000/ciudades/?nombre={nombre_ciudad}")
                if response.status_code == 200:
                    ciudades = response.json()
                    for ciudad in ciudades:
                        st.write(f"**ID**: {ciudad['id']}, **Nombre**: {ciudad['nombre_ciudad']}, **Departamento ID**: {ciudad['departamento_id']}")
                else:
                    st.error("No se encontraron ciudades con ese nombre.")
            else:
                st.warning("Por favor, ingresa un UUID o un nombre para buscar.")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar buscar la ciudad: {e}")
    
    if st.button("Eliminar"):
        try:
            if uuid_ciudad:
                response = requests.delete(f"http://127.0.0.1:8000/ciudades/{uuid_ciudad}/")
                if response.status_code == 204:
                    st.success("Ciudad eliminada con éxito.")
                else:
                    st.error("Error al eliminar la ciudad. Código de estado: {}".format(response.status_code))
            else:
                st.warning("Por favor, ingresa un UUID para eliminar la ciudad.")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar eliminar la ciudad: {e}")
