from tkinter import *
from math import ceil
import os
from pathlib import Path
#Note: Python3x required

############function code#####################################

def get_side(i):
    try:
        return list_button[i].image['file'][-8]
    
    except:
        return True
    

    
def on_click(i):
    
    global is_raised, current_turn, side_raised, prev_i, prev_moves

    #problem is_valid_move(): is_raised is still True after an erroneous move is made
    
    
        
    if is_raised:
        if is_valid_move(prev_i, i):
            if side_raised == 'b':
                current_turn = 'r'
            else:
                current_turn = 'b'

            
            img_prev_button = list_button[prev_i].image
            list_button[prev_i].configure(image = '')
            list_button[prev_i].image = ''

            try_save_img(i)
            list_button[i].configure(image = img_prev_button)
            list_button[i].image = img_prev_button

            
            prev_moves.append(prev_i)
            prev_moves.append(i)

            blink(prev_moves[-1], True)
            
            if len(prev_moves) >= 2:
                button_undo['state'] = NORMAL
                
            is_raised = False
            return
        
        else:
            print('invalid move')
            #print('move-from is:{}'.format(list_button[prev_i].image['file'][-8:-4]))
           
            is_raised = False
            return
    
    
    #by selecting the wrong side, is_raised can still be False while
    #mistakenly 'raising' the empty spot
    if is_raised == False and list_button[i]['image'] != '':
        side_raised = get_side(i)
        
        if current_turn == side_raised:
            print('raised {}'.format(side_raised))
            is_raised = True
            try:   
                blink(prev_moves[-1], False)
            except IndexError:
                pass  
                    
            store_button_info(i) #i is raised button

def blink(x, state):
    global colour_default

    if state == True:
        list_button[x].config(bg = 'red')
    else:
        list_button[x].config(bg = colour_default)
      
        
    
def store_button_info(i):
    global prev_i
    prev_i = i
    
