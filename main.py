import tkinter
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
from datetime import date
from datetime import datetime
import shutil
import subprocess

root = Tk()
root.title("Backup Tool")
root.iconbitmap("Images/icon.ico")

def Screen():
    root.geometry("450x350")
    tlo = PhotoImage(file="Images/bg.png")
    my_label = Label(root,image=tlo)
    my_label.place(x=0,y=0,relwidth=1,relheight=1)


    lbl1 = Label(root,text="Backup TOOL")
    lbl1.pack()



    lbl2 = Label(root,text="Wpisz Sciezke do folderu z którego pliki maja byc skopiowane")
    lbl2.pack(pady=10)

    entry1 = Entry(root,width=50)
    entry1.pack(pady=5)
    
    lbl3 = Label(root,text="Wpisz sciezke do folderu do ktorego pliki maja byc kopiowane")
    lbl3.pack(pady=12)



    entry2 = Entry(root,width=50)
    entry2.pack(pady=10)

    def start():
        x = open("logs.txt","a")
        print("LOGS-",datetime.now() ,"- Wystartowano backup",file=x)
        get1 = entry1.get()
        get2 = entry2.get()

        # Tutaj wpisujemy do skryptu bat ktory odpowiada za kopiowanie plikow nasze sciezki

        y = open("main.bat","w")
        y.write("xcopy" + " " + "\"" + get1 + "\"" + " " + "\"" + get2 + "\"" + " " + "/Y /E /D /C /F /H /I /Z /J")
        y.close()
        # Przez to powyzej do skryptu bat zostala napisana komenda ktora kopjuje pliki
        # Teraz zrobie zeby python uruchomil ten skrypt w batchu
        filepath = "main.bat"
        p = subprocess.Popen(filepath)
        #,shell=True,stdout=subprocess.PIPE
        #stdout, stderr = p.communicate()
        dekoder = print(p.returncode) # is 0 if success
        print("LOGS-",datetime.now() ,"- Zakonczono backup",file=x)
        print("----------",file=x)
        x.close()
        messagebox.showinfo("INFO","Zamknij Okienko programu dopiero po zakonczeniu kopiowania \n Aby sprawdzic kiedy kopiowanie sie skonczylo patrz w konsole aplikacji \n Kopiowanie zakonczylo sie w momencie w ktorym w konsoli pojawil sie dopisek 'X File(s) copied")





    btn1 = Button(root,text="Submit",command=start)
    btn1.pack(pady=10)

    def load():
        f = open("Data/data0.txt","r")
        fileread = f.read()
        
        u = open("main.bat", "w")
        u.write("xcopy" + " " + fileread)
        
        u.close()
        filepath = "main.bat"
        p = subprocess.Popen(filepath)

        #y.write("xcopy" + " " + "\"" + get1 + "\"" + " " + "\"" + get2 + "\"" + " " + "/Y /E /D /C /F /H /I /Z /J")


        

    btn2 = Button(root,text="Wczytaj Sciezki",command=load)
    btn2.pack(pady=5)


    def settingsavex():
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        lbl1.destroy()
        lbl2.destroy()
        lbl3.destroy()
        entry1.destroy()
        entry2.destroy()
        # Usuwanie elemtnow z screen()

        lbl4 = Label(root,text="Podaj sciezke folderu z ktorego pliki maja byc kopiowane")
        lbl4.pack(pady=5)

        entry3 = Entry(root,width=50)
        entry3.pack(pady=10)

        lbl5 = Label(root,text="Podaj sciezke do folderu do ktorego maja byc kopiowane pliki")
        lbl5.pack(pady=5)

        entry4 = Entry(root,width=50)
        entry4.pack(pady=10)

        def zapisz():
            x = open("Data/data0.txt","w")
            get1 = entry3.get()
            get2 = entry4.get()
            print("\"" + get1 + "\""  + " " + "\"" + get2 + "\"" + " " +  "/Y /E /D /C /F /H /I /Z /J",file=x)
            print("start notify.vbs",file=x)
            
    



        btn4 = Button(root,text="Zapisz",command=zapisz)
        btn4.pack()

        def back():
            entry3.destroy()
            entry4.destroy()
            lbl4.destroy()
            lbl5.destroy()
            Screen()

        btn5 = Button(root,text="Powroc do menu glownego (glitched as fuck)",command=back)
        btn5.pack(pady=10)


        


    btn3 = Button(root,text="Zapisz sciezki",command=settingsavex)
    btn3.pack(pady=5)




    root.mainloop()



Screen()




