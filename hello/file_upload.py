from flask import *
app=Flask(__name__)

app.secret_key='abc'


@app.route('/',methods=['GET','POST'])
def index():
    er="hhhhhhhhhhhh"
    if request.method=='GET':
        return render_template('file.html') 
    else:
        
        f=request.files['dp']
        f.save(f.filename)
        # return 'success'
        a=1
        if a==1:
            flash('successfully saved')
        else:
            flash('error')
        return render_template('file.html',error=er)

if __name__=="__main__":
    app.run(debug=True)