import streamlit as st
import requests

def actualizar_toners():
    st.header("Actualizar Tóner")
    
    uuid_toner = st.text_input("Ingresa el UUID del tóner a actualizar:")
    
    # Inicializar variables para los datos del tóner
    referencia = ""
    estado = ""
    empresa_id = ""
    sede_id = ""
    
    if st.button("Cargar Datos"):
        try:
            if not uuid_toner:
                st.warning("Por favor, ingresa un UUID para cargar los datos.")
                return
            
            response = requests.get(f"http://127.0.0.1:8000/toners/{uuid_toner}/")
            if response.status_code == 200:
                toner = response.json()
                referencia = toner.get("referencia", "")
                estado = toner.get("estado", "")
                empresa_id = toner.get("empresa_id", "")
                sede_id = toner.get("sede_id", "")
                st.success("Datos cargados con éxito.")
            else:
                st.error("Error al cargar los datos del tóner. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar cargar los datos: {e}")
    
    nuevo_referencia = st.text_input("Nueva referencia del tóner:", value=referencia)
    nuevo_estado = st.selectbox("Nuevo estado del tóner:", ["Asignado", "Disponible", "En Recarga"], index=0 if estado == "Asignado" else (1 if estado == "Disponible" else 2))
    nuevo_empresa_id = st.text_input("Nuevo ID de empresa:", value=empresa_id)
    nuevo_sede_id = st.text_input("Nuevo ID de sede:", value=sede_id)
    
    if st.button("Actualizar"):
        try:
            if not uuid_toner:
                st.warning("Por favor, ingresa un UUID para actualizar el tóner.")
                return
            
            if not nuevo_referencia or not nuevo_estado or not nuevo_empresa_id or not nuevo_sede_id:
                st.warning("Por favor, completa todos los campos para actualizar el tóner.")
                return
            
            url = f"http://127.0.0.1:8000/toners/{uuid_toner}/"
            data = {
                "referencia": nuevo_referencia,
                "estado": nuevo_estado,
                "empresa_id": nuevo_empresa_id,
                "sede_id": nuevo_sede_id
            }
            response = requests.put(url, json=data)
            
            if response.status_code == 200:
                st.success("Tóner actualizado con éxito.")
            else:
                st.error("Error al actualizar el tóner. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar actualizar el tóner: {e}")
