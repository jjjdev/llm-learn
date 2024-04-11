from openai import OpenAI
import streamlit as st
import instructor
from pydantic import BaseModel
from stock_data import get_stock_prices

# create client
client = OpenAI(
    api_key='notactuallycallingChatGPTsothisisjunk',
    base_url='http://localhost:8000/v1'
)

# patched client
client = instructor.patch(client=client)

# Structure what we want extracted
class ResponseModel(BaseModel):
    ticker:str
    days:int

st.title('Rocket🚀 Llama Server')
prompt = st.chat_input('Pass Your Prompt Here:')

# if user types a prompt and hits enter
if prompt:
    st.chat_message('user').markdown(prompt)

    # Function calling LLM call
    response = client.chat.completions.create(
        # specify model we want to use
        #model = '~/repos/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf',
        model="mistral-function-calling",
        # specify prompt
        messages=[{"role": "user", "content": prompt}], 
        
        # add stream
        #stream=True

        # need to use Functionary Chat Format
        response_model = ResponseModel,
    )

    st.chat_message("ai").markdown(response)

   # if there's a problem, display an error to the user
    try:
        prices = get_stock_prices(response.ticker, response.days)
        st.chat_message("ai").markdown(prices)
    except Exception as e:
        st.chat_message("ai").markdown('😥 Minor Error in my programming' + str(e))


    # with st.chat_message('ai'):
    #     completed_msg = ""
    #     message = st.empty()


    #     for chunk in response:

    #         #response = chunk.choices[0].delta.content
    #         if chunk.choices[0].delta.content is not None:
    #             completed_msg += chunk.choices[0].delta.content
    #             message.markdown(completed_msg)
    #             #print(response, flush=True, end="")

# the prompt
    # summarize the stock price movements for AAPL for the past 7 days
