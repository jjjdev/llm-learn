from openai import OpenAI

# create client
client = OpenAI(
    api_key='notneededsothisisjunk',
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
)

# print a response
print (response)