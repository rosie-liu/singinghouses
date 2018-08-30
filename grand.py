from mcpi.minecraft import Minecraft
import time
import serial
import serial.tools.list_ports

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

pos=mc.player.getTilePos()


ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "Arduino" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')

#wait 2 seconds for arduino board restart
time.sleep(2)

roof1 = []
f=open("roof1.csv",'r')
yay = f.read()
roof_split = yay.split("\n")
for awesome in roof_split:
    roof1.append(awesome.split(","))
print(roof1)

roof2 = []
f2 = open("roof2.csv",'r')
haha = f2.read()
roof2_split = haha.split("\n")
for XD in roof2_split:
    roof2.append(XD.split(","))
print(roof2)

roof3 = []
f3 = open("roof3.csv", 'r')
lmao = f3.read()
roof3_split = lmao.split("\n")
for lul in roof3_split:
    roof3.append(lul.split(","))
print(roof3)

roofs = [roof1,roof2,roof3]


songs = []
f4 = open("songs.csv",'r')
songsyay= f4.read()
songssplit = songsyay.split("\n")
for row in songssplit:
    songs.append(row.split(','))    

song=songs[0]
for note in song:
    ser.write(note.encode())
    time.sleep(1)

class House:
    def __init__(self,data):
        self.x=data[0]
        self.y=data[1]
        self.z=data[2]
        
        print("iminisideinitoooooooooooooooooooooooooooooooooooooooooooooooo",self.x,self.y,self.z)
    def printpos(self):
        print(self.x,self.y,self.z)


    def buildwall(self):
        x0=self.x
        y0=self.y
        z0=self.z
        #wall
        for y in range(4):     
            for x in range(10):
                mc.setBlock(x0+x,y0+y,z0,89)
            for z in range(10):
                mc.setBlock(x0,y0+y,z0+z,89)
            for z in range(10):
                mc.setBlock(x0+x,y0+y,z0+z,89)
            for x in range(10):
                mc.setBlock(x0+x,y0+y,z0+z,89)

        #doorway
        mc.setBlock(x0,y0+1,z0+5,0)
        mc.setBlock(x0,y0+2,z0+5,0)
        mc.setBlock(x0,y0,z0+5,0)
        mc.setBlock(x0,y0+1,z0+4,0)
        mc.setBlock(x0,y0+2,z0+4,0)
        mc.setBlock(x0,y0,z0+4,0)

        #window
        mc.setBlock(x0+5,y0+1,z0,102)
        mc.setBlock(x0+5,y0+2,z0,102)
        mc.setBlock(x0+4,y0+1,z0,102)
        mc.setBlock(x0+4,y0+2,z0,102)
    def getroofpat(self,csvname):
        roof1 = []
        f=open(csvname,'r')
        yay = f.read()
        roof_split = yay.split("\n")
        for awesome in roof_split:
            roof1.append(awesome.split(","))
        print(roof1)
        self.roof = roof1
    def getsong(self,songid):
        self.songid = songid
        print(songid)
    def playsong(self):
        song=songs[self.songid]
        print(song)
        for notes in song:
            ser.write(notes.encode())
            print ("send:"+notes)
            time.sleep(1)
    def buildroof(self):
        roof = self.roof
        x0=self.x
        y0=self.y
        z0=self.z
        print(roof)
        for z in range(10):
            for x in range(10):
                if roof[x][z]=="1":
                    mc.setBlock(x0+x,y0+4,z0+z,1)
                else:
                    mc.setBlock(x0+x,y0+4,z0+z,133)
    def buildfloor(self):
        x0=self.x
        y0=self.y
        z0=self.z
        for z in range(10):
            for x in range(10):
                mc.setBlock(x0+x,y0-1,z0+z,57)

    def buildall(self):
        self.buildwall()
        self.buildfloor() 
        self.buildroof()

myhouses=[]
for Hx in range(3):
    for Hz in range(3):
        for Hy in range(2):
            myhouses.append(House([pos.x+15*Hx,pos.y+15*Hy,pos.z+15*Hz]))

for myhouse in myhouses:
    myhouse.getroofpat("roof1.csv")
    myhouse.getsong(0)
    

myhouses[9].getroofpat("roof3.csv")
myhouses[8].getroofpat("roof2.csv")
myhouses[9].getsong(2)
myhouses[8].getsong(1)

for myhouse in myhouses:
    print("build lot of housesasdlfpqowueioppppppppppppppppppppajskdkjkasdaaaaaaaaaaaaa")
    myhouse.buildall()

if pos.x>=-521 and pos.x<=-514 and pos.z<=64 and pos.z>=57 and pos.y==68:
    mc.postToChat("song one daa")
    stayed_time=stayed_time+1
    if stayed_time>=300:
        mc.player.setTilePos(-527,68,92)
        stayed_time=0
    else:
        nosong

if pos.x>=-574 and pos.x<=-567 and pos.z<=125 and pos.z>=118 and pos.y==69:
    mc.postToChat("song two doodoo")
    stayed_time=stayed_time+1
    if stayed_time>=300:
        mc.player.setTilePos(-527,68,92)
        stayed_time=0
    else:
        nnosong

stayed_time = 0
while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    print("hehe1")
    pos=mc.player.getTilePos()
    print("heeh2")
    mc.postToChat("please goto home x=-530 y=57 z=88 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))


    for myhouse in myhouses:
        if pos.x > myhouse.x and pos.x < myhouse.x+10 and pos.z > myhouse.z and pos.z < myhouse.z+10 and pos.y > myhouse.y and pos.y < myhouse.y+4:
            myhouse.playsong()
    
    if pos.x>=-530 and pos.x<=-523 and pos.z<=95 and pos.z>=88 and pos.y==57:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-527,68,92)
            stayed_time=0
    else:
        stayed_time=0



    