def is_valid_move(prev_i, i):
    if prev_i != i and get_side(prev_i) != get_side(i):
        
        piece_name =list_button[prev_i].image['file'][-8:-4]
        
        row_i = ceil((i + 1)/9)  #1, 2, 3 ...
        col_i = i % 9 + 1
        row_prev_i = ceil((prev_i + 1)/9)  #1, 2, 3 ...
        col_prev_i = (prev_i) % 9 + 1

        row_vec = row_i - row_prev_i
        col_vec = col_i - col_prev_i
        
        mov_vector = i - prev_i
        
        if piece_name == 'bhor' or piece_name == 'rhor':
            print(piece_name)
            if row_vec == -2 and (col_vec == 1 or col_vec == -1): #top
                if list_button[prev_i - 9]['image'] != '':
                    return False
            elif row_vec == 2 and (col_vec == 1 or col_vec == -1):#bottom
                if list_button[prev_i + 9]['image'] != '':
                    return False
                
            #elif mov_vector == -11 or mov_vector == 7: #hori bot left
            elif (row_vec == -1 or row_vec == 1) and col_vec == -2 :
                print('bot left')
                if list_button[prev_i - 1]['image'] != '':
                    return False
            elif (row_vec == -1 or row_vec == 1) and col_vec == 2 : #horizontal bottom right
                #bottom left
                if list_button[prev_i + 1]['image'] != '':
                    return False
            else:
                print(row_vec, col_vec)
                return False
                
        elif piece_name == 'bcha' or piece_name == 'rcha':
            print(piece_name)
            if mov_vector / -9 == abs(ceil(mov_vector / 9)): #up vector -ve
                print(1)
                start = i + 9
                step = 9
            elif mov_vector / 9 == abs(ceil(mov_vector / 9)): #down
                print(2)
                start = i - 9
                step = -9
            elif row_i == row_prev_i and col_vec <= 8 and \
                 col_vec >= 1:
                print(row_i, row_prev_i) 
                print(3)   #right
                start = i - 1
                step = -1
            elif row_i == row_prev_i and col_vec >= -8 and \
                 col_vec <= -1: #left
                print(4)
                start = i + 1
                step = 1
            else:
                return False

            for x in range(start, prev_i, step):
                if list_button[x]['image'] != '':
                    return False
            
            
        elif piece_name == 'bele' or piece_name == 'rele':
            print(piece_name)
            cond = 0
            
            if piece_name[0] == 'b':
                cond = i < 45 -1
            else:
                cond = i > 45 -1
            
            if cond:
                if mov_vector == -16:
                    print(1)
                    if list_button[prev_i - 8]['image'] != '':
                        return False
                elif mov_vector == -20:
                    print(2)
                    if list_button[prev_i - 10]['image'] != '':
                        return False
                elif mov_vector == 16:
                    print(3)
                    if list_button[prev_i + 8]['image'] != '':
                        return False
                elif mov_vector == 20:
                    print(4)
                    if list_button[prev_i + 10]['image'] != '':
                        return False
                else:
                    return False
            else:
                return False
        #advisor
        elif piece_name == 'badv' or piece_name == 'radv':
            print(piece_name)
            centre = 0
            if piece_name[0] == 'b':
                centre = 14 -1
            else:
                centre = 77 -1

            dist_from_centre = abs(i - centre)
            print(mov_vector)
            if not ((dist_from_centre == 10 or dist_from_centre == 8 or\
                    dist_from_centre == 0) and (abs(mov_vector) == 10 or \
                    abs(mov_vector) == 8)):
                return False
            
        elif piece_name == 'rcan' or piece_name == 'bcan':
            print(piece_name)
            if mov_vector / -9 == abs(ceil(mov_vector / 9)): #up
                step = 9
                
            elif mov_vector / 9 == abs(ceil(mov_vector / 9)):
                step = -9
            
           
            elif row_i == row_prev_i and col_vec <= 8 and \
                 col_vec >= 1:
                step = -1
                print('can right')
            elif row_i == row_prev_i and col_vec >= -8 and \
                 col_vec <= -1: #left
                print('can left')
                step = 1 

            else:
                
                return False
            
            ct_in_between = 0
                
            for x in range(i, prev_i, step):
                if list_button[x]['image'] != '':
                    ct_in_between += 1
                    
            if ct_in_between != 2 and ct_in_between != 0:
                return False
                
                
        elif piece_name == 'rsol' or piece_name == 'bsol':
            print(piece_name)
            if piece_name[0] == 'b':
                cond = i <= 45 - 1
                forward = 9
            else:
                cond = i >= 46 - 1
                forward = -9
            if cond:
                if mov_vector != forward:
                    return False
            else:
                if abs(mov_vector) != 1 and mov_vector != forward:
                    return False
                
        elif piece_name == 'bgen' or piece_name == 'rgen':
            print(piece_name)
            centre = 0
            if piece_name[0] == 'b':
                centre = 14 - 1
            else:
                centre = 77 - 1
                
            dist_from_centre = abs(i - centre)
            if not((abs(mov_vector) == 9 or abs(mov_vector) == 1) and\
                   (dist_from_centre == 0 or dist_from_centre == 9 or \
                   dist_from_centre == 1 or dist_from_centre == 10 or\
                   dist_from_centre == 8)):
        
                return False
            
            
        
    else:
        return False
        
    return True

