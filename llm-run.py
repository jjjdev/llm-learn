from huggingface_hub import hf_hub_download
from llama_cpp import Llama

# Define model name and file name
#model_name = "TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF"
#model_file = "mixtral-8x7b-instruct-v0.1.Q4_K_M.gguf"

# Mixtral Instruct 
model_name = "TheBloke/Mistral-7B-OpenOrca-GGUF"
model_file = "mistral-7b-openorca.Q4_K_M.gguf"

# Vicuna
#model_name = "TTheBloke/vicuna-13B-v1.5-16K-GGUF"
#model_file = "vicuna-13b-v1.5-16k.Q4_K_M.gguf"

# Download the model
model_path = hf_hub_download(model_name, filename=model_file)


model_kwargs = {
  "n_ctx":4096,    # Context length to use
  "n_threads":4,   # Number of CPU threads to use
  "n_gpu_layers":31,  # Number of model layers to offload to GPU. Set to 0 to use just the CPU
}

# Instantiate model from downloaded file
llm = Llama(model_path=model_path, model_kwargs)

# Generation kwargs
generation_kwargs = {
    "max_tokens":512, # Max number of new tokens to generate
    "stop":["<|endoftext|>", "</s>"], # Text sequences to stop generation on
    "echo":False, # Echo the prompt in the output
    "top_k":1 # This is essentially greedy decoding, since the model will always return the highest-probability token. Set this value > 1 for sampling decoding
}

# Run inference
prompt = "The meaning of life is "
res = llm(prompt, generation_kwargs) # Res is a dictionary

# Unpack and the generated text from the LLM response dictionary and print it
print(res["choices"][0]["text"])