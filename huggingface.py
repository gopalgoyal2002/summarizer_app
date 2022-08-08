import requests

API_URL = "https://api-inference.huggingface.co/models/google/pegasus-large"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def summrizer(text:str,minlen=20,maxlen=512):
    output = query({
        "inputs":text,
        "parameters":{
            "min_length":minlen,
            "max_length":maxlen
        }
    })
    print(output)
    return output