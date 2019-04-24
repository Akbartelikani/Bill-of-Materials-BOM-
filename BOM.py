
    
#----------------------------
print('p1')

from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
from math import *
t=[0,"ATLAS", 'Tower48','140', '50','40','110000','50000', '25','5000', '200', '43000','bom.txt','price.txt']
ta=''
t2=['INPUT DATA','Company name:','Product name:','Working hour/month','Total number of personnel','Production workers',
                  'Total cost of company employees/month ($)','Monthly current expenses ($)','The percentage of gross profit tax (%)','The cost of services outside of the company ($)',
                  'Man hour/product','Sell price ($)','BOM file','Price list file'] 
def writef(t1,t2,f):
        #f1=f+".txt"
        #print('file;',f1)
        filew = open(f,"w") 
        for i in range(len(t1)):
            
            print (i,';',t2[i],';',t1[i], file=filew)
            print (i,t2[i],';',t1[i]) 
def saveasa():                         
       t1=[0]
       for i in range (1,14):
            temp=e[i].get()
            print(temp)
            t1.append(temp)  
       print('t1:\n',t1)                   
       directory = asksaveasfilename(initialdir = "/")
       #print (directory  )

       f=directory
       #print('f:',f)
       writef(t1,t2,f)        
def savea():
       f=e26.get()
              
       t1=[0]
       for i in range (1,14):
            temp=e[i].get()
            #print(temp)
            t1.append(temp)  
       print('t1:\n',t1)
       #print('f',f)
       writef(t1,t2,f)
def cal():
   
    def readpr(f):
            list=[]
            file = open(f,"r")
            file.readline()
            for line in file:
                #file.readline()
                temp=line.split("\n")
                line1=str(temp [0])
                line1=line1.replace(',',';')
                line1=line1.split(";")
                y=[x.strip() for x in line1 ]
                list.append(y[2])
                #print(y)
                file.close
            return list
    filename = askopenfilename()
    t=readpr(filename)
    #print(t)
    for i in range(1,len(t)):
        e[i].delete(0, END)
        e[i].insert(10,t[i-1])
    e26.delete(0, END)
    e26.insert(10,filename)    
def bom_open():   
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file    
    e[12].delete(0, END)   
    e[12].insert(10,filename)
    
def pric_open():    
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file    
    e[13].delete(0, END)   
    e[13].insert(10,filename)
    
def win_exit():
    wi.destroy()
    sys.exit()
def show_entry_fields():
   for i in range (16,25):
       Label(wi, text="----------------------------------------------------------").grid(row=i,column=2)
   Label(wi, text="                                                                               ").grid(row=15,column=2)
   for i in range (1,23):
       Label(wi, text="                                                                                  ").grid(row=i,column=3)                          
   Label(wi, text=e[1].get()).grid(row=1,column=3)  
   Label(wi, text=e[2].get()).grid(row=2,column=3)     
   err=0
   for i in range (3,len(e)-3):
       ea=e[i].get()
       s=ea.replace('.','1')
       if s.isdigit():
           eb=ea
           Label(wi, text=eb).grid(row=i,column=3)
       else:
           eb='Error number'
           err=1           
           Label(wi,bg="red", text=eb).grid(row=i,column=3)
           for i in range(15,20):
              Label(wi, text='                                                                ').grid(row=i,column=3) 
   for i in range (12,14):
       ea=e[i].get()
       if os.path.isfile(ea):                                                  
           Label(wi, text=ea).grid(row=i,column=3)
       else:
          Label(wi,bg='red', text='Error file name').grid(row=i,column=3)
          err=1               
   if err==0:
       sumfi,Lacost,Cex_pr,pr_cost,Gp,tx,npr,p_npr= comput(e)
       Label(wi, text=sumfi).grid(row=16,column=3)
       Label(wi, text=e[9].get()).grid(row=17,column=3)
       Label(wi, text=Lacost ).grid(row=18,column=3)
       Label(wi, text=Cex_pr ).grid(row=19,column=3)
       Label(wi, text=pr_cost).grid(row=20,column=3)
       Label(wi, text=Gp).grid(row=21,column=3)
       Label(wi, text=tx).grid(row=22,column=3)
       Label(wi, text=npr).grid(row=23,column=3)
       Label(wi, text=p_npr).grid(row=24,column=3)
   else:
      Label(wi,bg='red', text='Error! Please check the values and try again').grid(row=15,column=2) 
wi = Tk()       
for i in range (1,12):
  Label(wi, text="-----").grid(row=i,column=1)
for i in range (15,25):
  Label(wi, text="-----").grid(row=i,column=1)  
