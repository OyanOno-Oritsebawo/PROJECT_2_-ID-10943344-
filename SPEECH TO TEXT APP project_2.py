import pyttsx3 as pt
import PySimpleGUI as sg

 
layout = [
[sg.Text('Input Text', background_color='#24003e'), sg.Input(key = 'IN_TEXT')],
[sg.Text('Select voice type', background_color='#24003e'), sg.Radio('Male', 'gender', key='MALE', background_color='#24003e', default=False), 
 sg.Radio('Female', 'gender', key='FEMALE', background_color='#24003e', default=False)],
[sg.Text('Voice Speed', background_color='#24003e'), sg.Slider(range=(100, 500), resolution=1, default_value=150, key='VS', orientation="h", background_color='#6501ba')],
[sg.Text('Volume', background_color='#24003e'), sg.Slider(range=(0.0,1.0), resolution=0.01, default_value=1, key='VO', orientation="h", background_color='#6501ba')],
[sg.Text('Note: !!You may need to press the button twice for the program to run!!', background_color='#24003e', text_color='orange')],
[sg.Button('Convert to Speech', key='CTS'), sg.Button('Close')],
]

window = sg.Window('Speech-to-Text App', layout, background_color='#24003e', button_color='#6501ba', font = 'Georgia')

window.read()

while True:
    event, values = window.read()

    in_text = values['IN_TEXT']

    if event in (sg.WINDOW_CLOSED, 'Close'):
        break
             
    if len(in_text)<1:
        sg.popup_error('Please input text to be converted')

    if event == 'CTS':
        speak = pt.init()

        in_text = values['IN_TEXT']
        voices = speak.getProperty('voices')
        vs = values['VS']
        vol = values['VO']

        if values['MALE']==True:
             speak.setProperty('voice', voices[1].id)
        elif values['FEMALE']==True:
            speak.setProperty('voice', voices[0].id)

        speak.getProperty('rate')
        speak.setProperty('rate', vs)

        speak.getProperty('volume')
        speak.setProperty('volume', vol)

        speak.say(in_text)
        speak.runAndWait()
    
 
window.close()