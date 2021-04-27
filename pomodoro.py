import time 
from playsound import playsound
import tkinter as tk



root = tk.Tk()

class PomodoroApp:
	def __init__(self, master):
		myFrame = tk.Frame(master)
		myFrame.grid()
		name_label = tk.Label(master, text = "Enter a name").grid(row = 1, column = 1)
		time_label = tk.Label(master, text = "Enter how long you want each pomedoro to be: ").grid(row = 2, column = 1)
		session_label = tk.Label(master, text = "Enter how many sessions you will be completing: ").grid(row = 3, column = 1)
		self.master = master


		#canvas = tk.Canvas(root, width = 400, height = 400)
		#canvas.grid()
		self.name_entry = tk.Entry(master)
		self.name_entry.grid(row = 1, column = 2)

		self.time_entry = tk.Entry(master)
		self.time_entry.grid(row = 2, column = 2)

		
		
		self.sessions_entry = tk.Entry(master)
		self.sessions_entry.grid(row = 3, column = 2)
		
		self.myButton = tk.Button(master, text = "Start Pomodoro", command = self.pomodoro, width = 20, height = 1, font = ("Courier", 20))
		self.myButton.grid(row = 20, column = 1)

		self.label = tk.Label(master, text = "", font = ("Courier", 75))
		self.label.grid(row = 20, column = 4)

		self.end_label = tk.Label(master, text = "")
		self.end_label.grid(row = 10, column = 10)
	def countdown(self, time_): 
		t = int(time_*60)
		
		while t > -1:
			mins, secs = divmod(t, 60)
			timer =  '{:02d}:{:02d}'.format(mins, secs)
			self.label.config(text="%s" % timer)
			self.master.update()
			#print(timer, end = "\r")
			time.sleep(1)
			t -= 1 

	def pomodoro(self):
		session_counter = 0
		while session_counter != int(self.sessions_entry.get()): 
			self.countdown(int(self.time_entry.get()))
			playsound('2021-04-26 11-21-29.wav')
			session_counter+=1
			self.countdown(int(self.time_entry.get())/6)
		self.end_label.config(text = f"Nice Job {self.name_entry.get()} you have completed {self.sessions_entry.get()} {self.time_entry.get()} minute sessions")


pomodoro_clock = PomodoroApp(root)

root.mainloop()




#name = input("Enter A name: ")
#t1 = input("Enter how long you want each pomedoro to be: ")
#sessions = input("Enter how many sessions you will be completing: ")
#pomodoro(int(t1), int(sessions), name)