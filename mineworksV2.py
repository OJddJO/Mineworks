from math import *
from kandinsky import fill_rect as fRect,draw_string as dStr
from ion import keydown as k,KEY_EXE as EXE,KEY_OK as OK,KEY_ONE as k1,KEY_TWO as k2,KEY_THREE as k3,KEY_FOUR as k4,KEY_FIVE as k5,KEY_SIX as k6,KEY_SEVEN as k7,KEY_NINE as k9
from random import *
from time import *

dark,light,purple,gray=(75,40,75),(150,100,150),(150,40,150),(125,125,125)

class Menu():
  def mine():
    fRect(170,48,145,126,light);anim(" [1]:Mine",0,30)
      if pickaxe==1:loot=10;chance=6
      if pickaxe==2:loot=20;chance=9
      if pickaxe==3:loot=30;chance=10
      if pickaxe==4:loot=55;chance=13
      if pickaxe==5:loot=50;chance=15
      ld_bar(0.1,210,180)
      fRect(170,46,145,128,light)
      dStr("You mined",170,48,dark,light)
      for i in range(loot*(rebirth+1)):
        _item=item_mining[randint(0,chance)]
        if _item=="s":item[0]+=1;c_stone+=1
        if _item=="c":item[1]+=1;c_coal+=1
        if _item=="ri":item[2]+=1;c_iron+=1
        if _item=="rg":item[3]+=1;c_gold+=1
        if _item=="d":item[4]+=1;c_diamond+=1
        if _item=="o":item[7]+=1;c_obsidian+=1
      dStr(str(c_stone)+"x Stone",190,66,dark,light)
      dStr(str(c_coal)+"x Coal",190,84,dark,light)
      dStr(str(c_iron)+"x Raw Iron",190,102,dark,light)
      dStr(str(c_gold)+"x Raw Gold",190,120,dark,light)
      dStr(str(c_diamond)+"x Diamond",190,138,dark,light)
      dStr(str(c_obsidian)+"x Obsidian",190,156,dark,light)
      sleep(0.1);return item
  def craft():
    
  def smelt():
    
  def sell():
    
  def inventory():
    
  def rebirth():
    
class GameSys():
  def save():    
    open("mw.sav","w").write(str(money)+"\n"+str(pickaxe)+"\n"+str(item)+"\n"+str(rebirth))
  def loadSav():
    anim("[OK]:LOAD SAVE",90,180,purple,dark,3)
      try:
        tmp=open("mw.sav").readlines()
        global money,pickaxe,item,rebirth=tmp[0],tmp[1],tmp[2],tmp[3]
        fRect(0,0,320,222,dark)
        ld_bar()
        sleep(0.1)
        dStr(" Loading save success !",50,101,'green',dark)
      except:
        global money,pickaxe,item,rebirth=0,1,[0,0,0,0,0,0,0,0],0
        fRect(0,0,320,222,dark)
        ld_bar();sleep(0.1)
        dStr(" Loading save failed !",55,97,'red',dark)
  def anim(txt,x,y,col1=gray,col2=dark,rep=1):
    for i in range(rep):
      sleep(0.15)
      dStr(txt,x,y,'white',col2)
      sleep(0.15)
      dStr(txt,x,y,col1,col2)
  def ld_bar(cd=0.075,a=108,b=128):
    x=0
    fRect(a,b,104,9,light)
    for i in range(19):
      sleep(cd)
      fRect(a+2+x,b+2,10,5,(100,40,150))
      x+=5
  def titleScreen():
    fRect(0,0,320,222,dark)
    dStr(" MINEWORKS ",106,100,dark,light)
    dStr("by OJd_dJO",110,125,light,dark)
  def titleAnim():
    if _c==150:add=-1
    if _c==75:add=1
    _c+=add
    dStr("[OK]:PLAY",114,180,(_c,40,_c),dark)
    sleep(0.0075)
    if k(OK):
        anim("[OK]:PLAY",114,180,purple,dark,3)
        run=1
    return _c
  def ini():
    fRect(0,0,320,29,dark)
    dStr("MONEY : "+str(money),12,5,'yellow',dark)
    dStr("[EXE]:Save and Exit",60,200,light,dark)
    fRect(170,30,145,144,light)
    dStr("LD:",170,174,dark,light)
    fRect(210,180,104,9,light)
    fRect(0,30,169,164,dark)
