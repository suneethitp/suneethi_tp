from flask import *

app = Flask(__name__)
app.secret_key="aa"


@app.route('/Gstudreg',methods=['GET'])
def mygetmthd():
    name=request.args.get('fname')
    email=request.args.get('em')
    ph=request.args.get('ph')
    print(name,email,ph)
    return 'success'



@app.route('/Pstudreg',methods=['POST'])
def mypostmthd():
    name=request.form['fname']
    email=request.form['em']
    phone=request.form['ph']
    print(name,email,phone)
    return 'success post method'

# --------------------------form-------------------------
@app.route('/n')
def reg():
    return render_template('d5.html')


@app.route('/succ',methods=['POST','GET'])
def get_data():
    if request.method=='POST':
        data=request.form
        return data
    else:
        return render_template('d5.html')
# ---------------cookie------------------------------------------- 

@app.route('/sc')
def set_cook():
    res=make_response("<h1> cookie is set </h1>")
    res.set_cookie('fname','ammu')
    return res



@app.route('/gc')
def get_cook():
    name=request.cookies.get('fname')
    return name

# -------------------------------session-----------------------------


@app.route('/ss')
def set_sess():
    res=make_response('session is set')
    session['phone']=456789
    return res


@app.route('/gs')
def get_sess():
    if "phone" in session:
        return str(session['phone'])


# -------------------------------------------------------------------------------------------------------------------------

@app.route('/hh')
def frontpg():
    return render_template('frontpg.html')



@app.route('/lgn',methods=['POST','GET'])
def logindata():
    if request.method=='POST':
        email=request.form['em']
        password=request.form['pswd']
        if password=="admin":
            session['em']=email
            return render_template("lg.html")
        else:
            return render_template('frontpg.html')
           

    else:
        return render_template('frontpg.html')
 


@app.route('/ge')
def getem():
    if "em" in session:
        return render_template("wel.html",mail=session["em"])
    else:
        return("<script>window.alert('error!!!');window.location.href='/lgn'</script>")


@app.route('/out')
def logout():
    del session['em']
    return redirect(url_for('logindata'))















if __name__=="__main__":
    app.run(debug=True)