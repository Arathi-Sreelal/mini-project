from django.shortcuts import render
import mysql.connector
from pyexpat.errors import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request,'DrCabapp/index.html')
def userreg(request):
    return render(request,'DrCabapp/userreg.html')
def driverreg(request):
    return render(request,'DrCabapp/driverreg.html')
def mechreg(request):
    return render(request,'DrCabapp/mechreg.html')
def cabowner(request):
    return render(request,'DrCabapp/cabowner.html')
def userlogin(request):
    messages=""
    return render(request,'DrCabapp/userlogin.html',{'message':messages})
def adminlogin(request):
    messages=""
    return render(request,'DrCabapp/adminlogin.html',{'message':messages})
def driverlogin(request):
    messages=""
    return render(request,'DrCabapp/driverlogin.html',{'message':messages})
def mechaniclogin(request):
    messages=""
    return render(request,'DrCabapp/mechaniclogin.html',{'message':messages})
def cabownerlogin(request):
    messages=""
    return render(request,'DrCabapp/cabownerlogin.html',{'message':messages})
def contact(request):
    return render(request,'DrCabapp/contact.html')
def about(request):
    return render(request,'DrCabapp/about.html')
def service(request):
    return render(request,'DrCabapp/service.html')
def addaccessories(request):
    return render(request,'DrCabapp/addaccessories.html')
def cabdetails(request):
    return render(request,'DrCabapp/cabdetails.html')
def feedback(request):
    return render(request,'DrCabapp/adduserfeedback.html')


def homepage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass"]
        print(username + password)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        mycursor = conn.cursor()
        query = "select * from admin where username='" + username + "' and password = '" + password +"'"
        mycursor.execute(query)
        mycursor.fetchall()
        print(mycursor.rowcount)
        if mycursor.rowcount == 0:
            #name = request.sesson['tchrn']
            messages= "invalid username and password."
            return render(request,'DrCabapp/adminlogin.html',{'message':messages})
        else:
            return render(request,'DrCabapp/adminhome.html')
def user_reg(request):
    if request.method == "POST":
        fm = request.POST["first_name"]
        ln = request.POST["last_name"]
        em = request.POST["email"]
        gn = request.POST["gender"]
        pw = request.POST["password"]
        ph = request.POST["phone"]
        cp = request.POST["confirm_password"]
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="drcab")
        mycursor = mydb.cursor()
        q = "insert into user_reg(first_name,last_name,email,password,phone_number,confirm_password,gender) values('" + fm + "','" + ln + "','" + em + "','" + pw + "','" + ph + "','" + cp + "','" + gn + "')"
        mycursor.execute(q)
        mydb.commit()
        return render(request,'DrCabapp/index.html', {'msg': 'Registration successfull'})
def mech_reg(request):
    if request.method == "POST":
        fname = request.POST["first_name"]
        lname = request.POST["last_name"]
        eml = request.POST["email"]
        gen = request.POST["gender"]
        pwd = request.POST["password"]
        phn = request.POST["phone"]
        cpd = request.POST["cf"]
        ex = request.POST["experience"]
        cw = request.POST["current_working"]
        pa = request.POST["pan"]
        eq = request.POST["educational_qualification"]
        cf = request.POST["certification"]
        lc = request.POST["location"]
        sb = request.POST["subject"]
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="drcab")
        mycursor = mydb.cursor()
        q = "insert into mech_reg(first_name,last_name,email,password,phone_number,confirm_password,gender,pan,vehicle_type,edu_qualification,certification,location,experience,currently_working) values('" + fname + "','" + lname + "','" + eml + "','" + pwd + "','" + phn + "','" + cpd + "','" + gen + "','" + pa + "','" + sb + "','" + eq + "','" + cf + "','" + lc + "','" + ex + "','" + cw + "')"
        mycursor.execute(q)
        mydb.commit()
        return render(request,'DrCabapp/index.html', {'msg': 'Registration successfull'})

