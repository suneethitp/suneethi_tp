from flask import *
from flask_mail import *
app=Flask(__name__)

mail1=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='achuaks2000@gmail.com'
app.config['MAIL_PASSWORD']='htbu splg sumk dbuh'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True



@app.route('/sm')
def smail():
    msg=Message('subject',sender='achuaks2000@gmail.com',recipients=['suneethitp14@gmail.com'])
    msg.body='hi my first message in flask'
    mail1.send(msg)
    return 'success'

if __name__=="__main__":
    app.run(debug=True)