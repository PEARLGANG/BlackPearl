import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from local_config import Development as Config
    
else:
    from heroku_config import Var as Config

Var = Config
