import streamlit as st
import requests

def buscar_eliminar_departamentos():
    st.header("Buscar y Eliminar Departamentos")
    
    uuid_departamento = st.text_input("Ingresa el UUID del departamento a buscar:")
    nombre_departamento = st.text_input("Ingresa el nombre del departamento a buscar:")
    
    if st.button("Buscar"):
        try:
            if uuid_departamento:
                response = requests.get(f"http://127.0.0.1:8000/departamentos/{uuid_departamento}/")
                if response.status_code == 200:
                    departamento = response.json()
                    st.write(f"**ID**: {departamento['id']}, **Nombre**: {departamento['nombre_departamento']}")
                else:
                    st.error("No se encontró el departamento con ese UUID.")
            elif nombre_departamento:
                response = requests.get(f"http://127.0.0.1:8000/departamentos/?nombre={nombre_departamento}")
                if response.status_code == 200:
                    departamentos = response.json()
                    for departamento in departamentos:
                        st.write(f"**ID**: {departamento['id']}, **Nombre**: {departamento['nombre_departamento']}")
                else:
                    st.error("No se encontraron departamentos con ese nombre.")
            else:
                st.warning("Por favor, ingresa un UUID o un nombre para buscar.")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar buscar el departamento: {e}")
    
    if st.button("Eliminar"):
        try:
            if uuid_departamento:
                response = requests.delete(f"http://127.0.0.1:8000/departamentos/{uuid_departamento}/")
                if response.status_code == 204:
                    st.success("Departamento eliminado con éxito.")
                else:
                    st.error("Error al eliminar el departamento. Código de estado: {}".format(response.status_code))
            else:
                st.warning("Por favor, ingresa un UUID para eliminar el departamento.")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar eliminar el departamento: {e}")
