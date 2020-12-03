from tkinter import *
import tkinter.font as tkFont
import pymysql
import tkinter.messagebox as box
root = Tk()
root.title('Login Page')
root.geometry('600x600')
root['bg'] = '#bed2ed'
conn = pymysql.connect("localhost", "root", "mumbai@2019", "dbmsp")
cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS details
#  (Name CHAR(15) NOT NULL,
#  RollNO CHAR(10) NOT NULL,
#  Class CHAR(10) NOT NULL,
#  ID CHAR(10) NOT NULL,
#  EMail CHAR(100) NOT NULL,
#  MobileNo CHAR(50) NOT NULL)""")
fontStylem = tkFont.Font(family="Algerian", size=40)
wlcm = Label(root, text = "Welcome\n To\n Golden Finger", font = fontStylem, bg='#bed2ed')
wlcm.place(x=80,y=20)
# fontStyle = tkFont.Font(family="Calibri", size=15)
# sel = Label(root, text = "Please select the type of room", font = fontStyle, bg='#bed2ed')
# sel.grid(row = 5, column = 10)

# Create a Tkinter variable
# tkvar = StringVar(root)

# # Dictionary with options
# choices = { 'Pizza','Lasagne','Fries','Fish','Potatoennnnnnnnnnnnnnnnnnnnn'}
# tkvar.set('Pizza') # set the default option

# popupMenu = OptionMenu(root, tkvar, *choices)

# popupMenu.grid(row = 30, column=10, columnspan=2, pady=10, padx=10, ipadx=135)
# # on change dropdown value
# def change_dropdown(*args):
#     print( tkvar.get() )

# #link function to change dropdown
# tkvar.trace('w', change_dropdown)

def proceed_br():

	h_city = hce.get()
	r_no = rne.get()
	pbr = Tk()
	pbr.title('book room')
	pbr.geometry('600x600')
	pbr['bg'] = '#bed2ed'

	conn = pymysql.connect("localhost", "root", "mumbai@2019", "dbmsp")
	cur=conn.cursor()
	cur.execute("SELECT count(*) from cust_hist where room_no = " +str(r_no)+" and hotel_id in (SELECT hotel_id FROM hotel where hotel_city = '"+h_city+"')")
	nm =[ naam[0] for naam in cur.fetchall()]
	lb1 = Label(pbr, text = "Total times booked: "+str(nm[0]),font=("arial", 20, "bold"), bg='#bed2ed')
	lb1.place(x=150,y=50)


def proceed_fr():
	hname = hne.get()
	rtype = rte.get()
	pfr = Tk()
	pfr.title('book room')
	pfr.geometry('600x600')
	pfr['bg'] = '#bed2ed'
	
	conn = pymysql.connect("localhost", "root", "mumbai@2019", "dbmsp")
	cur=conn.cursor()
	cur.execute("SELECT count(room_no) from rooms where room_type = '" +rtype+"' and hotel_id in (SELECT hotel_id FROM hotel where hotel_city = '"+hname+"')")
	nm =[ naam[0] for naam in cur.fetchall()]
	lb1 = Label(pfr, text = "Total: "+str(nm[0]),font=("arial", 20, "bold"), bg='#bed2ed')
	lb1.place(x=150,y=50)

	cur.execute("SELECT count(room_no) from rooms where is_available = 'y' and room_type = '" +rtype+"' and hotel_id in (SELECT hotel_id FROM hotel where hotel_city = '"+hname+"')")
	nm1 =[ naam[0] for naam in cur.fetchall()]
	lb2 = Label(pfr, text = "Available: "+str(nm1[0]),font=("arial", 20, "bold"), bg='#bed2ed')
	lb2.place(x=150,y=90)

	conn.commit()
	conn.close() 


def findroom():
	global hne, rte
	fr = Tk()
	fr.title('find room')
	fr.geometry('600x600')
	fr['bg'] = '#bed2ed'

	hn = Label(fr, text = "Enter the Hotel Name",font=("arial", 20, "bold"), bg='#bed2ed')
	hn.place(x=150,y=50)
	hne = Entry(fr,width=25,font=("arial", 20))
	hne.place(x=100,y=100)

	rt = Label(fr, text = "Enter the Room Type",font=("arial", 20, "bold"), bg='#bed2ed')
	rt.place(x=150,y=200)
	rte = Entry(fr,width=25,font=("arial", 20))
	rte.place(x=100,y=250)

	pr_btn = Button (fr, text = "Proceed", font=("arial", 20, "bold"), command = proceed_fr)
	pr_btn.place(x=200, y=380, width = 200 )




def bookroom():
	
	global hce, rne
	br = Tk()
	br.title('book room')
	br.geometry('600x600')
	br['bg'] = '#bed2ed'

	hn = Label(br, text = "Enter the Hotel Name",font=("arial", 20, "bold"), bg='#bed2ed')
	hn.place(x=150,y=50)
	hce = Entry(br,width=25,font=("arial", 20))
	hce.place(x=100,y=100)

	rn = Label(br, text = "Enter the Room Number",font=("arial", 20, "bold"), bg='#bed2ed')
	rn.place(x=150,y=200)
	rne = Entry(br,width=25,font=("arial", 20))
	rne.place(x=100,y=250)

	pr_btn = Button (br, text = "Proceed", font=("arial", 20, "bold"), command = proceed_br)
	pr_btn.place(x=200, y=380, width = 200 )





	


fr_btn = Button (root, text = "find room", font=("arial", 20, "bold"), command = findroom)
fr_btn.place(x=200, y=270, width = 200 )

rb_btn = Button(root, text="room book", font=("arial", 20, "bold"), command = bookroom)
rb_btn.place(x=200, y=350, width = 200 )



# fontStyles = tkFont.Font(family="Calibri", size=15)
# sel = Label(root, text = "Please enter the room number", font = fontStyle, bg='#bed2ed')
# sel.grid(row = 40, column = 10)

# name = Entry(width=30)
# name.place(x=0,y=200)
conn.commit()
conn.close()
root.mainloop() 