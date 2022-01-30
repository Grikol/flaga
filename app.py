from flask import Flask, render_template
import os


app=Flask(__name__)

@app.route('/')
def index():
    
    text = "Siema G tu Ildefons koduje"   # open('xd.txt').read()

    text = open('xd.txt').read()
    
    return render_template("index.html", text=text)
    
if __name__=="__main__":
    app.run()
