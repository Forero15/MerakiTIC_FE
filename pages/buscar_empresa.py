import streamlit as st
import pandas as pd
import requests

def buscar_empresa():
    st.header("Buscar Empresa")
    
    # Campos para ingresar el nombre de la empresa o el UUID
    nombre_empresa = st.text_input("Ingresa el nombre de la empresa:")
    uuid_empresa = st.text_input("Ingresa el UUID de la empresa:")
    
    # Botón para buscar
    if st.button("Buscar"):
        try:
            # Construir la URL de búsqueda
            if uuid_empresa:
                response = requests.get(f"http://127.0.0.1:8000/empresas/?uuid={uuid_empresa}")
            elif nombre_empresa:
                response = requests.get(f"http://127.0.0.1:8000/empresas/?nombre={nombre_empresa}")
            else:
                st.warning("Por favor, ingresa un nombre de empresa o un UUID para buscar.")
                return
            
            if response.status_code == 200:
                empresas = response.json()
                if empresas:
                    # Mostrar solo el primer resultado encontrado
                    empresa_encontrada = empresas[0]  # Obtener el primer resultado
                    st.json(empresa_encontrada)  # Mostrar el resultado en formato JSON
                else:
                    st.warning("No se encontraron empresas con ese criterio de búsqueda.")
            else:
                st.error("Error al buscar la empresa. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar buscar la empresa: {e}")