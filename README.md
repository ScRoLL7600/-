from tkinter import*
chis=Tk()
chis.title("Численность популяций")
chis.geometry("550x580")

lb_nr=Label(chis, bg="black", fg="red");lb_nr["text"]="Неограниченный рост";lb_nr.place(x=200, y=5)
lb_a=Label(chis, bg="black", fg="lime", width=2);lb_a["text"]="a";lb_a.place(x=15, y=45)
ent_nr=Entry(chis, width=5, bg="black", fg="orange"); ent_nr.place(x=50, y=46)
bt_nr=Button(chis, width=20, background="black", foreground="yellow"); bt_nr["text"]="Неограниченный рост"; bt_nr.place(x=100, y=42)
lb_nr=Label(chis, bg="gray", fg="red", width=30);lb_nr.place(x=300, y=45)

lb_or=Label(chis, bg="black", fg="red");lb_or["text"]="Ограниченный рост";lb_or.place(x=206, y=90)
lb_b=Label(chis, bg="black", fg="lime", width=2);lb_b["text"]="b";lb_b.place(x=15, y=130)
ent_or=Entry(chis, width=5, bg="black", fg="orange"); ent_or.place(x=50, y=132)
bt_or=Button(chis, width=20, background="black", foreground="yellow"); bt_or["text"]="Ограниченный рост"; bt_or.place(x=100, y=130)
lb_or=Label(chis, bg="gray", fg="red", width=5);lb_or.place(x=300, y=133)

lb_ort=Label(chis, bg="black", fg="red");lb_ort["text"]="Ограниченный рост с отловом";lb_ort.place(x=180, y=175)
lb_c=Label(chis, bg="black", fg="lime", width=2);lb_c["text"]="c";lb_c.place(x=15, y=220)
ent_ort=Entry(chis, width=5, bg="black", fg="orange"); ent_ort.place(x=50, y=222)
bt_ort=Button(chis, width=25, background="black", foreground="yellow"); bt_ort["text"]="Ограниченный рост с отловом"; bt_ort.place(x=100, y=220)
lb_ort=Label(chis, bg="gray", fg="red", width=5);lb_ort.place(x=330, y=223)

lb_jx=Label(chis, bg="black", fg="red");lb_jx["text"]="Жертва-хищник";lb_jx.place(x=220, y=260)
lb_d=Label(chis, bg="black", fg="lime", width=2);lb_d["text"]="d";lb_d.place(x=15, y=305)
ent_jx=Entry(chis, width=5, bg="black", fg="orange"); ent_jx.place(x=50, y=306)
bt_jx=Button(chis, width=25, background="black", foreground="yellow"); bt_jx["text"]="Жертва-хищник"; bt_jx.place(x=330, y=302)
lb_f=Label(chis, bg="black", fg="lime", width=2);lb_f["text"]="f";lb_f.place(x=95, y=305)
ent_f=Entry(chis, width=5, bg="black", fg="orange"); ent_f.place(x=130, y=306)
lb_g=Label(chis, bg="black", fg="lime", width=2);lb_g["text"]="g";lb_g.place(x=175, y=305)
ent_g=Entry(chis, width=5, bg="black", fg="orange"); ent_g.place(x=210, y=306)
lb_jer=Label(chis, bg="black", fg="lime", width=10);lb_jer["text"]="Жертвы";lb_jer.place(x=70, y=330)
lb_jr=Label(chis, bg="gray", fg="red", width=3);lb_jr.place(x=150, y=330)
lb_xish=Label(chis, bg="black", fg="lime", width=10);lb_xish["text"]="Хищники";lb_xish.place(x=270, y=330)
lb_xis=Label(chis, bg="gray", fg="red", width=3);lb_xis.place(x=350, y=330)

lb_jrt=Label(chis, width=8, bg="black", fg="lime"); lb_jrt["text"]="Жертвы"; lb_jrt.place(x=10, y=380)
ent_jrt=Entry(chis, width=5, bg="black", fg="orange"); ent_jrt.place(x=100, y=381)
lb_xsn=Label(chis, width=8, bg="black", fg="lime"); lb_xsn["text"]="Хищники"; lb_xsn.place(x=10, y=410)
ent_xsn=Entry(chis, width=5, bg="black", fg="orange"); ent_xsn.place(x=100, y=411)

lb_kc=Label(chis, width=10, bg="black", fg="lime"); lb_kc["text"]="Кол.циклов"; lb_kc.place(x=10, y=450)
ent_kc=Entry(chis, width=5, bg="black", fg="orange"); ent_kc.place(x=100, y=451)

bt_gra=Button(chis, width=8, bg="black", fg="yellow"); bt_gra["text"]="График"; bt_gra.place(x=50, y=510)
lb_gra=Label(chis, bg="gray", width=50); lb_gra.place(x=175, y=375)

chis.mainloop()  

