from tkinter import *
from tkinter import messagebox
import random,os


def search_bills():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumber.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('error','invalid bill number')






if not os.path.exists('bills'):
    os.mkdir('bills')
 #functionality part
def save_bill():
    global  billnumber
    result=messagebox.askyesno('confirm','do you want Bill')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('success',f'fBill number:{billnumber}bill is saved succesfully')


billnumber=random.randint(500,5000)

def bill_area():
    textarea.delete(1.0,END)
    if nameEntry.get()=='':
        messagebox.showerror('Error','Phone number is required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and colddrinkpriceEntry.get()=='':
        messagebox.showerror('Error','no products selected')
    elif  cosmeticpriceEntry.get()=='0Rs' and grocerypriceEntry.get()=='0Rs' and colddrinkpriceEntry.get()=='0Rs':
        messagebox.showerror('Error', 'no products selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBill Number:{billnumber}')
        textarea.insert(END, f'\nCustomer Name:{nameEntry.get()}')
        textarea.insert(END, f'\n=======================================================')
        textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, f'\n=======================================================')
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBath soap\t\t\t{bathsoapEntry.get()}\t\t\t{soaprice}Rs')
        if FacewashEntry.get()!='0':
            textarea.insert(END,f'\nFace wash\t\t\t{FacewashEntry.get()}\t\t\t{Facewashprice}Rs')
        if FacecreamEntry.get()!='0':
            textarea.insert(END,f'\nFaceCream\t\t\t{FacecreamEntry.get()}\t\t\t{Facecreamprice}Rs')
        if  hairgelEntry.get()!='0':
            textarea.insert(END,f'\nHairgel\t\t\t{hairgelEntry.get()}\t\t\t{ hairgelprice}Rs')
        if  perfumeEntry.get()!='0':
            textarea.insert(END,f'\nPerfume\t\t\t{ perfumeEntry.get()}\t\t\t{ perfumeprice}Rs')
        if  BodylotionEntry.get()!='0':
            textarea.insert(END,f'\nBodylotion\t\t\t{ BodylotionEntry.get()}\t\t\t{bodylotionprice}Rs')
        if  RiceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t\t{RiceEntry.get()}\t\t\t{riceprice}Rs')
        if  WheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat\t\t\t{RiceEntry.get()}\t\t\t{Wheatprice}Rs')
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice}Rs')
        if SugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t\t{SugarEntry.get()}\t\t\t{sugarprice}Rs')
        if PulsesEntry.get()!='0':
            textarea.insert(END,f'\nPulses\t\t\t{PulsesEntry.get()}\t\t\t{pulsesprice}Rs')
        if TeaEntry.get()!='0':
            textarea.insert(END,f'\nTea\t\t\t{TeaEntry.get()}\t\t\t{teaprice}Rs')

        if CampaEntry.get() != '0':
            textarea.insert(END, f'\ncampa\t\t\t{CampaEntry.get()}\t\t\t{campaprice}Rs')
        if RedbullEntry.get() != '0':
            textarea.insert(END, f'\nRed BUll\t\t\t{RedbullEntry.get()}\t\t\t{redbull}Rs')
        if spriteEntry.get() != '0':
            textarea.insert(END, f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice}Rs')
        if lassiEntry.get() != '0':
            textarea.insert(END, f'\nLassi\t\t\t{lassiEntry.get()}\t\t\t{lassiprice}Rs')
        if SliceEntry.get() != '0':
            textarea.insert(END, f'\nSlice\t\t\t{SliceEntry.get()}\t\t\t{sliceprice}Rs')
        if ThumbsupEntry.get() != '0':
            textarea.insert(END, f'\nThumbs up\t\t\t{ThumbsupEntry.get()}\t\t\t{thumbsupprice}Rs')
        textarea.insert(END, f'\n-------------------------------------------------------')

        if cosmetictaxEntry.get()!='0.0Rs':
            textarea.insert(END, f'\nCosmetic tax\t\t\t\t\t\t{cosmetictaxEntry.get()}')
        if grocertaxEntry.get() != '0.0Rs':
            textarea.insert(END, f'\nGrocery tax\t\t\t\t\t\t{grocertaxEntry.get()}')
        if drinktaxpriceEntry.get() != '0.0Rs':
            textarea.insert(END, f'\nColdrink tax\t\t\t\t\t\t{drinktaxpriceEntry.get()}')
            textarea.insert(END, f'\n-------------------------------------------------------')
            textarea.insert(END, f'\nTotal bill\t\t\t\t\t\t{totalbillprice}')
            save_bill()
