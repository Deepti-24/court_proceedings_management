from flask import Flask,render_template,request,json,session,redirect
from flask_bootstrap import Bootstrap
from flaskext.mysql import MySQL

app=Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'
Bootstrap(app)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pre$entI$2gl0ry'
app.config['MYSQL_DATABASE_DB'] = 'Court_Proceedings'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

mysql.init_app(app)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/suspects")
def suspects():
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("select * from suspects")
    data=cursor.fetchall()
    return render_template('example.html',value=data)
    cursor.close()
    conn.close()

@app.route("/advocates")
def advocates():
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("select * from advocate")
    data=cursor.fetchall()
    return render_template('advocates.html',value=data)
    cursor.close()
    conn.close()

@app.route("/stations")
def stations():
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("select * from police_station")
    data=cursor.fetchall()
    return render_template('stations.html',value=data)
    cursor.close()
    conn.close()

@app.route("/firs")
def firs():
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("select * from fir")
    data=cursor.fetchall()
    return render_template('firs.html',value=data)
    cursor.close()
    conn.close()

@app.route("/cases")
def cases():
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("select * from criminal_case")
    data=cursor.fetchall()
    return render_template('cases.html',value=data)
    cursor.close()
    conn.close()

@app.route("/profiles")
def profiles():
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("select * from client_profile")
    data=cursor.fetchall()
    return render_template('profiles.html',value=data)
    cursor.close()
    conn.close()

@app.route("/showNewProfile")
def showNewProfile():
    return render_template('/addProfile.html')

@app.route("/newProfile", methods=['GET','POST'])
def newProfile():
        ID = request.form['caseId']
        Name = request.form['name']
        Phone = request.form['phone']
        Address = request.form['address']
        EmailID = request.form['email']
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO client_profile(case_id,client_name,client_phone,client_address,client_email) VALUES(%s,%s,%s,%s,%s)",(ID,Name,Phone,Address,EmailID))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('userHome.html')

@app.route("/showUpdateProfile")
def showUpdateProfile():
    return render_template('/updateProfile.html')

@app.route("/editProfile", methods=['GET','POST'])
def editProfile():
        ID = request.form['clientID']
        Name = request.form['name']
        Phone = request.form['phone']
        Address = request.form['address']
        EmailID = request.form['email']
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute("UPDATE client_profile SET client_name=%s,client_phone=%s,client_address=%s,client_email=%s WHERE client_id=%s",(Name,Phone,Address,EmailID,ID))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('userHome.html')

@app.route("/ShowDelete")
def showDelete():
    return render_template('/delete.html')

@app.route("/delete", methods=['GET','POST'])
def delete():
    AID = request.form['advID']
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM advocate WHERE adv_id=%s",(AID))
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('userHome.html')

@app.route("/showNewCase")
def showNewCase():
    return render_template('/addCase.html')

@app.route("/newCase", methods=['GET','POST'])
def newCase():
        ID = request.form['caseId']
        FIR = request.form['fir_no']
        Victim = request.form['victim']
        Type = request.form['type']
        Accused = request.form['accused']
        Court = request.form['court']
        Judge = request.form['judge']
        Defence = request.form['defence']
        Pros = request.form['pros']
        Last = request.form['last']
        Next = request.form['next']
        Verdict = request.form['verdict']
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO criminal_case(case_id,fir_no,victim,case_type,accused,court_name,judge,defense_id,prosecutor_id,last_hearing_date,next_hearing_date,final_verdict) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(ID,FIR,Victim,Type,Accused,Court,Judge,Defence,Pros,Last,Next,Verdict))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('userHome.html')

@app.route("/showUpdateCase")
def showUpdateCase():
    return render_template('/updateCase.html')

@app.route("/editCase", methods=['GET','POST'])
def editCase():
    ID = request.form['caseId']
    Last = request.form['last']
    Next = request.form['next']
    Verdict = request.form['verdict']
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("UPDATE criminal_case SET last_hearing_date=%s,next_hearing_date=%s,final_verdict=%s WHERE case_id=%s",(Last,Next,Verdict,ID))
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('userHome.html')

@app.route("/showNewFir")
def showNewFir():
    return render_template('/addFir.html')

@app.route("/newFir", methods=['GET','POST'])
def newFir():
        Pin = request.form['pin']
        Name = request.form['name']
        Date = request.form['date']
        Time = request.form['time']
        Desc = request.form['desc']
        Section= request.form['section']
        Suspect = request.form['suspect']
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO fir(pincode,complainant_name,date,time,description,section,suspect_or_accused) VALUES(%s,%s,%s,%s,%s,%s,%s)",(Pin,Name,Date,Time,Desc,Section,Suspect))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('userHome.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['GET','POST'])
def signUp():
    try:
        _uname=request.form['input_uname']
        _uid=request.form['input_uid']
        _upwd=request.form['input_pwd']
        if _uname and _uid and _upwd:
            conn=mysql.connect()
            cursor=conn.cursor()
            cursor.callproc('signup_proc',(_uname,_uid,_upwd))
            data = cursor.fetchall()
            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})
    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
         cursor.close()
         conn.close()

@app.route('/showLogIn')
def showLogIn():
     if session.get('user'):
        return render_template('userHome.html')
     else:
        return render_template('login.html')

@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return json.dumps({'message':'Error'})

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')

@app.route('/logIn',methods=['POST'])
def logIn():
    try:
        _uname=request.form['input_uname']
        _upwd=request.form['input_pwd']
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('login_proc',(_uname,))
        data = cursor.fetchall()

        if len(data) > 0:
            if _upwd==str(data[0][2]):
                session['user'] = data[0][0]
                return redirect('/userHome')
            else:
                return json.dumps({'message':'Error'})
        else:
            return json.dumps({'message':'Error'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()

if __name__=="__main__":
    app.run(debug=True)
