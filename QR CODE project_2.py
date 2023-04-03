import PySimpleGUI as sg
import qrcode as qrc

layout = [
[sg.Text('Input Text', background_color='#24003e'), sg.Input(key = 'IN_TEXT')],
[sg.Text('Note: !!You may need to press the button twice for the program to run!!', background_color='#24003e', text_color='orange')],
[sg.Text('Note: !!The QR Code will generate after you close the app!!', background_color='#24003e', text_color='orange')],
[sg.Button('Create QR Code', key='-Q'), sg.Button('Close')],
]

window = sg.Window('QR Code Generator App', layout, background_color='#24003e', button_color='#6501ba', font = 'Georgia')

window.read()

while True:
    event, values = window.read()

    if event == 'CQ':
        qrtext = values['IN_TEXT']

    if event in (sg.WINDOW_CLOSED, 'Close'):
        break
    
    
qrtext = values['IN_TEXT']
qr = qrc.QRCode(version=2, box_size=20, border=3)
qr.add_data(qrtext)
qr.make(fit=True)
img = qr.make_image(fill_color='#a366d6', back_color='#010001')
img.show()
img.save('QRCode_project2.png')


try:
    img.show()
except:
    sg.popup_error("Error: Unable to generate QR code.")
finally:
    print('QR code generated successfully')



window.close()