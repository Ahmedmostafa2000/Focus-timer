import time
from playsound import playsound
from win32api import GetKeyState

from tkinter import *
from tkinter.tix import Balloon,Tk

class timer():
   def __init__(self):
      
      self.start = None
      self.wait_var = None
      self.action = None
      self.running = True
      self.break_dict = {"10%":.1,"20%":.2,"30%":.3,"50%":.5,"60%":.6,"80%":.8}

      self.app()

   def countdowntimer(self,event=None):
      wait_var = self.wait_var
      start = int(self.hrs.get())*3600+ int(self.mins.get())*60 + int(self.sec.get())
      self.repeat_n = int(self.repeat.get())
      while self.repeat_n != -1:
         times = start
         while (times > -1) and self.running:
                    
            minute,second = (times // 60 , times % 60)
            hour =0
            if minute > 60:
               hour , minute = (minute // 60 , minute % 60)
            self.sec.set(second)
            self.mins.set(minute)
            self.hrs.set(hour)
            #Update the time
            self.win.update()

            time.sleep(1)

            if(times == 0):
               self.start = start
               self.break_()
            times -= 1
         self.repeat_n-=1
         self.repeat.set(self.repeat_n)
      else:
         self.repeat_n=0
         self.repeat.set(self.repeat_n)

      
   def break_(self):

      action = self.action
      start = self.start
      wait_var = self.wait_var
      action.set('Break!')
      self.win.attributes('-topmost',1)
      playsound('notify.mp3')
      
      times = int(self.start*float(self.break_dict[self.option_choice.get()]))
      while (times > -1) and self.running:
         minute,second = (times // 60 , times % 60)
         hour =0
         if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
         self.sec.set(second)
         self.mins.set(minute)
         self.hrs.set(hour)
         #Update the time
         self.win.update()

         time.sleep(1)

         if(times == 0):
            self.win.attributes('-topmost',1)
            playsound('notify2.mp3')
            action.set("Focus time!")
            self.sec.set('00')
            self.mins.set('00')
            self.hrs.set('00')
         times -= 1

   def SaveLastClickPos(self,event):
       self.lastClickX, self.lastClickY
       self.lastClickX = event.x
       self.lastClickY = event.y


   def Dragging(self,event):
       x, y = event.x - self.lastClickX + self.win.winfo_x(), event.y - self.lastClickY + self.win.winfo_y()
       self.win.geometry("+%s+%s" % (x , y))

   def wait(self,event=None):
      self.running = not self.running
      if self.running:
         self.countdowntimer()
      

   def quit(event=None):
      exit()

   def empty():
      ...


   def app(self):
      self.win = Tk()

      screen_width = self.win.winfo_screenwidth()-300
      screen_height = self.win.winfo_screenheight()-210



      self.win.title('Focus')
      self.win.geometry(f'280x120+{screen_width}+{screen_height}')
      self.win.overrideredirect(0)
      self.win.frame = Frame(self.win,borderwidth=3,bg='#2d2d2d')

      self.lastClickX = 0
      self.lastClickY = 0


      #self.attributes('-fullscreen', True)
      #self.state('zoomed')
      self.action = StringVar()


      self.win.resizable(False,False)
      self.win.config(bg='#2d2d2d')

      Label(self.win, font =('Consolas',20), textvariable= self.action,bg="#2d2d2d",fg = 'white').place(x=30,y=20-10)
      self.action.set("Focus time!")

      self.sec = StringVar()
      e1 = Entry(self.win, textvariable=self.sec, width = 2, font = 'Consolas 20',bg = "#393939",fg = 'white')
      e1.place(x=110, y=60-10)
      self.sec.set('00')


      self.mins= StringVar()
      e2 = Entry(self.win, textvariable = self.mins, width =2, font = 'Consolas 20',bg = "#393939",fg = 'white')
      e2.place(x=70, y=60-10)
      self.mins.set('00')


      self.hrs= StringVar()
      e3 = Entry(self.win, textvariable = self.hrs, width =2, font = 'Consolas 20',bg = "#393939",fg = 'white')
      e3.place(x=30, y=60-10)
      self.hrs.set('00')


      self.repeat= StringVar()
      e4 = Entry(self.win, textvariable = self.repeat, width =1, font = 'Consolas 20',bg = "#393939",fg = 'white')
      e4.place(x=170, y=60-10)
      self.repeat.set('0')

      Balloon(self.win).bind_widget(e4,balloonmsg="Number of repeats")

      self.repeat_n = int(self.repeat.get())
      



      Button(self.win, text='START', fg = 'white',bd ='0', bg = '#393939',font =('Consolas',10), command = self.countdowntimer).place(x=30, y=100-10)
      Button(self.win, text='⏯', fg = 'white',bd ='0', bg = '#393939',font =('Consolas',10), command = self.wait).place(x=120, y=100-10)
      Button(self.win, text='QUIT', fg = 'white',bd ='0', bg = '#393939',font =('Consolas',10), command = self.quit).place(x=80, y=100-10)


      wait_var = 0







      self.win.bind('<Button-1>', self.SaveLastClickPos)
      self.win.bind('<B1-Motion>', self.Dragging)
      self.win.bind('<Return>', self.countdowntimer)
      self.win.bind('<Escape>',self.quit)

      # if GetKeyState(65) and GetKeyState(32):
      #    self.attributes('-topmost',1)

      OPTIONS = [
      "10%","20%","50%","60%","80%",
      ]


      self.option_choice = StringVar(self.win)
      self.option_choice.set(OPTIONS[1]) # default value

      break_percentile = OptionMenu(self.win, self.option_choice,*OPTIONS)
      break_percentile.place(x=210, y=25-10)

      #Balloon(self.win).bind_widget(break_percentile,balloonmsg="Break Percentile")


      self.win.mainloop()

timer()