def driver_reg(request):
    if request.method == "POST":
        fnm = request.POST["first_name"]
        lnm = request.POST["last_name"]
        el = request.POST["email"]
        gnr = request.POST["gender"]
        pd = request.POST["password"]
        phm = request.POST["phone"]
        cpwd = request.POST["confirm_password"]
        exp = request.POST["exp"]
        pn = request.POST["pan"]
        dln = request.POST["dlnumber"]
        status="Denied"
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="drcab")
        mycursor = mydb.cursor()
        q = "insert into driver_reg(first_name,last_name,email,password,phone_number,confirm_password,gender,experience,dl_number,pan,status) values('" + fnm + "','" + lnm + "','" + el + "','" + pd + "','" + phm + "','" + cpwd + "','" + gnr+ "','" + exp + "','" + dln  +"','" + pn + "','" + status + "')"
        mycursor.execute(q)
        mydb.commit()
        return render(request,'DrCabapp/index.html', {'msg': 'Registration successfull'})

def cabowner_reg(request):
    if request.method == "POST":
        ftn = request.POST["first_name"]
        ltn = request.POST["last_name"]
        ema = request.POST["email"]
        gdr = request.POST["gender"]
        psd = request.POST["password"]
        phne = request.POST["phone"]
        cpsd = request.POST["confirm_password"]
        locn = request.POST["location"]
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="drcab")
        mycursor = mydb.cursor()
        q = "insert into cabowner_reg(first_name,last_name,email,password,phone_number,confirm_password,gender,location) values('" + ftn + "','" + ltn + "','" + ema + "','" + psd + "','" + phne + "','" + cpsd + "','" + gdr+ "','" + locn + "')"
        mycursor.execute(q)
        mydb.commit()
        return render(request,'DrCabapp/index.html', {'msg': 'Registration successfull'})

def user_homepage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass"]
        print(username + password)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        con = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        co = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        mycursor = conn.cursor()
        mycursor1 = con.cursor()
        mycursor2 = co.cursor()
        query = "select * from user_reg where email='" + username + "' and password = '" + password +"'"
        q1 = "select first_name from user_reg where email='" + username + "' and password = '" + password +"'"
        q2 = "select last_name from user_reg where email='" + username + "' and password = '" + password + "'"
        mycursor.execute(query)
        mycursor1.execute(q1)
        mycursor2.execute(q2)
        mycursor.fetchall()
        print(mycursor.rowcount)
        ((fname,),) = mycursor1.fetchall()
        ((lname,),) = mycursor2.fetchall()
        request.session['uname'] = fname + lname
        if mycursor.rowcount == 0:
            # name = request.sesson['tchrn']
            messages = "invalid username and password."
            return render(request, 'DrCabapp/userlogin.html', {'message': messages})
        else:
            return render(request, 'DrCabapp/userhome.html')
def driver_homepage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass"]
        print(username + password)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        mycursor = conn.cursor()
        query = "select * from driver_reg where email='" + username + "' and password = '" + password +"'"
        mycursor.execute(query)
        mycursor.fetchall()
        print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        # name = request.sesson['tchrn']
        messages = "invalid username and password."
        return render(request, 'DrCabapp/driverlogin.html', {'message': messages})
    else:
        return render(request, 'DrCabapp/driverhome.html')
def mech_homepage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass"]
        print(username + password)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        mycursor = conn.cursor()
        query = "select * from mech_reg where email='" + username + "' and password = '" + password +"'"
        mycursor.execute(query)
        mycursor.fetchall()
        print(mycursor.rowcount)
        if mycursor.rowcount == 0:
            # name = request.sesson['tchrn']
            messages = "invalid username and password."
            return render(request, 'DrCabapp/mechaniclogin.html', {'message': messages})
        else:
            return render(request, 'DrCabapp/mechhome.html')
