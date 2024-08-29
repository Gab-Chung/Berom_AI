# Berom_AI

Berom Language is one of the minor languages/tribes in central Nigeria that is under represented in the digital world. This AI chatbot is developed specially to bring the Berom language to light. This bot can teach Berom, tell you some history and facts about Berom, write in Berom and translate words and sentences between English and Berom

## Before you run this bot

Create a `.env` file and add your api tokens

- OPENAI_API_KEY="your openai api key"

## To run the bot

- First run the `finetuning_file_upload.py` file to generate your `file_id`
- Then copy your generated `file_id` and replace it in the file `finetuning_job.py` and run this file

* python3 finetuning_job.py

This will begin your fine-tuning job which can be monitored on [OpenAI platform](https://platform.openai.com/finetune/ftjob-GGaxIRVupBuKUygfmCAw1iAK?filter=all)

Alternatively, you can monitor your fine-tuning job on [Weights and Biases platform](wandb.ai). But you first need to create an account, create a project, get an API key which you will integrate on your OpenAI platform. You can see detailed instructions on how to do that on [OpenAI's documentation](https://platform.openai.com/docs/guides/fine-tuning/fine-tuning-integrations)
