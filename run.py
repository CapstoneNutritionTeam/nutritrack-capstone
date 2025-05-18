from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "WHO LET THE DOGS OUT"

if __name__ == '__main__':
    app.run(debug=True)



#Once you are ready to make yoour first changes--
#1.) <source venv/bin/activate> -> ssh git@github.com>
#2.) <cd ~/Desktop/nutritrack-capstone>
#3.) <git checkout -b editor/AJprogramming123> -> <git pull origin features/[branch]> <- (Creates your own branch)
#4.) "Start making the changes"
#5.) <git add run.py> -> <git commit -m  "Resolve merge conflict"
#6.) <git push origin editor/AJprogramming123> <- this is my personal branch where i make my changes to then send to get pull request to merge with approval)


#Basically the most we have to worry about is that when you open a Pull Request and GitHub checks:
    #"Can this be merged cleanly into features?”
#If someone else's PR already changed a line you also changed, then GitHub will say:
    #"This branch has conflicts that must be resolved"

#Now after youre first branch build you can do: <git checkout editor/AJprogramming123> to make sure youre on your branch


#What happens when theres conflict code after doing <git pull origin features>?
# git checkout --ours run.py (Keep their changes) or git checkout --theirs run.py> (Their changes)
# OR you can just remove these -> (<<<<<<, ========, >>>>>>>>), move the lines you do want to keep or remove and: <git add run.py>
#Finally: <git commit -m "Merge conflict resolved - kept both changes"


#Eventually we will have all branches open for changes so youd use: <git add .> or <git pull origin> instead of specific files or branches
