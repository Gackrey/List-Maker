from tkinter import *
import operator
root=Tk()
root.title("LiSt MaKer")
root.minsize(300,300)
root.iconbitmap("pypad.ico")
Label(root,text="Enter the item to insert:",anchor=W).pack(fill=X)
var=Entry(root)
var.pack(fill=BOTH)
Label(root,text="\nThe List is:\n",anchor=W).pack(fill=X)
scr=Scrollbar()
scr.pack(side=RIGHT,fill=Y)
b1=Listbox(exportselection=0,selectmode=EXTENDED,yscrollcommand=(scr, 'set'))
b1.pack(fill=BOTH)
scr.config(command=(b1,'yview'))
save=[]
def ins():
	b1.insert(END,var.get())
	save.append(var.get())
        
def about():
       root1=Tk()
       root1.title("About")
       Label(root1,text="welcome to list maker",font=("ALGERIAN",22,("bold","italic"))).pack()
       Label(root1,text="\n\nMade by:-Gaurav Dey\n Software used:-Python\n\n ",font=("Elephant",14)).pack()
       Label(root1,text="Thanks!!!!!",font=("Forte",16,"bold")).pack()

def usage():
       root2=Tk()
       root2.title("Help")
       Label(root2,text="How to use:",font=("Elephant",18)).pack()
       Label(root2,text="\n\nYou need to enter the list item in the \nsmall box and press the Insert button\n To delete an item click on the item and \npress the Delete button",font=("Bradley Hand ITC",14,"bold")).pack()
       Label(root2,text="Thanks for using LiSt MaKer",font=("Magneto",16)).pack()

def bye():
        root.quit()
        exit()
def delete():
	dell=save.index(b1.get(ANCHOR))
	save.remove(save[dell])
	b1.delete(ANCHOR)

def save1():
            root=Tk()
            root.title("Save")
            root.minsize(200,90)
            Label(root,text="Enter the name of the list:",anchor=W).pack(fill=X)
            name=Entry(root)
            name.pack(side='top',fill=BOTH)
            Button(root,text="Save",command=lambda:save2(root,save,name.get())).pack()
            
            
def save2(master,mem,name):
	x=operator.concat(name,".txt")
	var2=mem+mem
	for i in range(len(mem)):
		var2[i*2]=mem[i]
		var2[(i*2)+1]='\n'
	file=open(x,'w')
	file.writelines(var2)
	file.close()
	y=operator.concat(name," list is saved\nClick on the Close button")
	Label(master,text=y,font=("Arial",12,("bold","italic"))).pack()
	    
b=Button(root,text="Insert",cursor='hand2',command=ins)
b.pack(side="left")
b2= Button(root,text="Delete",cursor='hand1',command=delete)
b2.pack(side="left")
menub=Menu(root)
file=Menu(menub,tearoff=0)
file.add_command(label="Save",command=save1)
file.add_command(label="Exit",command=bye)
menub.add_cascade(label="File",menu=file)
helpo= Menu(menub, tearoff=0)
helpo.add_command(label="How to use", command=usage)
helpo.add_command(label="About...", command=about)
menub.add_cascade(label="Help", menu=helpo)
root.config(menu=menub)
mainloop()
