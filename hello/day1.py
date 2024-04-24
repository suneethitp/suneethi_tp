from flask import Flask
app = Flask(__name__)



@app.route('/m')
def hai():
    return "<h1>hiii</h1>"

@app.route('/hello')
def hello():
    return  "<h1>hello</h1>"

@app.route('/hello/<name>')
def hello1(name):
    return "<h1>hello " +name+"</h1>"

@app.route('/hello/<int:name>')
def hello2(name):
    return "num->%d" %name

def welcome():
    return "welcome"

app.add_url_rule("/w","welcome",welcome)
#ap.add_url_rule(<url rule>,<end point>,<view function>)



if __name__ =="__main__":
    app.run(debug=True)  #app.run(host,port,debug,options)