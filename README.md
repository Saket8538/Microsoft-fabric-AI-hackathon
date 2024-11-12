# Microsoft-fabric-AI-hackathon
# Customer Sentiment Analysis with OpenAI

**Overview**

This repository provides a Python-based implementation of customer sentiment analysis using the OpenAI API. By leveraging the power of advanced language models, this project accurately classifies customer feedback as positive, negative, or neutral.

**Prerequisites**

* **Python (version 3.6 or later)**
* **OpenAI API Key**
* **Required Python libraries:**
  * `openai`
  * `requests`
  * `json`


**Installation**

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Saket8538/Microsoft-fabric-AI-hackathon.git](https://github.com/Saket8538/Microsoft-fabric-AI-hackathon.git)

2. **Install dependencies**
   * `pip install openai requests json`

* **Create and activate a virtual environment:**
  * `python -m venv venv`
  * `.\venv\Scripts\activate ` # On Windows
  * `source venv/bin/activate ` # On macOS/Linux

3. **Install the required packages:**
   * ` pip install -r requirements.txt`

4.**Set up environment variables:**

#Create a .env file in the root directory of the project and add your environment variables.

* `OPENAI_API_KEY=your_openai_api_key`
* `SQL_SERVER=your_sql_server`
* `SQL_DATABASE=your_database_name`
* `SQL_USERNAME=your_database_username`
* `SQL_PASSWORD=your_database_password`

##
Replace placeholders like `your_openai_api_key`, `your_sql_server`, `your_database_name`, `your_database_username`, `your_database_password`, `YourUsername`, `YourRepository`, and `Your Name` with your actual information. 
This [README.md](http://_vscodecontentref_/1) file provides an overview of the project, installation instructions, usage guidelines, and other relevant details.

5.**Usage**
  
   1.*Run the streamlit app:*
      
       python -m run python_file.py
    
    2.*Open the app in your browser:*
       
       The app will be available at http://localhost:8000

**Project structure**

*`app.py`: Main application file containing the Streamlit app and sentiment analysis logic.

*`requirements.txt`: List of required Python packages.

*`.env`: Environment variables file (not included in the repository for security reasons).

*`README.md`: Project documentation.

**Dependencies**

*`streamlit`: Web application framework for creating interactive web apps.

*`pyodbc`: Python library for connecting to ODBC databases.

*`pandas`: Data manipulation and analysis library.

*`matplotlib`: Plotting library for creating visualizations.

*`python-dotenv`: Library for loading environment variables from a .env file.

*`openai`: OpenAI API client library.

**License**

This project is licensed under the MIT License. See the LICENSE file for more details.

**Acknowledgements**

`Streamlit`

`OpenAI`

`pandas`

`matplotlib`

`python-dotenv`

`pyodbc`

**Contributing:**

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
