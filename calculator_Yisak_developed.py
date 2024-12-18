# import necessary packages
import FreeSimpleGUI as Sg
import MathFunction as Mf

answer = "result"

# initialize some widgets
label = Sg.Text("Solve your math problems right here.")
input_label1 = Sg.Text("Enter Two numbers separated by space", text_color="Black", size=30)
input_box = Sg.Input(tooltip="Type...", size=20)
answer_box = Sg.Input(answer, tooltip="result", size=20, enable_events=True, key='show')

# initialize some operational buttons
add_button = Sg.Button(" Add (X+Y) ", tooltip="Addition", key="add")
sub_button = Sg.Button(" Subtract (X-Y) ", tooltip="Subtraction", key="minus")
times_button = Sg.Button(" Multiply(X*Y) ", tooltip="Multiplication", key='times')
divide_button = Sg.Button(" Divide(X/Y) ", tooltip="Division", key='divide')
modulo_button = Sg.Button(" Find modulus(X % Y) ", tooltip="Modulus", key='modulo')
power_button = Sg.Button(" Power (X^Y) ", tooltip="Power", key='power')

# group buttons together
operation_list1 = [add_button, sub_button, times_button]
operation_list2 = [divide_button, modulo_button, power_button]

window = Sg.Window("Calculator", layout=[[label],
                                         [input_label1], [input_box, answer_box],
                                         [operation_list1, operation_list2]])


while True:
    x = 0
    y = 0
    operation, value = window.read()
    if value is not None:
        values = value[0]

        try:
            if values is not None:
                if values.index(" ") + 1 < len(values):
                    x = float(values.split(" ")[0])
                    y = float(values.split(" ")[1])
        except AttributeError:
            Sg.popup("Error occurred")
        except TypeError:
            Sg.popup("TypeError occurred")
        except ValueError:
            Sg.popup("ValueError occurred")

    match operation:
        case 'add':
            answer = Mf.addition(x, y)
            window['show'].update(str(answer))
            Sg.popup("Result = "+str(answer))
        case 'minus':
            answer = Mf.subtract(x, y)
            window['show'].update(str(answer))
            Sg.popup("Result = "+str(answer))
        case 'times':
            answer = Mf.multiply(x, y)
            window['show'].update(str(answer))
            Sg.popup("Result = "+str(answer))
        case 'divide':
            answer = Mf.divide(x, y)
            window['show'].update(str(answer))
            Sg.popup("Result = "+str(answer))
        case 'modulo':
            answer = Mf.modulo(x, y)
            window['show'].update(str(answer))
            Sg.popup("Result = "+str(answer))
        case 'power':
            answer = Mf.power(x, y)
            window['show'].update(str(answer))
            Sg.popup("Result = "+str(answer))
        case None:
            break

window.close()
