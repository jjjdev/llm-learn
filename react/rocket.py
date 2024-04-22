from openai import OpenAI
import streamlit as st

# create client
client = OpenAI(
    api_key='notactuallycallingChatGPTsothisisjunk',
    base_url='http://localhost:8000/v1'
)

st.title('🚀 Llama Server')
prompt = st.chat_input('Pass Your Prompt Here:')

# if user types a prompt and hits enter
if prompt:
    st.chat_message('user').markdown(prompt)

    # chat completion
    response = client.chat.completions.create(
        # specify model we want to use
        model = '~/repos/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf',
        # specify prompt
        messages=[{
            "role": "user", 
            "content": "You are a helpful assistant."}, 
            {"role": "user", 
            "content": prompt}], 
            # add stream
            stream=True
    )

    with st.chat_message('ai'):
        completed_msg = ""
        message = st.empty()


        for chunk in response:

            #response = chunk.choices[0].delta.content
            if chunk.choices[0].delta.content is not None:
                completed_msg += chunk.choices[0].delta.content
                message.markdown(completed_msg)
                #print(response, flush=True, end="")
