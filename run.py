from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "WHO LET THE DOGS OUT"

if __name__ == '__main__':
    app.run(debug=True)



#Once you are ready to make yoour first changes--
#1.) <cd ~/Desktop/nutritrack-capstone> -> <git fetch origin>
#2.) <git checkout features> -> <git pull origin features> <git checkout -b editor/AJprogramming123>
#3.) "Start making the changes"
#4.) <git add .> -> <git commit -m "COMMENT">
#5.) "You want to make sure youre up to date" -> <git pull origin features>
#6.) <git add run.py> -> <git commit -m  "Resolve merge conflict"
#7.) <git push origin editor/AJ123