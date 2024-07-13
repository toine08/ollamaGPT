import requests
import json
import streamlit as st

baseURL = "http://127.0.0.1:11434"
promptURL = baseURL + "/api/chat"
showModelURL = baseURL + "/api/tags"


def modelQuery():
    try:
        response = requests.get(showModelURL)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        models = response.json()
        models_name = models["models"]
        return models_name
    except requests.exceptions.RequestException:
        st.info("Server is off. Please start Ollama by opening Ollama or running the command ```ollama serve``` from your terminal")
        return []

def queryOllama():
    try:
        response = requests.get(baseURL)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def promptQuery(messagesHistory):
    data = {"model": modelName, "messages": messagesHistory, "stream": False}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    try:
        response = requests.post(promptURL, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an HTTPError for bad responses
        text = response.json()["message"]["content"]
        print(text)
        return text
    except requests.exceptions.RequestException:
         st.info("Server is off. Please start Ollama by opening Ollama or running the command ```ollama serve``` from your terminal")

modelList = modelQuery()
modelName = modelList[0]["name"]

def main():
    if not queryOllama():
        st.info("Server is off. Please start Ollama by opening Ollama or running the command ```ollama serve``` from your terminal")

    with st.sidebar:
        if modelList:
            st.text(f'Currently running on: {modelName}')
        else:
            st.text('No models available')

    st.title("Ollama GPT 🦙")

    if "messages" not in st.session_state or len(st.session_state["messages"]) == 0:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    messages = st.session_state.get("messages", [])

    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    if user_input := st.chat_input():
        if not queryOllama():
            st.info("Server is off. Please start Ollama by opening Ollama or running the command ```ollama serve``` from your terminal")

        messages.append({"role": "user", "content": user_input})

        st.chat_message("user").write(user_input)
        st.session_state["messages"] = messages
        response = promptQuery(st.session_state["messages"])
        messages.append({"role": "assistant", "content": response})
        st.session_state["messages"] = messages
        st.chat_message("assistant").write(response)

if __name__ == "__main__":
    main()
