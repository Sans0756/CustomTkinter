import customtkinter
from gpt4all import GPT4All

# Initialize GPT4All model
model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf")  # Downloads automatically on first run

# Create GUI
app = customtkinter.CTk()
app.geometry("400x500")
app.title("Luna AI")

# Chat display
chat_display = customtkinter.CTkTextbox(app, width=350, height=300, state="normal")
chat_display.pack(pady=20)

# User input
user_input = customtkinter.CTkEntry(app, width=350, placeholder_text="Type your message...")
user_input.pack(pady=10)

# Send button
def send_message():
    user_text = user_input.get()
    if not user_text.strip():
        return
    
    chat_display.insert("end", f"You: {user_text}\n")
    user_input.delete(0, "end")
    
    response = model.generate(user_text, max_tokens=200)
    chat_display.insert("end", f"Luna: {response}\n\n")
    chat_display.see("end")

send_button = customtkinter.CTkButton(app, text="Send", command=send_message)
send_button.pack(pady=10)

app.mainloop()