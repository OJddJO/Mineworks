from math import *
from kandinsky import fill_rect as fRect,draw_string as dStr
from ion import keydown as k,KEY_EXE as EXE,KEY_OK as OK,KEY_ONE as k1,KEY_TWO as k2,KEY_THREE as k3,KEY_FOUR as k4,KEY_FIVE as k5,KEY_SIX as k6,KEY_SEVEN as k7,KEY_NINE as k9
from random import *
from time import *

dark,light,purple,gray=(75,40,75),(150,100,150),(150,40,150),(125,125,125)

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
def ini():
  fRect(0,0,320,29,dark)
  dStr("MONEY : "+str(money),12,5,'yellow',dark)
  dStr("[EXE]:Save and Exit",60,200,light,dark)
  fRect(170,30,145,144,light)
  dStr("LD:",170,174,dark,light)
  fRect(210,180,104,9,light)
  fRect(0,30,169,164,dark)
def saving():
  open("money.conf","w").write(str(money))
  open("pickaxe.conf","w").write(str(pickaxe))
  open("item.conf","w").write(str(item))
  open("rebirth.conf","w").write(str(rebirth))

fRect(0,0,320,222,dark)
dStr(" MINEWORKS ",106,100,dark,light)
dStr("by OJd_dJO",110,125,light,dark)
run,load,_c=0,"menu",150

while run==0:
  if _c==150:add=-1
  if _c==75:add=1
  _c+=add
  dStr("[OK]:PLAY",114,180,(_c,40,_c),dark)
  sleep(0.0075)
  if k(OK):
    anim("[OK]:PLAY",114,180,purple,dark,3)
    run=1

dStr("[OK]:LOAD SAVE",90,180,purple,dark)
dStr("[EXE]:NEW GAME",90,198,purple,dark)

while run==1:
  if k(OK):
    anim("[OK]:LOAD SAVE",90,180,purple,dark,3)
    try:
      money=eval(open("money.conf").readline())
      pickaxe=eval(open("pickaxe.conf").readline())
      item=eval(open("item.conf").readline())
      rebirth=eval(open("rebirth.conf").readline())
      fRect(0,0,320,222,dark)
      ld_bar()
      sleep(0.1)
      dStr(" Loading save success !",50,101,'green',dark)
    except:
      money,pickaxe,item,rebirth=0,1,[0,0,0,0,0,0,0,0],0
      fRect(0,0,320,222,dark)
      ld_bar()
      sleep(0.1)
      dStr(" Loading save failed !",55,97,'red',dark)
    run=2
  elif k(EXE):
    anim("[EXE]:NEW GAME",90,198,purple,dark,3)
    money,pickaxe,item,rebirth=0,1,[0,0,0,0,0,0,0,0],0
    fRect(0,0,320,222,dark)
    ld_bar();sleep(0.1)
    dStr("Good Game !",106,101,'green',dark)
    run=2

sleep(2);fRect(0,0,320,222,dark)

while run==2:
  if load=="menu":
    ini();dStr("INFO :",170,30,dark,light)
    dStr(" [1]:Mine\n [2]:Craft\n [3]:Smelt\n [4]:Sell\n [5]:Inventory\n [6]:Rebirth",0,30,gray,dark)
    load="option"
  if load=="option":
    c_stone,c_coal,c_iron,c_gold,c_diamond,c_obsidian=0,0,0,0,0,0
    item_mining=["s","s","s","s","s","c","c","c","c","ri","ri","ri","rg","rg","d","o"]
