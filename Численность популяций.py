from tkinter import*
chis=Tk()
chis.title("Численность популяций")
chis.geometry("550x580")

lb_fon=Label(chis, bg="purple", width=150, height=100);lb_fon.place(x=0,y=0)

lb_nr=Label(chis, bg="khaki", fg="blue", width=40, font='Times 15');lb_nr["text"]="Неограниченный рост";lb_nr.place(x=50, y=5)
lb_a=Label(chis, bg="black", fg="gold", width=2);lb_a["text"]="a";lb_a.place(x=15, y=45)
ent_nr=Entry(chis, width=5, bg="cyan", fg="black"); ent_nr.place(x=50, y=46)
bt_nr=Button(chis, width=20, background="brown", foreground="lime"); bt_nr["text"]="Неограниченный рост"; bt_nr.place(x=100, y=42)
lb_ner=Label(chis, bg="aquamarine", fg="black", width=25, font='Times 15');lb_ner.place(x=260, y=41)

lb_or=Label(chis, bg="khaki", fg="blue", width=40, font='Times 15');lb_or["text"]="Ограниченный рост";lb_or.place(x=50, y=90)
lb_b=Label(chis, bg="black", fg="gold", width=2);lb_b["text"]="b";lb_b.place(x=15, y=130)
ent_or=Entry(chis, width=5, bg="cyan", fg="black"); ent_or.place(x=50, y=132)
bt_or=Button(chis, width=20, background="brown", foreground="lime"); bt_or["text"]="Ограниченный рост"; bt_or.place(x=100, y=130)
lb_og=Label(chis, bg="aquamarine", fg="black", width=5, font='Times 15');lb_og.place(x=270, y=129)

lb_ort=Label(chis, bg="khaki", fg="blue", width=40, font='Times 15');lb_ort["text"]="Ограниченный рост с отловом";lb_ort.place(x=50, y=175)
lb_c=Label(chis, bg="black", fg="gold", width=2);lb_c["text"]="c";lb_c.place(x=15, y=220)
ent_ort=Entry(chis, width=5, bg="cyan", fg="black"); ent_ort.place(x=50, y=222)
bt_ort=Button(chis, width=25, background="brown", foreground="lime"); bt_ort["text"]="Ограниченный рост с отловом"; bt_ort.place(x=100, y=220)
lb_ogr=Label(chis, bg="aquamarine", fg="black", width=5, font='Times 15');lb_ogr.place(x=300, y=219)

lb_jx=Label(chis, bg="khaki", fg="blue", width=40, font='Times 15');lb_jx["text"]="Жертва-хищник";lb_jx.place(x=51, y=260)
lb_d=Label(chis, bg="black", fg="gold", width=2);lb_d["text"]="d";lb_d.place(x=15, y=305)
ent_d=Entry(chis, width=5, bg="cyan", fg="black"); ent_d.place(x=50, y=306)
bt_jx=Button(chis, width=25, background="brown", foreground="lime"); bt_jx["text"]="Жертва-хищник"; bt_jx.place(x=330, y=302)
lb_f=Label(chis, bg="black", fg="gold", width=2);lb_f["text"]="f";lb_f.place(x=95, y=305)
ent_f=Entry(chis, width=5, bg="cyan", fg="black"); ent_f.place(x=130, y=306)
lb_g=Label(chis, bg="black", fg="gold", width=2);lb_g["text"]="g";lb_g.place(x=175, y=305)
ent_g=Entry(chis, width=6, bg="cyan", fg="black"); ent_g.place(x=210, y=306)
lb_jer=Label(chis, bg="black", fg="gold", width=10);lb_jer["text"]="Жертвы";lb_jer.place(x=70, y=330)
lb_jr=Label(chis, bg="aquamarine", fg="black", width=3);lb_jr.place(x=150, y=330)
lb_xish=Label(chis, bg="black", fg="gold", width=10);lb_xish["text"]="Хищники";lb_xish.place(x=270, y=330)
lb_xis=Label(chis, bg="aquamarine", fg="black", width=3);lb_xis.place(x=350, y=330)

lb_jrt=Label(chis, width=8, bg="black", fg="gold"); lb_jrt["text"]="Жертвы"; lb_jrt.place(x=10, y=380)
ent_jrt=Entry(chis, width=5, bg="cyan", fg="black"); ent_jrt.place(x=100, y=381)
lb_xsn=Label(chis, width=8, bg="black", fg="gold"); lb_xsn["text"]="Хищники"; lb_xsn.place(x=10, y=410)
ent_xsn=Entry(chis, width=5, bg="cyan", fg="black"); ent_xsn.place(x=100, y=411)

lb_kc=Label(chis, width=10, bg="black", fg="gold"); lb_kc["text"]="Кол.циклов"; lb_kc.place(x=10, y=450)
ent_kc=Entry(chis, width=5, bg="cyan", fg="black"); ent_kc.place(x=100, y=451)

bt_gra=Button(chis, width=8, bg="brown", fg="lime"); bt_gra["text"]="График"; bt_gra.place(x=50, y=510)
lb_gra=Label(chis, bg="white", width=50, height=13); lb_gra.place(x=175, y=365)

def neogr(event):
    a=float(ent_nr.get())
    N=int(ent_kc.get())
    jertv=int(ent_jrt.get())
    for i in range(N):
        jertv=jertv*a
    lb_ner["text"]=str(int(jertv))
bt_nr.bind("<Button-1>", neogr)

def ogr(event):
    a=float(ent_nr.get())
    b=float(ent_or.get())
    N=int(ent_kc.get())
    jertv=int(ent_jrt.get())
    for i in range(N):
        jertv=jertv*(a-b*jertv)
    lb_og["text"]=str(int(jertv))
bt_or.bind("<Button-1>", ogr)

def ogr_s_otl(event):
    a=float(ent_nr.get())
    b=float(ent_or.get())
    c=float(ent_ort.get())
    N=int(ent_kc.get())
    jertv=int(ent_jrt.get())
    for i in range(N):
        jertv=(a-b*jertv)*jertv-c
    lb_ogr["text"]=str(int(jertv))
bt_ort.bind("<Button-1>", ogr_s_otl)

def jer_xi(event):
    a=float(ent_nr.get())
    b=float(ent_or.get())
    c=float(ent_ort.get())
    d=float(ent_d.get())
    f=float(ent_f.get())
    g=float(ent_g.get())
    N=int(ent_kc.get())
    jertv=int(ent_jrt.get())
    xi=int(ent_xsn.get())
    for i in range(N):
        jertv=(a-b*jertv)*jertv-c-f*jertv*xi
        xi=d*xi+g*jertv*xi
    lb_jr["text"]=str(int(jertv))
    lb_xis["text"]=str(int(xi))
bt_jx.bind("<Button-1>", jer_xi)

chis.mainloop()


