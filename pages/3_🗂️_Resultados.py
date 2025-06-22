import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
import math
import numpy as np

# Aumentar el límite máximo de píxeles
Image.MAX_IMAGE_PIXELS = None 

#---------configuracion de la pagina ------
titulo = "Resultados"
st.set_page_config(page_title= titulo, 
                    page_icon = "🗂️", 
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

st.markdown("<h1 style='text-align: center; color: white;'>Resultados</h1>", unsafe_allow_html=True)

#---------- size font markdown -------------
st.markdown("""
<style>
.small-font {
    font-size:14px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.medium-font {
    font-size:18px !important;
}
</style>
""", unsafe_allow_html=True)

#-------------- datos ----------------------
df_motivos_atac_seq = pd.read_csv('data/tabla_motivos_atac_seq.csv',sep=",").iloc[:10,:5] #mostrar los primeros 10 registros y cuatro columnas
df_motivos_chip_seq = pd.read_csv('data/tabla_motivos_chip_seq.csv',sep=",").iloc[:10,:5]
df_atac_seq_annotate_peaks = pd.read_csv('data/Plotpie_atac_seq.csv')
df_gata1_annotate_peaks = pd.read_csv('data/Plotpie_GATA1.csv')
df_h3k27ac_annotate_peaks = pd.read_csv('data/Plotpie_H3K27ac.csv')
df_h3k27me3_annotate_peaks = pd.read_csv('data/Plotpie_H3K27me3.csv')
df_ontologia = pd.read_csv('data/ontologia.csv')
df_volcano = pd.read_csv('data/DiffBind_HSPC_D12_D0_labels.csv')

#--------------- Funciones ------------------
def grafico_barras_motivos(df):
    '''Grafico de barra de motivos'''
    fig = px.bar(df, '-Log P-value', 'Motif Name', color = 'Motif Name',
                hover_data= ['Motif Name','P-value', '-Log P-value'],
                orientation='h')

    # fig.update_layout(
    #     title={
    #         'text': 'Factores de transcripción',
    #         'x': 0.5,
    #         'xanchor': 'center'
    #     })
    fig.update_yaxes(title="Factores de transcripción (FT)")
    fig.update_layout(yaxis={'categoryorder':'total descending'}, showlegend=False)

    return st.plotly_chart(fig, use_container_width=True)

def pie_picos_anotados(df_atac_seq, df_GATA1,  df_H3K27ac, df_H3K27me3):
    '''Funcion sobre grafico de pie para picos anotados para ATAC-seq y CHIP-seq'''

    labels = df_atac_seq['Feature'].tolist()
    valores_ataqseq = df_atac_seq['Frequency'].tolist()
    valores_GATA1 = df_GATA1['Frequency'].tolist()
    valores_H3K27ac = df_H3K27ac['Frequency'].tolist()
    valores_H3K27me3 = df_H3K27me3['Frequency'].tolist()

    fig = make_subplots(rows=2, cols=2, specs=[[{'type':'domain'},{'type':'domain'}],
                                            [{'type':'domain'},{'type':'domain'}]])
    
    fig.add_trace(go.Pie(labels=labels, 
                     values = valores_ataqseq, name="ATAC-seq"),
                        row=1, col=1)

    fig.add_trace(go.Pie(labels=labels,
                        values = valores_GATA1, name="GATA1"), 
                        row=1, col=2)

    fig.add_trace(go.Pie(labels=labels, 
                        values = valores_H3K27ac, name="H3K27ac"), 
                         row=2, col=1)

    fig.add_trace(go.Pie(labels=labels, 
                        values = valores_H3K27me3, name="H3K27me3"),
                         row=2, col=2)

    # fig.update_traces(hole=.4, hoverinfo="label+percent+name")
    fig.update_traces(hole=.4, textposition='inside')

    fig.update_layout(
    # title_text="Anotacion de picos",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='ATAC-seq', x=sum(fig.get_subplot(1, 1).x) / 2, y=0.8,
                      font_size=20, showarrow=False, xanchor="center"),
                 
                 dict(text='GATA1', x=sum(fig.get_subplot(1, 2).x) / 2, y=0.8,
                      font_size=20, showarrow=False, xanchor="center"),
                 
                 dict(text='H3K27ac', x=sum(fig.get_subplot(2, 1).x) / 2, y=0.20,
                      font_size=20, showarrow=False, xanchor="center"),
                 
                 dict(text='H3K27me3', x=sum(fig.get_subplot(2, 2).x) / 2, y=0.20,
                      font_size=20, showarrow=False, xanchor="center")])
    
    # fig.update_layout(
    #     title={
    #         'text': 'Anotacion de picos',
    #         'x': 0.5,
    #         'xanchor': 'center'
    #     }
    # )

    fig.update_layout(showlegend=True)
    fig.update_traces(sort=False)
    fig.update_layout(uniformtext_minsize=15, uniformtext_mode='hide')
    fig.update_layout(height=1000, width=1000)
    return st.plotly_chart(fig)

