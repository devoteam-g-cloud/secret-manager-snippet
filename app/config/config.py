from .local import ENV as local_env
from .dev import ENV as dev_env
from .prd import ENV as prod_env
import os

ENV = None
DEBUG=True


if local_env == 'local':
    ENV = local_env
    GOOGLE_PROJECT_ID = os.environ['GOOGLE_PROJECT_ID']
if dev_env == 'dev':
    ENV = dev_env
    GOOGLE_PROJECT_ID = os.environ['GOOGLE_PROJECT_ID']
if prod_env == 'prd':
    ENV = prod_env
    GOOGLE_PROJECT_ID = os.environ['GOOGLE_PROJECT_ID']
    DEBUG=False

CURRENT_ENV = ENV
