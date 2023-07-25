from IPython.display import Markdown, display
from llama_index import VectorStoreIndex
from llama_index import download_loader
import os
import openai
import boto3
from dotenv import load_dotenv


def load_api_keys():
    load_dotenv()


openai.api_key = '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'

# HubspotReader = download_loader('HubspotReader')

# reader = HubspotReader("pat-na1-e3ea0414-3fc4-438a-9252-1a1e58c2d1f8")
# documents = reader.load_data()


# index = VectorStoreIndex.from_documents(documents)

# query_engine = index.as_query_engine()
# response = query_engine.query("Count the total number of records")
# display(Markdown(f"<b>{response}</b>"))


# GoogleDriveReader = download_loader("GoogleDriveReader")

# loader = GoogleDriveReader()

# # Using folder id
# documents = loader.load_data(folder_id="1MYms1q862OkZOwQT01RDfAEtA3pR56Se")

# index = VectorStoreIndex.from_documents(documents)

# query_engine = index.as_query_engine()
# response = query_engine.query("Count the total number of records")
# display(Markdown(f"<b>{response}</b>"))


S3Reader = download_loader("S3Reader")

loader = S3Reader(bucket='igebra-hubspot', key='bartleby.pdf', aws_access_id='AKIA4O72ODGD44COLZN2',
                  aws_access_secret='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')
documents = loader.load_data()

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("Tell me about Ginger Nut")
display(Markdown(f"<b>{response}</b>"))
