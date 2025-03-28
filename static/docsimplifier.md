<br><h1>Simplify Your Documents with Document-Simplifier</h1>

<h1>Table of Contents</h1>
- Introduction
- Why Document-Simplifier?
- Key Features
- Installation and Setup
- Usage and Examples
- Project Structure
- Conclusion

<h1>Introduction</h1>
In today's digital age, managing and digesting large documents can be challenging. Document-Simplifier is a tool designed to make text summarization more efficient and accessible. By leveraging transfer learning, it fine-tunes state-of-the-art large language models like Llama-2 on the CNN/Daily Mail dataset to create concise summaries of lengthy documents.

<h1>Why Document-Simplifier?</h1>
Training large language models (LLMs) from scratch requires huge amounts of data and computational power. Document-Simplifier overcomes these challenges by:<br>
- <b>Using Transfer Learning:</b> It adapts pre-trained Llama-2 models, significantly reducing training time and resources.<br>
- <b>Enhancing Summarization:</b> The fine-tuned model is tailored to generate clear, concise, and informative summaries.<br>
- <b>Improving Accessibility:</b> With an easy-to-use setup and clear instructions, it's accessible for users who need quick document simplification without extensive machine learning expertise.

<h1>Key Features</h1><br>
- <strong>Efficient Summarization:</strong> Fine-tunes Llama-2 on a well-known summarization dataset to produce high-quality summaries.
- <strong>Versatile Usage:</strong> Capable of summarizing various types of texts including emails, letters, and news articles.
- <strong>API Ready:</strong> Comes with a FastAPI backend that allows you to deploy the summarizer as a REST API.
- <strong>Prompt Engineering Guide:</strong> Includes a guide on prompt engineering (via LearnWithPrompts.md) to help you get the best out of the model.

<h1>Installation and Setup</h1>
Before using Document-Simplifier, ensure you have:
- Python 3.8 or higher
- pip (Python package manager)
- Git for cloning the repository
- A GPU is recommended for faster inference

<h2>Steps to Install:</h2>

<h3>1. Clone the Repository:</h3>
<pre>
git clone https://github.com/VITB-Tigers/Document-Simplifier.git
cd Document-Simplifier
</pre>

<h3>2. Install Dependencies:</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>3. Download the Pre-trained Model:</h3>
Use the Hugging Face Transformers library to download the pre-trained Llama-2 model:
<pre>
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "meta-llama/Llama-2-7b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
</pre>

<h1>Usage and Examples</h1>

<h2>Basic Summarization</h2>
You can quickly summarize any long text by running:
<pre>
from transformers import pipeline

summarizer = pipeline("summarization", model="meta-llama/Llama-2-7b")
text = """Paste your long document text here. The model will analyze and return a concise summary."""
summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
print(summary[0]['summary_text'])
</pre>

<h2>Running as an API</h2>
Document-Simplifier also provides a FastAPI implementation so you can deploy it as a web service:
<pre>
Start the FastAPI server:
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
</pre>
Access the summarization endpoint at:
<pre>
http://localhost:8000/summarize
</pre>

<h1>Project Structure</h1>
The repository is organized to help you quickly find what you need:
<pre>
Document-Simplifier/
├── models/                  # Pre-trained model files
├── data/                    # Sample datasets for testing
├── app.py                   # FastAPI backend server for the summarizer
├── main.py                  # Main script for running summarization
├── requirements.txt         # Required dependencies
├── README.md                # Project documentation
└── LearnWithPrompts.md      # Guide to prompt engineering for better results
</pre>

<h1>Conclusion</h1>
Document-Simplifier harnesses the power of transfer learning to provide a user-friendly solution for text summarization. Whether you're looking to simplify lengthy articles or deploy a summarization API for your application, this project offers a practical and efficient way to achieve high-quality summaries without the need for massive computational resources.
Explore the repository on <a href="https://github.com/VITB-Tigers/Document-Simplifier">GitHub</a> and start simplifying your documents today!