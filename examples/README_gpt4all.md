# CustomTkinter + GPT4All Example

This example demonstrates how to integrate GPT4All with a CustomTkinter GUI application.

## Prerequisites

- Python 3.7 or higher
- Internet connection for initial model download

## Installation

1. Clone or download the CustomTkinter repository:
   ```bash
   git clone https://github.com/TomSchimansky/CustomTkinter.git
   cd CustomTkinter
   ```

2. Install the required packages:
   ```bash
   pip install -e .
   ```

   This will install CustomTkinter and GPT4All.

## Setup

No API keys are required. GPT4All runs entirely locally after the model is downloaded.

## Running the Example

Run the example script:
```bash
python examples/gpt4all_example.py
```

A window will appear with:
- A field to enter your prompt
- Send and Clear buttons
- A response area

## System Requirements

- **Minimum**: 4GB RAM, 4GB free disk space
- **Recommended**: 8GB RAM, 8GB free disk space
- **Model**: Downloads ~2.2GB Phi-3-mini model on first run

## Features

- Local AI using GPT4All
- Simple chat interface
- Conversation clearing
- Modern GUI with dark theme

## Troubleshooting

- If you get a "no display" error, ensure you're running on a machine with a graphical desktop.
- First run may take time to download the model.
- Ensure sufficient disk space for the model download.
