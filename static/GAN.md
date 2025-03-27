<br><h1>GAN-Showcase: Mock Data Generation for Any Dataset</h1>
<h1>Business Case</h1>
In many real-world scenarios, datasets may be insufficient for training robust machine learning models due to limited data availability, privacy concerns, or regulatory restrictions. The GAN-Showcase project provides a solution by generating synthetic data that mimics real-world trends and patterns. This enables organizations to enhance data volume, preserve privacy, and ensure compliance without compromising sensitive information.

<h1>Industry Applications</h1>
- Healthcare: Generate synthetic patient records for model training without exposing real patient data.
- Finance: Create transaction datasets that follow market trends while maintaining privacy.
- Retail: Augment sales data for demand forecasting models.
- Telecommunications: Produce synthetic churn data to study customer attrition patterns.

<h1>Problem Statement</h1>
Many industries face challenges when working with limited datasets or handling sensitive data. Training models on small datasets can lead to overfitting, while using private data raises ethical and legal concerns. The GAN-Showcase solves this by leveraging Generative Adversarial Networks (GANs) to create synthetic data that retains the statistical properties of real data.

<h1>Objective</h1>
This project aims to provide a scalable and configurable pipeline to generate synthetic datasets based on any given structured dataset while maintaining:
- Feature Distribution Consistency
- Trend Preservation
- Data Privacy Compliance

<h1>Directory Structure</h1>
<pre>
├── code/
│   ├── __pycache__/          # Compiled Python files
│   ├── app.py                # Main application script
│   ├── generate.py           # Script to generate synthetic data
│   ├── ingest_transform.py   # Data ingestion and transformation
│   ├── train.py              # GAN training script
│   ├── load.py               # Script to load trained models
│
├── data/
│   ├── master/               # Original dataset storage
│   │   ├── input_dataset.csv # User-provided dataset
│   ├── pretrained_models/    # Pretrained GAN models
│   ├── saved_models/         # Models trained by the user
│
├── requirements.txt          # Dependencies
├── .gitignore               # Ignore files for version control
├── README.md                # Project documentation
</pre>

<h1>Data Definition</h1>
The synthetic dataset generated will preserve the key attributes of the input dataset, including:
- Demographic Information (if applicable)
- Transaction/Behavioral Data
- Numerical & Categorical Features
- Time-Series Trends (if included in dataset)

<h1>Program Flow</h1>
<h3>Data Ingestion:</h3>
- Load user-provided dataset (input_dataset.csv).
- Preprocess the data (encoding categorical variables, handling missing values, scaling numerical fields).

<h3>Model Training:</h3>
- Train a GAN model on the dataset to learn its distribution.
- Save trained models for future use.

<h3>Synthetic Data Generation:</h3>
- Use pretrained or self-trained GAN models to generate synthetic data.
- Export the generated data for analysis and model training.

<h3>Interactive Web Application:</h3>
A Streamlit-based UI enables users to upload data, configure training, and generate synthetic data easily.

<h1>Steps to Run</h1>
<h3>1. Setup Virtual Environment (Recommended)</h3>
To ensure dependencies are managed properly, create a Conda virtual environment:
<pre>
# Create a new Conda environment with Python 3.11.5
conda create --name gan-showcase-env python=3.11.5 -y

# Activate the environment
conda activate gan-showcase-env
</pre>

<h3>2. Install Dependencies</h3>
Once the environment is activated, install the required packages:
<pre>
pip install -r requirements.txt
</pre>

<h3>3. Launch Application</h3>
Run the Streamlit application:
<pre>
streamlit run code/app.py
</pre>
The app will open in your default web browser.

<h3>4. Model Configuration</h3>
- Navigate to the Model Config tab.
- Enter the path where your training data is located.
Example:
<pre>
data/master
</pre>
- Click "Use this Data Path" to confirm.

<h3>5. Model Training</h3>
- Go to the Model Training tab.
- Set the number of epochs (recommended: start with 100).
- Click "Train GAN Model" and wait for training to complete. Progress will be shown in the status bar.

<h3>6. Generate Synthetic Data</h3>
- Navigate to the Data Generation tab.
- Select the number of samples to generate.
- Choose a model type:
  - Pretrained GAN for quick results.
  - Self-trained GAN to use your custom-trained model.
- Click "Generate Fake Data" and download the generated data as a CSV.

<h1>Notes</h1>
- Ensure that the dataset provided follows a structured format (CSV).
- Preprocessing and encoding of categorical variables should be performed before training.
- Duplicate entries in synthetic data may appear; deduplication may be necessary before use.

This project provides a robust foundation for organizations looking to create synthetic data that retains real-world trends while ensuring privacy and compliance.