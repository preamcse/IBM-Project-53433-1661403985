

from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)
@app.route('/hello/<name>')
def hello_world(name):
    return"HEY %s! welcome to my page" %name 
@app.route('/user/<user>')
def hello(user):
  return"HELLO USER  %s " %user   


@app.route('/success/<name>')
def success(name):
    return "welcome %s" %name
 
@app.route('/login',methods=["POST","GET"])   
def login():
    if request.method=="POST":
        user=request.form["name"]
        return redirect(url_for('success',name=user))
    
    

@app.route('/value/<int:value>')
def user(value):
    return "number %d" %value

@app.route('/')
def welcome():
    return "You are in the first page"


    

@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('login.html',marks = score)





@app.route('/')
def index():
    return render_template("login2.html") 


if __name__ =='__main__':
     app.run(debug=True)