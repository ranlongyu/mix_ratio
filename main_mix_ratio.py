import os
import sys
import config

sys.path.append(os.path.abspath('.') + "/main_app")

from main_app import app

if __name__ == '__main__':
    app.run(debug=config.DEBUG, host='0.0.0.0', port=5000)
