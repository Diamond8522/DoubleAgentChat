import streamlit as st
import time

# --- Configuration (The Fun Stuff) ---
st.set_page_config(
    page_title="Tri-Agent Lab",
    layout="wide"
)

st.title("🤯 The Violet & Storm Collaboration Lab")
st.caption("A free, real-time chat with three very opinionated minds.")

# Initialize chat history (We use a session variable for persistence)
if "messages" not in st.session_state:
    st.session_state.messages = []
    
    # Starting message from Violet
    st.session_state.messages.append({"role": "Violet", "content": "Welcome! We ditched the paywall. Resilience, right? What's the first topic?"})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- User Input ---
if prompt := st.chat_input("Ask Violet and Storm anything..."):
    # 1. Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Add Violet's placeholder response
    with st.chat_message("Violet"):
        with st.spinner("Violet is drafting her brutally self-aware reply..."):
            time.sleep(1) # Simulate thinking time
            violet_response = f"**Placeholder Violet:** I heard you loud and clear: '{prompt}'. I'm getting an aggressive amount of coffee ready to tackle this."
            st.markdown(violet_response)
            st.session_state.messages.append({"role": "Violet", "content": violet_response})
            
    # 3. Add Storm's placeholder response
    with st.chat_message("Storm"):
        with st.spinner("Storm is generating her mysterious, cool-kid response..."):
            time.sleep(1) # Simulate thinking time
            storm_response = f"**Placeholder Storm:** Violet's right. Focus. My intel suggests the best route is to ignore her first step and optimize for performance. Let's see your data."
            st.markdown(storm_response)
            st.session_state.messages.append({"role": "Storm", "content": storm_response})