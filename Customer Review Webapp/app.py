from flask import Flask, render_template,request, flash
import sqlite3
app = Flask(__name__) 

con=sqlite3.connect('reviews.db')
con.execute('''CREATE TABLE IF NOT EXISTS Reviews
                (CUSTOMERNAME TEXT NOT NULL, 
                PRODUCTNAME TEXT NOT NULL, 
                REVIEW TEXT)''')
  
@app.route('/')
def home_page():
   return render_template('Main.html')

@app.route('/Review.html')
def Review():
    return render_template('Review.html')


@app.route('/RecentReviews',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
        Customername=request.form['Customer-name']
        Productname=request.form['Food-Product']
        Revieww=request.form['Review']

        con=sqlite3.connect("reviews.db")
        cur = con.cursor()
        cur.execute("""INSERT INTO Reviews (CUSTOMERNAME,PRODUCTNAME,REVIEW)
            VALUES (?,?,?)""",(Customername,Productname,Revieww) )
            
        con.commit()
        
        return render_template('Review.html',var=5)

@app.route('/RecentReviews.html')
def list():
    con = sqlite3.connect("reviews.db")
    cur = con.cursor()
    cur.execute("select * from Reviews")
    rows = cur.fetchall()
    return render_template("RecentReviews.html",rows = rows)



  
if __name__ == '__main__': 
   app.run(debug=True)
