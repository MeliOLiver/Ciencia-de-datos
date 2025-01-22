import streamlit as st

def page3():
    st.title("Última Página")
    st.write("Aquí acaban las páginas.")
    
    # Botón para regresar a la página anterior
    if st.button("Ir a la página anterior"):
        st.page_link("/page2")

if __name__ == "__main__":
    page3()