def total():
    global  soaprice,Facewashprice,Facecreamprice,hairgelprice,perfumeprice,bodylotionprice
    global riceprice,Wheatprice,oilprice,sugarprice,pulsesprice,teaprice
    global campaprice,redbull,spriteprice,lassiprice,sliceprice,thumbsupprice
    global totalbillprice
    #cosmetics price calculation
    soaprice=int(bathsoapEntry.get())*20
    Facewashprice=int(FacewashEntry.get())*30
    Facecreamprice=int(FacecreamEntry.get())*40
    hairgelprice=int(hairgelEntry.get())*20
    perfumeprice=int(perfumeEntry.get())*250
    bodylotionprice=int(BodylotionEntry.get())*100


    totalcosmeticprice=soaprice+Facewashprice+Facecreamprice+hairgelprice+perfumeprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,str(totalcosmeticprice)+'Rs')
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,f'{cosmetictax} Rs')

    #Grocery price calculation
    riceprice=int(RiceEntry.get())*50
    Wheatprice=int(WheatEntry.get())*35
    oilprice=int(oilEntry.get())*100
    sugarprice=int(SugarEntry.get())*40
    pulsesprice=int(PulsesEntry.get())*100
    teaprice=int(TeaEntry.get())*60

    totalGroceryprice=riceprice+Wheatprice+oilprice+sugarprice+pulsesprice+teaprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,str(totalGroceryprice)+'Rs')
    grocerytax = totalGroceryprice * 0.05
    grocertaxEntry.delete(0, END)
    grocertaxEntry.insert(0, f'{grocerytax} Rs')

    #coldrinks price calculation
    campaprice=int(CampaEntry.get())*20
    redbull=int(RedbullEntry.get())*45
    spriteprice=int(spriteEntry.get())*45
    lassiprice=int(lassiEntry.get())*30
    sliceprice=int(SliceEntry.get())*45
    thumbsupprice=int(ThumbsupEntry.get())*40

    totalcolddrinkprice=campaprice+redbull+spriteprice+lassiprice+sliceprice
    colddrinkpriceEntry.delete(0,END)
    colddrinkpriceEntry.insert(0,str(totalcolddrinkprice)+'Rs')
    colddrinktax = totalcolddrinkprice * 0.08
    drinktaxpriceEntry.delete(0, END)
    drinktaxpriceEntry.insert(0, f'{colddrinktax } Rs')

    totalbillprice=totalcolddrinkprice+totalcosmeticprice+totalGroceryprice+cosmetictax+grocerytax+colddrinktax
#gui part
root=Tk()
root.title('Retail billing system')
root.geometry('1270x685')
root.iconbitmap('bill_icon.ico')
headinglabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold')
                   ,bg='gray40',fg='gold',bd=12,relief=GROOVE)
headinglabel.pack(fill=X)


customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',13,'bold'),
                                  fg='gold',bd=8,bg='gray40',relief=GROOVE)
customer_details_frame.pack(fill=X)

customerlabel=Label(customer_details_frame,text='Name',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
customerlabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

Phonelabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
Phonelabel.grid(row=0,column=2,padx=20,pady=2)

ColumnEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
ColumnEntry.grid(row=0,column=3,padx=8)

Billnolabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
Billnolabel.grid(row=0,column=4,padx=20,pady=2)

BillnoEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
BillnoEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('times new roman',13,'bold'),bd=7,width=10,command=search_bills)
searchButton.grid(row=0,column=6,padx=10,pady=8)

productsFrame=Frame(root)
productsFrame.pack(fill=X)

cosmeticframe=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',13,'bold'),bg='gray40',
                    fg='gold')
cosmeticframe.grid(row=0,column=0)

