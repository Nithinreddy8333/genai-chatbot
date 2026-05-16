# 🤖 GenAI Chatbot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5%2FGPT--4-green.svg)](https://openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **Generative AI Chatbot** built with Python, OpenAI GPT API, and Streamlit. This project demonstrates how to build an interactive AI-powered chat interface with a clean, modern UI.

## 🌐 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://genai-chatbot-demo.streamlit.app)

> **Deploy your own:** Click the badge above or follow the deployment instructions below.
>
> ## ✨ Features
>
> - 💬 **Real-time AI Chat** - Powered by OpenAI GPT-3.5-turbo and GPT-4
> - - 🎨 **Modern UI** - Clean, responsive Streamlit interface with custom CSS
>   - - ⚙️ **Configurable** - Adjustable temperature, model selection, and max tokens
>     - - 📝 **Custom System Prompts** - Personalize the AI assistant's behavior
>       - - 📊 **Chat Statistics** - Track message count and token usage
>         - - 🔒 **Secure** - API keys are never stored, only used in-session
>           - - ⏰ **Timestamps** - Track when each message was sent
>             - - 🗑️ **Chat History** - Clear and reset conversation anytime
>              
>               - ## 🛠️ Tech Stack
>              
>               - | Technology | Purpose |
>               - |-----------|---------|
>               - | Python 3.8+ | Core programming language |
> | Streamlit | Web UI framework |
> | OpenAI API | GPT language models |
> | python-dotenv | Environment variable management |
>
> ## 🚀 Quick Start
>
> ### Prerequisites
> - Python 3.8 or higher
> - - OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
>  
>   - ### Installation
>  
>   - 1. **Clone the repository**
>     2.    ```bash
>              git clone https://github.com/Nithinreddy8333/genai-chatbot.git
>              cd genai-chatbot
>              ```
>
> 2. **Install dependencies**
> 3.    ```bash
>          pip install -r requirements.txt
>          ```
>
> 3. **Run the application**
> 4.    ```bash
>          streamlit run app.py
>          ```
>
> 4. **Open your browser** and navigate to `http://localhost:8501`
>
> 5. 5. **Enter your OpenAI API key** in the sidebar and start chatting!
>   
>    6. ## 📁 Project Structure
>   
>    7. ```
>       genai-chatbot/
>       ├── app.py              # Main Streamlit application
>       ├── requirements.txt    # Python dependencies
>       ├── README.md          # Project documentation
>       └── .gitignore         # Git ignore file
>       ```
>
> ## 🔧 Configuration Options
>
> | Option | Description | Default |
> |--------|-------------|---------|
> | Model | GPT model selection | gpt-3.5-turbo |
> | Temperature | Response creativity (0.0-2.0) | 0.7 |
> | Max Tokens | Response length limit | 500 |
> | System Prompt | AI personality/behavior | Helpful assistant |
>
> ## 🌍 Deploy on Streamlit Cloud (Free)
>
> 1. Fork this repository
> 2. 2. Go to [share.streamlit.io](https://share.streamlit.io)
>    3. 3. Click **New app** → Connect your GitHub repo
>       4. 4. Set **Main file path** to `app.py`
>          5. 5. Click **Deploy!**
>             6. 6. Add your OpenAI API key in the Streamlit secrets or through the app sidebar
>               
>                7. ## 📸 Screenshots
>               
>                8. ### Main Chat Interface
>                9. The app features a clean chat interface with message history, timestamps, and real-time AI responses.
>               
>                10. ### Sidebar Configuration
> Configure the AI model, creativity level, response length, and custom system prompts.
>
> ## 🤝 Contributing
>
> Contributions are welcome! Please feel free to submit a Pull Request.
>
> 1. Fork the project
> 2. 2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
>    3. 3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
>       4. 4. Push to the branch (`git push origin feature/AmazingFeature`)
>          5. 5. Open a Pull Request
>            
>             6. ## 📄 License
>            
>             7. This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
>            
>             8. ## 🙏 Acknowledgments
>
> - [OpenAI](https://openai.com) for the powerful GPT API
> - - [Streamlit](https://streamlit.io) for the amazing web framework
>   - - The open-source community for inspiration and support
>    
>     - ---
>
> ⭐ **If you find this project useful, please give it a star!**
>
> Made with ❤️ by [Nithinreddy8333](https://github.com/Nithinreddy8333)
