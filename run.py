from app import app
from app import models

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
