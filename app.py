from flask import Flask, render_template, render_template_string
import markdown2
import re
import os

app = Flask(__name__)
projects = [
    {
        "id": "sweetviz",
        "name": "SweetViz",
        "desc": "Lorem Ipsum is a standard placeholder text used in the printing and typesetting industry. It originates from a scrambled section of De Finibus Bonorum et Malorum, a work by Cicero written in 45 BC. Designers and developers use Lorem Ipsum to fill spaces in layouts, allowing them to focus on design rather than content. The text has no real meaning but mimics natural language patterns, making it ideal for mockups and prototypes. Over time, it has become the industry standard for testing typography, readability, and visual balance in digital and print media. Many online generators can create Lorem Ipsum text of any length.",
        "github": "https://github.com/VITB-Tigers/SweetViz-Python-Library",
        "blog": "/sweetviz",
        "link":"http://capstone.vanshr.live:8501/"
    },
    {
        "id": "image-recognition",
        "name": "Image Recognition",
        "github": "https://github.com/example/image-recognition",
        "website": "https://image-recognition.example.com",
        "blog": "image-recognition",
        "desc": "Lorem Ipsum is a standard placeholder text used in the printing and typesetting industry. It originates from a scrambled section of De Finibus Bonorum et Malorum, a work by Cicero written in 45 BC. Designers and developers use Lorem Ipsum to fill spaces in layouts, allowing them to focus on design rather than content. The text has no real meaning but mimics natural language patterns, making it ideal for mockups and prototypes. Over time, it has become the industry standard for testing typography, readability, and visual balance in digital and print media. Many online generators can create Lorem Ipsum text of any length."

    },
    {
        "id": "recommendation-system",
        "name": "Recommendation System",
        "github": "https://github.com/example/recommendation-system",
        "website": "https://recommendation.example.com",
        "blog": "recommendation-system",
        "blogcontent": "lorem50sjkcajscbjksabdkjabddakdbajsbdbdkjsabdakdbakjsbdjkbd",
        "desc": "Lorem Ipsum is a standard placeholder text used in the printing and typesetting industry. It originates from a scrambled section of De Finibus Bonorum et Malorum, a work by Cicero written in 45 BC. Designers and developers use Lorem Ipsum to fill spaces in layouts, allowing them to focus on design rather than content. The text has no real meaning but mimics natural language patterns, making it ideal for mockups and prototypes. Over time, it has become the industry standard for testing typography, readability, and visual balance in digital and print media. Many online generators can create Lorem Ipsum text of any length."

    },
    {
        "id": "text-summarizer",
        "name": "Text Summarizer",
        "github": "https://github.com/example/text-summarizer",
        "website": "https://text-summarizer.example.com",
        "blog": "text-summarizer",
        "blogcontent": "lorem50sjkcajscbjksabdkjabddakdbajsbdbdkjsabdakdbakjsbdjkbd",
        "desc": "Lorem Ipsum is a standard placeholder text used in the printing and typesetting industry. It originates from a scrambled section of De Finibus Bonorum et Malorum, a work by Cicero written in 45 BC. Designers and developers use Lorem Ipsum to fill spaces in layouts, allowing them to focus on design rather than content. The text has no real meaning but mimics natural language patterns, making it ideal for mockups and prototypes. Over time, it has become the industry standard for testing typography, readability, and visual balance in digital and print media. Many online generators can create Lorem Ipsum text of any length."

    },
    {
        "id": "voice-assistant",
        "name": "Voice Assistant",
        "github": "https://github.com/example/voice-assistant",
        "website": "https://voice-assistant.example.com",
        "blog": "voice-assistant",
        "blogcontent": "lorem50sjkcajscbjksabdkjabddakdbajsbdbdkjsabdakdbakjsbdjkbd",
        "desc": "Lorem Ipsum is a standard placeholder text used in the printing and typesetting industry. It originates from a scrambled section of De Finibus Bonorum et Malorum, a work by Cicero written in 45 BC. Designers and developers use Lorem Ipsum to fill spaces in layouts, allowing them to focus on design rather than content. The text has no real meaning but mimics natural language patterns, making it ideal for mockups and prototypes. Over time, it has become the industry standard for testing typography, readability, and visual balance in digital and print media. Many online generators can create Lorem Ipsum text of any length."

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

    return render_template("blog_template.html", content=html_content)


if __name__ == "__main__":
    app.run(debug=True)



