#mine
    if k(k1):
      fRect(170,48,145,126,light);anim(" [1]:Mine",0,30)
      if pickaxe==1:loot=10;chance=6
      if pickaxe==2:loot=20;chance=9
      if pickaxe==3:loot=30;chance=14
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
      sleep(0.1)
    if k(k2):anim(" [2]:Craft",0,48);load="craft"
    if k(k3):anim(" [3]:Smelt",0,66);load="smelt"
    if k(k4):anim(" [4]:Sell",0,84);load="sell"
    if k(k5):anim(" [5]:Inventory",0,102);load="inventory"
    if k(k6):anim(" [6]:Rebirth",0,120);load="rebirth"

  if load=="craft":
    fRect(170,30,145,144,light)
    dStr("CRAFT :",170,30,dark,light)
    fRect(0,30,169,162,dark)
    fRect(210,180,104,9,light)
    dStr(" [1]:Pickaxe\n\n\n\n\n\n\n\n [9]:Return",0,30,gray,dark)
    load="c_option"
  if load=="c_option":
    def ini_c():
      ini();dStr("CRAFT :",170,30,dark,light)
      dStr(" [1]:Stone\n [2]:Iron\n [3]:Gold\n [4]:Diamond\n\n\n\n\n [9]:Return",0,30,gray,dark)
    if k(k1):anim(" [1]:Pickaxe",0,30);ini_c();load="c_pick"
    if k(k9):anim(" [9]:Return",0,174);load="menu"
  if load=="c_pick":
    def craft(material,i,n_i,m,n_c,_i=item,_m=money,_p=pickaxe):
      if item[i]>=n_i and money>=m:
        ld_bar(0.1,210,180)
        _m-=m;_i[i]-=n_i
        dStr("You crafted",170,48,dark,light)
        dStr(material,170,66,dark,light)
        dStr("pickaxe",170,84,dark,light)
        _p=n_c
      else:
        fRect(170,48,145,126,light)
        dStr("You need "+str(n_i),170,48,dark,light)
        if i<=2:dStr(material+" and "+str(m),170,66,dark,light);dStr("money",170,84,dark,light)
        else:dStr(material+" and",170,66,dark,light);dStr(str(m)+" money",170,84,dark,light)
      return _i[i],_m,_p
    def msg():fRect(170,48,145,126,light);dStr("You already",170,48,dark,light);dStr("got this !",170,66,dark,light)
    if k(k1):
      anim(" [1]:Stone",0,30)
      if pickaxe>=2:msg()
      else:tmp=craft("Stone",0,1000,2000,2);item[0],money,pickaxe=tmp[0],tmp[1],tmp[2]
    if k(k2):
      anim(" [2]:Iron",0,48)
      if pickaxe>=3:msg()
      else:tmp=craft("Iron",5,2500,50000,3);item[5],money,pickaxe=tmp[0],tmp[1],tmp[2]
    if k(k3):
      anim(" [3]:Gold",0,66)
      if pickaxe>=4:msg()
      else:tmp=craft("Gold",6,1000,250000,4);item[6],money,pickaxe=tmp[0],tmp[1],tmp[2]
    if k(k4):
      anim(" [4]:Diamond",0,84)
      if pickaxe>=5:msg()
      else:tmp=craft("Diamond",4,7500,1000000,5);item[4],money,pickaxe=tmp[0],tmp[1],tmp[2]
    if k(k9):anim(" [9]:Return",0,174);load="craft"
    dStr("MONEY : "+str(money),12,5,'yellow',dark)

  if load=="smelt":
    ini();dStr("SMELT:",170,30,dark,light)
    dStr(" [1]:Iron\n [2]:Gold\n\n\n\n\n\n\n [9]:Return",0,30,gray,dark)
    load="s_option"
  if load=="s_option":
    def smelt(material,res,i,c=item[1],_i=item):
      if _i[i]>=1 and c>=1:
        ld_bar(0.1,210,180)
        _i[i]-=1;c-=1;_i[i+3]+=1
        dStr("You smelted ",170,48,dark,light)
        dStr(material,170,66,dark,light)
        dStr("and obtained ",170,84,dark,light)
        dStr(res,170,102,dark,light)
      else:dStr("You need",170,48,dark,light);dStr(material,170,66,dark,light);dStr("and Coal to",170,84,dark,light);dStr("obtain "+res,170,102,dark,light)
      return _i[i],c,_i[i+3]
    if k(k1):fRect(170,48,145,126,light);anim(" [1]:Iron",0,30);tmp=smelt("Raw Iron","Iron",2);item[2],item[1],item[5]=tmp[0],tmp[1],tmp[2]
    if k(k2):fRect(170,48,145,126,light);anim(" [2]:Gold",0,48);tmp=smelt("Raw Gold","Gold",3);item[3],item[1],item[6]=tmp[0],tmp[1],tmp[2]
    if k(k9):anim(" [9]:Return",0,174);load="menu"

  if load=="sell":
    ini();dStr("SELL :",170,30,dark,light)
    dStr(" [1]:Stone\n [2]:Coal\n [3]:Iron\n [4]:Gold\n [5]:Diamond\n\n\n\n [9]:Return",0,30,gray,dark)
    load="sell_option"
  if load=="sell_option":
    def sell(s_item,n_i,value,i=item,m=money):
      m_s=item[n_i]*value
      fRect(170,46,145,128,light)
      dStr("You sold "+str(item[n_i])+"x",170,48,dark,light)
      dStr(s_item,170,66,dark,light)
      dStr("for "+str(m_s),170,84,dark,light)
      i[n_i]-=item[n_i];m+=m_s
      return i[n_i],m
    if k(k1):anim(" [1]:Stone",0,30);tmp=sell("Stone",0,1);item[0],money=tmp[0],tmp[1]
    if k(k2):anim(" [2]:Coal",0,48);tmp=sell("Coal",1,5);item[1],money=tmp[0],tmp[1]
    if k(k3):anim(" [3]:Iron",0,66);tmp=sell("Iron",2,10);item[2],money=tmp[0],tmp[1]
    if k(k4):anim(" [4]:Gold",0,84);tmp=sell("Gold",3,20);item[3],money=tmp[0],tmp[1]
    if k(k5):anim(" [5]:Diamond",0,102);tmp=sell("Diamond",4,50);item[4],money=tmp[0],tmp[1]
    if k(k9):anim(" [9]:Return",0,174);load="menu"
    dStr("MONEY : "+str(money),12,5,'yellow',dark)

  if load=="inventory":
    ini();dStr("INVENTORY :",170,30,dark,light)
    dStr(" [1]:Ingredient\n [2]:Raw Item\n [3]:Miscellanous\n\n\n\n\n\n [9]:Return",0,30,gray,dark)        
    load="i_item"
  if load=="i_item":
    if k(k1):
      anim(" [1]:Ingredient",0,30)
      fRect(170,48,145,126,light)
      dStr("You've got",170,48,dark,light)
      dStr(str(item[0])+"x Stone",190,70,dark,light)
      dStr(str(item[5])+"x Iron",190,88,dark,light)
      dStr(str(item[6])+"x Gold",190,106,dark,light)
      dStr(str(item[4])+"x Diamond",190,124,dark,light)
    if k(k2):
      anim(" [2]:Raw Item",0,48)
      fRect(170,48,145,126,light)
      dStr("You've got",170,48,dark,light)
      dStr(str(item[1])+"x Coal",190,70,dark,light)
      dStr(str(item[2])+"x Raw Iron",190,88,dark,light)
      dStr(str(item[3])+"x Raw Gold",190,106,dark,light)
    if k(k3):
      anim(" [3]:Miscellanous",0,66)
      fRect(170,48,145,126,light)
      dStr("You've got",170,48,dark,light)
      dStr(str(item[7])+"x Obsidian",190,70,dark,light)
    if k(k9):anim(" [9]:Return",0,174);load="menu"

  if load=="rebirth":
    ini();fRect(0,0,320,29,dark)
    dStr("REBIRTH : "+str(rebirth),12,5,purple,dark)
    dStr("REBIRTH :",170,30,dark,light)
    dStr(" [1]:Rebirth\n\n\n\n\n\n\n\n [9]:Return",0,30,gray,dark)
    load="r_rebirth"
  if load=="r_rebirth":
    if k(k1):
      anim(" [1]:Rebirth",0,30)
      if item[7]>=10000:
        ld_bar(0.5,210,180)
        money,pickaxe,item=0,1,[0,0,0,0,0,0,0,0];rebirth+=1
        dStr("Congrats !",170,48,dark,light)
        dStr("Rebirth give",170,66,dark,light)
        dStr("you some boost",170,84,dark,light)
        sleep(2);load="menu"
      else:dStr("You need 10000",170,48,dark,light);dStr("obsidian to",170,66,dark,light);dStr("create the",170,84,dark,light);dStr("portal !",170,102,dark,light)
    if k(k9):anim(" [9]:Return",0,174);load="menu"

  if k(EXE):
    anim("[EXE]:Save and Exit",60,200,light,dark,3)
    saving();fRect(0,0,320,222,dark)
    ld_bar();sleep(0.2)
    dStr("CLICK ON [OK]",94,100,'white',dark);dStr("Your progress has been saved ",18,120,'green',dark);run=3