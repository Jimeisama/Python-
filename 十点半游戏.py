#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
十点半游戏2.0
Author:Zuyou
Date:2022-03-10
"""
bout=0    #回合 
f1="log.txt"
f2="result.txt"
import random
import sys
import tkinter as tk
from tkinter import messagebox

class player():    #创建玩家类
    def __init__(self,player_type_n,card=None):
        self.player_type=player_type_n   #玩家类别，0为闲家，1为庄家
        if player_type_n==0:
            self.player_type="闲家"
        else:
            self.player_type="庄家"
        if card==None:
            self.card=[]
            
    def __str__(self):
        return '{}'.format(self.name)
            
        
        
        
        
        
    #玩家属性:姓名、手牌、手牌点数、筹码、下注数、要牌、爆牌、输赢
    point=0      
    name="bot"    
    chip=100
    bet=0
    flag=True
    bombc=0
    wstaus=None


    
#    def setinfo(self):
#        self.name="bot"
#        self.player_type=player_type
#        self.card=[]
#        self.point=0
#        self.chip=100
#        self.bet=0
#        self.flag=True
#        self.point=0
#        self.wstaus=None
#        self.bombc=0
    
    def showinfo(self):
        if self.bombc==0:
            self.bombc1="否"
        else:
            self.bombc1="是"
        
        if self.wstaus==0:
            self.wstaus1="输了"

        elif self.wstaus==1:
            self.wstaus1="赢了"

        else:
            self.wstaus1='胜负未定/平局'
        print("玩家名称：{}".format(self.name),"玩家类别：{}".format(self.player_type),"筹码数：{}".format(self.chip),"下注数：{}".format(self.bet),"是否要牌：{}".format(self.flag),"手牌：{}".format(self.card),"点数：{}".format(self.point),"是否爆牌：{}".format(self.bombc1),sep="\n")
    
    def wif(self,f):
        seq=("玩家名称：{}".format(self.name),"玩家类别：{}".format(self.player_type),"筹码数：{}".format(self.chip),"下注数：{}".format(self.bet),"是否要牌：{}".format(self.flag),"手牌：{}".format(self.card),"点数：{}".format(self.point),"是否爆牌：{}".format(self.bombc1),"胜负状态：{}".format(self.wstaus1))
        with open(f,"a") as log:            
            log.writelines('\n'+"\n".join(seq)+"\n"+"\n")
            
            
            
    def countpoint(self):       #计算手牌点数程序，输入的参数c是玩家编号
        self.point=0
        for cd in self.card:
            if cd[1:] in ("J", "Q", "K"):
                self.point+=0.5
            elif cd[1:]=="A":
                self.point+=1
            elif len(cd[1:])<2:
                self.point+=int(cd[1:])
            else:
                self.point+=10
        return self.point
    

class cards():                 #创建一个牌类
    def suit(self,n):#用1代表黑桃（spade）、用2代表方片（dianmond）、用3代表红桃（heart）、用4代表梅花（club）#调出花色方法
        SUITS=["♠","♦","♥","♣"]
        self.suit=SUITS[n-1]
        return self.suit

    def newcard(self):    #生成一副新牌方法
        RANKS=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]  #定义了RANKS列表拥有13个元素来存储牌的数值
        SUITS=["♠","♦","♥","♣"]  #定义了SUITS列表来存储牌的4种花色。
        #用s代表黑桃（spade）、用h代表红桃（heart）、用c代表梅花（club）、用d代表方片（dianmond）
        newcd=[]            #定义一个列表用于保存一副牌，初始为空列表。
        i=0;j=0             #创建一副去除大小王的扑克牌
        while i <=12:
            while j <=3:
                newcd.append(SUITS[j]+RANKS[i]) 
                j=j+1
            i=i+1
            j=0
        return newcd
    
    def deal(self):              #一轮的过程
        flag_l=[]
        global bout

        if bout>=1:
            for d in b_seq:
                exec("player{}.flag=random.choice([True,False])".format(d)) 
            flag1=" "
            while flag1 != "T" or flag1 != "F":
                flag1=input("您是否补牌？（是，输入T；不是，输入F。）")
                if flag1=="T":
                    print("yes")
                    exec("player{}.flag=True".format(nb_local))
                    break
                elif flag1=="F":
                    exec("player{}.flag=False".format(nb_local))
                    break
                else:
                    print("重新再输")
                    continue
                
            for d in player_seq:         #发牌
                if eval('player{}.flag==True'.format(d)):
                    flag_l.append(1)
            print('要牌人数',len(flag_l))
            if len(flag_l)==0:
                win()              

            hh=1
            while hh <= len(player_seq):
                if eval('player{}.flag==True'.format(hh)):
                    exec('player{}.card.append(scard[0])'.format(hh))
                    del scard[0] 
                hh+=1
            
            player_point=[]            #爆牌检测
            for q in player_seq:
                exec('player{}.countpoint()'.format(q))
#                exec('print(player{}.countpoint())'.format(q));exec('print(player{}.card)'.format(q))
                exec('player_point.append(player{}.point)'.format(q))
            print(player_point)
            for d in player_seq:       
                if player_point[d_local-1]>10.5 and d==d_local-1:
                    exec('player{}.bombc=1'.format(d_local))   #庄家爆牌标识码更新
                    exec('player{}.wstaus=0'.format(d_local)) 
                    p_ndwin()               #庄家失败，写入log文件

                    print("庄家爆牌，游戏结束")
                    print("庄家手牌如下：",eval('player{}.card'.format(d_local)))
                    sys.exit()
                    
                elif player_point[d-1]>10.5 and d!=d_local:
                    exec('player{}.bombc=1'.format(d))
                    print("闲家",eval('player{}.name'.format(d)),"点数为",player_point[d-1],"爆牌了！")
                    print("手牌如下：",eval('player{}.card'.format(d)))

            bomb_l=[]     #闲家爆牌列表
            for e in nd_seq:
                if eval('player{}.bombc==1'.format(e)):
                    bomb_l.append(1)
            if len(bomb_l)==len(nd_seq):                
                p_dwin()         #闲家失败，写入log文件                

                print("闲家均爆牌，庄家胜利！游戏结束。");result_tx="闲家均爆牌，庄家胜利！游戏结束。"
                sys.exit()
            

#——————————————————————————函数部分——————————————————————————————————————

        
snip="——————————————————————"
def psnip():                #分割线打印程序
    print(snip)
   
def printinfo(n):    #第bout回合玩家信息打印程序
    global result_tx,bout
    psnip()
    print("第",bout,"轮结束")
    psnip()
    print("玩家信息",snip,end="\n")
        
    print("这是你第{}轮的信息：".format(bout))     #打印和写入非机器人玩家信息
    exec("player{}.showinfo()".format(nb_local))   
    psnip()
    exec("player{}.wif(f1)".format(nb_local))                                         
    for na in b_seq:                           #打印和写入机器人玩家信息
        exec("player{}.showinfo()".format(na))
        psnip()
    exec("player{}.wif(f1)".format(na))        
    print("牌堆还有",len(scard),"张牌")
   
    with open("log.txt","a") as log:    #本回合信息写入log文件
        log.writelines("第{}轮结束,本回合信息如下：".format(n+1)+snip+"\n")
    for d in player_seq:
        exec('player{}.wif(f1)'.format(d))

def p_ndwin():      #闲家胜利，写入两个文件
    global bout,f1,f2
    exec('player{}.wstaus=0'.format(d_local))   #更新胜负信息
    for e in nd_seq:
        exec('player{}.wstaus=1'.format(e))
    printinfo(bout)
            
    with open("log.txt","a") as log:
        log.write("游戏在第{}回合结束".format(bout)+"闲家胜利！输出信息"+"\n")
    for d in player_seq:
        exec('player{}.wif(f1)'.format(d))
  
    with open(f2,"a") as result:
        result.write("游戏在第{}回合结束".format(bout)+"闲家胜利！结算信息如下"+"\n")
    for d in player_seq:
        exec('player{}.wif(f2)'.format(d)) 
        
    print("游戏在第{}回合结束".format(bout)+"闲家胜利！")



def p_dwin():
    global bout,f1,f2
    exec('player{}.wstaus=1'.format(d_local))   #更新胜负信息
    for e in nd_seq:
        exec('player{}.wstaus=0'.format(e))
    printinfo(bout)

    with open("log.txt","a") as log:
        log.write("游戏在第{}回合结束!".format(bout)+"庄家胜利！输出信息:"+"\n")
    for d in player_seq:
        exec('player{}.wif(f1)'.format(d))
        
    with open(f2,"a") as result:
        result.write("游戏在第{}回合结束".format(bout)+"庄家胜利！结算信息如下"+"\n")
    for d in player_seq:
        exec('player{}.wif(f2)'.format(d))
    
    print("游戏在第{}回合结束".format(bout)+"庄家胜利！")


def ww():
    global bout
    exec('player{}.wstaus=None'.format(d_local))   #更新胜负信息
    for e in nd_seq:
        exec('player{}.wstaus=None'.format(e))
    printinfo(bout)
    with open("log.txt","a") as log:
        log.write("游戏在第{}回合结束".format(bout)+"平局！输出信息"+"\n")
    for d in player_seq:
        exec('player{}.wif(f1)'.format())
        
    with open(f2,"a") as result:
        result.write("游戏在第{}回合结束".format(bout)+"平局！结算信息如下"+"\n")
    for d in player_seq:
        exec('player{}.wif(f2)'.format())
    
    print("游戏在第{}回合结束".format(bout)+"平局！")

    
def win():           #比牌程序
    global result_tx,bout
    player_point=[]
    fl=[]   #五龙玩家编号列表
    e=0
    d=0
    while d <= len(player_seq)-1:
        exec('player_point.append(player{}.countpoint())'.format(d+1))       
    fpoint=player_point[:]
    for point in player_point:
        e+=1
        if point<10.5 and eval('len(player{}.card)==5'.format(e)):
            fl.append(e)
    
    if len(fl)==0:          #无五龙出现
        if fpoint.count(max(fpoint))==1 and fpoint[d_local]==max(fpoint):   #庄家胜利
            p_dwin()
            
        elif fpoint.count(max(fpoint))==1 and fpoint[d_local]!=max(fpoint):
            p_ndwin()
            
        elif fpoint.count(max(fpoint))>1 and fpoint[d_local]==max(fpoint):
            ww()
 
        elif fpoint.count(max(fpoint))>1 and fpoint[d_local]!=max(fpoint):            
            p_ndwin()
            
    elif len(fl)==1 and fl[d_local]==0:
        p_dwin()
        
    elif len(fl)==1 and fl[d_local]!=0:
        p_ndwin()
 
    elif len(fl)>1 and fl[d_local]==0:
        ww()
        
    elif len(fl)>1 and fl[d_local]!=0:
        p_ndwin()
    sys.exit() 
    result_tx=result_tx+"\n".join(seq)+"\n"
    result=tk.Tk();result.title("游戏结果");result.geometry("400x400")
    text=tk.Text(result);text.insert(tk.INSERT,result_tx);text.pack()
    result.mainloop()           
   


#———————————————————————————————————主程序—————————————————————————————————————
card1=cards()
raw_card=card1.newcard()             #生成一副洗好的牌
scard=raw_card[:]
random.shuffle(scard)

'''
wel_window=tk.Tk()                  #游戏初始界面窗体
wel_window.geometry('600x800');wel_window.title('十点半游戏 by Zuyou')
lab_1=tk.Label(wel_window,font=('楷体',36,'bold'),bg='green',fg='pink',\
               padx=5,pady=10,text='十点半游戏')
lab_1.pack()
def st_warn():
    messagebox.showwarning('FBI Warning','游戏即将开始')
    wel_window.destroy()
start_bt=tk.Button(wel_window,text='开始游戏',command=st_warn)
start_bt.pack()
exit_bt=tk.Button(wel_window,text='退出游戏',command=lambda:wel_window.destroy())
exit_bt.pack()
wel_window.mainloop()
'''

try:
    player_num=int(input("指定玩家人数:(最少两人，最多四人)"))
except ValueError:
    print("只能输入数字！")
    player_num=input("指定玩家人数:(最少两人，最多四人)")
    while player_num.isdigit()==0 or player_num==None:
        print("只能输入数字！")
        player_num=input("指定玩家人数:(最少两人，最多四人)")
    player_num=int(player_num)
finally:
    while player_num<=1 or player_num>4:
        print("人数溢出，重新再输！")
        try:
            player_num=int(input("指定玩家人数:(最少两人，最多四人)"))  
        except ValueError:
            print("只能输入数字！")
            player_num=input("指定玩家人数:(最少两人，最多四人)")
            while player_num.isdigit()==0 or player_num==None:
                print("只能输入数字！")
                player_num=input("指定玩家人数:(最少两人，最多四人)") 
            player_num=int(player_num)



player_seq=[]
for i in range(1,player_num+1):
    player_seq.append(i)                          #玩家编号列表
for i in range(player_num):                      #创建闲家
    exec('player{}=player(0)'.format(i+1))
d_local=random.choice(player_seq)                           #地主标识码
exec('player{}=player(1)'.format(d_local))    #创建庄家
nd_seq=player_seq[:]                   
nd_seq.remove(d_local)                     #闲家标识码列表
try:
    i=int(input("你想做闲家还是庄家？做庄家输入1，做闲家输入0。"))  
except ValueError:
    print("只能输入数字！")
    i=input("你想做闲家还是庄家？做庄家输入1，做闲家输入0。")
    while i.isdigit()==0 or i==None:
        print("只能输入数字！")
        i=input("你想做闲家还是庄家？做庄家输入1，做闲家输入0。")
    i=int(i)
finally:
    while i<0 or i>1:
        print("重新再输！")
        try:
            i=int(input("你想做闲家还是庄家？做庄家输入1，做闲家输入0。"))  
        except ValueError:
            print("只能输入数字！")
            i=input("你想做闲家还是庄家？做庄家输入1，做闲家输入0。")
            while i.isdigit()==0 or i==None:
                print("只能输入数字！")
                i=input("你想做闲家还是庄家？做庄家输入1，做闲家输入0。")
            i=int(i)                

if i==1:                 #玩家信息初始化
    nb_local=d_local            #玩家标识码
#    exec('player{}.name={}'.format(nb_local,input("输入你的姓名:"))
elif i==0:
    nb_local=random.choice(nd_seq)

exec('player{}.name=str(input("输入你的姓名:"))'.format(nb_local))  #玩家命名      
b_seq=player_seq[:]
b_seq.remove(nb_local)                            #机器人编号列表
d=1
for b in b_seq:                                  #为机器人玩家编号
    exec('player{}.name+=str(d)'.format(b))
    d+=1

for e in b_seq:             #下注
    rb=random.randint(20,99)
    exec('player{}.bet=rb'.format(e))
    exec('player{}.chip-=rb'.format(e))
try:
    exec('player{}.bet=int(input("你要下多少注:"))'.format(nb_local))
except ValueError:
    print("只能输入数字！")
    exec('player{}.bet=int(input("你要下多少注:"))'.format(nb_local))
    while eval('player{}.bet.isdigit()==0'.format(nb_local)) or eval('player{}.bet==None'.format(nb_local)):
        print("重新再输！")
        exec('player{}.bet=input("你要下多少注:")'.format(nb_local))
    exec('g=player{}.bet'.format(nb_local))
    exec('player{}.bet=int(g)'.format(nb_local))
finally:    
    while eval('player{}.bet<=0 or player{}.bet>player{}.chip'.format(nb_local,nb_local,nb_local)):
        print("重新再输！")
        try:
            exec('player{}.bet=int(input("你要下多少注:"))'.format(nb_local))
        except ValueError:
            print("只能输入数字！")
            exec('player{}.bet=input("你要下多少注:")'.format(nb_local))
            while eval('player{}.bet.isdigit()==0'.format(nb_local)) or eval('player{}.bet==None'.format(nb_local)):
                print("重新再输！")
                exec('player{}.bet=input("你要下多少注:")'.format(nb_local))
        exec('g=player{}.bet'.format(nb_local))
        exec('player{}.bet=int(g)'.format(nb_local))
exec('player{}.chip-=player{}.bet'.format(nb_local,nb_local))

                
print('回合开始前的信息:'+snip)
for d in player_seq:
    exec('player{}.showinfo()'.format(d))
    psnip()


while bout<5:
    bout+=1 
    card1.deal()
    printinfo(bout)
win()
