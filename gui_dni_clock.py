from tkinter import *
import dni_clock
import math
import time

canvas_width = canvas_height = 300
window = Tk()
canvas = Canvas(window, width = canvas_width, height = canvas_height)
canvas.pack()
y = int(canvas_height / 2)
#Misc.tk_bisque(canvas)
center = int(canvas_height / 2)
r = int(canvas_height / 2) - 3
a = math.radians(49)
end_x = int(r*math.cos(a)) + center
end_y = int(r*math.sin(a)) + center

''' Clockface decorations ''' 
# Background
canvas.create_rectangle(0,0,canvas_width,canvas_height, fill="black")
# Circle
canvas.create_oval(3,3,canvas_width-3,canvas_height-3)
# Background pie
pie_fills = ['#531f10', '#79303a', '#dfcf9f', '#d3e0c5', '#e8e1bc']
for n in range(5):
	canvas.create_arc(3,3,canvas_width-3,canvas_height-3, start=-90-72*n, extent=72,fill=pie_fills[n])

# Small divisions/ticks
twentyfifths = 2*math.pi/25
b = math.pi/2
while b <= math.pi/2+2*math.pi:
	end_x = r*math.cos(b) + center
	end_y = r*math.sin(b) + center
	canvas.create_line(center, center, end_x, end_y, fill="#476042", tag='divider')
	b += twentyfifths
# Mask
#canvas.create_oval(15,15,canvas_width-15,canvas_height-15, fill="black")
# Big divisions
fifths = 2*math.pi/5
b = math.pi/2
while b <= math.pi/2+2*math.pi:
	end_x = r*math.cos(b) + center
	end_y = r*math.sin(b) + center
	canvas.create_line(center, center, end_x, end_y, fill="#476042", tag='divider')
	b += fifths
# Pie slices
for n in range(5):
	canvas.create_arc(15,15,canvas_width-15,canvas_height-15, start=-90-72*n, extent=72,fill=pie_fills[n])
	
which = canvas.create_line(center, center, end_x, end_y, fill="#476042", tag='clock_hand')

#img = "hourglass"
#w.create_bitmap(center, center, bitmap=img)

deltax = 2
deltay=3
delta_angle = 2*math.pi/25
angle = math.pi/2

def draw_clock_hands(pahrtahvo=0, tahvo=0, gorahn=0, prorahn=0): 
	''' Set the clockface to a certain time. Defaut position is straight down.'''
	# Draw the pahrtahvo hand
	r = center/2
	angle = pahrtahvo*2*math.pi/5 + math.pi/2
	end_x = r*math.cos(angle) + center
	end_y = r*math.sin(angle) + center
	canvas.create_line(center, center, end_x, end_y, fill="#476042", tag='clock_hand', width=10)
	# Draw the tahvo hand
	r = center/1.5
	angle = tahvo*2*math.pi/25 + math.pi/2
	end_x = r*math.cos(angle) + center
	end_y = r*math.sin(angle) + center
	canvas.create_line(center, center, end_x, end_y, fill="#476042", tag='clock_hand', width=6)
	# Draw the gorahn hand
	r = center*0.97
	angle = gorahn*2*math.pi/25 + math.pi/2
	end_x = r*math.cos(angle) + center
	end_y = r*math.sin(angle) + center
	canvas.create_line(center, center, end_x, end_y, fill="#476042", tag='clock_hand', width=3)
	# Draw the prorahn hand
	r = center*0.97
	angle = prorahn*2*math.pi/25 + math.pi/2
	end_x = r*math.cos(angle) + center
	end_y = r*math.sin(angle) + center
	canvas.create_line(center, center, end_x, end_y, fill="#FF0042", tag='clock_hand', width=1, smooth=1)

smooth_movement=False
#smooth_movement=True

while True:
	end_x = r*math.cos(angle) + center
	end_y = r*math.sin(angle) + center
	canvas.delete('clock_hand')
	t = dni_clock.dni_time(give_float=True)

	#draw_clock_hands(1.25, 7, 15, 22)
	pahrtahvo = 5*t[3]
	if smooth_movement:
		draw_clock_hands(pahrtahvo, t[5], t[6], (t[7]))
		canvas.after(26)
	else:
		draw_clock_hands(pahrtahvo, t[5], t[6], math.trunc(t[7]))
		canvas.after(1393)

	canvas.update()
	angle += delta_angle
window.mainloop()

