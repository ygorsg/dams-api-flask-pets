from dotenv import load_dotenv
from os import environ
from app import app

load_dotenv()

def validate_env_vars():
    """Valida se as variáveis de ambiente essenciais estão configuradas."""
    required_vars = ['SERVER_HOST', 'ENV']
    for var in required_vars:
        if not environ.get(var):
            raise EnvironmentError(f"A variável de ambiente '{var}' não está definida.")

if __name__ == '__main__':

    validate_env_vars()

    SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
    SERVER_PORT = int(environ.get('SERVER_PORT', 5500))
    DEBUG_MODE = environ.get('ENV') != 'PRODUCTION'
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=DEBUG_MODE, threaded=True)
