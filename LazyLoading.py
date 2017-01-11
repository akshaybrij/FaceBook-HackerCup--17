import numpy as np
import math

#x=[y]


i=int(raw_input ( "Enter the input : \n"))
for x in range(i):
    j=int(raw_input(""))
    #print j
    k=[]
    q=[]
    temp=[]
    fin=[]
    cnt=0
    for y in range(j):

        s=int(raw_input(""))
        k.append(s)
        for z in k:
            if z >=  50:
             q.append(z)
             ls=np.asarray(q)
             sort=sorted(ls)
             l=  k.index(z)
             del k[l]


            elif z < 50:
                o=np.array(k)
                w=max(o)
                f=min(o)
                p=2
                sort= sorted(o)

    if z < 50:

                 # print "z",z
                  p=2
                  print sort
                  while(len(sort)>1):
                    try:

                     if(sort[-1] * p >= 50):
                         if(len(sort) > 0):
                             cnt=cnt+1
                             print cnt

                         temp.append(sort[-1])
                         if(len(sort)>=p):
                             del sort[-1]
                         else:

                            break;
                         for e in range(p-1):
                             temp.append(sort[0])

                             del sort[0]


                         print sort
                         if(len(sort)==1):
                              del sort[0]


                     elif(sort[-1] * p < 50):
                         p=p+1

                         if((p-1) > (len(sort)-1)):
                              if(temp > 0):
                                  tempo=sorted(temp)
                                  if(tempo[-1]*p<100):
                                      if(len(sort)>=p):

                                       del sort[:p]
                                      temp.append(sort[-1])
                                      del sort[-1]

                                  else:
                                      print "Come'on"
                     else:
                      break
                    except Exception as e:
                      print str(e)
                  try:
                   if(len(q) > 0) :

                    stm  =  sorted(temp)
                    if(len(q) >= len(sort)):
                       if min(q)*2 < 100 :
                          del(sort[0])

                       else:

                         if(stm[0] < 100):
                             del(sort[0])

                             print sort

                    else:
                       stm  =  sorted(temp)
                       print stm,"stm"
                  except Exception as e:
                      print str(e)



    elif z > 50:
       print "Case#",i,":",len(q)+cnt




print "Case#",i,cnt








                #print k[d-1]






#x.append(i)
#print x
