#I want to create a to-do app. What features would it need? 
# 1. Start with thinking about the output? - 
# a) A list of thing that need to be done 
# b) the status & Next steps - red (NOT STARTED)/amber (IN PROGRESS) /green (ALMOST DONE IN TIME)/ blue(COMPLETED)
# c) the description of the item
# d) it's importance
# e) urgency & delivery date
# where do we save the to-do list, apart from in the RAM.
# Other features that aren't priority - Overarching workstream for each item (like grouping items)/ recurring to-dos that could be set on a weekly basis/ dragging items to top 
from functions import get_todos,write_todos
import FreeSimpleGUI as simp


label = simp.Text('Type in a to-do')
input_box = simp.InputText(tooltip='Enter to-do', key='todo')
list_box = simp.Listbox(values = get_todos('to_dos.txt'), key='to-dolist', enable_events=True, size=[50,10])
add_button = simp.Button('Add')
edit_button = simp.Button('Edit')
complete_button = simp.Button('Complete')
exit_button = simp.Button('Exit')
window = simp.Window('Seyilayo To-do App', 
            layout= [[label], [input_box, add_button], [list_box,complete_button, edit_button],
                        [exit_button]],
                    font= ('Helvetica', 20))


while True: 
    event,values = window.read()
    print(event)
    print(values)
    match event:
    #user_inp=(input(user_prompt))
    #user_inp = user_inp.strip()
    #user_inp= user_inp.lower()
    #adds a new action to the to-do list
    
        case ('Add'):
            #new_inp = user_inp[4:]
            #new_inp = input('Enter a todo: ')+'\n'
            add_to_dos = get_todos('to_dos.txt')
            new_inp = values['todo']
            add_to_dos.append(new_inp)
            with open ('to_dos.txt','a') as file:
                file.writelines(new_inp + '\n')

            window['to-dolist'].update(values=add_to_dos)
        #prints out the to-do list in a numbered format
        #case('Show') :
        #    show_to_dos = get_todos('to_dos.txt')
        #        i= i.strip("\n")
        #    for index,i in enumerate(show_to_dos):
        #        index= index+1 #increasing the list number to initalise from 0 to 1
        #        user_list= f"{index}. {i}"
        #        print(user_list)
        #a feature to improve the mutability of the to-do do list. It has error handling
        case('Edit'):
            
            try:
                #editted_item = int(new_inp[5:])
                #edit_list = int(input('What list item do you want to edit'))
                #editted_item -=1
                #new_list = input('Type new list item:') #getting the user input on what they want to replace with
                edit_to_dos = get_todos('to_dos.txt')
                #edit_popup = int(simp.popup_get_text('What list item do you want to edit'))
                old_inp = values['to-dolist'][0]
                new_inp= values['todo']
                index= edit_to_dos.index(old_inp)
                edit_to_dos[index] = new_inp+'\n'
                #new_data = data.replace (edit_data,new_list) // not sure why this line doesn't work
                w_edit_to_dos = write_todos('to_dos.txt',edit_to_dos)
                window['to-dolist'].update(values=edit_to_dos)
                
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
                break
            #print(to_do)
        #a feauture intended to remove complete items from the to-do list
        case ('to-dolist'):
            window['todo'].update(value= values['to-dolist'][0])
        case ('Complete'):
            try:
                complete_to_dos = get_todos('to_dos.txt')
                complete_inp = values['to-dolist'][0]
                index= complete_to_dos.index(complete_inp)
                complete_to_dos[index] = ''
                #new_data = data.replace (edit_data,new_list) // not sure why this line doesn't work
                w_edit_to_dos = write_todos('to_dos.txt',complete_to_dos)
                window['to-dolist'].update(values=complete_to_dos)
            except IndexError:
                print('Oops!...This number is not in the list.')
            #print(to_do)
            #print(user_list)
        case ('Exit'):
            break
        case simp.WIN_CLOSED:
            break
        case _:
            print('Unknown command')

window.close() 
        
    #user_inp.capitalize
    #to_do.append(to_do_inp)
    
    #Legacy code for initialising if statement
        #if 'add' in user_inp:
        #new_inp = user_inp[4:]
        #new_inp = input('Enter a todo: ')+'\n'
        #with open ('to_dos.txt', 'r') as file:
        #    to_dos = file.readlines()
        #to_dos.append(new_inp + '\n')
        #with open ('to_dos.txt','a') as file:
        #    file.writelines(new_inp)
        
    #Legacy code when editting the todo list (this didn't work)
            #with open('to_dos.txt','r') as file:
            #data = file.readlines() #reading the lines of the file into a variable - with a list type
            #try: 
            #    for i in data:
            #        if i == editted_item:
            #            print(True)
            #            new_1 = input('What do you want the item to be editted to`')
            #except ValueError:
            #    print('This keyword is not in list, use list number')
            #    pass