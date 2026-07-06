import json
import requests
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def lambda_handler(event, context):
    
    API_KEY = os.getenv("API_KEY")
    