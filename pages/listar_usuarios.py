import streamlit as st
import pandas as pd
import requests

def listar_usuarios():
    # Título de la página
    st.header("Lista de Usuarios")

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

    # Sección para listar usuarios
    st.header("Usuarios Registrados")
