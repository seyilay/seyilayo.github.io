#I want to create a to-do app. What features would it need? 
# 1. Start with thinking about the output? - 
# a) A list of thing that need to be done 
# b) the status & Next steps - red (NOT STARTED)/amber (IN PROGRESS) /green (ALMOST DONE IN TIME)/ blue(COMPLETED)
# c) the description of the item
# d) it's importance
# e) urgency & delivery date
# where do we save the to-do list, apart from in the RAM.
# Other features that aren't priority - Overarching workstream for each item (like grouping items)/ recurring to-dos that could be set on a weekly basis/ dragging items to top 

user_prompt='Type to add, edit, show, complete or exit list'
to_do=[]

from functions import get_todos,write_todos
import FreeSimpleGUI as simp


label = simp.Text('Type in a to-do')
input_box = simp.InputText(tooltip='Enter to-do')
add_button = simp.Button('Add')
window = simp.Window('Seyilayo To-do App', layout= [[label], [input_box, add_button]])
window.read()
window.close()    

while True: 
    user_inp=(input(user_prompt))
    user_inp = user_inp.strip()
    user_inp= user_inp.lower()
        #adds a new action to the to-do list
    if user_inp.startswith('add'):
        new_inp = user_inp[4:]
        #new_inp = input('Enter a todo: ')+'\n'
        add_to_dos = get_todos('to_dos.txt')
        add_to_dos.append(new_inp)
        with open ('to_dos.txt','a') as file:
            file.writelines(new_inp + '\n')
    #prints out the to-do list in a numbered format
    elif user_inp.startswith('show') :
        show_to_dos = get_todos('to_dos.txt')
        for index,i in enumerate(show_to_dos):
            i= i.strip("\n")
            index= index+1 #increasing the list number to initalise from 0 to 1
            user_list= f"{index}. {i}"
            print(user_list)
    #a feature to improve the mutability of the to-do do list. It has error handling
    elif user_inp.startswith('edit'):
        try:
            editted_item = int(user_inp[5:])
            #edit_list = int(input('What list item do you want to edit'))
            editted_item -=1
            new_list = input('Type new list item:') #getting the user input on what they want to replace with
            edit_to_dos = get_todos('to_dos.txt')
            edit_to_dos[editted_item] = new_list+'\n'
            #new_data = data.replace (edit_data,new_list) // not sure why this line doesn't work
            w_edit_to_dos = write_todos('to_dos.txt',edit_to_dos)
            
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            break
        #print(to_do)
    #a feauture intended to remove complete items from the to-do list
    elif user_inp.startswith('complete'):
        try:
            complete_list = int(input('What list item have you finished?'))
            complete_list = complete_list - 1
            with open('to_dos.txt','r') as file:
                data = file.readlines()
            
            data.pop(complete_list)    
            with open('to_dos.txt', 'w') as file:
                file.writelines(data)
        except IndexError:
            print('Oops!...This number is not in the list.')
        #print(to_do)
        #print(user_list)
    elif user_inp.startswith('exit'):
        break
    else:
        print('Unknown command')


        
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