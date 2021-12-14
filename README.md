## Secret manager snippet

A quick start to configure a project with secret manager

## Requirements
- Secret manager api activated and secrets added


## Usage

- Go to `https://console.cloud.google.com/security/secret-manager?project=YOUR_PROJECT_ID`  
- Make sure the Secret manager API is activated  
- Add secrets e.g : PYTHON_ENV = prd for production project-id-prd  
- Once the app is deployed to project-id-prd, the app/config/prd.py will read  
the env variable `GOOGLE_CLOUD_PROJECT` automatically set by GCP and then  
loads your secret accordingly.  

- Having already added a secret to secret manager :  
     Starting an client instance :  
         `client = secretmanager.SecretManagerServiceClient()`
     Setting the path to your secret:  
         `MY_SECRET_NAME = f"projects/{project_id}/secrets/MY_SECRET_NAME/versions/latest"`
     load the response :  
         `response = client.access_secret_version(name=MY_SECRET_NAME)`
     Finally utf-8 :  
         `MY_SECRET_STR = response.payload.data.decode("UTF-8")` and use it as you see fit.

## Install
- `python3 -m virtualenv venv`
- `source ./venv/bin/activate`
- `pip install -r requirements.txt`
