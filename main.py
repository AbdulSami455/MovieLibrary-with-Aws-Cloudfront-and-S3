from flask import Flask,render_template,jsonify

app=Flask(__name__)

@app.route("/")
def helloworld():
 return render_template('index.html')

@app.route("/movie1")
def movie1():
 moviename="name"
 return render_template('movie1.html',name=moviename)
app.run()