from openai import OpenAI

client = OpenAI(api_key=api_key)

# Define a function to open a file and return its contents as a string 
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read ()

# Define a function to save content to a file
def save_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as outfile:
        outfile.write (content)

# Set the OpenAI API keys by reading them from files
api_key = open_file('openaikey.txt')


# Assuming the file name is 'processed_data jsonl'
with open("/Users/gabrielchung/Desktop/Berom_project/new_dataset.jsonl", "rb") as file:
    response = client.files.create(file = file,
    purpose = 'fine-tune')

file_id = response.id
print(f"File uploaded successfully with ID: {file_id}")