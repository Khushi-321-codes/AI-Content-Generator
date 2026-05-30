import streamlit as st

# Page Configuration
st.set_page_config(page_title="AI Content Generator", layout="centered", initial_sidebar_state="expanded")

# Initialize Session State
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Function to reset form
def reset_form():
    st.session_state['user_input'] = ""
    st.session_state['url_input'] = ""
    st.session_state['uploaded_file'] = None

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
        st.rerun() # Refresh to clear everything

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
        # Mock result
        result = f"Here is your AI generated content for {mode}..."
        st.session_state['history'].append({"result": result})
        
        st.success("Draft Generated!")
        st.code(result, language='text')
        
        col1, col2 = st.columns(2)
        with col1: st.button("👍 Good")
        with col2: st.button("👎 Improve")