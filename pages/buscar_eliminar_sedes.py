import streamlit as st
import requests

def buscar_eliminar_sedes():
    st.header("Buscar y Eliminar Sedes")
    
    uuid_sede = st.text_input("Ingresa el UUID de la sede a buscar:")
    nombre_sede = st.text_input("Ingresa el nombre de la sede a buscar:")
    
    if st.button("Buscar"):
        try:
            if uuid_sede:
                response = requests.get(f"http://127.0.0.1:8000/sedes/{uuid_sede}/")
                if response.status_code == 200:
                    sede = response.json()
                    st.write(f"**ID**: {sede['id']}, **Nombre**: {sede['nombre_sede']}, **Email**: {sede['email']}, **Número de Contacto**: {sede['numero_contacto']}, **Departamento ID**: {sede['departamento_id']}, **Ciudad ID**: {sede['ciudad_id']}")
                else:
                    st.error("No se encontró la sede con ese UUID.")
            elif nombre_sede:
                response = requests.get(f"http://127.0.0.1:8000/sedes/?nombre={nombre_sede}")
                if response.status_code == 200:
                    sedes = response.json()
                    for sede in sedes:
                        st.write(f"**ID**: {sede['id']}, **Nombre**: {sede['nombre_sede']}, **Email**: {sede['email']}, **Número de Contacto**: {sede['numero_contacto']}, **Departamento ID**: {sede['departamento_id']}, **Ciudad ID**: {sede['ciudad_id']}")
                else:
                    st.error("No se encontraron sedes con ese nombre.")
            else:
                st.warning("Por favor, ingresa un UUID o un nombre para buscar.")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar buscar la sede: {e}")
    
    if st.button("Eliminar"):
        try:
            if uuid_sede:
                response = requests.delete(f"http://127.0.0.1:8000/sedes/{uuid_sede}/")
                if response.status_code == 204:
                    st.success("Sede eliminada con éxito.")
                else:
                    st.error("Error al eliminar la sede. Código de estado: {}".format(response.status_code))
            else:
                st.warning("Por favor, ingresa un UUID para eliminar la sede.")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar eliminar la sede: {e}")
