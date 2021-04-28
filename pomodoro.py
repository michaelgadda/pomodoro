import time 
import playsound as playsound
from playsound import playsound
import tkinter as tk



root = tk.Tk()
root.title("Pomodoro")
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
		
		#Read text file containing amount of time spent using in focus
		self.file = open(r"time_log.txt")
		self.all_time = int(self.file.readline())

		#self.w_file = open("time_log.txt", 'w')
		
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


		self.session_tracker_label = tk.Label(master, text = "0/0" , font = ("Courier",20), foreground = "red", background = "black")
		self.session_tracker_label.grid(row = 20, column = 2)

		self.all_time_tracker_label = tk.Label(master, text = f" {self.all_time} minutes studied to-date" , font = ("Courier", 15), foreground = "Midnight Blue")
		self.all_time_tracker_label.grid(row = 2, column = 4)

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
		self.session_tracker_label.config(text = f"{session_counter}/{self.sessions_entry.get()}")
		while session_counter != int(self.sessions_entry.get()): 
			self.countdown(int(self.time_entry.get()))
			self.track_time()
			self.read_and_update_total_time()
			self.master.update()
			playsound('stronger.wav')
			session_counter+=1
			self.session_tracker_label.config(text = f"{session_counter}/{self.sessions_entry.get()}")
			self.countdown(int(self.time_entry.get())/6)
		self.end_label.config(text = f"{self.name_entry.get()}, you have completed {self.sessions_entry.get()} - {self.time_entry.get()} minute session(s)!  ", font = ('Courier', 20), foreground = 'deep pink')


	def track_time(self):
		t_file = open(r"time_log.txt")
		t_all_time = int(t_file.readline())

		add_currently_completed_sess = t_all_time + int(self.time_entry.get())
		#print(add_currently_completed_sess)
		with open('time_log.txt', 'w') as t: 
			t.write(str(add_currently_completed_sess))
	
	def read_and_update_total_time(self):
		r_u_file = open(r"time_log.txt")
		r_u_all_time = int(r_u_file.readline())
		self.all_time_tracker_label.config(text = f" {r_u_all_time} minutes focused to-date")


pomodoro_clock = PomodoroApp(root)

root.mainloop()




#name = input("Enter A name: ")
#t1 = input("Enter how long you want each pomedoro to be: ")
#sessions = input("Enter how many sessions you will be completing: ")
#pomodoro(int(t1), int(sessions), name) 