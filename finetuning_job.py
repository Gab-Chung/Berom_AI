import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment
api_key = os.getenv('OPENAI_API_KEY')

# Set the OpenAI API key
openai.api_key = api_key

# Define a function to open a file and return its contents as a string
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read().strip()

# Using the provided file_id
file_id = "file-tzQnqWQpqlbd2lMrprWgx4C5"
model_name = "gpt-4o-mini-2024-07-18"

# Create the fine-tuning job
response = openai.FineTuningJob.create(
    training_file=file_id,
    model=model_name,
    integrations=[
        {
            "type": "wandb",
            "wandb": {
                "project": "Berom AI bot",
                "name": "ft-run-display-name",
                "tags": [
                    "first-experiment", "v2"
                ]
            }
        }
    ]
)

# Get and print the job ID
job_id = response['id']
print(f"Finetuning job created successfully with ID: {job_id}")