def create_piece():
    global list_button
    
    for i in range(1, 91):
        
        row = ceil(i/9)  #1, 2, 3 ...
        col = (i - 1) % 9 + 1
        

        piece_here = False
        path = ''
        
        if row == 1 or row == 10 or ((row == 3 or row == 8) and (col == 2 or col == 8))\
          or ((row == 4 or row == 7) and (col % 2 != 0)):

            piece_here = True
            if row == 1:       
                #check chariot
                if col == 1 or col == 9:
                    path = path_bchar
                   
                #check horse    
                elif col == 2 or col == 8:
                    path = path_bhor
                    
                #check elephant   
                elif col == 3 or col == 7:
                    path = path_bele
                    

                #check advisor   
                elif col == 4 or col == 6:
                    path = path_badv

                #check general
                elif col == 5:
                    path = path_bgen
            
            elif row == 10:
                #check chariot
                if col == 1 or col == 9:
                    path = path_rchar
                    
                #check horse    
                elif col == 2 or col == 8:
                    path = path_rhor
                    
                #check elephant   
                elif col == 3 or col == 7:
                    path = path_rele

                #check advisor   
                elif col == 4 or col == 6:
                    path = path_radv

                #check general
                elif col == 5:
                    path = path_rgen
                    
            elif row == 3 and (col == 2 or col == 8):
                path = path_bcan

            elif row == 8 and (col == 2 or col == 8):
                path = path_rcan

            elif row == 4 and (col % 2 != 0):
                path = path_bsol
                
            elif row == 7 and (col % 2 != 0):
                path = path_rsol
                
        if piece_here:
            
            img_piece = PhotoImage(file = path)
            button = Button(root, image = img_piece, command = lambda i = i:on_click(i - 1))
            button.image = img_piece

        
        else: #not in specified coords
            button = Button(root, image='', command = lambda i = i:on_click(i - 1))
            
        window_coord = canvas_board.create_window( offset_border_x + \
                       (col - 1) * distance_between_coords, \
                       offset_border_y + (row - 1) * distance_between_coords,\
                       window = button)
        
        
        list_button.append(button)

def try_save_img(i):
    try:
        images_saved.append(list_button[i].image)
    except:
        images_saved.append('')
        
def undo():
    global current_turn
    if len(prev_moves) == 2:
        button_undo.config(state = DISABLED)

    if current_turn == 'b':
        current_turn = 'r'
    else:
        current_turn = 'b'
        
    after = list_button[prev_moves[-1]]
    before = list_button[prev_moves[-2]]
    
    blink(prev_moves[-1], False)
    try: 
        blink(prev_moves[-3], True)
    except IndexError:
        pass
    
    before.configure(image = after.image)
    before.image = after.image
    
    
    after.image = images_saved[-1]
    after.configure(image = images_saved[-1])
    
    images_saved.pop()
    prev_moves.pop()
    prev_moves.pop()
      
############GUI code##########################################


folder = Path(os.getcwd())

path_board = folder / 'assets'/'chess_board.png'

path_bchar = folder / 'assets'/ 'bcha.png'
path_bhor = folder / 'assets'/'bhor.png'
path_bele = folder / 'assets'/ 'bele.png'
path_bgen = folder / 'assets'/'bgen.png'
path_badv = folder / 'assets'/'badv.png'
path_bsol = folder / 'assets'/'bsol.png'
path_bcan = folder / 'assets'/'bcan.png'

path_rchar = folder / 'assets'/'rcha.png'
path_rhor = folder / 'assets'/'rhor.png'
path_rele = folder / 'assets'/'rele.png'
path_rgen = folder / 'assets'/'rgen.png'
path_radv = folder / 'assets'/'radv.png'
path_rsol = folder / 'assets'/'rsol.png'
path_rcan = folder / 'assets'/'rcan.png'
bchar = 2
width_board = 571
height_board = 640

offset_border_x = 30
offset_border_y = 25

distance_between_coords = 64

x_coord_undo = offset_border_x + 8 * distance_between_coords + 20
y_coord_undo = offset_border_y + 4.5 * distance_between_coords

prev_button_raised = ''
prev_moves = []
images_saved = []

is_raised = False

current_turn = 'r'

list_button = []
root = Tk()


root.title('Chess')

img_board = PhotoImage(file = path_board)


canvas_board = Canvas(root, width = width_board, height = height_board)
canvas_board.pack()

canvas_board.create_image(width_board/2, height_board /2, image = img_board)

button_undo = Button(root, text = 'undo', command = undo)
button_undo.config(state = DISABLED)
colour_default = button_undo.cget('background')
canvas_board.create_window( x_coord_undo, y_coord_undo, window = button_undo)

create_piece()

root.mainloop()
