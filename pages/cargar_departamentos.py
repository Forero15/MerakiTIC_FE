import streamlit as st
import pandas as pd
import requests

def cargar_departamentos():
    st.header("Cargar Departamentos en Bulk")
    
    uploaded_file = st.file_uploader("Selecciona un archivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Leer el archivo CSV
            df = pd.read_csv(uploaded_file)
            # Asegurarse de que el DataFrame tenga las columnas necesarias
            if 'nombre_departamento' not in df.columns:
                st.error("El archivo CSV debe contener una columna llamada 'nombre_departamento'.")
                return
            
            # Cargar cada departamento
            for index, row in df.iterrows():
                data = {"nombre_departamento": row['nombre_departamento']}
                response = requests.post("http://127.0.0.1:8000/departamentos/", json=data)
                if response.status_code == 201:
                    st.success(f"Departamento '{row['nombre_departamento']}' cargado con éxito.")
                else:
                    st.error(f"Error al cargar el departamento '{row['nombre_departamento']}'. Código de estado: {response.status_code}")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar cargar los departamentos: {e}")
