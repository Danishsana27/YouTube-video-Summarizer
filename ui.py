import streamlit as st
from Youtube_Analyser import build_yt_agent

st.set_page_config(
    page_title = "Youtube Video analyzer",
    layout = "centered"
)

st.title("🎥 AI Youtube Video analyzer")

@st.cache_resource
def get_agent():
    return build_yt_agent()

agent = get_agent()

#input
Video_url = st.text_input("Enter youtube Video URL")
button = st.button("Analyze Video")

if Video_url and button:
    with st.spinner("Analyzing Video...."):
        response = agent.run(
            f"Analyze this Video : {Video_url}"
        )
    st.markdown("Analysis report of video")
    st.markdown(response.content)





#streamlit run ui.py 