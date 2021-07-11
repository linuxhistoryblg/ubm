import sys
import random
import PySimpleGUI as sg
from psutil import sensors_battery

# Some Defaults for drawing
mysize = (12,1)
GRAPH_SIZE = (300,300)
DATA_SIZE = (500,500)
bcols = ['blue','red']
myfont = "Ariel 18"

# Get battery percent charge from psutil.sensors_battery() 
def get_battery_percent():
  battery = sensors_battery() 
  return battery.percent

# Draw Graph 
graph = sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE)
# Set Layout 
layout = [[sg.Text('Ugly Battery Monitor',font=myfont)],
  [graph],
  [sg.Text('Battery Level',text_color=bcols[0],font=myfont,size=mysize)],
  [sg.Exit()]]
 
# Draw Window
window = sg.Window('UBM by DCD', layout)

# Event Loop
while True:
    event, values = window.read(timeout=2000)
    
    if event in (None, 'Exit'):
        break
 
    graph.erase()
    # Printing for now. Remove for prod.
    print(get_battery_percent())
    graph_value = get_battery_percent()
    if graph_value <= 10:
      graph.draw_rectangle(top_left=(100, graph_value*4), 
    bottom_right=(300, 10), fill_color=bcols[1])
    else:
      graph.draw_rectangle(top_left=(100, graph_value*4), 
    bottom_right=(270, 10), fill_color=bcols[0])
window.close()