#wi = Tk()
wi.geometry("950x650") # the size of the window width:950, height:650
Label(wi, text="INPUT DATA:").grid(row=0,column=2)
Label(wi, text="OUTPUT DATA:").grid(row=0,column=3)
Label(wi, text="Company name:------------------------------------").grid(row=1)
Label(wi, text="Product name:-------------------------------------").grid(row=2)
Label(wi, text="Working hour/month:-----------------------------").grid(row=3)
Label(wi, text="Total number of employees:-----------------------").grid(row=4)
Label(wi, text="Number of manufacturing employees:------------").grid(row=5)
Label(wi, text="Total cost of company employees/month $:-------").grid(row= 6)
Label(wi, text="Monthly current expenses $:-----------------------").grid(row=7)
Label(wi, text="Percentage of Gross profit tax %:------------------").grid(row=8)
Label(wi, text="Cost of service outside of the company/product $:").grid(row=9)
Label(wi, text="Man hour/product:---------------------------------").grid(row=10)
Label(wi, text="Sell price: $:----------------------------------------").grid(row=11)
Label(wi, text=" B.O.M list fjle:").grid(row=12)
Label(wi, text=" Price list file:").grid(row=13)
Label(wi, text=" RESULT:").grid(row=15)
Label(wi, text="B.O.M cost $-------------------------------------").grid(row=16)
Label(wi, text="Cost of service outside of the company/product $:").grid(row=17)
Label(wi, text="Labor cost $-------------------------------------").grid(row=18)
Label(wi, text="Current expenses /product $------------------------").grid(row=19)
Label(wi, text="Total product cost $--------------------------------").grid(row=20)
Label(wi, text="Gross profit:--------------------------------------").grid(row=21)
Label(wi, text="Tax $:--------------------------------------------- ").grid(row=22)
Label(wi, text="Net profit $:---------------------------------------").grid(row=23)
Label(wi, text="Percentage net profit/ product cost %:-----------").grid(row=24)
Label(wi, text="Current product file:").grid(row=26)
e=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1,14):
   e[i] = Entry(wi,width=50)
   e[i].grid(row=i, column=2)
   e[i].insert(10,t[i])
e26 = Entry(wi,width=50)
e26.grid(row=26, column=2)
e26.insert(10,ta)   
Button(wi, text='Save', command=savea).grid(row=27, column=0, sticky=W, pady=4)
Button(wi, text='Save as', command=saveasa).grid(row=27, column=1, sticky=W, pady=4)
Button(wi, text='Comput', command=show_entry_fields).grid(row=27, column=2, sticky=W, pady=4)
Button(wi, text='exit', command=win_exit).grid(row=27, column=3, sticky=W, pady=4)
Button(wi, text='open', command=bom_open).grid(row=12, column=1, sticky=W, pady=4)
Button(wi, text='open', command=pric_open).grid(row=13, column=1, sticky=W, pady=4)
Button(wi, text='open', command=cal).grid(row=26, column=1, sticky=W, pady=4)
def comput(e):
        
    e1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(3,12):
        e1[i]=e[i].get()
        e1[i]=float(e1[i])
    e1[12]=e[12].get()
    e1[13]=e[13].get()
    def readf(f):
        list=[]
        file = open(f,"r")
        for line in file:
            temp=line.split("\n")
            line1=str(temp [0])
            
            line1=line1.replace(",",";")
            
            line1=line1.split(";")
            
            list.append(line1)
            file.close
        return list
    bom=readf(e1[12])
    print('\nbom:')
    for i in range(len(bom)):
        print(bom[i])
    price=readf(e1[13])
    print('\nprice:')
    bomp=[]
    sumfi=0

    for i in range(len(price)):
        print(price[i])
    print('\ncomput bom price')
    print(['code', 'name', 'unit', 'Required', 'price/unit$','total price'])
    for i in range(1,len(bom)):
        for j in range(len(price)):
            if bom[i][0]==price[j][0]:
                fi=float(bom[i][3])*float(price[j][3])
                sumfi+=fi         
                temp=[bom[i][0],bom[i][1],bom[i][2],bom[i][3],price[j][3], fi]
                print(temp)
                
                bomp.append(temp)
    print("B.O.M Total cost $:",sumfi) #B.O.M Total cost
    em_hour=e1[6]/e1[3]                #Total cost of company employees/hour  $
    em_hour_man= em_hour/e1[5]        #Total cost of company employees/hour/man  $
    Lacost= em_hour_man*e1[10]        #Labor cost
    Lacost=round(Lacost,2) 
    print('Labor cost $:',Lacost)
    Cex_hour=e1[7]/e1[3]               # current expenses/hour
    Cex_hour_man=Cex_hour/e1[5]       # current expenses/hour/man
    Cex_pr= Cex_hour_man*e1[10]       # current expenses/product
    Cex_pr=round(Cex_pr,2) 
    print('The current expenses/product $:', Cex_pr)
    print( 'The cost of service outside of the company/product($)',e1[9])
    pr_cost= sumfi+Lacost+Cex_pr+e1[9] #Total product cost
    pr_cost=round(pr_cost,2)
    print('The cost of product', pr_cost)
    Gp=e1[11]- pr_cost              #Gross profit
    Gp=round(Gp,2)
    print('Gross profit $:',Gp) 
    tx=0
    if Gp>0:
        tx=Gp*e1[8]/100
    print('Tax value($):',tx)
    npr=Gp-tx                       #net profit $
    npr=round(npr,2)  
    print('Net profit $: ',npr)
    p_npr=100*npr/pr_cost                #Percentage net profit/ product cost %
    p_npr=round(p_npr,2) 
    print( 'The percentage of net profit/product cost(%):',p_npr)
    #return pr_cost,Gp,tx,npr,p_npr  
    return sumfi,Lacost,Cex_pr,pr_cost,Gp,tx,npr,p_npr 
mainloop( )

