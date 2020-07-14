from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.utils import json
from rest_framework_jwt.settings import api_settings


# Create your tests here.

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

