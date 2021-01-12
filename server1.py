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
amount = 0
total = 0
n = []
n1 = []
qty =0
#sum2 = 0
noProcess = 0

def process_start(s_sock):
  global data,sum,co
  s_sock.send(str.encode(data))
  #name1 = s_sock.recv(2048).decode('utf-8')
  #s_sock.send(str.encode(name1))
  #num = s_sock.recv(2048).decode('utf-8')
  #s_sock.send(str.encode(num))
  total=0
  #n=[]
  while True:
   # name = s_sock.recv(2048)
   # s_sock.send(str.encode(name))
   # num = s_sock.recv(2048)
   # s_sock.send(str.encode(num))
    
    opt = s_sock.recv(2048)
    #total =0
    if str(opt.decode('ascii')) in d.keys():
    
      s_sock.send(b"YES")
      name,cost = d[str(opt.decode('ascii'))]
      qty = s_sock.recv(2048).decode('utf-8')
      print(qty)
      s_sock.send(name.encode())
      print ('Product selected -> :',name,'\n','Cost->:',cost)
      amount = (int(qty)*float(cost))
      sum = "{:.2f}".format(amount)
      print("Total ->RM: ",amount)
      total = float(total)+float(amount)
      total = "{:.2f}".format(total)
      print("Big Total->: RM ",total)

      #join sum and total
      out = str(amount)+"-"+str(total)
      print('Total->:',sum)
      s_sock.send(out.encode())
    
      #insert data to list
      n.append([name,cost,qty,amount,total])

    elif str(opt.decode('ascii')) == '99':

      s_sock.send(b"FINISH")
      print(type(n))
      print (n)
      ans = s_sock.recv(2048).decode('utf-8')
      print (ans)
      

      if ans == "YES":
        s_sock.send(bytes(str(ans),'ascii'))
        ans1 = s_sock.recv(2048).decode('utf-8')
        print (ans1)
        fb1 = [item[0] for item in n]
        print (fb1)
        res = [ele for ele in fb1 if(ele in ans1)]
        print (bool(res))
        if bool(res) == True:
          s_sock.send(b"The Product exist") #fb1 in client
          ans2 = s_sock.recv(2048).decode('utf-8') #ans2 in client
          print ("ans2:")
          print (ans2)
          s_sock.send(bytes(str(ans2),'ascii')) #fb2 in client
          print ("fb1")
          print (fb1)
#
          if ans2 == "YES":

            tot2 =0
            tot =0
            for list in range(len(n)):
              for value in range(len(n[list])):
  #              qty1=n[list][2]
   #             cost1=n[list][1]
    #            tot1 = int(qty1)*float(cost1)
     #           n[list][3] = tot1
                if n[list][0] == ans1:
                   print(n[list][0])
                   print ("Jumpa")
      #            qty2 = n[list][2]
       #           cost2=n[list][1]
        #          tot=int(qty2)*float(cost2)
         #         print(tot)
                   y = list
                   y1 = n[y][3]
              tot1 = n[list][3]
              tot2 = tot2+tot1 #total bef delete
            print ("y1")
            print (y1)
            print ("y")
            print (y)
            print ("Delete list==>")
            del n[y]
            print ("n")
            print (n)
     #       tot1 = tot1+tot1
      #      global tott1
       #     tott=0
#            for i in range(len(n)):
#              for j in range (len(n[i])):
 #               if n[i][0] != ans1: #kalau x sama nama product dia akan kurangkan
  #                print ("n[-1][4]")
   #               print (n[-1][4])
    #              sum = n[-1][4]
     #             if y == -1:
      #                sum2 = float(n[i][4])
       #           else:
        #            print ("len(n)")
         #           print (len(n))
          #          sum= float(n[i][4]) 
           #         print ("n[i][4]")
            #        print (n[i][4])
             #       print ("Y1")
              #      print (y1)
                
 #           print ("After delete")
  #          print (n)
   #         sum2 = sum - float(y1)
    #         n[i][4] = sum2
            #print ("Sum3")
            #print (sum3)
   #         print ("Sum2")
    #        print (sum2)
     #       print ("sum")
      #      print (sum)
          #  print ("sum1")
           # print (sum1)
            print ("n")
            print (n)  
             #      print(n[i][3])
           #     tott1= n[i][3]
            #  tott= tott+tott1
             # print(tott)
