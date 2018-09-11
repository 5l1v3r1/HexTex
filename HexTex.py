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

####Colors##########
wi = '\033[1;37m' ##>>White
rd = '\033[1;31m' ##>Red
gr = '\033[1;32m' ##>Green
yl = '\033[1;33m' ##>Yallow
bl = '\033[1;34m' ##>Blou
pu = '\033[1;35m' ##>Purple
cy = '\033[1;36m' ##>Cyan
####################

  
## Random Say
say = ["GoodBye", "See You Later", "Have A Nice Day"]
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
     sy("cls || clear")
     se(0.10)
     print(bl+"["+rd+"---"+bl+"]"+wi+" SCRIPT: "+rd+"[HexTex]"+bl+"                       ["+rd+"---"+bl+"]")
     print(bl+"["+rd+"---"+bl+"]"+wi+" Job: "+gr+"[ Text to Hex | Hex to Text ]"+bl+"     ["+rd+"---"+bl+"]")
     print(bl+"["+rd+"---"+bl+"]"+wi+" CodedBy: "+gr+"OseidAldary.                 "+bl+" ["+rd+"---"+bl+"]")
     print(yl+"["+wi+"------------------------------------------------"+yl+"]")
     print(bl+"["+rd+"---"+bl+"]"+"               ["+rd+"Welcome"+bl+"]                ["+rd+"---"+bl+"]")

     se(0.10)
     print(pu+"="*50)
     se(0.10)
     print(rd+"\n   HexTex")
     print(bl+"================")
     se(0.10)
     print(wi+"\t.::["+gr+"1"+wi+"]::."+yl+"  >"+cy+"  Hex"+rd+" Some"+pu+" Text")
     se(0.10)
     print(wi+"\t.::["+gr+"2"+wi+"]::."+yl+"  >"+cy+"  Tex"+rd+" Some"+gr+" Hex")
     se(0.10)
     print(wi+"\t.::["+gr+"3"+wi+"]::."+yl+"  >"+cy+"  Hex"+rd+" Some"+yl+" Text"+wi+" File")
     se(0.10)
     print(wi+"\t.::["+gr+"4"+wi+"]::."+yl+"  >"+cy+"  Tex"+rd+" Some"+cy+" Hex "+rd+"File\n")
     se(0.10)
     print(wi+"\t.::["+gr+"5"+wi+"]::."+yl+"  >"+rd+"  Exit"+wi+" -->")
     se(0.10)
     print(" ")
     ch = raw_input(rd+"["+bl+"HexTex"+rd+"]"+cy+" ==> "+rd)
     while ch =="" or ch is None or ch not in ['1','2','3','4','5']:
      if ch !="":
	if ch not in ['1','2','3','4','5']:
		print(yl+"["+rd+"!"+yl+"][ERROR] Of Your Choice["+rd+ch+yl+"] Is Not In Menu"+rd+"!!!")
      ch = raw_input(rd+"[!]"+bl+"Enter Your Choice"+yl+"?"+cy+" ==> "+rd)

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
	bs = raw_input(gr+"\n["+wi+"b"+gr+"]"+wi+"ack "+gr+"["+wi+"e"+gr+"]"+wi+"xit "+cy+"==> "+gr)
	while bs =="" or bs not in ['b','B','back','Back','BACK','e','E','exit','Exit','EXIT']:
	    bs = raw_input(gr+"["+wi+"b"+gr+"]"+wi+"ack"+gr+" ["+wi+"e"+gr+"]"+wi+"xit "+yl+"==>"+rd+"? "+gr)
	if bs in ['b','B','back','Back','BACK']:
            sy("cls && HexTex.py || clear && python HexTex.py")
	else:
            print(rd+"\n\n[E]"+yl+" Exiting"+rd+"....\n")
            se(1.5)
            print(gr+"[*] "+rd+randsay+gr+":)\n"+wi)
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
	   print(cy+"[H]"+pu+" Hex=[ "+yl+str(hex)+pu+" ] Text=[ "+yl+str(text)+pu+" ]...."+rd+"Done"+gr+" :)")
           bs = raw_input(gr+"\n["+wi+"b"+gr+"]"+wi+"ack "+gr+"["+wi+"e"+gr+"]"+wi+"xit "+cy+"==> "+gr)
           while bs =="" or bs not in ['b','B','back','Back','BACK','e','E','exit','Exit','EXIT']:
              bs = raw_input(gr+"["+wi+"b"+gr+"]"+wi+"ack"+gr+" ["+wi+"e"+gr+"]"+wi+"xit "+yl+"==>"+rd+"? "+gr)
           if bs in ['b','B','back','Back','BACK']:
             sy("cls && HexTex.py || clear && python HexTex.py")
           else:
              print(rd+"\n\n[E]"+yl+" Exiting"+rd+"....\n")
              se(1.5)
              print(gr+"[*] "+rd+randsay+gr+":)\n"+wi)
              exit(1)
        except:
              print(rd+"["+yl+"!"+rd+"]["+yl+"ERROR"+rd+"]"+yl+" This["+rd+hex.strip()+yl+"] Is Not A Hex Code"+rd+" !!!")
              bs = raw_input(gr+"\n["+wi+"b"+gr+"]"+wi+"ack "+gr+"["+wi+"e"+gr+"]"+wi+"xit "+cy+"==> "+gr)
              while bs =="" or bs not in ['b','B','back','Back','BACK','e','E','exit','Exit','EXIT']:
                bs = raw_input(gr+"["+wi+"b"+gr+"]"+wi+"ack"+gr+" ["+wi+"e"+gr+"]"+wi+"xit "+yl+"==>"+rd+"? "+gr)
              if bs in ['b','B','back','Back','BACK']:
                  sy("cls && HexTex.py || clear && python HexTex.py")
              elif bs in ["e","E","exit","Exit","EXIT"]:
                  print(rd+"\n\n[E]"+yl+" Exiting"+rd+"....\n")
                  se(1.5)
                  print(gr+"[*] "+rd+randsay+gr+":)\n"+wi)
                  pass
            
     elif ch =="3":
	 se(0.10)
	 tf = raw_input(pu+"\n[TF]"+rd+"["+gr+"TextFile"+rd+"]"+cy+":> "+yl)
	 while tf =="" or tf is None:
          tf = raw_input(rd+"[!]"+pu+"["+gr+"TextFile"+pu+"]?"+cy+":> "+yl)
	 try:
	    textfile = open(tf, "r")
	 except:
	    print(rd+"[!][ERROR]"+pu+" TextFile"+yl+"[ "+str(tf)+" ]"+pu+" Is Not Found"+rd+" !!!\n"+yl+"[#]"+pu+" Check Your File Location"+gr+" And Try Again :)")
	    exit()

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
	 print(wi+"\n-------------------------------\n"+gr+"[*]"+yl+" Shutdown At:[ "+bl+timenow+yl+" ]")
	 print(yl+"[*]"+rd+" Done! "+gr+":)")
         bs = raw_input(gr+"\n["+wi+"b"+gr+"]"+wi+"ack "+gr+"["+wi+"e"+gr+"]"+wi+"xit "+cy+"==> "+gr)
         while bs =="" or bs not in ['b','B','back','Back','BACK','e','E','exit','Exit','EXIT']:
             bs = raw_input(gr+"["+wi+"b"+gr+"]"+wi+"ack"+gr+" ["+wi+"e"+gr+"]"+wi+"xit "+yl+"==>"+rd+"? "+gr)
         if bs in ['b','B','back','Back','BACK']:
            sy("cls && HexTex.py || clear && python HexTex.py")
         else:
            print(rd+"\n\n[E]"+yl+" Exiting"+rd+"....\n")
            se(1.5)
            print(gr+"[*] "+rd+randsay+gr+":)\n"+wi)
            exit(1)

     elif ch =="4":
	 se(0.10)
	 hf = raw_input(pu+"\n[HF]"+rd+"["+gr+"HexFile"+rd+"]"+cy+":> "+yl)
	 while hf =="" or hf is None:
          hf = raw_input(rd+"[!]"+pu+"["+gr+"HexFile"+pu+"]?"+cy+":> "+yl)
	 try:
	    hextfile = open(hf, "r")
	 except:
	    print(rd+"[!][ERROR]"+pu+" HexFile"+yl+"[ "+str(hf)+" ]"+pu+" Is Not Found"+rd+" !!!\n"+yl+"[#]"+pu+" Check Your File Location"+gr+" And Try Again :)")
	    exit()

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
                  T = rd+"["+yl+"!"+rd+"]["+yl+"ERROR"+rd+"]"+yl+" This["+rd+h.strip()+yl+"] Is Not A Hex Code"+rd+"!!!\n"
	    print(bl+"["+str(loop)+"]"+pu+" Decode"+yl+"["+str(h).strip()+"]"+rd+" Text:"+cy+" ==> "+gr+str(T))
	    loop +=1
	    se(.1)
	 print(wi+"\n-------------------------------\n"+gr+"[*]"+yl+" Shutdown At:[ "+bl+timenow+yl+" ]")
	 print(yl+"[*]"+rd+" Done! "+gr+":)")
         bs = raw_input(gr+"\n["+wi+"b"+gr+"]"+wi+"ack "+gr+"["+wi+"e"+gr+"]"+wi+"xit "+cy+"==> "+gr)
         while bs =="" or bs not in ['b','B','back','Back','BACK','e','E','exit','Exit','EXIT']:
             bs = raw_input(gr+"["+wi+"b"+gr+"]"+wi+"ack"+gr+" ["+wi+"e"+gr+"]"+wi+"xit "+yl+"==>"+rd+"? "+gr)
         if bs in ['b','B','back','Back','BACK']:
            sy("cls && HexTex.py || clear && python HexTex.py")
         else:
           
            print(rd+"\n\n[E]"+yl+" Exiting"+rd+"....\n")
            se(1.5)
            print(gr+"[*] "+rd+randsay+gr+":)\n"+wi)
            exit(1)

     elif ch =="5":
         
	print(rd+"\n\n[E]"+yl+" Exiting"+rd+"....\n")
	se(1.5)
	print(gr+"[*] "+rd+randsay+gr+":)\n"+wi)
	exit(1)

  except KeyboardInterrupt:
      
	print(rd+"\n\n[E]"+yl+" Exiting"+rd+"....\n")
	se(1.5)
	print(gr+"[*] "+rd+randsay+gr+":)\n"+wi)
	exit(1)
	
  except EOFError:
	print(rd+"\n\n[E]"+yl+" Exiting"+rd+"....\n")
	se(1.5)
	print(gr+"[*] "+rd+randsay+gr+":)\n"+wi)
	exit(1)

## HexTex Function Done !:)

## Run HexTex Function

HexTex()

#####################################
## End Of File ######################
## This Script By Oseid Aldary ######
## Have A Nice Day, GoodBye :) ######
#####################################>>Thanks For Using My Simple Script ..Bye :)
