from tkinter import *
import socket
from ipaddress import IPv4Network
from IPy import IP

root=Tk()
root.geometry("800x600")
root.resizable(0,0)
root.title("Ipv4")

ip=StringVar()
binrep=StringVar()
classabc=StringVar()
sysop=StringVar()
typeip=StringVar()
gethost=StringVar()
subnet=StringVar()

#-------------------------------Label section-----------------------------#

Label(root,text="IPv4 split",font="Timesnewroman 20 bold").pack()

Label(root,text="Enter Website Address",font="Timesnewroman 12 bold").place(x=30,y=60)

#--------------------------------Entry section------------------------------------------#

Entry(root,font="Timesnewroman 12 italic",textvariable=ip,bg="white",width=35).place(x=210,y=60)

Entry(root,font="Timesnewroman 12 italic",textvariable=gethost,bg="white").place(x=210,y=100)

Entry(root,font="Timesnewroman 12 italic",textvariable=subnet,bg="white",width=35,).place(x=210,y=140)

Entry(root,font="Timesnewroman 12 italic",textvariable=binrep,bg="white",width=35,).place(x=210,y=180)

Entry(root,font="Timesnewroman 12 italic",textvariable=classabc,bg="white").place(x=210,y=220)

Entry(root,font="Timesnewroman 12 italic",textvariable=sysop,bg="white",width=40).place(x=210,y=520)

Entry(root,font="Timesnewroman 12 italic",textvariable=typeip,bg="white").place(x=210,y=260)

#-----------------------------------Functions-------------------------------#

def split(ip1):
    ip=socket.gethostbyname(ip1)
    l=ip.split(sep=".")
    binl=[]
    if((l[0]<'255') and int(l[1]<'255') and int(l[2]<'255') and int(l[2]<'255')):
        for i in range(0,len(l)):
            new=bin(int(l[i])).replace('0b','')
            bin8 = new[::-1]
            while len(bin8) < 8:
                bin8 += '0'
                new = bin8[::-1]
            binl.append(new)
        n=".".join(binl)
        return n
    else:
        return "Check IP address"
    
def sysinfo():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
    sysop.set((f"Hostname: {hostname}"))
    sysop.set((f"{ip_address}"+(f"  Hostname: {hostname}")))

def output():
    binrep.set("")
    binrep.set(split(ip.get()))

def classs(ip1):
    ip=socket.gethostbyname(ip1)
    l=ip.split(sep=".")
    if (int(l[0])<=127):
        return "class A "
    elif(int(l[0])>127 and int(l[0])<=191):
        return "class B"
    elif(int(l[0])>191 and int(l[0])<=223):
        return "class C"
    elif(int(l[0])>223 and int(l[0])<=239):
        return "class D"
    elif(int(l[0])>239 and int(l[0])<255):
        return "class E"
    else:
        return "Please check IP address"
    
def outputclass():
    classabc.set(classs(ip.get()))

def IPtype(ip1):
    ip=socket.gethostbyname(ip1)
    typeofip=IP(ip)
    return (typeofip.iptype())

def outputIPtype():
    typeip.set(IPtype(ip.get()))

def gethostname(ip):
    return socket.gethostbyname(ip)

def outputgethostbyname():
    gethost.set(gethostname(ip.get()))

def sub_net(ip1):
    ip=socket.gethostbyname(ip1)
    net = IPv4Network(ip)
    return net.netmask

def outputsubnet():
    subnet.set(sub_net(ip.get()))

def reset():
    ip.set("")
    binrep.set("")
    classabc.set("")
    sysop.set("")
    typeip.set("")
    gethost.set("")
    subnet.set("")
#--------------------------------------Button Section-------------------------------#

Button(root,font='timesnewroman 10 bold',text="IP address",width=6,command=outputgethostbyname,bg="lightblue",padx=20).place(x=40,y=100)

Button(root,font='timesnewroman 10 bold',text="Subnet Mask",width=6,command=outputsubnet,bg="lightblue",padx=46).place(x=40,y=140)

Button(root,font='timesnewroman 10 bold',text="Binary Representation",width=6,command=output,bg="lightblue",padx=46).place(x=40,y=180)

Button(root,font='timesnewroman 10 bold',text="Class",width=6,command=outputclass,bg="lightblue",padx=2).place(x=40,y=220)

Button(root,font='timesnewroman 10 bold',text="IP Type",width=6,command=outputIPtype,bg="lightblue",padx=3).place(x=40,y=260)

Button(root,font='timesnewroman 10 bold',text="Reset",width=6,command=reset,bg="magenta",padx=20).place(x=60,y=300)

Button(root,font='timesnewroman 10 bold',text="System IP Address",width=6,command=sysinfo,bg="lightblue",padx=45).place(x=40,y=520)



#---------------------------------------------------------#

root.mainloop()