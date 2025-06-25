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

# st.markdown("""
# <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Stardos+Stencil:wght@700&display=swap" rel="stylesheet">
# <h1 style='text-align: center; font-family: "Stardos Stencil", serif; font-size: 56px; color: white; letter-spacing: 2px;'>
# Flujo de trabajo
# </h1>
# """, unsafe_allow_html=True)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Ultra&display=swap" rel="stylesheet">

<h1 style='font-family: "Ultra", serif; text-align: center; font-size: 56px; color: #D3D3D3;'>
  Flujo de trabajo
</h1>
""", unsafe_allow_html=True)

# st.markdown("<h1 style='text-align: center; color: white;'>Flujo de trabajo</h1>", unsafe_allow_html=True)
with st.container(border=True):
  st.image("data/Flujo_trabajo.png", use_column_width=True)
