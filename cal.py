
"""
USING TKINTER
PLEASE USE YOUR OWN
TEXT EDITOR OR IT 
WON'T WORK!!!


Please recommend changes


This is my first tkinter project


"""



from tkinter import *
import math
import datetime

def sayNum(x):
    global exprText
    global mathExrpession
    mathExrpession += x
    exprText.set(mathExrpession)

def enter():
    try:
        global ansText
        global mathExrpession

        
        answer = eval(str(mathExrpession))
        
        
        #print(x=mathExrpession + " = " + str(answer))
        ansText.set(answer)
        
        history(str(mathExrpession) + " = " + str(answer))
        
    
    except ZeroDivisionError:
        ansText.set("ZeroDivisionError")
        history(str(mathExrpession) + " = ZeroDivisionError")
    except SyntaxError:
        ansText.set("SyntaxError")
        history(str(mathExrpession) + " = SyntaxError")
    except:
        ansText.set("Error")
        history(str(mathExrpession) + " = Error")
    finally:
        mathExrpession = ""

def clearC():
    global mathExrpession
    global exprText
    global ansText
    mathExrpession = ""
    exprText.set(None)
    ansText.set(0)

def history(x):
    text = ("[ %s ] %s" % (datetime.datetime.time(datetime.datetime.now()),x))
    text = str(text)
    with open("log.txt","a+") as file:
        file.write(text+"\n")

#Formula
def py(a,b):
    return math.sqrt(a**2+b**2)



# Grid ONLY!!!
def makeButton(location,Btext,Bfont,Bwidth,Bheight,Bbg,Bcommand,Brow,Bcol):
    Button(location,text=Btext,font=Bfont,width=Bwidth,height=Bheight,bg=Bbg,command=Bcommand).grid(row=Brow,column=Bcol)

    
fontSize = ("Times New Roman",32)
buttonWidth = 10
buttonHeight = 1
buttonColor = "#CCCCCC"

mathExrpession = ""
    
root = Tk()
root.title("Calculator")


exprText = StringVar()
ansText = StringVar()

ExprLabel = Label(root,textvariable=exprText,font=fontSize).grid(columnspan=2,row=0,column=0,pady=20)
ansLabel = Label(root,textvariable=ansText,font=fontSize).grid(columnspan=2,row=0,column=2)

exprText.set(None)
ansText.set(0)


# Number 7
makeButton(root,"7",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("7")),1,0)
# Number 8
makeButton(root,"8",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("8")),1,1)
# Number 9
makeButton(root,"9",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("9")),1,2)
# Number 4
makeButton(root,"4",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("4")),2,0)
# Number 5
makeButton(root,"5",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("5")),2,1)
# Number 6
makeButton(root,"6",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("6")),2,2)
# Number 1
makeButton(root,"1",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("1")),3,0)
# Number 2
makeButton(root,"2",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("2")),3,1)
# Number 3
makeButton(root,"3",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("3")),3,2)



# Number 0
makeButton(root,"0",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("0")),4,1)
# Button Period
makeButton(root,".",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum(".")),4,2)
# Button Clear
makeButton(root,"C",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: clearC()),4,0)
# Opening Parentheses
makeButton(root,"(",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("(")),5,0)
# Closing Parentheses
makeButton(root,")",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum(")")),5,1)
# Button Exponent
makeButton(root,"x^y",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("**")),5,2)
# Button Equals
makeButton(root,"=",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: enter()),5,3)
# Button Divide
makeButton(root,"/",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("/")),1,3)
# Button Multiply
makeButton(root,"*",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("*")),2,3)
# Button Subtract
makeButton(root,"-",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("-")),3,3)
# Button Add
makeButton(root,"+",fontSize,buttonWidth,buttonHeight,buttonColor,(lambda: sayNum("+")),4,3)






root.mainloop()

