import streamlit as st
import streamlit.components.v1 as components

titulo = "Conclucion"
st.set_page_config(page_title= titulo, 
                    page_icon = "🤔", 
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

st.markdown("<h1 style='text-align: center; color: white;'>Conclusión</h1>", unsafe_allow_html=True)

# Reproduce pero oculto con CSS
st.markdown("""
    <style>
        audio {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
st.audio('data/finish2.mp3', autoplay=True)

st.markdown(
    """
        <div style="text-align: justify;">
        <li>
        De un total de 7,491 y 15,676 picos analizados para las condiciones D0 y D12, respectivamente,
        solo 1,390 mostraron diferencias significativas entre ambas condiciones (<span style="color:orange;">289 incrementados, 234 conservados y 867 reducidos</span>),
        lo cual evidencia una dinámica importante en la accesibilidad cromatínica durante este periodo. 
        (<span style="color:#04fcb5;"><em>Fig. 1. Mapa de calor entre D0 y D12 para ATAC-seq</em></span>)
        </li>
        <br>
        <li>
        Se observaron diferencias relevantes entre la anotación de picos de <span style="color:#e74c3c;">ATAC-seq</span> y <span style="color:#42c106;">ChIP-seq</span>.
        Particularmente, los <span style="color:orange;">sitios intergénicos distales y las regiones intrónicas</span> mostraron un mayor porcentaje
        de asociación con posibles funciones reguladoras de genes cercanos. 
        (<span style="color:#04fcb5;"><em>Fig. 2. Anotación comparativa de picos ATAC-seq vs ChIP-seq</em></span>).
        </li>
        <br>
        <li>
        El análisis de motivos resaltó la presencia de sitios de unión para factores del linaje <span style="color:orange;">GATA</span>,
        conocidos por su papel esencial en el desarrollo y diferenciación de linajes hematopoyéticos,
        especialmente en eritroides y megacariocitos. 
        (<span style="color:#04fcb5;"><em>Fig. 3. Análisis de motivos en ATAC-seq y ChIP-seq</em></span>).
        </li>
        <br>
        <li>
        La ontología génica indicó que los genes <span style="color:orange;">SREBF2, DEPDC5, RBX1, TXNRD2, MED15, TANGO2 y TXN2</span> están asociados
        con el síndrome por variación en el número de copias 22q11.2, condición relacionada con el síndrome velocardiofacial,
        caracterizado por disfunción faríngea, anomalías cardíacas y dismorfismo facial. 
        (<span style="color:#04fcb5;"><em>Fig. 4. Ontología génica</em></span>).
        </li>
        <br>
        <li>
        Se identificaron regiones compartidas entre <span style="color:#e74c3c;">ATAC-seq</span> y <span style="color:#42c106;">ChIP-seq</span>, ubicadas en los genes <span style="color:orange;"><em>RBX1, TXNRD2, TANGO2 y TXN2</em></span>.
        Estas regiones se presentaron en los intrones de los genes lo cual podría tener un rol regulador en la expresión de dichos genes.
        Sin embargo, para probar esto es necesario la integración de datos de RNA-seq. 
        (<span style="color:#04fcb5;"><em>Fig. 5. Volcanoplot y Gráfico de señales</em></span>).
        </li>
        </div>
    """, unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; font-size: 25px; color: white;'>✨Gracias por tu apoyo✨</h1>",
             unsafe_allow_html=True)
# st.markdown("<h1 style='text-align: center; font-size: 15px; color: white;'><em>...Yo sé lo que quiero, el chiste es que los demás lo averigüen...</em></h1>",
#              unsafe_allow_html=True)