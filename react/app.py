from openai import OpenAI

# create client
client = OpenAI(
    api_key='notactuallycallingChatGPTsothisisjunk',
    base_url='http://localhost:8080/v1'
)

# chat completion
response = client.chat.completions.create(
    # specify model we want to use
    model = '~/repos/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf',
    # specify prompt
    messages=[{
        "role": "user", 
        "content": "You are a helpful assistant."}, 
        {"role": "user", 
         "content": "What is ROI in reference to finance?"}], 
         # add stream
         stream=True
)

# print a full response
#print (response)

# print response text only
#print (response.choices[0].message.content)

for chunk in response:
    # Print streamed tokens
    #print(chunk)
    response = chunk.choices[0].delta.content
    if response is not None:
        print(response, flush=True, end="")
