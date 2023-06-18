import openai
import gradio
import pymysql
import io
import sys


# Connect to the database
connection = pymysql.connect(host='localhost', user='sgr', password='password', database='dbo_ctr_mng')

# Create a cursor object
cursor = connection.cursor()

# Get the database structure
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

database_structure = {}

# Iterate over the tables
for table in tables:
    table_name = table[0]
    cursor.execute(f"DESCRIBE {table_name}")
    columns = cursor.fetchall()
    database_structure[table_name] = columns

# Close the cursor and connection
cursor.close()
connection.close()

# Store the database structure in a variable
output_buffer = io.StringIO()
sys.stdout = output_buffer

for table_name, columns in database_structure.items():
    print(f"Table: {table_name}")
    for column in columns:
        print(column)

sys.stdout = sys.__stdout__
output_string = output_buffer.getvalue()
output_buffer.close()

# Print the output string
#print(output_string)


openai.api_key = "openAI_API_Key"

messages = [{"role": "system", "content": "where the database structure is " + output_string}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "DB Pro")

demo.launch(share=True)