bathsoaplabel=Label(cosmeticframe,text='Bath soap',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
bathsoaplabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
bathsoapEntry=Entry(cosmeticframe,font=('times new roman',13,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

Facecreamlabel=Label(cosmeticframe,text='Face Cream',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
Facecreamlabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
FacecreamEntry=Entry(cosmeticframe,font=('times new roman',13,'bold'),width=10,bd=5)
FacecreamEntry.grid(row=1,column=1,pady=9,padx=10)
FacecreamEntry.insert(0,0)

Facewashlabel=Label(cosmeticframe,text='Face Wash',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
Facewashlabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
FacewashEntry=Entry(cosmeticframe,font=('times new roman',13,'bold'),width=10,bd=5)
FacewashEntry.grid(row=2,column=1,pady=9,padx=10)
FacewashEntry.insert(0,0)

perfumelabel=Label(cosmeticframe,text='Perfume',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
perfumelabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
perfumeEntry=Entry(cosmeticframe,font=('times new roman',13,'bold'),width=10,bd=5)
perfumeEntry.grid(row=3,column=1,pady=9,padx=10)
perfumeEntry.insert(0,0)

hairgellabel=Label(cosmeticframe,text='Hair Gel',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
hairgellabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
hairgelEntry=Entry(cosmeticframe,font=('times new roman',13,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

Bodylotionlabel=Label(cosmeticframe,text='Body Lotion',font=('times new roman',15,'bold'),bg='gray40',
                    fg='white')
Bodylotionlabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
BodylotionEntry=Entry(cosmeticframe,font=('times new roman',13,'bold'),width=10,bd=5)
BodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
BodylotionEntry.insert(0,0)

Groceryframe=LabelFrame(productsFrame,text='Grocery',font=('times new roman',13,'bold'),bg='gray40',
                    fg='gold')
Groceryframe.grid(row=0,column=1)

Ricelabel=Label(Groceryframe,text='Rice',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
Ricelabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
RiceEntry=Entry( Groceryframe,font=('times new roman',13,'bold'),width=10,bd=5)
RiceEntry.grid(row=0,column=1,pady=9,padx=10)
RiceEntry.insert(0,0)

Wheatlabel=Label(Groceryframe,text='Wheat',font=('times new roman',15,'bold'),bg='gray40',
                    fg='white')
Wheatlabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
WheatEntry=Entry( Groceryframe,font=('times new roman',13,'bold'),width=10,bd=5)
WheatEntry.grid(row=1,column=1,pady=9,padx=10)
WheatEntry.insert(0,0)

Pulseslabel=Label(Groceryframe,text='Pulses',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
Pulseslabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
PulsesEntry=Entry( Groceryframe,font=('times new roman',13,'bold'),width=10,bd=5)
PulsesEntry.grid(row=2,column=1,pady=9,padx=10)
PulsesEntry.insert(0,0)

oillabel=Label(Groceryframe,text='Oil',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
oillabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
oilEntry=Entry( Groceryframe,font=('times new roman',13,'bold'),width=10,bd=5)
oilEntry.grid(row=3,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

Sugarlabel=Label(Groceryframe,text='Sugar',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
Sugarlabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
SugarEntry=Entry( Groceryframe,font=('times new roman',13,'bold'),width=10,bd=5)
SugarEntry.grid(row=4,column=1,pady=9,padx=10)
SugarEntry.insert(0,0)

Tealabel=Label(Groceryframe,text='Tea',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
Tealabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
TeaEntry=Entry( Groceryframe,font=('times new roman',13,'bold'),width=10,bd=5)
TeaEntry.grid(row=5,column=1,pady=9,padx=10)
TeaEntry.insert(0,0)

Cold_drinksframe=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',13,'bold'),bg='gray40',
                    fg='gold')
Cold_drinksframe.grid(row=0,column=2)

campalabel=Label( Cold_drinksframe,text='Campa',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
campalabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
CampaEntry=Entry( Cold_drinksframe,font=('times new roman',13,'bold'),width=10,bd=5)
CampaEntry.grid(row=0,column=1,pady=9,padx=10)
CampaEntry.insert(0,0)

Redbulllabel=Label( Cold_drinksframe,text='Red Bull',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
Redbulllabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
RedbullEntry=Entry( Cold_drinksframe,font=('times new roman',13,'bold'),width=10,bd=5)
RedbullEntry.grid(row=1,column=1,pady=9,padx=10)
RedbullEntry.insert(0,0)

spritelabel=Label( Cold_drinksframe,text='Sprite',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
spritelabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
spriteEntry=Entry( Cold_drinksframe,font=('times new roman',13,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

Slicelabel=Label( Cold_drinksframe,text='Slice',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
Slicelabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
SliceEntry=Entry( Cold_drinksframe,font=('times new roman',13,'bold'),width=10,bd=5)
SliceEntry.grid(row=3,column=1,pady=9,padx=10)
SliceEntry.insert(0,0)

Thumbsuplabel=Label( Cold_drinksframe,text='Thumbsup',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
Thumbsuplabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
ThumbsupEntry=Entry( Cold_drinksframe,font=('times new roman',13,'bold'),width=10,bd=5)
ThumbsupEntry.grid(row=4,column=1,pady=9,padx=10)
ThumbsupEntry.insert(0,0)

lassilabel=Label( Cold_drinksframe,text='Lasssi',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
lassilabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
lassiEntry=Entry( Cold_drinksframe,font=('times new roman',13,'bold'),width=10,bd=5)
lassiEntry.grid(row=5,column=1,pady=9,padx=10)
lassiEntry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billarealabel=Label(billframe,text='Bill Area',font=('times new roman',13,'bold'),bd=7,relief=GROOVE)
billarealabel.pack(fill=X)
scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

Billmenuframe=LabelFrame(root,text='Bill Menu',font=('times new roman',13,'bold'),bg='gray40',
                    fg='gold')
Billmenuframe.pack(fill=X)
cosmeticpricelabel=Label(Billmenuframe ,text='Cosmetic Price',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
cosmeticpricelabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

cosmeticpriceEntry=Entry( Billmenuframe,font=('times new roman',13,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=9,padx=10)

grocerypricelabel=Label(Billmenuframe ,text='Grocery Price',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
grocerypricelabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

grocerypriceEntry=Entry( Billmenuframe,font=('times new roman',13,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=9,padx=10)

colddrinkpricelabel=Label(Billmenuframe ,text='Cold drink Price',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
colddrinkpricelabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

colddrinkpriceEntry=Entry( Billmenuframe,font=('times new roman',13,'bold'),width=10,bd=5)
colddrinkpriceEntry.grid(row=2,column=1,pady=9,padx=10)

cosmetictaxlabel=Label(Billmenuframe ,text='Cosmetic Tax',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
cosmetictaxlabel.grid(row=0,column=2,pady=9,padx=10,sticky='w')

cosmetictaxEntry=Entry( Billmenuframe,font=('times new roman',13,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=9,padx=10)

grocertaxlabel=Label(Billmenuframe ,text='Grocery tax',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
grocertaxlabel.grid(row=1,column=2,pady=9,padx=10,sticky='w')

grocertaxEntry=Entry( Billmenuframe,font=('times new roman',13,'bold'),width=10,bd=5)
grocertaxEntry.grid(row=1,column=3,pady=9,padx=10)

drinktaxpricelabel=Label(Billmenuframe ,text='Cold drink Tax',font=('times new roman',13,'bold'),bg='gray40',
                    fg='white')
drinktaxpricelabel.grid(row=2,column=2,pady=9,padx=10,sticky='w')

drinktaxpriceEntry=Entry( Billmenuframe,font=('times new roman',13,'bold'),width=10,bd=5)
drinktaxpriceEntry.grid(row=2,column=3,pady=9,padx=10)



buttonframe=Button(Billmenuframe,bd=8,relief=GROOVE)
buttonframe.grid(row=0,column=4,rowspan=3)
billnumberEntry = Entry(customer_details_frame, font=('arial', 15), bdecommerce.py=7, width=18)
billnumberEntry.grid(row=0, column=5, padx=8)


totalbutton=Button(buttonframe,text='Total',font=('arial',16,'bold'),bg='gray40',fg='white'
                   ,bd=5,width=8,pady=10,command=total)
totalbutton.grid(row=0,column=0,pady=20,padx=5)

billbutton=Button(buttonframe,text='Bill',font=('arial',16,'bold'),bg='gray40',fg='white'
                   ,bd=5,width=8,pady=10,command=bill_area)
billbutton.grid(row=0,column=1,pady=20,padx=5)

emailbutton=Button(buttonframe,text='Email',font=('arial',16,'bold'),bg='gray40',fg='white'
                   ,bd=5,width=8,pady=10)
emailbutton.grid(row=0,column=2,pady=20,padx=5)

printbutton=Button(buttonframe,text='Print',font=('arial',16,'bold'),bg='gray40',fg='white'
                   ,bd=5,width=8,pady=10)
printbutton.grid(row=0,column=3,pady=20,padx=5)

clearbutton=Button(buttonframe,text='Clear',font=('arial',16,'bold'),bg='gray40',fg='white'
                   ,bd=5,width=8,pady=10)
clearbutton.grid(row=0,column=4,pady=20,padx=5)
root.mainloop()
