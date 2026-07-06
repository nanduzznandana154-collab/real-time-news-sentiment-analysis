import json
import requests
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def lambda_handler(event, context):

    API_KEY = os.getenv("API_KEY")
    
    url = f"https://newsdata.io/api/1/latest?apikey=pub_4d3a5600b39c4069b1155376328c26f2&language=en"

    data = requests.get(url).json()
