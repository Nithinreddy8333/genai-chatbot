import streamlit as st
import openai
from datetime import datetime

st.set_page_config(page_title="GenAI Chatbot", page_icon="🤖", layout="centered")

st.markdown("""
<style>
.main-header {
    text-align: center;
    padding: 20px;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    border-radius: 10px;
    color: white;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>🤖 GenAI Chatbot</h1>
    <p>Powered by OpenAI GPT | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="Enter your OpenAI API key...",
        help="Get your API key from platform.openai.com"
    )
    model = st.selectbox(
        "Select Model",
        ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-preview"],
        index=0
    )
    temperature = st.slider(
        "Temperature (Creativity)",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1
    )
    max_tokens = st.slider(
        "Max Response Length",
        min_value=100,
        max_value=2000,
        value=500,
        step=100
    )
    st.divider()
    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful, friendly AI assistant. Provide clear and accurate responses.",
        height=100
    )
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.markdown("**📊 Chat Stats**")
    if "messages" in st.session_state:
        st.metric("Total Messages", len(st.session_state.messages))
    st.markdown("---")
    st.markdown("Built with ❤️ using [Streamlit](https://streamlit.io) & [OpenAI](https://openai.com)")

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.info("👋 Welcome! Configure your API key in the sidebar and start chatting!")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "timestamp" in message:
            st.caption(f"⏰ {message['timestamp']}")

if prompt := st.chat_input("Type your message here..."):
    if not api_key:
        st.error("⚠️ Please enter your OpenAI API key in the sidebar to start chatting!")
        st.stop()

    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
        "timestamp": timestamp
    })

    with st.chat_message("user"):
        st.markdown(prompt)
        st.caption(f"⏰ {timestamp}")

    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            try:
                client = openai.OpenAI(api_key=api_key)
                messages = [{"role": "system", "content": system_prompt}]
                messages.extend([
                    {"role": msg["role"], "content": msg["content"]}
                    for msg in st.session_state.messages
                ])
                response = client.chat.completions.create(
                    model=model,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                assistant_message = response.choices[0].message.content
                response_timestamp = datetime.now().strftime("%H:%M:%S")
                st.markdown(assistant_message)
                st.caption(f"⏰ {response_timestamp} | Model: {model} | Tokens: {response.usage.total_tokens}")
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_message,
                    "timestamp": response_timestamp
                })
            except openai.AuthenticationError:
                st.error("❌ Invalid API key. Please check your OpenAI API key.")
            except openai.RateLimitError:
                st.error("⚠️ Rate limit exceeded. Please wait and try again.")
            except openai.APIConnectionError:
                st.error("🌐 Connection error. Please check your internet connection.")
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")

st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("🔒 **Secure**")
with col2:
    st.markdown("⚡ **Fast**")
with col3:
    st.markdown("🎨 **Customizable**")
