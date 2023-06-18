# DB Pro

This is a Python script that interacts with a database and provides a conversational interface using OpenAI's ChatGPT model. The script connects to a MySQL database, retrieves the structure of the tables, and allows users to query the database using natural language.

## Prerequisites

To run this script, you need the following:

- Python (version 3.6 or higher)
- MySQL Server
- Required Python packages: `openai`, `gradio`, `pymysql`

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/db-pro.git
   ```

2. Install the required Python packages using pip:

   ```
   pip install openai gradio pymysql
   ```

3. Set up the MySQL database:
   - Make sure you have a running MySQL server with the necessary credentials.
   - Update the connection details in the script (`host`, `user`, `password`, `database`) to match your MySQL server configuration.

4. Set up the OpenAI API:
   - Obtain an OpenAI API key from the OpenAI website.
   - Replace `'openAI_API_Key'` with your actual API key in the script.

## Usage

1. Run the script:

   ```
   python db_pro.py
   ```

2. Once the script is running, you can access the conversational interface through a web browser.
3. Enter your queries or statements in the provided input box and press Enter to interact with the ChatGPT model.
4. The model will provide responses based on the conversation history and the structure of the database tables.

## Important Note

- Please ensure the security of your MySQL database and OpenAI API key. Do not share them publicly or expose them to unauthorized access.
