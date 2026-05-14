import gradio as gr
import requests

BACKEND_URL = "http://backend:8000/predict"

def predict(number):

    response = requests.post(
        BACKEND_URL,
        json={"number": number}
    )

    return response.json()["prediction"]

iface = gr.Interface(
    fn=predict,
    inputs=gr.Number(),
    outputs=gr.Number(),
    title="S3 Model Inference App"
)

iface.launch(server_name="0.0.0.0", server_port=7860)