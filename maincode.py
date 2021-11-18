import sys
import PySimpleGUI as sg

# defines main welcome screen
def welcome():
    layout = [
        [sg.Text("Welcome to Let's Go Out!", font=("Arial", 25))],
        [sg.Text('The best way to find a date night idea!', font=("Arial", 15))],
        [sg.Button('Click me to begin!', size=(25))]
    ]

    # create the window
    window = sg.Window("Let's Go Out!", layout, size=(500,250), element_justification='c')

    #create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # move to main to begin 
        if event ==sg.WIN_CLOSED:
            break
        elif event == 'Click me to begin!':
            window.close()
            main()
    window.close()

# defines main code
def main():
    layout = [
        [sg.Text("Hello! What are you looking to do this evening?", font=("Arial", 15))],
        [sg.Button("Get Food"), sg.Button("See a Movie")],
        [sg.Button("Go On An Adventure"), sg.Button("Surprise Me!")]
    ]

    # create the window
    window = sg.Window("Let's Go Out", layout, size=(500,250), auto_size_buttons=True, element_justification='c')

    while True:
        event, values = window.read()
        # End program if user closes window or
        # move different response function 
        if event == sg.WIN_CLOSED:
             break
        elif event == "Get Food":
            window.close()
            dinner()
        elif event == "See a Movie":
            window.close()
            movie()
        elif event == "Go On An Adventure":
            window.close()
            adventure()
        elif event == "Surprise Me!":
            window.close()
            surprise()
            
    window.close()

# defines response dinner
def dinner():
    layout = [
        [sg.Text("Dinner!")],
        [sg.Button("OK")]
    ]

    # create the window
    window = sg.Window("Let's Go Out", layout, size=(500,250), element_justification='c')

    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses OK
        if event == "OK" or sg.WIN_CLOSED:
            break
    window.close()

# defines response movie
def movie():
    layout = [
        [sg.Text("Movie!")],
        [sg.Button("OK")]
    ]

    # create the window
    window = sg.Window("Let's Go Out", layout, size=(500,250), element_justification='c')

    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses OK
        if event == "OK" or sg.WIN_CLOSED:
            break
    window.close()

# defines response adventure
def adventure():
    layout = [
        [sg.Text("Adventure!")],
        [sg.Button("OK")]
    ]

    # create the window
    window = sg.Window("Let's Go Out", layout, size=(500,250), element_justification='c')

    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses OK
        if event == "OK" or sg.WIN_CLOSED:
            break
    window.close()


# defines response surprise me
def surprise():
    layout = [
        [sg.Text("Surprise!")],
        [sg.Button("OK")]
    ]

    # create the window
    window = sg.Window("Let's Go Out", layout, size=(500,250), element_justification='c')

    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses OK
        if event == "OK" or sg.WIN_CLOSED:
            break
    window.close()


if __name__ == '__main__':
    welcome()