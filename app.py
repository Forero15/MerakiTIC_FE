import streamlit as st

# Título de la aplicación
st.title("Meraki TIC")

# Menú de navegación
st.sidebar.title("Navegación")
page = st.sidebar.selectbox("Selecciona una opción:", 
                             ["Listar Empresas", 
                              "Cargar Empresas", 
                              "Buscar Empresa", 
                              "Crear Empresa", 
                              "Actualizar Empresa",
                              "Listar Departamentos", 
                              "Cargar Departamentos", 
                              "Buscar y Eliminar Departamentos", 
                              "Actualizar Departamentos",
                              "Listar Ciudades", 
                              "Cargar Ciudades", 
                              "Buscar y Eliminar Ciudades", 
                              "Actualizar Ciudades",
                              "Listar Sedes", 
                              "Cargar Sedes", 
                              "Buscar y Eliminar Sedes", 
                              "Actualizar Sedes",
                              "Listar Impresoras", 
                              "Cargar Impresoras", 
                              "Buscar y Eliminar Impresoras", 
                              "Actualizar Impresoras",
                              "Listar Tóners", 
                              "Cargar Tóners", 
                              "Buscar y Eliminar Tóners", 
                              "Actualizar Tóners",
                              "Listar Usuarios", 
                              "Crear Usuarios", 
                              "Buscar y Eliminar Usuarios", 
                              "Actualizar Usuarios"])

# Mostrar la página correspondiente
if page == "Listar Empresas":
    from pages.listar_empresas import listar_empresas
    listar_empresas()
elif page == "Cargar Empresas":
    from pages.cargar_empresas import cargar_empresas
    cargar_empresas()
elif page == "Buscar Empresa":
    from pages.buscar_empresa import buscar_empresa
    buscar_empresa()
elif page == "Crear Empresa":
    from pages.crear_empresa import crear_empresa
    crear_empresa()
elif page == "Actualizar Empresa":
    from pages.actualizar_empresa import actualizar_empresa
    actualizar_empresa()
elif page == "Listar Departamentos":
    from pages.listar_departamentos import listar_departamentos
    listar_departamentos()
elif page == "Cargar Departamentos":
    from pages.cargar_departamentos import cargar_departamentos
    cargar_departamentos()
elif page == "Buscar y Eliminar Departamentos":
    from pages.buscar_eliminar_departamentos import buscar_eliminar_departamentos
    buscar_eliminar_departamentos()
elif page == "Actualizar Departamentos":
    from pages.actualizar_departamentos import actualizar_departamentos
    actualizar_departamentos()
elif page == "Listar Ciudades":
    from pages.listar_ciudades import listar_ciudades
    listar_ciudades()
elif page == "Cargar Ciudades":
    from pages.cargar_ciudades import cargar_ciudades
    cargar_ciudades()
elif page == "Buscar y Eliminar Ciudades":
    from pages.buscar_eliminar_ciudades import buscar_eliminar_ciudades
    buscar_eliminar_ciudades()
elif page == "Actualizar Ciudades":
    from pages.actualizar_ciudades import actualizar_ciudades
    actualizar_ciudades()
elif page == "Listar Sedes":
    from pages.listar_sedes import listar_sedes
    listar_sedes()
elif page == "Cargar Sedes":
    from pages.cargar_sedes import cargar_sedes
    cargar_sedes()
elif page == "Buscar y Eliminar Sedes":
    from pages.buscar_eliminar_sedes import buscar_eliminar_sedes
    buscar_eliminar_sedes()
elif page == "Actualizar Sedes":
    from pages.actualizar_sedes import actualizar_sedes
    actualizar_sedes()
elif page == "Listar Impresoras":
    from pages.listar_impresoras import listar_impresoras
    listar_impresoras()
elif page == "Cargar Impresoras":
    from pages.cargar_impresoras import cargar_impresoras
    cargar_impresoras()
elif page == "Buscar y Eliminar Impresoras":
    from pages.buscar_eliminar_impresoras import buscar_eliminar_impresoras
    buscar_eliminar_impresoras()
elif page == "Actualizar Impresoras":
    from pages.actualizar_impresoras import actualizar_impresoras
    actualizar_impresoras()
elif page == "Listar Tóners":
    from pages.listar_toners import listar_toners
    listar_toners()
elif page == "Cargar Tóners":
    from pages.cargar_toners import cargar_toners
    cargar_toners()
elif page == "Buscar y Eliminar Tóners":
    from pages.buscar_eliminar_toners import buscar_eliminar_toners
    buscar_eliminar_toners()
elif page == "Actualizar Tóners":
    from pages.actualizar_toners import actualizar_toners
    actualizar_toners()
elif page == "Listar Usuarios":
    from pages.listar_usuarios import listar_usuarios
    listar_usuarios()
elif page == "Crear Usuarios":
    from pages.crear_usuarios import crear_usuarios
    crear_usuarios()
elif page == "Buscar y Eliminar Usuarios":
    from pages.buscar_eliminar_usuarios import buscar_eliminar_usuarios
    buscar_eliminar_usuarios()
elif page == "Actualizar Usuarios":
    from pages.actualizar_usuarios import actualizar_usuarios
    actualizar_usuarios()