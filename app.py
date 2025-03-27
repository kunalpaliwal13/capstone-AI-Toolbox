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
        "desc": "Lorem Ipsum is a standard placeholder text used in the printing and typesetting industry. It originates from a scrambled section of De Finibus Bonorum et Malorum, a work by Cicero written in 45 BC. Designers and developers use Lorem Ipsum to fill spaces in layouts, allowing them to focus on design rather than content. The text has no real meaning but mimics natural language patterns, making it ideal for mockups and prototypes. Over time, it has become the industry standard for testing typography, readability, and visual balance in digital and print media. Many online generators can create Lorem Ipsum text of any length.",
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
        "desc": "Lorem Ipsum is a standard placeholder text used in the printing and typesetting industry. It originates from a scrambled section of De Finibus Bonorum et Malorum, a work by Cicero written in 45 BC. Designers and developers use Lorem Ipsum to fill spaces in layouts, allowing them to focus on design rather than content. The text has no real meaning but mimics natural language patterns, making it ideal for mockups and prototypes. Over time, it has become the industry standard for testing typography, readability, and visual balance in digital and print media. Many online generators can create Lorem Ipsum text of any length."

    },
    {
        "id": "GAN",
        "name": "GAN",
        "github": "https://github.com/VITB-Tigers/GAN-Project",
        "link": "https://recommendation.example.com",
        "blog": "GAN",
        "blogcontent": "lorem50sjkcajscbjksabdkjabddakdbajsbdbdkjsabdakdbakjsbdjkbd",
        "desc": "Lorem Ipsum is a standard placeholder text used in the printing and typesetting industry. It originates from a scrambled section of De Finibus Bonorum et Malorum, a work by Cicero written in 45 BC. Designers and developers use Lorem Ipsum to fill spaces in layouts, allowing them to focus on design rather than content. The text has no real meaning but mimics natural language patterns, making it ideal for mockups and prototypes. Over time, it has become the industry standard for testing typography, readability, and visual balance in digital and print media. Many online generators can create Lorem Ipsum text of any length."

    },
    {
        "id": "autoviz",
        "name": "AutoViz",
        "github": "https://github.com/VITB-Tigers/AutoViz-Python-Library",
        "link": "/",
        "blog": "autoviz",
        "blogcontent": "lorem50sjkcajscbjksabdkjabddakdbajsbdbdkjsabdakdbakjsbdjkbd",
        "desc": "Lorem Ipsum is a standard placeholder text used in the printing and typesetting industry. It originates from a scrambled section of De Finibus Bonorum et Malorum, a work by Cicero written in 45 BC. Designers and developers use Lorem Ipsum to fill spaces in layouts, allowing them to focus on design rather than content. The text has no real meaning but mimics natural language patterns, making it ideal for mockups and prototypes. Over time, it has become the industry standard for testing typography, readability, and visual balance in digital and print media. Many online generators can create Lorem Ipsum text of any length."

    },
    {
        "id": "rag",
        "name": "RAG",
        "github": "https://github.com/VITB-Tigers/RAG-Project",
        "link": "/",
        "blog": "rag",
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