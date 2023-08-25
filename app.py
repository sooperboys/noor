import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful, kind, professional AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Chat bot by Noor",
             description="Ask any Quiery you want Also some special credit to my parents :)",
             theme="compact").launch(share=True)