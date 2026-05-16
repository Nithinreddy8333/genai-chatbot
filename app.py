import streamlit as st
import openai
import os
from datetime import datetime

# Page configuration
st.set_page_config(
      page_title="GenAI Chatbot",
      page_icon="🤖",
      layout="centered"
)

# Custom CSS for better styling
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
                                                            .chat-message {
                                                                    padding: 10px;
                                                                            border-radius: 10px;
                                                                                    margin: 5px 0;
                                                                                        }
                                                                                            .user-message {
                                                                                                    background-color: #e3f2fd;
                                                                                                            text-align: right;
                                                                                                                }
                                                                                                                    .assistant-message {
                                                                                                                            background-color: #f3e5f5;
                                                                                                                                    text-align: left;
                                                                                                                                        }
                                                                                                                                        </style>
                                                                                                                                        """, unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 GenAI Chatbot</h1>
        <p>Powered by OpenAI GPT | Built with Streamlit</p>
        </div>
        """, unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
      st.header("⚙️ Configuration")

    # API Key input
      api_key = st.text_input(
          "OpenAI API Key",
          type="password",
          placeholder="Enter your OpenAI API key...",
          help="Get your API key from platform.openai.com"
      )

    # Model selection
      model = st.selectbox(
          "Select Model",
          ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-preview"],
          index=0
      )

    # Temperature slider
      temperature = st.slider(
          "Temperature (Creativity)",
          min_value=0.0,
          max_value=2.0,
          value=0.7,
          step=0.1,
          help="Higher values = more creative, Lower values = more deterministic"
      )

    # Max tokens
      max_tokens = st.slider(
          "Max Response Length",
          min_value=100,
          max_value=2000,
          value=500,
          step=100
      )

    st.divider()

    # System prompt
    system_prompt = st.text_area(
              "System Prompt",
              value="You are a helpful, friendly, and knowledgeable AI assistant. Provide clear, accurate, and concise responses.",
              height=100
    )

    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
              st.session_state.messages = []
              st.rerun()

    st.divider()
    st.markdown("**📊 Chat Stats**")
    if "messages" in st.session_state:
              st.metric("Total Messages", len(st.session_state.messages))

    st.markdown("---")
    st.markdown("Built with ❤️ using [Streamlit](https://streamlit.io) & [OpenAI](https://openai.com)")

# Initialize chat history
if "messages" not in st.session_state:
      st.session_state.messages = []

# Display welcome message if no messages
if not st.session_state.messages:
      st.info("👋 Welcome! Configure your API key in the sidebar and start chatting!")

# Display chat history
for message in st.session_state.messages:
      with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if "timestamp" in message:
                              st.caption(f"⏰ {message['timestamp']}")

        # Chat input
        if prompt := st.chat_input("Type your message here..."):

              # Check for API key
              if not api_key:
                        st.error("⚠️ Please enter your OpenAI API key in the sidebar to start chatting!")
                        st.stop()

              # Add user message to history
              timestamp = datetime.now().strftime("%H:%M:%S")
              st.session_state.messages.append({
                  "role": "user",
                  "content": prompt,
                  "timestamp": timestamp
              })

    # Display user message
    with st.chat_message("user"):
              st.markdown(prompt)
              st.caption(f"⏰ {timestamp}")

    # Generate AI response
    with st.chat_message("assistant"):
              with st.spinner("🤔 Thinking..."):
                            try:
                                              # Initialize OpenAI client
                                              client = openai.OpenAI(api_key=api_key)

                # Prepare messages for API call
                                messages = [{"role": "system", "content": system_prompt}]
                messages.extend([
                                      {"role": msg["role"], "content": msg["content"]}
                                      for msg in st.session_state.messages
                ])

                # Make API call
                response = client.chat.completions.create(
                                      model=model,
                                      messages=messages,
                                      temperature=temperature,
                                      max_tokens=max_tokens
                )

                assistant_message = response.choices[0].message.content
                response_timestamp = datetime.now().strftime("%H:%M:%S")

                # Display response
                st.markdown(assistant_message)
                st.caption(f"⏰ {response_timestamp} | Model: {model} | Tokens used: {response.usage.total_tokens}")

                # Add to history
                st.session_state.messages.append({
                                      "role": "assistant",
                                      "content": assistant_message,
                                      "timestamp": response_timestamp
                })

except openai.AuthenticationError:
                st.error("❌ Invalid API key. Please check your OpenAI API key.")
except openai.RateLimitError:
                st.error("⚠️ Rate limit exceeded. Please wait a moment and try again.")
except openai.APIConnectionError:
                st.error("🌐 Connection error. Please check your internet connection.")
except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
      st.markdown("🔒 **Secure** - Keys never stored")
with col2:
      st.markdown("⚡ **Fast** - Real-time responses")
with col3:
      st.markdown("🎨 **Customizable** - Adjust settings")
