import PySimpleGUI as sg
import threading
import time

# Function to check for tasks and trigger alarms
def check_tasks():
    while True:
        current_time = time.strftime("%H:%M:%S")
        for task, trigger_time in tasks:
            if current_time == trigger_time:
                sg.popup(f"Task '{task}' is due now!")
                tasks.remove((task, trigger_time))
        time.sleep(1)

# Task list (defined programmatically)
tasks = [
    ('Task 1', '12:00:00'),
    ('Task 2', '14:30:00'),
    ('Task 3', '15:45:00'),
]

# Start the task checking thread
task_thread = threading.Thread(target=check_tasks)
task_thread.daemon = True
task_thread.start()

# Event loop (GUI)
sg.theme('LightGreen')
layout = [
    [sg.Text('Task Scheduler', font=('Helvetica', 20))],
    [sg.Text('Current Tasks:')],
    [sg.Listbox(values=[f'{task[0]} - {task[1]}' for task in tasks], size=(40, 6), key='-TASKS-')],
    [sg.Button('Exit')],
]

window = sg.Window('Task Scheduler', layout, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

window.close()
