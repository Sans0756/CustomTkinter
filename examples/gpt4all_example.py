import os
import sys
import logging

# Only check DISPLAY on Unix-like systems (Linux/macOS)
if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    if not os.environ.get("DISPLAY"):
        sys.exit(
            "Unable to start the GUI because no display is available. "
            "Set DISPLAY or run this on a machine with a graphical environment."
        )

import customtkinter

try:
    from gpt4all import GPT4All
except ImportError as e:
    raise ImportError(
        f"Required package missing: {e}. Install with `pip install gpt4all`."
    )

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Global variables
model = None

def load_model():
    global model
    if model is None:
        logging.info("Loading GPT4All model...")
        try:
            # Use a lightweight model suitable for basic hardware
            model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf")  # ~2.3GB, fast and efficient
            logging.info("GPT4All model loaded successfully.")
        except Exception as e:
            logging.error(f"Failed to load model: {e}")
            return f"Failed to load model: {e}"
    return None

def send_prompt():
    user_prompt = prompt_entry.get().strip()
    if not user_prompt:
        logging.warning("No prompt entered.")
        return

    # Load model if not loaded
    error = load_model()
    if error:
        response_textbox.configure(state="normal")
        response_textbox.delete("0.0", "end")
        response_textbox.insert("0.0", error)
        response_textbox.configure(state="disabled")
        return

    # Clear previous response
    response_textbox.configure(state="normal")
    response_textbox.delete("0.0", "end")
    response_textbox.insert("0.0", "Generating response...\n")
    response_textbox.configure(state="disabled")
    app.update_idletasks()

    try:
        logging.info("Generating response with GPT4All...")
        # Generate response
        response = model.generate(user_prompt, max_tokens=200)
        ai_response = response.strip()

        # Display response
        response_textbox.configure(state="normal")
        response_textbox.delete("0.0", "end")
        response_textbox.insert("0.0", f"You: {user_prompt}\n\nAI: {ai_response}")
        response_textbox.configure(state="disabled")
        logging.info("Response generated successfully.")
    except Exception as e:
        logging.error(f"GPT4All error: {e}")
        response_textbox.configure(state="normal")
        response_textbox.delete("0.0", "end")
        response_textbox.insert("0.0", f"Error: {e}")
        response_textbox.configure(state="disabled")

def clear_conversation():
    response_textbox.configure(state="normal")
    response_textbox.delete("0.0", "end")
    response_textbox.configure(state="disabled")
    logging.info("Conversation cleared.")

# GUI Setup
app = customtkinter.CTk()
app.title("CustomTkinter + GPT4All Chat")
app.geometry("800x600")

# Main frame
main_frame = customtkinter.CTkFrame(app)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Title
title_label = customtkinter.CTkLabel(main_frame, text="GPT4All Chat", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Prompt entry
prompt_entry = customtkinter.CTkEntry(main_frame, placeholder_text="Enter your message here...", width=600)
prompt_entry.pack(pady=10)

# Buttons frame
buttons_frame = customtkinter.CTkFrame(main_frame, fg_color="transparent")
buttons_frame.pack(pady=10)

send_button = customtkinter.CTkButton(buttons_frame, text="Send", command=send_prompt)
send_button.pack(side="left", padx=10)

clear_button = customtkinter.CTkButton(buttons_frame, text="Clear", command=clear_conversation)
clear_button.pack(side="left", padx=10)

# Response textbox
response_textbox = customtkinter.CTkTextbox(main_frame, wrap="word", height=400)
response_textbox.pack(pady=10, fill="both", expand=True)
response_textbox.configure(state="disabled")

# Run the app
if __name__ == "__main__":
    app.mainloop()
