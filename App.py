import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="AI Content Generator", layout="centered", initial_sidebar_state="expanded")

# API Configuration
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# Initialize Session State
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Sidebar History
with st.sidebar:
    st.subheader("📜 Generated History")
    for i, item in enumerate(reversed(st.session_state['history'])):
        with st.expander(f"Post {len(st.session_state['history'])-i}"):
            st.write(item['result'])

# Main UI
st.title("✨ AI Content Generator")

# Buttons Row
col_top1, col_top2 = st.columns([4, 1])
with col_top2:
    if st.button("🔄 New Content"):
        st.rerun()

mode = st.selectbox("Select Role:", ["Student", "Creator", "Business Brand"], key="role")
user_input = st.text_area("What's the update today?", key="user_input")
url_input = st.text_input("🔗 Paste a URL to analyze:", key="url_input")
uploaded_file = st.file_uploader("Upload Assets:", type=["jpg", "png", "mp4", "mov"], key="uploaded_file")

c1, c2 = st.columns(2)
with c1: selected_lang = st.radio("Language:", ["English", "Hinglish"], horizontal=True)
with c2: selected_audience = st.selectbox("Target Audience:", ["General", "Peers", "Experts", "Recruiters"])

platforms = st.multiselect("Choose Platforms:", ["LinkedIn", "Instagram", "Twitter", "Facebook", "YouTube"])

# Generation Logic
if st.button("✨ Generate Content"):
    if not user_input and not url_input:
        st.warning("Please provide input or a URL!")
    else:
        with st.spinner("Generating..."):
            prompt = f"Create a post for {mode} in {selected_lang} for {platforms}. Audience: {selected_audience}. Context: {user_input}. Reference URL: {url_input}"
            response = model.generate_content(prompt)
            result = response.text
            
            st.session_state['history'].append({"result": result})
            
            st.success("Draft Generated!")
            st.write(result)
            
            col1, col2 = st.columns(2)
            with col1: st.button("👍 Good")
            with col2: st.button("👎 Improve")
