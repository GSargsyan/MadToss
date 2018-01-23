import os
import sys
from app import app as application

BASE_DIR = os.path.join(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    application.run()
