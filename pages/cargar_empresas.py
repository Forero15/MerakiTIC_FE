import streamlit as st
import pandas as pd
import requests

def cargar_empresas():  # Asegúrate de que esta función esté definida
    st.header("Cargar Empresas")  # Agrega un encabezado para la página

    # Cargar el archivo CSV a través de Streamlit
    uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")

    if uploaded_file is not None:
        # Mostrar el botón solo si se ha cargado un archivo
        if st.button("Cargar Empresas"):
            # Crear un diccionario para el formato requerido
            empresas_data = {"empresas": []}
            df_empresas = pd.read_csv(uploaded_file)  # Cargar el DataFrame desde el archivo subido

            for index, row in df_empresas.iterrows():
                # Asegúrate de que las columnas del CSV coincidan con el esquema
                empresa_data = {
                    "nombre_empresa": row["nombre_empresa"],
                    "email": row["email"],
                    "nit": str(row["nit"]),  # Convertir a string
                    "numero_contacto": str(row["numero_contacto"]),  # Convertir a string
                    "sede": row["sede"]
                }
                empresas_data["empresas"].append(empresa_data)

            # Enviar los datos a la API
            try:
                response = requests.post("http://127.0.0.1:8000/empresas/bulk/", json=empresas_data)
                if response.status_code == 200:  # Cambia 201 a 200
                    st.success("Empresas cargadas exitosamente.")
                else:
                    st.error(f"Error al cargar las empresas: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Ocurrió un error al intentar cargar las empresas: {e}")
    else:
        st.info("Por favor, carga un archivo CSV para continuar.")  # Mensaje informativo si no se ha cargado un archivo