# OllamaGPT

OllamaGPT is a user-friendly interface for interacting with Ollama, a local AI service. This project uses Streamlit to create an interactive chat interface that communicates with the Ollama API.

## Features

- Intuitive chat interface
- Utilization of locally installed Ollama models
- Display of the currently used model
- Error handling for Ollama server connection issues

## Prerequisites

- Python 3.6+
- Ollama installed and configured on your local machine and at least one model downloaded 
- The following Python libraries:
  - streamlit
  - requests
  - subprocess

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/toine08/ollamaGPT.git
   cd ollamaGPT
   ```

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. (optional) Ensure Ollama is running on your local machine. You can start it by running:
   ```
   ollama serve
   ```

2. Launch the Streamlit application:
   ```
   streamlit run app.py
   ```
3. Start chatting with the Ollama AI through the user interface!

## Notes

- The application assumes the Ollama server is running on `http://127.0.0.1:11434`. If your setup is different, please adjust the `baseURL` variable in the code.
- If the Ollama server is not accessible, the application will display an error message.

## Contributing

Contributions to this project are welcome. Feel free to open an issue or submit a pull request.

## License

[MIT License](https://github.com/toine08/ollamaGPT/blob/main/LICENSE)
