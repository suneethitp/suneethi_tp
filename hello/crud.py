from flask import *
import sqlite3
app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def stud_reg():
    if request.method=="POST":
        n=request.form["fname"]
        e=request.form["em"]
        p=request.form["ph"]
        with sqlite3.connect("stud.db") as con:
            cur=con.cursor()
            cur.execute("""
            insert into student(name,email,phone)
            values(?,?,?)""",(n,e,p))
            con.commit()
        return "success"
    else:
        return render_template("studreg.html")


@app.route("/sv")
def stuview():
    con=sqlite3.connect('stud.db')
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from student")
    rows=cur.fetchall()

    return render_template('studview.html',data=rows)




@app.route('/sd/<int:id>')
def sdel(id):
    print(id)
    with sqlite3.connect("stud.db") as con:
        cur=con.cursor()
        cur.execute("delete from student where id=?",(id,))
        con.commit()
        return("<script>window.alert('successfully delected');window.location.href='/sv'</script>")
      
@app.route('/se/<int:id>')
def sedt(id):
    print(id)
    with sqlite3.connect("stud.db") as con:
        con=sqlite3.connect('stud.db')
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        # cur=execute(  "update student set fname=?,email=?,phone=? where id=?") 
        rows=cur.fetchone()             
        # con.commit()
        return render_template('studedit.html',data=rows)
    
        

if __name__=="__main__":
    app.run(debug=True)