def ontologia_bar(df):
    '''Grafico de barras de genes con funcionalidad'''
    df['-log10(P)'] = df['LogP'] * -1

    fig = px.bar(df, '-log10(P)', 'Description',
             color= 'Description', orientation = 'h')

    fig.update_yaxes(
            title="Clúster de ontología enriquecido")  
           
    fig.update_layout(
    #         title={
    #             'text': 'Ontologia genica',
    #             'x': 0.5,
    #             'xanchor': 'center'},
             showlegend=False
        )
    return st.plotly_chart(fig, use_container_width=True)

def volcano_plot(df):
    '''Grafico de volcano que muestra los picos de ATAC-seq Ganados, Conservados y reducidos '''
    #Clasificar los picos
    df['State'] = 'Conserved'
    df.loc[(df['Fold'] > 1.5) & (df['FDR'] < 0.05), 'State'] = 'Gained'
    df.loc[(df['Fold'] < -1.5) & (df['FDR'] < 0.05), 'State'] = 'Reduced'
    df['-log10(FDR)'] = -np.log10(df['FDR'])
    df.loc[(df['Name']=='ATAC_seq463') | (df['Name'] == 'ATAC_seq31') | (df['Name'] == 'ATAC_seq2') |
           (df['Name'] == 'ATAC_seq5') | (df['Name']=='ATAC_seq30') | (df['Name']=='ATAC_seq1346')  |
           (df['Name']=='ATAC_seq1192') | (df['Name']=='ATAC_seq750') | (df['Name']=='ATAC_seq880') |
           (df['Name']=='ATAC_seq177'), 'State'] = 'Validated' 
    
    #Grafico
    fig =  px.scatter(df, 'Fold', '-log10(FDR)',
                  color = 'State', hover_name = 'Name',
                  #Diccionario de colores para la clasificacion
                  color_discrete_map={
                    "Reduced": "skyblue",
                    "Conserved": "grey",
                    "Gained": "red",
                    "Validated": "#42c106"})
    
    # fig.update_layout(
    #     title={
    #         'text': 'Volcanoplot',
    #         'x': 0.5,
    #         'xanchor': 'center'
    #     }
    # )
    fig.update_xaxes(
            title="Fold change (FC)") 
    fig.add_vline(x=-1.5, line_width=3, line_dash="dot", line_color="black")
    fig.add_vline(x=1.5, line_width=3, line_dash="dot", line_color="black")
    fig.add_hline(y=-np.log10(0.05), line_width=3, line_dash="dot", line_color="black")

    return st.plotly_chart(fig, use_container_width=True)

#----------------- Visualizacion ------------------------
# https://discuss.streamlit.io/t/align-text-in-justify-alignment/22270
# https://discuss.streamlit.io/t/change-font-size-and-font-color/12377/3

with st.expander("*Fig.1.* :red[Mapa de calor entre D0 y D12 para ATAC-seq]"):
    st.markdown(
    """
    <div style="text-align: justify; font-family:serif; font-size: 14px;"> El mapa de calor indica mediante colores la cantidad de señal (conteos normalizados)
        en una ventana de ±1000 pb alrededor del TSS (<em>Transcription Start Site</em>, por sus siglas en inglés), que es el centro.
        <span style="color:orange;">Cuanto más rojo, mayor es la señal; cuanto más amarillo, menor</span>.
        En la condición <span style="color:orange;">D12</span> se observa un aumento de la señal en los picos, lo que sugiere una <span style="color:#55ee0f;">mayor accesibilidad
        a la cromatina</span>. En cambio, los picos conservados y reducidos en <span style="color:orange;">D0</span> 
        tienden a mostrar una <span style="color:#f20a1d;">menor señal</span>.
    </div>
    <br>
    """, unsafe_allow_html=True
    ) 
    st.image('data/heatmap.png', use_column_width=True)

with st.expander("*Fig.2.* :green[Anotacion de picos]"):
    st.markdown(
    """
    <div style="text-align: justify; font-family:serif; font-size: 14px;">Los gráficos de anotación de picos (Peak Annotation) muestra la distribución de los picos detectados
              en relación con diferentes regiones genómicas, <span style="color:orange;">como promotores, exones, intrones o regiones intergénicas para el Cromosoma 22</span>.
              Esta información permite identificar en qué partes del cromosoma 22 se encuentran los picos,
              lo cual es útil para entender su posible función reguladora.
    </div>
    """, unsafe_allow_html=True
    ) 