def cabowner_homepage(request):
    if request.method == "POST":
        username = request.POST["username"]
        #request.session['']
        password = request.POST["pass"]
        print(username + password)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        mycursor = conn.cursor()
        query = "select * from cabowner_reg where email='" + username + "' and password = '" + password +"'"
        mycursor.execute(query)
        mycursor.fetchall()
        print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        # name = request.sesson['tchrn']
        messages = "invalid username and password."
        return render(request, 'DrCabapp/cabownerlogin.html', {'message': messages})
    else:
        query = "select first_name from cabowner_reg where email='" + username + "' and password = '" + password + "'"
        mycursor.execute(query)
        fname = mycursor.fetchone()
        query1 = "select last_name from cabowner_reg where email='" + username + "' and password = '" + password + "'"
        mycursor.execute(query1)
        lname = mycursor.fetchone()
        print(fname+lname)
        request.session["cname"]=fname+lname
        return render(request, 'DrCabapp/cabownerhome.html')

def tabletry(request):

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        mycursor = conn.cursor()
        query = "select id,first_name,last_name,phone_number,email,experience,dl_number,pan,gender,status from driver_reg"
        mycursor.execute(query)
        if mycursor.rowcount == 0:
            msg = "No records found"
            return render(request,'DrCabapp/tabletry.html', {'trpic': msg})
        else:
            records = mycursor.fetchall()
            return render(request,'DrCabapp/tabletry.html', {'records': records})
def dr_approve(request):
    conn = mysql.connector.connect(user='root',password='',host='localhost',database='drcab')
    mycursor = conn.cursor()
    id = request.POST["did"]
    s = "Admitted"
    s1 = "Denied"

    if request.method == 'POST':
        if request.POST.get("status"):
            query = "update driver_reg set status = '" + s + "' where id =" + id + " "
            mycursor.execute(query)
            conn.commit()
            query1 = " select id,first_name,last_name,phone_number,email,experience,dl_number,pan,gender,status from driver_reg"
            mycursor.execute(query1)
            records = mycursor.fetchall()
           # messages.success(request,"Approved.")
            return render(request,'DrCabapp/tabletry.html',{'records':records})
        elif request.POST.get("status1"):
                query = "update driver_reg set status = '" + s1 + "' where id =" + id + " "
                mycursor.execute(query)
                conn.commit()
                query1 = " select id,first_name,last_name,phone_number,email,experience,dl_number,pan,gender,status from driver_reg"
                mycursor.execute(query1)
                records = mycursor.fetchall()
                #messages.error(request,"Denied.")
                return render(request, 'DrCabapp/tabletry.html', {'records': records})

def driverview(request):

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    s="Admitted"
    query = "select id,first_name,last_name,phone_number,email,experience,dl_number,pan,gender from driver_reg where status ='"+ s+"' "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/adminhome.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/driverviewtable.html', {'records': records})
def mechtry(request):

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    query = "select id,first_name,last_name,phone_number,email,gender,status from mech_reg"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/mechtry.html', {'trpic': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/mechtry.html', {'records': records})


