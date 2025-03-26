from flask import Flask, render_template, render_template_string
import markdown2
import re
import os

app = Flask(__name__)

# Sample AI Projects Data
projects = [
    {
        "id": "ai-chatbot",
        "name": "SweetViz",
        "desc": "Lorem Ipsum is a standard placeholder text used in the printing and typesetting industry. It originates from a scrambled section of De Finibus Bonorum et Malorum, a work by Cicero written in 45 BC. Designers and developers use Lorem Ipsum to fill spaces in layouts, allowing them to focus on design rather than content. The text has no real meaning but mimics natural language patterns, making it ideal for mockups and prototypes. Over time, it has become the industry standard for testing typography, readability, and visual balance in digital and print media. Many online generators can create Lorem Ipsum text of any length.",
        "github": "https://github.com/example/ai-chatbot",
        "website": "https://ai-chatbot.example.com",
        "blog": "ai-chatbot",
        "blogcontent": '''
                    <h1>Introduction to SweetViz</h1>
                    Exploratory Data Analysis (EDA) is a crucial step in any data science project. SweetViz is a Python library designed to automate EDA, providing visual and detailed insights into datasets with just a few lines of code.
                    This blog post explores the SweetViz-Python-Library repository, explaining its usage, features, and how you can leverage it for your data analysis needs.<br>
                    <h1>Why Use SweetViz for EDA?</h1>
                    Manual EDA can be time-consuming, requiring multiple visualization and statistical functions. SweetViz simplifies this process by:
                    <ul><br>
                        <li>Generating a comprehensive HTML report in seconds.</li>
                        <li>Providing visual comparisons between datasets.</li>
                        <li>Automatically highlighting key statistics.</li>
                        <li>Offering correlation insights and data imbalances.</li>
                        <li>This makes it an excellent choice for beginners and experienced data scientists alike.</li>\
                    </ul>
                    <h1>Features of SweetViz</h1>
                    SweetViz comes packed with features to streamline EDA:
                    <ul><br>
                        <li>Automatic data profiling (mean, median, missing values, etc.).</li>
                        <li>Correlation analysis using interactive visualizations.</li>
                        <li>Comparison reports for train vs. test datasets.</li>
                        <li>Feature distribution analysis with histograms and density plots.</li>
                        <li>Target analysis to understand the impact of variables on the target column.</li>
                    </ul>

                    <h1>Installation and Setup</h1>
                    Setting up SweetViz is straightforward. Ensure you have Python installed and use the following commands:

                    <ol>
                    <li>Clone the repository:</li>
                    <pre><code>git clone https://github.com/VITB-Tigers/SweetViz-Python-Library</code></pre>
                    <li>Create and activate a virtual environment (recommended).</li> 
                    If using Conda:
                        <pre>conda create -n env_name python==3.10.15 -y</pre>
                        <pre>conda activate env_name</pre>
                    <li>Install dependencies:</li>
                    <pre>pip install -r requirements.txt</pre></ol>


                    <h1>Using SweetViz for Data Analysis</h1>
                    SweetViz works seamlessly with pandas DataFrames. Below is an example usage:
                    <ol><br>
                        <li>i. Start the Streamlit application:
                        <pre>streamlit run source/app.py</pre>

                        <li>ii. Access the web interface a
                        <pre> http://localhost:8501 </pre>
                        <br><img src="/static/images/sweetviz.png" alt="Sweetviz Report"><br><br>
                        <li> Upload your CSV dataset and generate EDA reports!</li>
                    </ol>
                    <h1>Visualizing and Interpreting Reports</h1>
                    After running the Generate Full Report, you will get:
                    <br><img src="/static/images/sweetviz.png" alt="Sweetviz Report"><br><br>
                    <ul>
                    <li>General statistics about each column.</li>
                    <li>Feature distributions for numerical and categorical data.</li>
                    <li>Correlation heatmaps showing relationships between variables.</li>
                    <li>Missing value summaries</li>
                    </ul>

                    <br><img src="/static/images/sweetviz.png" alt="Sweetviz Report"><br><br>
                    This intuitive visualization helps identify potential data preprocessing steps.
                    <h1>Customization and Advanced Usage</h1>
                    SweetViz also supports advanced customization:
                    <br><img src="/static/images/sweetviz.png" alt="Sweetviz Report"><br><br>
                    <b>Comparing Two Datasets</b>
                    To compare a training and test dataset:
                    <br><img src="/static/images/sweetviz.png" alt="Sweetviz Report"><br><br>
                    <br><img src="/static/images/sweetviz.png" alt="Sweetviz Report"><br><br>

                    <b>Target Variable Analysis</b>
                    You can analyze how features impact a specific target variable:
                    <br><img src="/static/images/sweetviz.png" alt="Sweetviz Report"><br><br>
                    <br><img src="/static/images/sweetviz.png" alt="Sweetviz Report"><br><br>
                    <h1>Conclusion</h1>
                    SweetViz is a must-have tool for automated, quick, and insightful exploratory data analysis. Whether you are handling small datasets or large-scale projects, this library saves time and enhances data understanding.
                    Check out the SweetViz-Python-Library repository here to explore the code and contribute!










                    
                    
                    
                    
                    '''
    },
    {
        "id": "image-recognition",
        "name": "Image Recognition",
        "github": "https://github.com/example/image-recognition",
        "website": "https://image-recognition.example.com",
        "blog": "image-recognition",
        "blogcontent": "lorem50sjkcajscbjksabdkjabddakdbajsbdbdkjsabdakdbakjsbdjkbd",
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

file_path = "static\\x.md"
@app.route("/")
def home():
    return render_template("index.html", projects=projects)

@app.route("/blog/<project_id>")
def blog(project_id):
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return "Project not found", 404
    return render_template("blog.html", project=project)

@app.route("/blogs")
def blogs():
    return render_template("blogs.html", projects=projects)


def convert_markdown(md_text):
    """Convert Markdown to HTML and apply custom classes to h2 and ul tags."""
    html_content = markdown2.markdown(md_text, extras=["fenced-code-blocks"])
    html_content = re.sub(r'<img(.*?)>', r'<img\1 class="custom-image">', html_content)

    
    return html_content


@app.route("/trial")
def trial():
    md_path = os.path.join("static", "x.md")  # Ensure correct path
    if not os.path.exists(md_path):
        return "Markdown file not found!", 404

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Convert Markdown to HTML
    html_content = convert_markdown(md_content)

    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Markdown Viewer</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    </head>
    <body>
    <nav class="navbar">
        <div class="logo">AI Project Hub</div>
        <ul class="nav-links">
            <li><a href="/">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#features">Features</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
     <div class="blog-body">
    <section class="cta-blog">
        {{ content|safe }}
    </section>
    </div>
    <script src="{{ url_for('static', filename='script.js') }}"></script>
    </body>
    </html>
    """
    return render_template_string(template, content=html_content)




if __name__ == "__main__":
    app.run(debug=True)
