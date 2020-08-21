from flask import Flask,render_template,request
#importing the flask module
#import render template to serve html files on server

app = Flask(__name__)

# app.config["DEBUG"] = True
#DEBUG : Disable in production


@app.route('/')
''' Default route for our flask web app
    Renders the form.html template on init    
'''
def index():
    return render_template("form.html")


@app.route('/welcome', methods=['POST','GET'])
''' 
   API call from form.html
   This route gets the form data and passes the name and city parameters to the welcome template
   ----------------------------------------------------------------------

   Arguments recieved from request:
   name: User's Full Name
   city: City of residence
   
'''
def welcome():
    if request.method=='POST':
        return render_template("welcome.html",name=request.form["name"],city=request.form["city"])

    return "Request Failed"


if __name__ == '__main__':
#Platform Ready =>
    app.run()
