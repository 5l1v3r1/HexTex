#!/usr/bin/python
# -*- coding: utf-8 -*-

## Script: HexTex
## Job: Encode/Decode: encodeing From Hex To Text || Decoding From Hex To Text :)
## By: Oseid Aldary

## Liabraries ##

from time import sleep as se
from os import system as sy
from random import choice as cho
from datetime import datetime

###Colors###########
wi = "\033[1;37m" ##>>White
rd = "\033[1;31m" ##>Red
gr = "\033[1;32m" ##>Green
yl = "\033[1;33m" ##>Yallow
bl = "\033[1;34m" ##>Blou
pu = "\033[1;35m" ##>Purple
cy = "\033[1;36m" ##>Cyan
####################

## Random Say
say = ["\033[1;31mGoodBye","\033[1;31mSee You Later","\033[1;31m Have A Nice Day"]
randsay = cho(say)

## Show Time
now = datetime.now()
hour = now.hour
minute = now.minute
second = now.second
timenow = "{}:{}:{}".format(hour,minute,second)

## HEXTEX Function
def HexTex():

  try:
     sy("clear")
     se(0.10)
     print(bl+"["+rd+"---"+bl+"]"+wi+" SCRIPT: "+rd+"[HexTex]"+bl+"                       ["+rd+"---"+bl+"]")
     print(bl+"["+rd+"---"+bl+"]"+wi+" Job: "+gr+"[ Text to Hex | Hex to Text ]"+bl+"     ["+rd+"---"+bl+"]")
     print(bl+"["+rd+"---"+bl+"]"+wi+" CodedBy: "+gr+"OseidAldary.                 "+bl+" ["+rd+"---"+bl+"]")
     print(yl+"[\033[1;37m------------------------------------------------"+yl+"]")
     print(bl+"["+rd+"---"+bl+"]"+"               ["+rd+"Welcome"+bl+"]                ["+rd+"---"+bl+"]")

     se(0.10)
     print(pu+"="*50)
     se(0.10)
     print(rd+"\n   HexTex")
     print(bl+"================")
     se(0.10)
     print(pu+"\t[1]"+yl+"  >"+cy+"  Hex"+rd+" Some"+pu+" Text")
     se(0.10)
     print(pu+"\t[2]"+yl+"  >"+cy+"  Tex"+rd+" Some"+gr+" Hex")
     se(0.10)
     print(pu+"\t[3]"+yl+"  >"+cy+"  Hex"+rd+" Some"+yl+" Text"+wi+" File")
     se(0.10)
     print(pu+"\t[4]"+yl+"  >"+cy+"  Tex"+rd+" Some"+cy+" Hex "+rd+"File\n")
     se(0.10)
     print(pu+"\t[5]"+yl+"  >"+rd+"  Exit"+wi+" -->")
     se(0.10)
     print(" ")
     ch = raw_input(rd+"["+bl+"HexTex"+rd+"]"+cy+" ==> "+rd)
     while ch =="" or ch is None or ch not in ['1','2','3','4','5']:
      if ch not in ['1','2','3','4','5']:
		print("\033[1;33m[\033[1;31m!\033[1;33m][ERROR]\033[1;33m Of Your Choice[\033[1;31m{}\033[1;33m] Is Not In Menu\033[1;31m!!".format(ch))
      ch = raw_input("\033[31m[!]"+bl+"Enter Your Choice"+yl+"?"+cy+" ==> "+rd)

     if ch =="1":
	se(0.10)
	text = raw_input(rd+"[T]["+pu+"Text"+rd+"]"+cy+" ==> "+rd)
	while text =="" or text is None:
	 text = raw_input(rd+"[!]["+gr+"Text"+yl+"?"+rd+"]:> "+pu)
	se(0.10)
        print(" ")
	print(bl+"[H]"+yl+" Enecoding...."+rd+"Text")
	se(1)
	hext = text.encode('hex','strict')
	print(" ")
	print(cy+"[T]"+pu+" Text=[ "+yl+str(text)+pu+" ] Hex=[ "+yl+str(hext)+pu+" ]...."+rd+"Done"+gr+" :)")

     elif ch =="2":
        se(0.10)
        hex = raw_input(rd+"[H]["+pu+"HexCode"+rd+"]"+cy+" ==> "+rd)
        while hex =="" or hex is None:
         hex = raw_input(rd+"[!]["+gr+"HexCode"+yl+"?"+rd+"]:> "+pu)
        se(0.10)
        print(" ")
        print(bl+"[T]"+yl+" Decodeing...."+rd+"Hex")
        se(1)
        try:
           text = hex.decode('hex','strict')
        except:
              print("\033[1;31m[\033[1;33m!\033[1;31m][\033[1;33mERROR\033[1;31m]\033[1;33m This[\033[31m{}\033[1;33m] Is Not A Hex Code\033[1;31m !!!".format(hex.strip()))
	      exit(1)
        print(" ")
        print(cy+"[H]"+pu+" Hex=[ "+yl+str(hex)+pu+" ] Text=[ "+yl+str(text)+pu+" ]...."+rd+"Done"+gr+" :)")

     elif ch =="3":
	 se(0.10)
	 tf = raw_input(pu+"\n[TF]"+rd+"["+gr+"TextFile"+rd+"]"+cy+":> "+yl)
	 while tf =="" or tf is None:
          tf = raw_input(rd+"[!]"+pu+"["+gr+"TextFile"+pu+"]?"+cy+":> "+yl)
	 try:
	    textfile = open(tf, "r")
	 except:
	    print(rd+"[!][ERROR]"+pu+" TextFile"+yl+"[ "+str(tf)+" ]"+pu+" Is Not Found"+rd+" !!!\n"+yl+"[#]"+pu+" Check Your File Location"+gr+" And Try Again :)")
	    exit(1)

	 textfile = open(tf,"r").readlines()
	 se(0.20)
	 print(pu+"="*10+yl+"> "+gr+"Config "+yl+"<"+pu+"="*10)
	 se(0.10)
	 print(gr+"[*]"+pu+" Start At"+yl+":> "+gr+timenow)
         se(0.10)
	 print(gr+"[T]"+pu+" TextFile"+yl+":> "+gr+tf)
         se(0.10)
	 print(cy+"="*30)
	 print(cy+"[H]"+rd+" Hexing"+gr+"......\n")
	 se(1.5)
         loop = 1
	 for T in textfile:
	     H = T.encode('hex','strict')
	     print(bl+"["+str(loop)+"]"+pu+" Encode"+yl+"["+str(T).strip()+"]"+rd+" Hex:"+cy+" ==> "+gr+str(H))
	     loop +=1
	     se(.1)
	 print("\n\033[1;37m-------------------------------\n"+gr+"[*]"+yl+" Shutdown At:[ "+bl+timenow+yl+" ]")
	 print(yl+"[*]"+rd+" Done! "+gr+":)")

     elif ch =="4":
	 se(0.10)
	 hf = raw_input(pu+"\n[HF]"+rd+"["+gr+"HexFile"+rd+"]"+cy+":> "+yl)
	 while hf =="" or hf is None:
          hf = raw_input(rd+"[!]"+pu+"["+gr+"HexFile"+pu+"]?"+cy+":> "+yl)
	 try:
	    hextfile = open(hf, "r")
	 except:
	    print(rd+"[!][ERROR]"+pu+" HexFile"+yl+"[ "+str(hf)+" ]"+pu+" Is Not Found"+rd+" !!!\n"+yl+"[#]"+pu+" Check Your File Location"+gr+" And Try Again :)")
	    exit(1)

	 hexfile = open(hf,"r").readlines()
	 se(0.20)
	 print(pu+"="*10+yl+"> "+gr+"Config "+yl+"<"+pu+"="*10)
	 se(0.10)
	 print(gr+"[*]"+pu+" Start At"+yl+":> "+gr+timenow)
         se(0.10)
	 print(gr+"[H]"+pu+" HexFile"+yl+":> "+gr+hf)
         se(0.10)
	 print(cy+"="*30)
	 print(cy+"[T]"+rd+" Texing"+gr+"......\n")
	 se(1.5)
         loop = 1
	 for h in hexfile:
            try:
	       T = ' '.join([x.decode('hex') for x in h.split()])
            except:
                  T = "\033[1;31m[\033[1;33m!\033[1;31m][\033[1;33mERROR\033[1;31m]\033[1;33m This[\033[31m{}\033[1;33m] Is Not A Hex Code\033[1;31m !!!\n".format(h.strip())
	    print(bl+"["+str(loop)+"]"+pu+" Decode"+yl+"["+str(h).strip()+"]"+rd+" Text:"+cy+" ==> "+gr+str(T))
	    loop +=1
	    se(.1)
	 print("\n\033[1;37m-------------------------------\n"+gr+"[*]"+yl+" Shutdown At:[ "+bl+timenow+yl+" ]")
	 print(yl+"[*]"+rd+" Done! "+gr+":)")

     elif ch =="5":
	print("\n\n\033[31m[E]\033[1;33m Exiting\033[1;31m....\n")
	se(1.5)
	print("\033[1;32m[*] "+randsay+"\033[1;32m :)\033[1;0m\n")

  except KeyboardInterrupt:
	print("\n\n\033[31m[E]\033[1;33m Exiting\033[1;31m....\n")
        se(1.5)
        print("\033[1;32m[*] "+randsay+"\033[1;32m :)\033[1;0m\n")

## HexTex Function Done !:)

## Run HexTex Function
HexTex()
#####################################
## End Of File ######################
## This Script By Oseid Aldary ######
## Have A Nice Day, GoodBye :) ######
#####################################>>Thanks For Using My Simple Script ..Bye :)

