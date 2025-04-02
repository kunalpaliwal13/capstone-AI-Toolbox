from flask import Flask, render_template, render_template_string
import markdown2
import re
import os

app = Flask(__name__)

# Sample AI Projects Data
projects = [
    {
        "id": "sweetviz",
        "name": "SweetViz",
        "desc": "A Python library that generates beautiful, high-density visualizations for a quick and easy exploration of your data. It helps in analyzing and comparing datasets with clear and interactive reports.",
        "github": "https://github.com/VITB-Tigers/SweetViz-Python-Library",
        "blog": "/sweetviz",
        "link":"http://capstone.vanshr.live:8501/"
    },
    {
        "id": "h2oautoml",
        "name": "H2O Auto-ML",
        "github": "https://github.com/VITB-Tigers/H20AutoML",
        "link": "http://capstone.vanshr.live:8502/",
        "blog": "/h2oautoml",
        "desc": "A comprehensive framework for training AutoML models using H2O's AutoML library. This project includes data ingestion, transformation, and model training functionalities, all accessible through an interactive Streamlit web application."

    },
    {
        "id": "GAN",
        "name": "GAN",
        "github": "https://github.com/VITB-Tigers/GAN-Project",
        "link": "https://recommendation.example.com",
        "blog": "GAN",
        "desc": "Generative Adversarial Network (GAN) for generating realistic synthetic customer churn data to enable predictive modeling and insights without using sensitive customer information."

    },
    {
        "id": "autoviz",
        "name": "AutoViz",
        "github": "https://github.com/VITB-Tigers/AutoViz-Python-Library",
        "link": "/",
        "blog": "autoviz",
        "desc": "A Python library for automatic data visualization that helps users generate insightful visualizations with minimal effort, making data exploration faster and more efficient."

    },
    {
        "id": "rag",
        "name": "RAG",
        "github": "https://github.com/VITB-Tigers/RAG-Project",
        "link": "/",
        "blog": "rag",
        "desc": "A powerful Retrieval-Augmented Generation (RAG) system built with Mistral LLM, offering local document processing and intelligent question answering capabilities."

    },
    {
        "id": "cozyreader",
        "name": "CozyReader",
        "github": "https://github.com/VITB-Tigers/CozyReader",
        "link": "/",
        "blog": "cozyreader",
        "desc": "CozyReader is an AI-powered bedtime storyteller that crafts personalized bedtime stories using advanced AI techniques, aiming to provide engaging and comforting narratives for users."

    },
    {
        "id": "supervisedclassifiers",
        "name": "Supervized Classifiers",
        "github": "https://github.com/VITB-Tigers/Supervised-Classifiers",
        "link": "/",
        "blog": "supervizedclassifiers",
        "desc": "This repository contains various supervised machine learning classifiers implemented in Python, providing tools to train and evaluate models for classification tasks across different datasets."

    },
    {
        "id": "dataex",
        "name": "Data Exploration",
        "github": "https://github.com/VITB-Tigers/DataExploration-Pandas",
        "link": "/",
        "blog": "dataex",
        "desc": "A Python library designed to assist in the data exploration process using Pandas. It provides efficient tools and methods to quickly clean, visualize, and analyze data, aiding in the initial stages of data science workflows."

    },
    {
        "id": "rep",
        "name": "Reinforcement Learning Policies",
        "github": "https://github.com/VITB-Tigers/ReinforcementLearning-Policy",
        "link": "/",
        "blog": "rep",
        "desc": "A repository focused on reinforcement learning algorithms with an emphasis on policy-based method DQN. It provides an implementation to explore various decision-making strategies through interaction with an environment."

    },
    {
        "id": "docsimplifier",
        "name": "Document Simplifier",
        "github": "https://github.com/VITB-Tigers/Document-Simplifier",
        "link": "/",
        "blog": "docsimplifier",
        "desc": "Document-Simplifier utilizes transfer learning to fine-tune large language models like Llama-2 on the CNN/Daily Mail dataset, enhancing text summarization capabilities for efficient and accessible content simplification."

    }
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects)


@app.route("/blogs")
def blogs():
    return render_template("blogs.html", projects=projects)

@app.route("/projlist")
def projlist():
    return render_template("ProjList.html", projects=projects)

def convert_markdown(md_text):
    """Convert Markdown to HTML and apply custom classes to h2 and ul tags."""
    html_content = markdown2.markdown(md_text, extras=["fenced-code-blocks"])
    html_content = re.sub(r'<img(.*?)>', r'<img\1 class="custom-image">', html_content)
    return html_content

@app.route("/blog/<project_id>")
def blog(project_id):
    md_path = os.path.join("static", f"{project_id}.md")  
    if not os.path.exists(md_path):
        return "Markdown file not found!", 404
    abs_path = os.path.abspath(md_path)
    print(f"Looking for file at: {abs_path}")

    if not os.path.exists(md_path):
        return f"Markdown file not found at {abs_path}!", 404

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_content = convert_markdown(md_content)
    print("aa",html_content)

    return render_template("blog_template.html", content=html_content, project_id = project_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

























# @app.route("/sweetviz")
# def trial():
#     md_path = os.path.join("static", "x.md")  # Ensure correct path
#     if not os.path.exists(md_path):
#         return "Markdown file not found!", 404

#     with open(md_path, "r", encoding="utf-8") as f:
#         md_content = f.read()

#     # Convert Markdown to HTML
#     html_content = convert_markdown(md_content)

#     template = """
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Markdown Viewer</title>
#         <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
#     </head>
#     <body>
#     <nav class="navbar">
#         <div class="logo">AI Project Hub</div>
#         <ul class="nav-links">
#             <li><a href="/">Home</a></li>
#             <li><a href="#about">About</a></li>
#             <li><a href="#features">Features</a></li>
#             <li><a href="#projects">Projects</a></li>
#             <li><a href="#contact">Contact</a></li>
#         </ul>
#     </nav>
#      <div class="blog-body">
#     <section class="cta-blog">
#         {{ content|safe }}
#     </section>
#     </div>
#     <script src="{{ url_for('static', filename='script.js') }}"></script>
#     </body>
#     </html>
#     """
#     return render_template_string(template, content=html_content)



# @app.route("/blog/<project_id>")
# def blog(project_id):
#     project = next((p for p in projects if p["id"] == project_id), None)
#     if not project:
#         return "Project not found", 404
#     return render_template("blog.html", project=project)
