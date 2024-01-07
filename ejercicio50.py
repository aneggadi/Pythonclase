#Anwar Neggadi

tab1=0
tab2=0
tab3=0
tab4=0
tab5=0
tab6=0
tab7=0
tab8=0
tab9=0
tab10=0
num=int(input("Elige una tabla del 1 al 10:"))
for f in range(12):
    if num==1:
        tab1=tab1+1
        print(tab1)
    else:
        if num==2:
            tab2=tab2+2
            print(tab2)
        if num==3:
            tab3=tab3+3
            print(tab3)
        if num==4:
            tab4=tab4+4
            print(tab4)
        if num==5:
            tab5=tab5+5
            print(tab5)
        if num==6:
            tab6=tab6+6
            print(tab6)
        if num==7:
            tab7=tab7+7
            print(tab7)
        if num==8:
            tab8=tab8+8
            print(tab8)
        if num==9:
            tab9=tab9+9
            print(tab9)
        if num==10:
            tab10=tab10+10
            print(tab10)
        if num>10:
            print("Es un numero mayor del 10")  