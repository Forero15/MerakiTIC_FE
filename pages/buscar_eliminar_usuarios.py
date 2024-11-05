import streamlit as st
import requests

def buscar_eliminar_usuarios():
    st.header("Buscar y Eliminar Usuarios")
    
    uuid_usuario = st.text_input("Ingresa el UUID del usuario a buscar:")
    cedula_usuario = st.text_input("Ingresa la cédula del usuario a buscar:")
    
    if st.button("Buscar"):
        try:
            if uuid_usuario:
                response = requests.get(f"http://127.0.0.1:8000/usuarios/{uuid_usuario}/")
                if response.status_code == 200:
                    usuario = response.json()
                    st.write(f"**ID**: {usuario['id']}, **Nombre**: {usuario['nombre']}, **Cédula**: {usuario['cedula']}, **Correo**: {usuario['correo']}, **Celular**: {usuario['celular']}")
                else:
                    st.error("No se encontró el usuario con ese UUID.")
            elif cedula_usuario:
                response = requests.get(f"http://127.0.0.1:8000/usuarios/?cedula={cedula_usuario}")
                if response.status_code == 200:
                    usuarios = response.json()
                    for usuario in usuarios:
                        st.write(f"**ID**: {usuario['id']}, **Nombre**: {usuario['nombre']}, **Cédula**: {usuario['cedula']}, **Correo**: {usuario['correo']}, **Celular**: {usuario['celular']}")
                else:
                    st.error("No se encontraron usuarios con esa cédula.")
            else:
                st.warning("Por favor, ingresa un UUID o una cédula para buscar.")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar buscar el usuario: {e}")
    
    if st.button("Eliminar"):
        try:
            if uuid_usuario:
                response = requests.delete(f"http://127.0.0.1:8000/usuarios/{uuid_usuario}/")
                if response.status_code == 204:
                    st.success("Usuario eliminado con éxito.")
                else:
                    st.error("Error al eliminar el usuario. Código de estado: {}".format(response.status_code))
            else:
                st.warning("Por favor, ingresa un UUID para eliminar el usuario.")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar eliminar el usuario: {e}")
