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
            <ul>
                <li>
                De un total de 7,491 y 15,676 picos analizados para las condiciones D0 y D12, respectivamente,
                solo 1,390 mostraron diferencias significativas entre ambas condiciones (<span style="color:orange;">289 incrementados, 234 conservados y 867 reducidos</span>),
                lo cual evidencia una dinámica importante en la accesibilidad cromatínica durante este periodo. 
                (<span style="color:#04fcb5;"><em>Fig. 1. Mapa de calor entre D0 y D12 para ATAC-seq</em></span>)
                </li>
                <br>
                <li>
                Se observaron diferencias relevantes entre la anotación de picos de <span style="color:orange;">ATAC-seq, GATA1, H3K27ac y H3K27me3</span>.
                Particularmente, los <span style="color:orange;">sitios intergénicos distales y las regiones intrónicas</span> mostraron un mayor porcentaje
                de asociación con posibles funciones reguladoras de genes cercanos. 
                (<span style="color:#04fcb5;"><em>Fig. 2. Anotacion de picos</em></span>).
                </li>
                <br>
                <li>
                El análisis de motivos resaltó la presencia de sitios de unión para factores del linaje <span style="color:orange;">GATA</span>,
                conocidos por su papel esencial en el desarrollo y diferenciación de linajes hematopoyéticos,
                especialmente en eritroides y megacariocitos. 
                (<span style="color:#04fcb5;"><em>Fig. 3. Análisis de Motivos</em></span>).
                </li>
                <br>
                <li>
                La ontología génica indicó que los genes <span style="color:orange;">SREBF2, DEPDC5, RBX1, TXNRD2, MED15, TANGO2 y TXN2</span> están asociados
                con el síndrome por variación en el número de copias 22q11.2, condición relacionada con el síndrome velocardiofacial,
                caracterizado por disfunción faríngea, anomalías cardíacas y dismorfismo facial.
                Aunque este análisis se enfocó únicamente en el cromosoma 22 y las muestras utilizadas no presentan dicha condición genética,
                los resultados sugieren que los mecanismos reguladores implicados en el desarrollo hematopoyético comparten vías funcionales clave
                con aquellas alteradas en este síndrome. Esto refuerza la idea de que genes con síndrome por variación en el número de copias 22q11.2 cumplen funciones
                esenciales en procesos celulares que van más allá de contextos patológicos. (<span style="color:#04fcb5;"><em>Fig. 4. Grafico de ontología génica</em></span>)
                </li>
                <br>
                <li>
                Se identificaron regiones compartidas entre <span style="color:orange;">ATAC-seq (D12), GATA1 y H3K27ac en los genes DEPDC5, RBX1, MED15, TANGO2 y TXN2</span>,
                lo cual sugiere que estas regiones podrían estar funcionalmente activas en la transcripción durante el día 12 de diferenciación
                hematopoyética. Por otro lado, genes como <span style="color:orange;">SREBF2 y TXNRD2 presentaron señal combinada en ATAC-seq (D0 y D12), así como en H3K27ac,
                H3K27me3 y GATA1</span>, lo que sugiere que estas regiones podrían encontrarse en un estado bivalente, es decir, “preparadas” para activarse
                o reprimirse en función de las señales de diferenciación celular. No obstante, para validar esta hipótesis es necesaria
                la integración de datos de expresión génica, como <span style="color:red;"><strong>RNA-seq</strong></span>, que permita confirmar si estos cambios epigenéticos
                se reflejan en la activación o silenciamiento de los genes implicados.
                (<span style="color:#04fcb5;"><em>Fig. 5. Volcanoplot y Gráfico de señales</em></span>).
                </li>
            </ul>     
            <br>
                <ul>
                    <li>
                    Como hemos visto, el análisis bioinformático de ATAC-seq y ChIP-seq permite reducir y organizar
                    la información generada por la secuenciación de nueva generación (NGS) a una escala cromosómica,
                    facilitando así su interpretación como:
                        <ul>
                            <li>
                            ¿Qué genes podrían estar regulados por la accesibilidad a la cromatina?
                            <li>
                            Regiones con modificaciones en las histonas y los genes que podrían estar bajo control epigenético.
                            </li>
                        </ul>
                    </li>    
                </ul>    
        </div>
    """, unsafe_allow_html=True
)

st.markdown("<h3 style='text-align: center; font-size: 25px; color: white;'>✨Gracias por tu apoyo✨</h3>",
             unsafe_allow_html=True)
# st.markdown("<h1 style='text-align: center; font-size: 15px; color: white;'><em>...Yo sé lo que quiero, el chiste es que los demás lo averigüen...</em></h1>",
#              unsafe_allow_html=True)