import streamlit as st
import requests

def actualizar_impresoras():
    st.header("Actualizar Impresora")
    
    uuid_impresora = st.text_input("Ingresa el UUID de la impresora a actualizar:")
    
    # Inicializar variables para los datos de la impresora
    serial = ""
    modelo = ""
    marca = ""
    estado = ""
    empresa_id = ""
    sede_id = ""
    
    if st.button("Cargar Datos"):
        try:
            if not uuid_impresora:
                st.warning("Por favor, ingresa un UUID para cargar los datos.")
                return
            
            response = requests.get(f"http://127.0.0.1:8000/impresoras/{uuid_impresora}/")
            if response.status_code == 200:
                impresora = response.json()
                serial = impresora.get("serial", "")
                modelo = impresora.get("modelo", "")
                marca = impresora.get("marca", "")
                estado = impresora.get("estado", "")
                empresa_id = impresora.get("empresa_id", "")
                sede_id = impresora.get("sede_id", "")
                st.success("Datos cargados con éxito.")
            else:
                st.error("Error al cargar los datos de la impresora. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar cargar los datos: {e}")
    
    nuevo_serial = st.text_input("Nuevo serial de la impresora:", value=serial)
    nuevo_modelo = st.text_input("Nuevo modelo de la impresora:", value=modelo)
    nuevo_marca = st.text_input("Nueva marca de la impresora:", value=marca)
    nuevo_estado = st.selectbox("Nuevo estado de la impresora:", ["Asignada", "Disponible"], index=0 if estado == "Asignada" else 1)
    nuevo_empresa_id = st.text_input("Nuevo ID de empresa:", value=empresa_id)
    nuevo_sede_id = st.text_input("Nuevo ID de sede:", value=sede_id)
    
    if st.button("Actualizar"):
        try:
            if not uuid_impresora:
                st.warning("Por favor, ingresa un UUID para actualizar la impresora.")
                return
            
            if not nuevo_serial or not nuevo_modelo or not nuevo_marca or not nuevo_estado or not nuevo_empresa_id or not nuevo_sede_id:
                st.warning("Por favor, completa todos los campos para actualizar la impresora.")
                return
            
            url = f"http://127.0.0.1:8000/impresoras/{uuid_impresora}/"
            data = {
                "serial": nuevo_serial,
                "modelo": nuevo_modelo,
                "marca": nuevo_marca,
                "estado": nuevo_estado,
                "empresa_id": nuevo_empresa_id,
                "sede_id": nuevo_sede_id
            }
            response = requests.put(url, json=data)
            
            if response.status_code == 200:
                st.success("Impresora actualizada con éxito.")
            else:
                st.error("Error al actualizar la impresora. Código de estado: {}".format(response.status_code))
        except Exception as e:
            st.error(f"Ocurrió un error al intentar actualizar la impresora: {e}")
