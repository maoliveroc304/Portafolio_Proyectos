# landing_page_proyectos_rect.py
import streamlit as st
from streamlit.components.v1 import html
from typing import Optional

# ---------------- CONFIGURACIÓN ----------------
DIALOGFLOW_AGENT_ID = "372a5eeb-31b9-4777-bfd4-a9a2af72e162"
CHAT_TITLE = "Asistente virtual - OliveroBOT"

# Tamaño rectangular deseado
THUMB_W = 230  # ancho en px
THUMB_H = 195  # alto en px

# Proyectos Python con URLs de screenshots
# Nota: eliminé el proyecto "API model-deploy" según tu pedido.
PYTHON_PROJECTS = [
    {
        "title": "📈 Análisis Económico Lima",
        "desc": "Explora los datos económicos de Lima (ventas, trabajadores y más) con mapas y gráficos interactivos.",
        "url": "https://proyecto-1-python.streamlit.app/",
        "sources": "https://datosabiertos.gob.pe/dataset/desempe%C3%B1o-econ%C3%B3mico-de-las-grandes-empresas-manufactureras-ministerio-de-la-produccion",
        "screenshots": [
            "https://raw.githubusercontent.com/maoliveroc304/Portafolio_Proyectos/main/proyecto_1/capturas/proyecto1_foto1.png",
            "https://raw.githubusercontent.com/maoliveroc304/Portafolio_Proyectos/main/proyecto_1/capturas/proyecto1_foto2.png"
        ]
    },
]

HTML_PROJECTS = {
    "mi-sitio-1": {
        "title": "Gestión del Personal - Tienda Buendía",
        "url": "https://script.google.com/macros/s/AKfycbwvIzl2QR6T--xe5zh9GAJO1Nb2vrSTre_PY-9lU2Oz0NZY9gySx5l-vXHx1RC04NXI/exec"
    },
    "mi-sitio-2": {
        "title": "Selección de Personal - Adecco (Formulario)",
        "url": "https://script.google.com/macros/s/AKfycbz53NsJvs699L1cPNUU6AqmSfakuCEQrM-BpiRWokUjX9pcZV1fFV4upY-lnvtGZ8WTpQ/exec"
    },
}

st.set_page_config(page_title="Portfolio · Proyectos", layout="wide")

# ---------------- CSS limpio ----------------
st.markdown(
    """
<style>
body, html, [data-testid="stAppViewContainer"] { margin:0; padding:0; }
.project-button, .source-button {
    display:inline-block;
    padding:8px 14px;
    border-radius:6px;
    font-size:14px;
    text-decoration:none;
    color:#fff;
    cursor:pointer;
    margin:4px 0;
}
.project-button { background:#4CAF50; }
.source-button  { background:#0b6cff; }

.screenshot-row-inline {
    display:flex !important;
    gap:20px !important;
    flex-wrap:wrap !important;
    margin-top:8px !important;
    padding:0 !important;
    align-items:flex-start;
}
.screenshot-row-inline a {
    margin:0 !important;
    padding:0 !important;
}
.screenshot-row-inline img {
    display:block;
    border-radius:8px;
    border:1px solid #ccc;
    object-fit:cover;
    box-shadow:0 2px 6px rgba(0,0,0,0.12);
}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------- HEADER ----------------
st.title("Landing — Proyectos: Python · HTML · ChatBot")
st.write("Presentación rápida de proyectos. Miniaturas rectangulares, separadas y con embebidos HTML en zoom-out.")

# ---------------- HELPER BOTONES ----------------
def render_project_buttons(url: str, sources: Optional[str]):
    abrir_html = f'''
    <a href="{url}" target="_blank" rel="noopener noreferrer">
        <div class="project-button">Abrir Proyecto</div>
    </a>
    '''
    sources_html = ""
    if sources:
        sources_html = f'''
        <a href="{sources}" target="_blank" rel="noopener noreferrer">
            <div class="source-button">Fuentes</div>
        </a>
        '''
    html(
        f'''
    <div style="display:flex; gap:8px; flex-wrap:wrap;">
        {abrir_html}{sources_html}
    </div>
    ''',
        height=48,
    )


# ---------------- 2 COLUMNAS ----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Proyectos Python")
    for p in PYTHON_PROJECTS:
        st.markdown(f"### {p.get('title')}")
        st.markdown(f"{p.get('desc')}")
        render_project_buttons(url=p.get("url"), sources=p.get("sources"))

        # Miniaturas rectangulares con gap consistente
        w = THUMB_W
        h = THUMB_H
        screenshots_html = '<div class="screenshot-row-inline">'
        for s in p.get("screenshots", []):
            screenshots_html += (
                f'<a href="{s}" target="_blank" rel="noopener noreferrer">'
                f'<img src="{s}" width="{w}" height="{h}" />'
                f'</a>'
            )
        screenshots_html += '</div>'
        html(screenshots_html, height=h, scrolling=False)
        st.markdown("---")

with col2:
    st.subheader("HTML / Micro-sitios (Adscript)")
    for slug, meta in HTML_PROJECTS.items():
        st.markdown(f"**{meta.get('title')}**")
        st.markdown(f"[Abrir]({meta.get('url')})")
        embed_html = f"""
        <div style="width:100%; height:{int(700*0.5)}px; margin-bottom:18px; overflow:hidden;">
            <iframe src="{meta.get('url')}" 
                    style="transform:scale(0.5); transform-origin:0 0; width:200%; height:200%;" 
                    frameborder="0" scrolling="yes"></iframe>
        </div>
        """
        html(embed_html, height=int(700 * 0.5))
        st.markdown("---")

# ---------------- CHATBOT (Dialogflow) ----------------
# Mantengo el injector de Dialogflow según estaba en el original.
DIALOGFLOW_INJECTOR = f"""
<script>
(function(){{
  const P = window.parent;
  if (!P || !P.document) return;
  if (!P.document.getElementById('df-messenger-bootstrap')) {{
      const s = P.document.createElement('script');
      s.id = 'df-messenger-bootstrap';
      s.src = 'https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1';
      P.document.head.appendChild(s);
  }}
  if (!P.document.getElementById('df-messenger-container')) {{
      const c = P.document.createElement('div');
      c.id = 'df-messenger-container';
      c.style.position = 'fixed';
      c.style.right = '16px';
      c.style.bottom = '16px';
      c.style.zIndex = '2147483647';
      c.innerHTML = `
        <df-messenger
          chat-title="{CHAT_TITLE}"
          agent-id="{DIALOGFLOW_AGENT_ID}"
          intent="WELCOME"
          language-code="es"
          chat-icon="https://cdn-icons-png.flaticon.com/512/8943/8943377.png"
        ></df-messenger>
      `;
      P.document.body.appendChild(c);
  }}
}})();
</script>
"""
html(DIALOGFLOW_INJECTOR, height=0)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    """
    <div style='font-size:0.85rem; color:gray;'>
    © 2025 · Miguel Olivero · Todos los derechos reservados · 
    <a href='https://github.com/maoliveroc304/Portafolio_Proyectos' target='_blank' style='color:gray; text-decoration:underline;'>Base en GitHub</a>
    </div>
    """,
    unsafe_allow_html=True,
)