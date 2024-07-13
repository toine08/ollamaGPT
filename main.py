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
    if requests.get(baseURL).status_code == 200:
        return True
    return False
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

    if "messages" not in st.session_state or len(st.session_state["messages"]) == 0:
        st.session_state["messages"] = [{"role":"assistant", "content": "How can I help you ?"}]

    messages = st.session_state.get("messages", [])

    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    if user_input := st.chat_input():
        if queryOllama() == False:
            st.info("Server is off please start ollama by opening ollama or running the command ```ollama serve``` from your terminal")
            st.stop()

        messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)
        st.session_state["messages"] = messages
        response = promptQuery(st.session_state["messages"])
        msg = response["content"]
        messages.append({"role": "assistant", "content": msg})
        st.session_state["messages"] = messages
        st.chat_message("assistant").write(msg)




if __name__ == "__main__":
    main()
