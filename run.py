from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

#Testing for productivity

#IF only this changed then the .gititignore works fine now after you clone you need to do something specific on your command line:
#1.) go into the VENV environment always before installing python packages to not conflict your local system
#2.) Before adding/committing any new updates do this (Only need to this once unless you use a new device or clone again):
    # touch .env
    # (write something on it to test if it commits)
    # git rm --cached .env
    # git commit -m "Stop tracking .env file"
