# PandasAI with Llama3 for Interactive Data Analysis

Welcome to the **PandasAI with Llama3** project! This Streamlit-based web application empowers users to perform intuitive data analysis using natural language queries on CSV datasets, leveraging the power of Llama3 and PandasAI.

---

## Introduction

This project combines the capabilities of the `PandasAI` library and a local instance of the `Llama3` language model to provide seamless, conversational data analysis. With a clean, glassmorphism-inspired UI, users can upload CSV files, ask questions about the data, and receive insightful answers.

## Features

- **Upload CSV Files**: Easily upload your data in CSV format.
- **Natural Language Queries**: Ask questions about your data and get answers powered by Llama3.
- **Error Handling**: Robust handling of malicious queries and errors.
- **Glassmorphism UI**: A visually appealing interface built with Streamlit.
- **Detailed Data Insights**: View the data preview and basic statistics.

## Installation

### Prerequisites

- Python 3.9 or higher
- `pip` package installer

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Pratik-Khose/PandasAI-with-Llama3.git
   cd PandasAI-with-Llama3

Install Dependencies

bash
Copy code
pip install -r requirements.txt
Run the Application

bash
Copy code
streamlit run main.py
Access the App

Open your browser and go to: http://localhost:8501
Usage
Launch the app using streamlit run main.py.
Upload your CSV file through the file uploader.
Enter a natural language query to ask questions about your data.
Click "Generate Analysis" to get responses powered by PandasAI and Llama3.
How It Works
The application is divided into multiple components:

Streamlit UI: Uses HTML and CSS to create a clean glassmorphism design.
Data Handling: Processes CSV uploads and initializes a SmartDataframe using PandasAI.
LLM Integration: Uses LocalLLM to handle queries and generate responses.
Error Management: Handles common errors like MaliciousQueryError and NoResultFoundError.
Tech Stack
Streamlit: Frontend framework for building interactive web apps.
PandasAI: Library for natural language data analysis.
Llama3: Local Language Model for query processing.
Pandas: For data manipulation and analysis.
Contributing
We welcome contributions to improve this project! Here's how you can get started:

Fork the project.
Create a feature branch: git checkout -b feature-name.
Commit your changes: git commit -m 'Add feature'.
Push to the branch: git push origin feature-name.
Open a Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Links
GitHub Repository: PandasAI with Llama3
Video Demonstration: Watch on YouTube
LinkedIn: Connect with me
Feel free to explore and contribute to the project!

Thank you for checking out this project! If you have any questions or suggestions, feel free to open an issue or reach out via LinkedIn.