#            print (n) #lepas delete
            
            for i in range(len(n)):
              if y == 0:
                for j in range(len(n[i])):
                  sum =float(n[y][3])
                  sum1 = float(n[i][3])
              elif y >= 1 and y <= -1:
                for j in rangee(len(n[i])):
                  sum = float(n[y][3])
                  sum1 = float(n[i][3])
              print ("sum")
              print(sum)
              print ("sum1")
              print (sum1)
              sum2 = float(sum1) - float(sum)
              n[i][4] = sum2
              print ("sum  n[i][4]")
              print (i)
              print (n[i][4])

            print ("n")
            print (n)

            anss2 = s_sock.recv(2048).decode('utf-8')
            print ("anss2")
            print (anss2)
            s_sock.send(bytes(str(anss2),'ascii'))
            anss3 = s_sock.recv(2048).decode('utf-8')
            print (anss3)
            s_sock.send(bytes(str(n),'ascii'))
            anss4 = s_sock.recv(2048).decode('utf-8')
            s_sock.send(bytes(str(sum2),'ascii'))
      #
      else:
        print("Client Dont delete anything..")
        sum2=0
        sum=0
        for list in range(len(n)):
          for value in range(len(n[list])):
            name = n[list][0]
            cost = n[list][1]
            qty = n[list][2]
            tcost = n[list][3]
            sum2 = n[list][3]
         
          sum = sum + sum2
        #  sum2 = sum2 +sum
          n1.append([name,cost,qty,tcost,sum2])

        print (n1)
        print("sum")
        print (sum)
        tot= sum2
        print("tot")
        print (tot)
        for i in range(len(n)):
          for j in range (len(n[i])):
            if i == -1:
              sum2 = n[i][4]
        print ("sum2")
        print (sum2)
#          print (sum2)
 #       n = n1.copy()
  #      print (n)

        s_sock.send(bytes(str(ans),'ascii'))
        print (ans)
        ans44=s_sock.recv(2048).decode('utf-8')
        print (ans44)
        s_sock.send(bytes(str(sum),'ascii'))
        ans55 =s_sock.recv(2048).decode('utf-8')
        print (ans55)
        s_sock.send(bytes(str(n),'ascii'))
      
      #insert list to table
      x = (tabulate(n, headers=['Product Name','Price','Quantity','Amount(RM)'],tablefmt="grid",colalign=("center","center","center","center")))
#      y = name1
 #     z = num
      z1 = str(sum2)
      #write table into file
      receipt_file(x,z1)
  #   receipt_file(x,y,z,z1)

      #send_file
      send_file()
      
      print("Connection end", s_addr)
      break

    else:
      s_sock.sendall(b"NO")
      print('No matched item code')
      


  s_sock.close()

#def receipt_file(x,y,z,z1):
def recceipt_file(x,z1):
  date_time = datetime.date.today()
  date_time_str = str(date_time)
  extension = ".txt"
  filename = date_time_str + extension

  with open(filename,'w') as f:
#    f.write("Name: ")
 #   f.write(y)
  #  f.write("\nNumber phone: ")
   # f.write(z)
    #f.write('\nTotal Price(RM): ')
  #  f.write(z1)
    f.write("\nOrder Information\n\n")
    f.close()

  with open(filename, 'a') as f:
    f.write(x)

  f.close()
 

def send_file():

  date_time = datetime.date.today()
  date_time_str = str(date_time)
  extension = ".txt"
  filename = date_time_str + extension
  s_sock.send(filename.encode())
  
  with open(filename,'rb') as f:
    sendF = f.read(1024)
    s_sock.sendall(sendF)
    f.close()

def delete_detail(n,y):
  print ("y")
  print (y)
  print ("Nilai n")
  print ("n[0]")
  print (n[0])
  print ("n[1]")
  print (n[1])
  print ("Delete n[y]")
  print (n[y])
  del n[y]
  print ("N after")
  print (n)
  for i in range(len(n)):
    tot1 =0
    print("tot in func")
    for j in range(len(n[i])):
      tot= n[i][3]
      print (n[i][j])
    tot1= tot1+tot
    print (tot1)

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
        noProcess += 1
        print ("Client: ",str(noProcess))

      except socket.error:
        print ('got a socket error')

  except Exception as e:
    print ('an exception occured!')
    print (e)