#Centrar grafico
    left, middle, right = st.columns((2, 5, 2))
    with middle:
        pie_picos_anotados(df_atac_seq_annotate_peaks, df_gata1_annotate_peaks,
                        df_h3k27ac_annotate_peaks, df_h3k27me3_annotate_peaks)

with st.expander("*Fig.3.* :rainbow[Análisis de Motivos]"):
    st.markdown(
    """
    <div style="text-align: justify; font-family:serif; font-size: 14px;">El gráfico muestra los <span style="color:orange;">10 principales factores de transcripción (FT)</span> potencialmente asociados con la regulación,
                 basándose en el enriquecimiento de secuencias específicas en las regiones analizadas mediante <span style="color:#e74c3c;">ATAC-seq</span>.
                 Los resultados indican que los factores del linaje <span style="color:#FF00FF;">GATA</span> podrían tener el mayor aporte en la regulación.
    </div>
    """, unsafe_allow_html=True
    )
    
    # st.markdown("<h1 style='text-align: center; color: white;font-size:20px;'>Análisis de motivo para ATAC-seq</h1>", unsafe_allow_html=True)
    grafico_barras_motivos(df_motivos_atac_seq)
    # st.markdown("<h1 style='text-align: center; color: white;font-size:20px;'>Análisis de motivo para CHIP-seq</h1>", unsafe_allow_html=True)
    # grafico_barras_motivos(df_motivos_chip_seq)
    st.markdown("Un valor mayor de :green[-Log P-value = más significativo.]")

# https://stackoverflow.com/questions/71988099/markdown-multiline-link-support
with st.expander("*Fig.4.* :orange[Grafico de ontología génica (Gene Ontology, GO)]"):
    # url = "https://rarediseases.org/es/rare-diseases/chromosome-22q11-2-deletion-syndrome/"
    st.markdown(
    """
    <div style="text-align: justify; font-family:serif; font-size: 14px;">El análisis de <span style="color:#55ee0f;">ontología genética (GO, por sus siglas en inglés)</span>
                se utiliza para comprender cómo los elementos reguladores del genoma (por ejemplo, <span style="color:red;">regiones promotoras y enhancers</span>)
                se relacionan con conjuntos de genes que desempeñan funciones biológicas específicas.
                Se identificaron los siguientes genes: <span style="color:orange;">SREBF2, DEPDC5, RBX1, TXNRD2, MED15, TANGO2 y TXN2</span>,
                los cuales se encuentran asociados al <span style="color:red;">síndrome por variación en el número de copias 22q11.2</span>.
                (<a href="https://rarediseases.org/es/rare-diseases/chromosome-22q11-2-deletion-syndrome/" target="_blank" style="color:orange; text-decoration:underline;">22q11.2 CNV syndrome</a>)
    </div>
    """, unsafe_allow_html=True
    )
    ontologia_bar(df_ontologia) 

with st.expander("*Fig.5.* :blue[Volcano]:red[Plot]"):
    st.markdown(
    """
    <div style="text-align: justify; font-family:serif; font-size: 14px;">El gráfico muestra los resultados de cambios en la accesibilidad de la cromatina entre las condiciones D0 y D12
                usando datos de <span style="color:#f20a1d;">ATAC-seq</span>. En el eje X se muestra el <span style="color:orange;">cambio en la accesibilidad</span> (<em>Fold Change</em>) entre las dos condiciones,
                y en el eje Y se muestra la <span style="color:orange;">importancia estadística</span> de ese cambio (<em>–log10 del FDR</em>, que es la tasa de falsos descubrimientos).
                Así, los puntos situados más alejados del centro en el eje x y con mayor altura en el eje y representan
                regiones con grandes cambios en su expresión y alta significancia estadística. Los puntos <span style="color:#42c106;">verdes</span> son picos 
                asociados a genes con funcionalidad del síndrome por variación en el número de copias 22q11.2.
    </div>
    """, unsafe_allow_html=True
    )
    volcano_plot(df_volcano)


#----------------------- IGV -------------------------------------
with st.container(border=True):
    # https://discuss.streamlit.io/t/how-do-i-align-st-title/1668/4    
    st.markdown("<h1 style='text-align: center; color: white;'>🧬Gráfico de señales🧬</h1>", unsafe_allow_html=True)

    _left, mid, _right = st.columns(3)

    with mid :
        st.image('data/ejemplo.png')
        st.markdown('''<div style="text-align:center; font-family:serif; font-size:12px;"><em>Instrucción: Coloca aqui el nombre del gen y presiona "enter"</em></div>
                    <br>''',
                    unsafe_allow_html= True)

