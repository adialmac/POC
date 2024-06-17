from gradio_client import Client

client = Client("ajamwal13/POC2")
result = client.predict(
		query="Hello!!",
		api_name="/predict"
)
print(result)
