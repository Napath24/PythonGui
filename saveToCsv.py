from tkinter import *
sa2F=Tk() #สร้างพื้นที่
sa2F.title('โปรแกรมบันทึกไฟล์ลง CSV')
sa2F.geometry("500x650")

txt_input = StringVar(value="")

nLabel = Label(text = "ป้อนข้อความที่ต้องการบันทึก", fg="black").pack()

#สร้างกล่องข้อความเพื่อมาแสดง
info = Entry().pack()
nButton =Button(text= "บันทึกเป็น CSV" ,fg="black").pack()




















sa2F.mainloop()