# st.markdown('''Puedes visualizar los siguientes genes con regiones accesibles de la cromatina: 
#             :red[SREBF2, DEPDC5, RBX1, TXNRD2, MED15, TANGO2 y TXN2]''')


    st.markdown('''<div style="text-align: justify; font-family:serif; font-size: 12px;">
            <li>
            Genes asociados con funcionalidad del síndrome por variación en el número de copias 22q11.2 : 
            <span style="color:orange;"><em>SREBF2, DEPDC5, RBX1, TXNRD2, MED15, TANGO2 y TXN2</em></span>
            </li>
            </div>
            <br>''',
            unsafe_allow_html=True) 
    
# https://github.com/igvteam/igv.js/issues/1484
    html_string = """
    <div id="igv-div" style="height:500px;"></div>
    <script src="https://cdn.jsdelivr.net/npm/igv@2.9.4/dist/igv.min.js"></script>
    <script>
        var igvDiv = document.getElementById("igv-div");
        var options = {
            genome: "hg38",
            locus: "chr22:1-51200000",
            tracks: [
            {
                    name: "Dia 0",
                    type: "wig",
                    format: "bigwig",
                    url: "https://raw.githubusercontent.com/Br1Rdz/Epigenetica/ce4e706f49c4a659fcaee68a6b08b53eada42e7d/data/day0_ATAC.bw",
                    autoscale: true,
                    color: "rgb(100, 100, 100)"
            },
            {
                    name: "Dia 12",
                    type: "wig",
                    format: "bigwig",
                    url: "https://raw.githubusercontent.com/Br1Rdz/Epigenetica/6fe7d1a9950b89587a251c4c3dc1f07c82c01e8d/data/day12_ATAC.bw",
                    autoscale: true,
                    color: "rgb(0, 0, 200)"
            },
            {
                    name: "GATA1",
                    type: "wig",
                    format: "bigwig",
                    url: "https://raw.githubusercontent.com/Br1Rdz/Epigenetica/6fe7d1a9950b89587a251c4c3dc1f07c82c01e8d/data/GATA1.bw",
                    autoscale: true,
                    color: "rgb(0, 0, 200)"
            },
            {
                    name: "H3K27ac",
                    type: "wig",
                    format: "bigwig",
                    url: "https://raw.githubusercontent.com/Br1Rdz/Epigenetica/e43dda79d6d16d846685c177a33816dd5adcb53c/data/H3K27ac.bw",
                    autoscale: true,
                    color: "rgb(0, 0, 200)"
            },
            {
                    name: "H3K27me3",
                    type: "wig",
                    format: "bigwig",
                    url: "https://raw.githubusercontent.com/Br1Rdz/Epigenetica/e43dda79d6d16d846685c177a33816dd5adcb53c/data/H3K27me3.bw",
                    autoscale: true,
                    color: "rgb(100, 100, 100)"
            },
            {
                    name: "ATAC-seq Peaks",
                    type: "annotation",
                    format: "bedtabix", 
                    url: "https://raw.githubusercontent.com/Br1Rdz/Epigenetica/ce4e706f49c4a659fcaee68a6b08b53eada42e7d/data/incrementados_atac_sorted_peaks.bed.gz",
                    indexURL: "https://raw.githubusercontent.com/Br1Rdz/Epigenetica/ce4e706f49c4a659fcaee68a6b08b53eada42e7d/data/incrementados_atac_sorted_peaks.bed.gz.tbi",
                    displayMode: "EXPANDED",
                    color: "rgb(231, 76, 60)"
            }
            ]
        };
        igv.createBrowser(igvDiv, options);
    </script>
    """

    components.html(html_string, height=550) 

#----------------- cita ----------------------------
    # https://discuss.streamlit.io/t/change-font-size-in-st-write/7606/2
    # st.markdown('<p class="medium-font">Integrative Genomics Viewer (IGV):</p>', unsafe_allow_html=True)
    # st.markdown('<p class="small-font">James T Robinson, Helga Thorvaldsdottir, Douglass Turner, Jill P Mesirov, igv.js: an embeddable JavaScript implementation of the Integrative Genomics Viewer (IGV), Bioinformatics, Volume 39, Issue 1, January 2023, btac830</p>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify; font-family:serif; font-size: 12px;"><em>Integrative Genomics Viewer (IGV)</em>:</div>',
                 unsafe_allow_html=True)
    st.markdown('''<div style="text-align: justify; font-family:serif; font-size: 10px;">
    James T Robinson, Helga Thorvaldsdottir, Douglass Turner, Jill P Mesirov, igv.js: an embeddable JavaScript
    implementation of the Integrative Genomics Viewer (IGV), Bioinformatics, Volume 39, Issue 1, January 2023.
    </div>''', unsafe_allow_html=True) 
