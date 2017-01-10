import matplotlib
from matplotlib.patches import Wedge
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import matplotlib.cm as cm
import spectral as sp
from pylab import figure, axes, pie, title, show
import pylab
from math import sqrt
import math
'''
fig=plt.figure()
ax=fig.add_subplot(111,aspect='equal')

fov = Wedge((50,50),50, 90,208, color="b", alpha=0.9)
print fov
ax.add_artist(fov)
s=100
plt.xticks([i for i in range(s)])
plt.yticks([i for i in range(s)])

plt.show()
'''
e=int(raw_input("Enter input: \n"))
for x in range(e):
    j=raw_input("Enter :")
    o=j.split( )
    deg=((float(o[0]) * (3.6))+ 90)

    f=float(o[1])
    X=float(100-int(o[1]))
    Y=float(o[2])
    di=(Y/X)

    if(sqrt((f-50.0)**2+(Y-50.0)**2) < 50):
     fig=plt.figure()
     ax=fig.add_subplot(111)
     fov=Wedge((50,50),50,90,deg,color='b',alpha=1)
     ax.add_artist(fov)


    #ax.imshow(fov, cmap=cm.jet, interpolation='nearest')
     s=101
     plt.xticks([i for i in range(s)])
     plt.yticks([i for i in range(s)])
     im=math.degrees(math.atan(di))

     if(int(X) > 50 & int(Y) < 50):
         X=X-50.0
         Y=50.0-Y
         si=-(Y/X)

         im=math.degrees(math.atan(si))
         fin = im+360.0
         if(90<=fin<=deg):
             print "Case #%d: black"%(x+1)
         else:
             print "Case #%d: white"%(x+1)

     elif(int(X) < 50 & int(Y) < 50):
         X=50.0-X
         Y=50.0-Y
         si=(Y/X)

         im=math.degrees(math.atan(si))
         fin = im+180.0
         if(90<=fin<=deg):
             print "Case #%d: black"%(x+1)
         else:
             print "Case #%d: white"%(x+1)


     elif(int(X) < 50 & int(Y) > 50):
         X=50.0-X
         Y=Y-50.0

         si=(Y/X)

         im=math.degrees(math.atan(si))
         fin = im-90.0
         if(90<=fin<=deg):
             print "Case #%d: black"%(x+1)
         else:
             print "Case #%d: white"%(x+1)
     elif(int(X) > 50 & int(Y) > 50):
          X=X-50.0
          Y=Y-50.0
          si=(Y/X)

          im=math.degrees(math.atan(si))
          fin = im
          if(90<=fin<=deg):
              print "Black"
          else:
              print "Case #%d: white"%(x+1)
     else:
         print "Case #%d: white"%(x+1)

     '''y=pylab.savefig('matp.png')
     s=plt.imread('matp.png')

     ds=np.array(s)
     l=len(ds)

    #img_artist = plt.imshow(s)

    #plt.plot(100,100,'rx', markeredgewidth=3, markersize=10)
    #print img_artist.cmap((img_artist.norm(s[X,Y])))
    #plt.axis('image')

    #plt.plot(45,55,'rx', markeredgewidth=3, markersize=10)
    #plt.imshow(fig, interpolation='nearest')'''

    else:
     print "white" #print img_artist,"asd"
