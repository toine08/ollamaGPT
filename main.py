import requests
import json
import streamlit as st

baseURL = "http://127.0.0.1:11434"
promptURL = baseURL + "/api/chat"
showModelURL = baseURL + "/api/tags"


def modelQuery():
    response = requests.get(showModelURL)
    models = response.json()
    return models["models"]

def queryOllama():
    if requests.get(baseURL) == 200:
        return False
    return True
def promptQuery(messagesHistory):
    data = {"model": "mistral", "messages": messagesHistory, "stream": False}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.post(promptURL, headers=headers, data=json.dumps(data))
    text = response.json()["message"]
    print(text)
    return text


#print("RESPONSE",promptQuery(userPrompt))
modelList = modelQuery()
def main():
    with st.sidebar:
        st.text(f'Currently Running: {modelList[0]["name"]}')

st.title("Ollama GPT")


if "message" not in st.session_state:
    st.session_state["messages"] = [{"role":"assistant", "content": "How can I help you ?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(key=msg):
    if queryOllama() == False:
        st.info("Server is off please start ollama by opening ollama or running the command ```ollama serve``` from your terminal")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    print("MESSAGES", st.session_state.messages)
    response = promptQuery(st.session_state.messages)
    print("RESPONSE", response)
    msg = response["content"]
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)





if __name__ == "__main__":
    main()