def mech_approve(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    id = request.POST["mechid"]
    s = "Admitted"
    s1 = "Denied"

    if request.method == 'POST':
        if request.POST.get("status"):
            query = "update mech_reg set status = '" + s + "' where id =" + id + " "
            mycursor.execute(query)
            conn.commit()
            query1 = " select id,first_name,last_name,phone_number,email,gender,status from mech_reg"
            mycursor.execute(query1)
            records = mycursor.fetchall()
            # messages.success(request,"Approved.")
            return render(request, 'DrCabapp/mechtry.html', {'records': records})
        elif request.POST.get("status1"):
            query = "update mech_reg set status = '" + s1 + "' where id =" + id + " "
            mycursor.execute(query)
            conn.commit()
            query1 = " select id,first_name,last_name,phone_number,email,gender,status from mech_reg"
            mycursor.execute(query1)
            records = mycursor.fetchall()
            # messages.error(request,"Denied.")
            return render(request, 'DrCabapp/mechtry.html', {'records': records})


def mechview(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    s = "Admitted"
    query = "select id,first_name,last_name,phone_number,email,gender from mech_reg where status ='" + s + "' "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/adminhome.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/mechviewtable.html', {'records': records})

def mechfulldetails(request):

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    s="Admitted"
    id = request.POST["mechid"]
    print("id",id)
    query = "select id,first_name,last_name,experience,pan,vehicle_type,edu_qualification,certification,location,currently_working from mech_reg where  id = "+ id +" "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/mechfulldetails.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/mechfulldetails.html', {'records': records})
def removemech(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    id = request.POST["mecid"]
    query = " delete from mech_reg where  id = "+ id +" "
    mycursor.execute(query)
    conn.commit()
    s = "Admitted"
    query = "select id,first_name,last_name,phone_number,email,gender from mech_reg where status ='" + s + "' "
    mycursor.execute(query)
    records = mycursor.fetchall()
    return render(request, 'DrCabapp/mechviewtable.html', {'records': records})


def usertry(request):

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    query = "select id,first_name,last_name,phone_number,email,gender,status from user_reg"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/usertry.html', {'trpic': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/usertry.html', {'records': records})


def user_approve(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    id = request.POST["uid"]
    s = "Admitted"
    s1 = "Denied"

    if request.method == 'POST':
        if request.POST.get("status"):
            query = "update user_reg set status = '" + s + "' where id =" + id + " "
            mycursor.execute(query)
            conn.commit()
            query1 = " select id,first_name,last_name,phone_number,email,gender,status from user_reg"
            mycursor.execute(query1)
            records = mycursor.fetchall()
            # messages.success(request,"Approved.")
            return render(request, 'DrCabapp/usertry.html', {'records': records})
        elif request.POST.get("status1"):
            query = "update user_reg set status = '" + s1 + "' where id =" + id + " "
            mycursor.execute(query)
            conn.commit()
            query1 = " select id,first_name,last_name,phone_number,email,gender,status from user_reg"
            mycursor.execute(query1)
            records = mycursor.fetchall()
            # messages.error(request,"Denied.")
            return render(request, 'DrCabapp/usertry.html', {'records': records})


def userview(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    s = "Admitted"
    query = "select id,first_name,last_name,phone_number,email,gender from user_reg where status ='" + s + "' "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/adminhome.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/userviewtable.html', {'records': records})
def removeuser(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    id = request.POST["usid"]
    query = " delete from user_reg where  id = "+ id +" "
    mycursor.execute(query)
    conn.commit()
    s = "Admitted"
    query = "select id,first_name,last_name,phone_number,email,gender from user_reg where status ='" + s + "' "
    mycursor.execute(query)
    records = mycursor.fetchall()
    return render(request, 'DrCabapp/userviewtable.html', {'records': records})



def addcabdetails(request):

    if request.method == "POST" and request.FILES['upload']:
        oname = request.POST["Owner_Name"]
        vehitype = request.POST["Vehtype"]
        vname = request.POST["Vehicle_Name"]
        mdlnum = request.POST["Model_Number"]
        engnum = request.POST["Engine_Number"]
        fultyp = request.POST["Fuel_Type"]
        insnum = request.POST["Insurance_Number"]
        insup = request.POST["Insurance_UpTo"]
        pucnum = request.POST["PUCC_Number"]
        pucup = request.POST["PUCC_UpTo"]
        rcnum = request.POST["RC_Number"]
        mlgkm = request.POST["Mileage"]
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        uploadone = request.FILES['uploadone']
        fss = FileSystemStorage()
        file = fss.save(uploadone.name, uploadone)
        filetwo_url = fss.url(file)
        status="Denied"

        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="drcab")
        mycursor = mydb.cursor()
        q = "insert into add_cabdetails(ownername,vehicle_type,vehicle_name,model_number,engine_number,fuel_type,insurance_number,insurance_upto,pucc_number,pucc_upto,rc_number,mileage,image1,image2,status) values('" + oname + "','" + vehitype + "','" + vname + "','" + mdlnum + "','" + engnum + "','" + fultyp + "','" + insnum + "','" + insup + "','" + pucnum + "','" + pucup + "','" + rcnum + "','" + mlgkm + "','" + file_url + "','" + filetwo_url + "' ,'" + status + "')"
        mycursor.execute(q)
        mydb.commit()
        return render(request,'DrCabapp/cabdetails.html')
    return render(request, 'DrCabapp/cabdetails.html')
def cabtry(request):

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    query = "select id,ownername,vehicle_type,vehicle_name,status from add_cabdetails  "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/cabtry.html', {'trpic': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/cabtry.html', {'records': records})


def cab_approve(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    id = request.POST["cabsid"]
    s = "Admitted"
    s1 = "Denied"

    if request.method == 'POST':
        if request.POST.get("status"):
            query = "update add_cabdetails set status = '" + s + "' where id =" + id + " "
            mycursor.execute(query)
            conn.commit()
            query1 = " select id,ownername,vehicle_type,vehicle_name,status from add_cabdetails "
            mycursor.execute(query1)
            records = mycursor.fetchall()
            # messages.success(request,"Approved.")
            return render(request, 'DrCabapp/cabtry.html', {'records': records})
        elif request.POST.get("status1"):
            query = "update add_cabdetails set status = '" + s1 + "' where id =" + id + " "
            mycursor.execute(query)
            conn.commit()
            query1 = "select id,ownername,vehicle_type,vehicle_name,status from add_cabdetails "
            mycursor.execute(query1)
            records = mycursor.fetchall()
            # messages.error(request,"Denied.")
            return render(request, 'DrCabapp/cabtry.html', {'records': records})

def cabviewtable(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    s = "Admitted"
    query = "select id,ownername,vehicle_type,vehicle_name from add_cabdetails where status ='" + s + "' "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/adminhome.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/cabviewtable.html', {'records': records})

def cabfulldetails(request):

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()

    s="Admitted"
    id = request.POST["cabsid"]
    print("id",id)
    query = "select id,vehicle_name,model_number,engine_number,fuel_type,insurance_number,insurance_upto,pucc_number,pucc_upto,rc_number,mileage from add_cabdetails where  id = "+ id +" "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/cabfulldetails.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        con = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        co = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        q = "select image1 from add_cabdetails where id = '" + id + "' "
        q1 = "select image2 from add_cabdetails where id = '" + id + "' "
        mycursor1 = con.cursor()
        mycursor2 = co.cursor()
        mycursor1.execute(q)
        mycursor2.execute(q1)
        ((img,),) = mycursor1.fetchall()
        ((img1,),) = mycursor2.fetchall()
        im = img.decode('UTF-8')
        imm = img1.decode('UTF-8')
        print(im)
        print(imm)
        return render(request, 'DrCabapp/cabfulldetails.html', {'records': records,'img':im,'img1':imm})
def removecab(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    id = request.POST["rid"]
    query = " delete from add_cabdetails where  id = "+ id +" "
    mycursor.execute(query)
    conn.commit()
    s = "Admitted"
    query = "select id,ownername,vehicle_type,vehicle_name from add_cabdetails where status ='" + s + "' "
    mycursor.execute(query)
    records = mycursor.fetchall()
    return render(request, 'DrCabapp/cabviewtable.html', {'records': records})

def adduserfeedback(request):
    if request.method == "POST":
        uname = request.POST["Username"]
        emil = request.POST["Email"]
        fdbk = request.POST["Feedback"]
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="drcab")
        mycursor = mydb.cursor()
        q = "insert into add_feedback(name,email,feedback) values('" + uname + "','" + emil + "','" + fdbk + "')"
        mycursor.execute(q)
        mydb.commit()
        return render(request,'DrCabapp/userhome.html')


def viewfeedback(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    query = "select id,name,email,feedback from add_feedback"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/adminhome.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/viewfeedback.html', {'records': records})
def viewcabuser(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    s = "Admitted"
    query = "select id,ownername,vehicle_type,vehicle_name from add_cabdetails where status ='" + s + "' "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/userhome.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/viewcabuser.html', {'records': records})
def userbookcab(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    id = request.POST['cabsid']
    s = "Admitted"
    query = "select id,ownername,vehicle_type,vehicle_name,model_number,engine_number,fuel_type,insurance_number,insurance_upto,pucc_number,pucc_upto,rc_number,mileage from add_cabdetails where  id = " + id + " "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/userbookcab.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        con = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        co = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        q = "select image1 from add_cabdetails where id = '" + id + "' "
        q1 = "select image2 from add_cabdetails where id = '" + id + "' "
        mycursor1 = con.cursor()
        mycursor2 = co.cursor()
        mycursor1.execute(q)
        mycursor2.execute(q1)
        ((img,),) = mycursor1.fetchall()
        ((img1,),) = mycursor2.fetchall()
        im = img.decode('UTF-8')
        imm = img1.decode('UTF-8')
        print(im)
        print(imm)
        return render(request, 'DrCabapp/userbookcab.html', {'records': records, 'img': im, 'img1': imm})
def viewdriveruser(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    s = "Admitted"
    query = "select id,first_name,last_name,phone_number,email,experience,dl_number,pan,gender from driver_reg where status ='" + s + "' "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/userhome.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/viewdriveruser.html', {'records': records})


def viewmechuser(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    s = "Admitted"
    query = "select id,first_name,last_name,phone_number,email,gender from mech_reg where status ='" + s + "' "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/userhome.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/viewmechuser.html', {'records': records})
def userbookmech(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    id = request.POST['mechid']
    s = "Admitted"
    query = "select id,first_name,last_name,experience,pan,vehicle_type,edu_qualification,certification,location,currently_working from mech_reg where  id = " + id + " "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/userbookmech.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        con = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        mycursor.execute(query)
        return render(request, 'DrCabapp/userbookmech.html', {'records': records})
def finalbookcab(request):
        name = request.session["uname"]
        vname = request.POST["modelnumber"]
        return render(request, 'DrCabapp/finalbookcab.html',{'name': name ,'vname': vname})
def finalbookingcab(request):
    if request.method == "POST":
        bkname = request.POST["Booker_Name"]
        vehinum = request.POST["Reg_Number"]
        bookdate = request.POST["booking_date"]
        fromloc = request.POST["from_location"]
        toloc = request.POST["to_location"]
        contnum = request.POST["contact_number"]
        status= "Denied"
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="drcab")
        mycursor = mydb.cursor()
        q = "insert into final_cabbook(name,vehicle_number,dateofbooking,from_location,to_location,contact_number,status) values('" + bkname + "', '" + vehinum + "','" + bookdate + "','" + fromloc + "' ,'" + toloc + "' ,'" + contnum + "','" + status + "' )"
        mycursor.execute(q)
        mydb.commit()
        return render(request, 'DrCabapp/finalbookcab.html')
def adminapprovecab(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    query = "select * from final_cabbook"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/adminhome.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/adminapprovecab.html', {'records': records})


def adminapprovingcab(request):
    conn = mysql.connector.connect(user='root',password='',host='localhost',database='drcab')
    mycursor = conn.cursor()
    id = request.POST["apid"]
    s = "Admitted"
    s1 = "Denied"
    if request.method == 'POST':
        if request.POST.get("status"):
            query = "update final_cabbook set status = '" + s + "' where id =" + id + " "
            mycursor.execute(query)
            conn.commit()
            query1 = " select id,name,vehicle_number,dateofbooking,from_location,to_location,contact_number,status from final_cabbook"
            mycursor.execute(query1)
            records = mycursor.fetchall()
           # messages.success(request,"Approved.")
            return render(request,'DrCabapp/adminapprovecab.html',{'records':records})
        elif request.POST.get("status1"):
                query = "update final_cabbook set status = '" + s1 + "' where id =" + id + " "
                mycursor.execute(query)
                conn.commit()
                query1 = " select id,name,vehicle_number,dateofbooking,from_location,to_location,contact_number,status from final_cabbook"
                mycursor.execute(query1)
                records = mycursor.fetchall()
                #messages.error(request,"Denied.")
                return render(request, 'DrCabapp/adminapprovecab.html', {'records': records})
def userviewbookedcabs(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    s = "Admitted"
    query = "select id,name,vehicle_number,dateofbooking,from_location,to_location,contact_number,status from final_cabbook where status ='" + s + "' "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/userhome.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/userviewbookedcabs.html', {'records': records})



def finalbookmech(request):
        name = request.session["uname"]
        return render(request, 'DrCabapp/finalbookmech.html', {'name': name})


def finalbookingmech(request):
    if request.method == "POST":
        bookname = request.POST["bookinguser_name"]
        bookvehname = request.POST["vehicle_name"]
        mdlnumber = request.POST["Model_Number"]
        probdes = request.POST["problem_description"]
        mecloc = request.POST["mech_location"]
        contactnum = request.POST["contact_number"]
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="drcab")
        mycursor = mydb.cursor()
        status = "Denied"
        q = "insert into final_mechbook(user_name,vehicle_name,model_number,problem_description,location,contact_number,status) values('" +  bookname + "','" + bookvehname + "','" + mdlnumber + "' ,'" + probdes + "' ,'" + mecloc + "','" + contactnum + "','" + status + "')"
        mycursor.execute(q)
        mydb.commit()
        return render(request, 'DrCabapp/finalbookmech.html')
def mechanicapproverequest(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    query = "select * from final_mechbook"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/mechhome.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/mechanicapproverequest.html', {'records': records})


def mechanicapprovingrequest(request):
    conn = mysql.connector.connect(user='root',password='',host='localhost',database='drcab')
    mycursor = conn.cursor()
    id = request.POST["reqid"]
    s = "Admitted"
    s1 = "Denied"
    if request.method == 'POST':
        if request.POST.get("status"):
            query = "update final_mechbook set status = '" + s + "' where id =" + id + " "
            mycursor.execute(query)
            conn.commit()
            query1 = "select id,user_name,vehicle_name,model_number,problem_description,location,contact_number,status from final_mechbook"
            mycursor.execute(query1)
            records = mycursor.fetchall()
           # messages.success(request,"Approved.")
            return render(request,'DrCabapp/mechanicapproverequest.html',{'records':records})
        elif request.POST.get("status1"):
                query = "update final_mechbook set status = '" + s1 + "' where id =" + id + " "
                mycursor.execute(query)
                conn.commit()
                query1 = "select id,user_name,vehicle_name,model_number,problem_description,location,contact_number,status from final_mechbook"
                mycursor.execute(query1)
                records = mycursor.fetchall()
                #messages.error(request,"Denied.")
                return render(request, 'DrCabapp/mechanicapproverequest.html', {'records': records})
def userviewbookedmechanics(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    s = "Admitted"
    query = "select id,user_name,vehicle_name,model_number,problem_description,location,contact_number,status from final_mechbook where status ='" + s + "' "
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/userhome.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/userviewbookedmechanics.html', {'records': records})


def finalbookdriver(request):
        name = request.session["uname"]

        vnum = request.POST["vnum"]
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
        mycursor = conn.cursor()
        s = "Admitted"
        query = "select id,first_name,last_name,phone_number,email,experience,dl_number,pan,gender from driver_reg where status ='" + s + "' "
        mycursor.execute(query)
        if mycursor.rowcount == 0:
            msg = "No records found"
            return render(request, 'DrCabapp/userhome.html', {'msg': msg})
        else:
            records = mycursor.fetchall()
            return render(request, 'DrCabapp/viewdriveruser.html', {'records': records ,'name': name, 'vnum': vnum })
def bookdriver(request):
    name = request.session["uname"]

    vnum = request.POST["vehicle_number"]
    print("hello")
    print(vnum)

    return render(request, 'DrCabapp/viewdriveruser.html', {'name': name,  'vnum': vnum})
def bookdriver1(request):
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    name = request.session["uname"]
    vnum = request.POST["vnum"]
    dname = fname+lname
    return render(request, 'DrCabapp/finalbookdriver.html', {'name': name,  'vnum': vnum ,'dname': dname })
def finalbookingdriver(request):
    if request.method == "POST":
        bokname = request.POST["bookername"]
        vehnumber = request.POST["vehnum"]
        bookidate = request.POST["bookingdate"]
        fromlocat = request.POST["from_location"]
        tolocat = request.POST["to_location"]
        contnumb = request.POST["contactnumber"]
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database="drcab")
        mycursor = mydb.cursor()
        status = "Denied"
        q = "insert into final_driverbook(name,vehicle_number,dateofbooking,from_location,to_location,contact_number,status) values('" + bokname + "', '" + vehnumber + "' , '" + bookidate + "','" + fromlocat + "' ,'" + tolocat + "' ,'" + contnumb + "','" + status + "')"
        mycursor.execute(q)
        mydb.commit()
        return render(request, 'DrCabapp/finalbookdriver.html')
def driverapproverequest(request):
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    query = "select * from final_driverbook"
    mycursor.execute(query)
    if mycursor.rowcount == 0:
        msg = "No records found"
        return render(request, 'DrCabapp/driverhome.html', {'msg': msg})
    else:
        records = mycursor.fetchall()
        return render(request, 'DrCabapp/driverapproverequest.html', {'records': records})

def driverapprovingrequest(request):
    conn = mysql.connector.connect(user='root',password='',host='localhost',database='drcab')
    mycursor = conn.cursor()
    id = request.POST["driverid"]
    s = "Admitted"
    s1 = "Denied"
    if request.method == 'POST':
        if request.POST.get("status"):
            query = "update final_driverbook set status = '" + s + "' where id =" + id + " "
            mycursor.execute(query)
            conn.commit()
            query1 = " select id,name,vehicle_number,dateofbooking,from_location,to_location,contact_number,status from final_driverbook"
            mycursor.execute(query1)
            records = mycursor.fetchall()
           # messages.success(request,"Approved.")
            return render(request,'DrCabapp/driverapproverequest.html',{'records':records})
        elif request.POST.get("status1"):
                query = "update final_driverbook set status = '" + s1 + "' where id =" + id + " "
                mycursor.execute(query)
                conn.commit()
                query1 = "select id,name,vehicle_number,dateofbooking,from_location,to_location,contact_number,status from final_driverbook"
                mycursor.execute(query1)
                records = mycursor.fetchall()
                #messages.error(request,"Denied.")
                return render(request, 'DrCabapp/driverapproverequest.html', {'records': records})
def usereditprofile1(request):
    return render(request,'DrCabapp/usereditprofile.html')

def usereditprofile(request):
    em = request.POST['mail']
    fn = request.POST['first_name']
    ln = request.POST['last_name']
    phno = request.POST['phone_number']
    newpass = request.POST['new_password']
    conpass = request.POST['confirm_password']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='drcab')
    mycursor = conn.cursor()
    if request.method == "POST":
        mw = "update user_reg set email='" + em + "',first_name='" + fn + "',last_name='" + ln + "',phone_number='" + phno + "', password='" + newpass + "', confirm_password='" + conpass + "' where email = '" + em + "' "
        mycursor.execute(mw)
        conn.commit()
       # m = "select email,first_name,last_name,phone_number,password,confirm_password from user_reg"
       # mycursor.execute(m)
        #records = mycursor.fetchall()
        return render(request, 'DrCabapp/usereditprofile.html')
    else:
        messages = "Please Enter valid data"
        return render(request,'DrCabapp/usereditprofile.html')








