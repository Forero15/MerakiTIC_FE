import streamlit as st
import pandas as pd
import requests

def listar_empresas():
    # Título de la página
    st.header("Lista de Empresas")

    # Estilo de la página
    st.markdown("""
    <style>
        .header {
            text-align: center;
            color: #4CAF50;
            font-size: 40px;
            font-weight: bold;
        }
        .table {
            border-collapse: collapse;
            width: 100%;
        }
        .table th, .table td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        .table th {
            background-color: #4CAF50;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

    # Sección para listar empresas
    st.header("Empresas Registradas")
    try:
        response = requests.get("http://127.0.0.1:8000/empresas/")
        if response.status_code == 200:
            df_empresas = pd.DataFrame(response.json())
            st.table(df_empresas.style.set_table_attributes('class="table"'))
        else:
            st.error("Error al obtener la lista de empresas. Código de estado: {}".format(response.status_code))
    except Exception as e:
        st.error(f"Ocurrió un error al intentar obtener las empresas: {e}")