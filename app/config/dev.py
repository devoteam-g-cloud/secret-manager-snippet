import os
from os.path import join, dirname
from dotenv import load_dotenv
from google.cloud import secretmanager
dotenv_path = join(dirname(__file__), 'env')
load_dotenv(dotenv_path)
basedir = os.path.abspath(os.path.dirname(__file__))


ENV = os.getenv('ENV', 'local')
project_id = os.getenv('GOOGLE_CLOUD_PROJECT', None) # this should return dev project-id if deployed in dev
if project_id:
    try:
        client = secretmanager.SecretManagerServiceClient()
        PYTHON_ENV = f"projects/{project_id}/secrets/PYTHON_ENV/versions/latest" # set path to secret /PYTHON_ENV
        env_response = client.access_secret_version(name=PYTHON_ENV) # Read secret in path
        ENV_VALUE = env_response.payload.data.decode("UTF-8") # ENV_VALUE == whatever we've put as a secret in secret manager of prod project.
        # get more secrets
    except Exception as e:
        print("Error reading secret :", e)
    if ENV == 'dev':
        os.environ['PYTHON_ENV'] = ENV_VALUE
        os.environ['GOOGLE_PROJECT_ID'] = project_id
        # do something if dev
