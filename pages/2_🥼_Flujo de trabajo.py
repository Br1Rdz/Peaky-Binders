import streamlit as st

titulo = "Flujo de trabajo"
st.set_page_config(page_title= titulo, 
                    page_icon = "🥼", 
                    layout="wide",
                    initial_sidebar_state = "collapsed",
                    menu_items=None)
#-------- Hide streamlit style ------------    
hide_st_style = '''
                    <style>
                    #Main Menu {visibility:hidden;}
                    footer {visibility:hidden;}
                    header {visibility:hidden;}
                    </style>
    '''
st.markdown(hide_st_style, unsafe_allow_html= True)
st.logo("./Informacion.png", icon_image="./info2.png")

st.markdown("<h1 style='text-align: center; color: white;'>Flujo de trabajo</h1>", unsafe_allow_html=True)

st.image("data/Diagrama.png", use_column_width=True)