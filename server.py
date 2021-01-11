import socket
import sys
import os
import time
import errno
from multiprocessing import Process
import math
import json
import datetime
from tabulate import tabulate

d = {'1':('Cleanser',30.45),'2':('Exfoliator',95.00),'3':('Serum',78.80),'4':('Sunscreen',47.50)}
data = json.dumps(d)
m= 0
sum = 0
n = []
n1 = []
qty =0

def process_start(s_sock):
  global data,sum,co
  s_sock.send(str.encode(data))
  name = s_sock.recv(2048).decode('utf-8')
  s_sock.send(str.encode(name))
  num = s_sock.recv(2048).decode('utf-8')
  s_sock.send(str.encode(num))


  while True:
   # name = s_sock.recv(2048)
   # s_sock.send(str.encode(name))
   # num = s_sock.recv(2048)
   # s_sock.send(str.encode(num))
    opt = s_sock.recv(2048)

    if str(opt.decode('ascii')) in d.keys():
    
      s_sock.send(b"YES")
      name,cost = d[str(opt.decode('ascii'))]
      qty = s_sock.recv(2048).decode('utf-8')
      print(qty)
      s_sock.send(name.encode())
      print ('Product selected -> :',name,'\n','Cost->:',cost)
      sum = float(sum) + (float(qty)*float(cost))
      print('Total->:',sum)
      s_sock.send(bytes(str(sum),'ascii'))
    
      #insert data to list
      n.append([name,cost,qty,sum])
      print("List n")
      print (n)

    elif str(opt.decode('ascii')) == '99':

      s_sock.send(b"FINISH")
      print(type(n))
      print (n)
      ans = s_sock.recv(2048).decode('utf-8')
      
      for list in range(len(n)):
        for value in range(len(n[list])):
          name = n[list][0]
          cost = n[list][1]
          qty = n[list][2]
          sum = n[list][3]
        print (sum)

      if ans == "YES":
        s_sock.send(bytes(str(n),'ascii'))
        ans1 = s_sock.recv(2048).decode('utf-8')
        fb1 = [item[0] for item in n]
        res = [ele for ele in fb1 if(ele in ans1)]
        if bool(res) == True:
          s_sock.send(b"The Product exist") #fb1 in client
          ans2 = s_sock.recv(2048).decode('utf-8') #ans2 in client
          s_sock.send(bytes(str(ans2),'ascii')) #fb2 in client
          print ("fb1")
          print (fb1)

          if ans2 == "YES":

            tot2 =0
            tot =0
            for list in range(len(n)):
              for value in range(len(n[list])):
                qty1=n[list][2]
                cost1=n[list][1]
                tot1 = int(qty1)*float(cost1)
                n[list][3] = tot1
                if n[list][0] == ans1:
                  print("list")
                  print(list)
                  print("ans1")
                  print (ans1)
                  print ("n[list][0]")
                  print(n[list][0])
                  qty2 = n[list][2]
                  cost2=n[list][1]
                  tot=int(qty2)*float(cost2)
                  print(tot)
                  y = list-1
                  if list == 0:
                    y = list
                else :
                  y =0
              tot1 = n[list][3]
              tot2 = tot2+tot1 #total bef delete
            print("Delete list==>")
            print(n[y])
            del n[y][0]
            del n[y][1]
            del n[y][2]
            del n[y][3]
            print (n[y][3]) #cost delete
            l = n[y][3]
            tot1 = tot1+tot1
            tots = tot2 - n[y][3]
            global tott1
            tott=0
            for i in range(len(n)):
              for j in range (len(n[i])):
                print(n[i][3])
                tott1= n[i][3]
              tott+=tott+tott1
              print(tott1)
            print (tot2)
            print (tot)
            print ("tot1b")
            print (tot1)
            print (n)
            
            anss2 = s_sock.recv(2048).decode('utf-8')
            print (anss2)
            s_sock.send(bytes(str(anss2),'ascii'))
            anss3 = s_sock.recv(2048).decode('utf-8')
            print ("anss3")
            s_sock.send(bytes(str(n),'ascii'))
            

      #insert list to table
      x = (tabulate(n, headers=['Product Name','Price','Quantity','Amount(RM)'],tablefmt="grid",colalign=("center","center","center","center")))

      #write table into file
      receipt_file(x)

      #send_file
      print("Connection endend")
      break

    else:
      s_sock.sendall(b"No")
      print('No mathced item code')
      continue


  s_sock.close()

def receipt_file(x):
  date_time = datetime.date.today()
  date_time_str = str(date_time)
  extension = ".txt"
  filename = date_time_str + extension

  with open(filename,'w') as f:
    f.write('Order Information\n\n')
    f.close()

  with open(filename, 'a') as f:
    f.write(x)

  f.close()

def delete_detail():
  ans1 = "yes"
  ans2 = "Yes"
  ans = input("Do you want to delete item?")
  if ans == ans1 or ans2:
    print ("delete time...")
    print ("The ori dict..:"+ str(d))
    inp2 = input("Enter item code :")
    if inp2 in d:
      del d[inp2]
      pop_e = d.pop(inp2)
      print ("The dict after delete :"+ str(d))
      print ("Item that has been delete :"+ str(pop_e))
    else:
      print ("Option dont exist")
  else:
    print ("you dont delete anything")

if __name__ == '__main__':

  s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.bind(("",8888))
  print ('listening...')
  s.listen(3)

  try:
    while True:
      try:
        s_sock,s_addr = s.accept()
        print ("\nConnection from:", s_addr)
        p = Process(target = process_start,args = (s_sock,))
        p.start()

      except socket.error:
        print ('got a socket error')

  except Exception as e:
    print ('an exception occured!')
    print (e)

