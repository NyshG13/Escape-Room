import pygame

pygame.init()
pygame.mixer.init()

from spot_new import spot_the_difference

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Mystery Rooms")

bg_beginning = pygame.image.load("assets/MYSTERY ROOMS.png")
bg_beginning = pygame.transform.scale(bg_beginning,(800,600))

introduction1 = pygame.image.load("assets/intro1.png")
introduction1 = pygame.transform.scale(introduction1,(800,600))

introduction2 = pygame.image.load("assets/intro2.png")
introduction2 = pygame.transform.scale(introduction2,(800,600))

introduction3 = pygame.image.load("assets/intro3.png")
introduction3 = pygame.transform.scale(introduction3,(800,600))

room1 = pygame.image.load("assets/room1.png")
room1 = pygame.transform.scale(room1,(800,600))

mirror_text = pygame.image.load("assets/painting hidden.png")
mirror_text = pygame.transform.scale(mirror_text,(800,600))

door_message = pygame.image.load("assets/door 1-1.png")
door_message = pygame.transform.scale(door_message,(800,600))

key = pygame.image.load("assets/key 1-1.png")
key = pygame.transform.scale(key, (50,50))

table_objects = pygame.image.load("assets/hidden obj bg1.jpg")
table_objects = pygame.transform.scale(table_objects,(800,600))

key_table = pygame.image.load("assets/key 1-1.png")
key_table = pygame.transform.scale(key_table, (40,40))

cupboard_objects = pygame.image.load("assets/cupboard 1-2.jpg")
cupboard_objects = pygame.transform.scale(cupboard_objects,(800,600))

key_cupboard = pygame.image.load("assets/key 1-1.png")
key_cupboard = pygame.transform.scale(key_cupboard, (40,40))

room2 = pygame.image.load("assets/room2.jpg")
room2 = pygame.transform.scale(room2, (800,600))

piano = pygame.image.load("assets/piano better text.png")
piano = pygame.transform.scale(piano, (800,600))

book = pygame.image.load("assets/book text.png")
book = pygame.transform.scale(book, (800,600))  

door2 = pygame.image.load("assets/door 2.png")
door2 = pygame.transform.scale(door2, (800,600))

room3 = pygame.image.load("assets/room3.jpg")
room3 = pygame.transform.scale(room3, (800,600))

door3 = pygame.image.load("assets/door 1-1.png")
door3 = pygame.transform.scale(door3, (800, 600))

mirror_rect = pygame.Rect(650, 150, 60, 65)
table_rect = pygame.Rect(300, 340, 100,100)
cupboard_rect = pygame.Rect(0,150,90,150)
door_rect = pygame.Rect(450,200,65,180)
key_mirror_rect = pygame.Rect(50, 400, 50, 50)
key_table_rect = pygame.Rect(225, 350, 40, 40)
key_cupboard_rect = pygame.Rect(600, 450, 40, 40)
piano_rect = pygame.Rect(370, 320, 50, 60)
book_rect = pygame.Rect(30, 540, 75, 30)
door2_rect = pygame.Rect(350, 80, 85, 220)
user_text = ""
candle_rect = pygame.Rect(90,220, 70, 90)
boat_rect = pygame.Rect(625, 375, 70, 100)
door3_rect = pygame.Rect(475, 210, 90, 200)
rubble_rect = pygame.Rect(300,400, 90,70)
game_over_rect = pygame.Rect(120, 150, 120, 300)

dialogue_box_width = 800-20
dialogue_box_height = 90
dialogue_box_x = 10
dialogue_box_y = 600-100

current_message_index = 0
dialogue_active = False 
dialogue_timer = 0  
dialogue_duration = 3000

mirror_message_index = 0
mirror_dialogue_active = False  
mirror_dialogue_timer = 0
mirror_dialogue_duration = 3000

table_message_index = 0
table_dialogue_active = False  
table_dialogue_timer = 0
table_dialogue_duration = 3000

cupboard_message_index = 0
cupboard_dialogue_active = False
cupboard_dialogue_timer = 0
cupboard_dialogue_duration = 3000

door_message_index = 0
door_dialogue_active = False
door_dialogue_timer = 0
door_dialogue_duration = 3000

room2_message_index = 0
room2_dialogue_active = False
room2_dialogue_timer = 0
room2_dialogue_duration = 3000

door3_message_index = 0
door3_dialogue_active = False
door3_dialogue_timer = 0
door3_dialogue_duration = 3000

dialogue_messages = [
    "             You are trapped in a haunted mansion...",
    "       To get out of this room, you need to find 3 keys..",
    "   Feel free to explore, but remember that your time is ticking"
]

mirror_dialogue_messages = [
    "               This painting is so scary...",
    "    Maybe the key is hidden somewhere inside this painting..?",
    "             Can you search for it before its too late..?"
]

table_dialogue_messages = [
    "             What a mess this table is in...",
    "             Maybe the key is hidden here..?",
    "     But will you be able to find it before the ghosts find you?"
]

cupboard_dialogue_messages = [
    "           Everything here is a mess ... even this cupboard",
    "            Could a key be hidden somewhere in here..?",
    "       But how will you find it before the ghosts come for you?"
]

door_dialogue_messages = [
    "                 The door is locked..",
    "         It wont open unless you find those 3 keys..",
    "      But will you be able to find them? HA HA HA"
]

room2_dialogue_messages = [
    "          you might have crossed the first room..",
    "        but you are still trapped in this mansion..",
    "and you wont get out of this room, especially since your time is limited"
]

door3_dialogue_messages = [
    "                    The door is locked...",
    "It wont open till you find and solve the 2 puzzles hidden in the room...",
    "        But will you be able to find them? HA HA HA"
]

inventory =['']

def draw_dialogue_box():
    pygame.draw.rect(screen, (0, 0, 0), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))
    pygame.draw.rect(screen, (128,128,128), (dialogue_box_x + 5, dialogue_box_y + 5, dialogue_box_width - 10, dialogue_box_height - 10))
    
    message_text = font.render(dialogue_messages[current_message_index], True, (0, 0, 0))
    screen.blit(message_text, (dialogue_box_x + 10, dialogue_box_y + 30))

def draw_dialogue_box_2():
    pygame.draw.rect(screen, (0, 0, 0), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))
    pygame.draw.rect(screen, (128,128,128), (dialogue_box_x + 5, dialogue_box_y + 5, dialogue_box_width - 10, dialogue_box_height - 10))
    
    message_text = font.render(room2_dialogue_messages[current_message_index], True, (0, 0, 0))
    screen.blit(message_text, (dialogue_box_x + 10, dialogue_box_y + 30))

font = pygame.font.Font("assets/Zombified.ttf", 48)

def draw_text_button():
    button_text = font.render("ENTER", True, (255,255,255))  
    button_width = button_text.get_width()
    button_height = button_text.get_height()
    
    button_x = 360
    button_y = 440
    
    screen.blit(button_text, (button_x, button_y))
    return button_x, button_y, button_width, button_height

def draw_inventory():
    pygame.draw.rect(screen, (0, 0, 0), (10, 10, 150, 50))  
    font = pygame.font.Font(None, 24)
    text = font.render(f"Inventory: {', '.join(inventory)}", True, (255, 255, 255))
    screen.blit(text, (15, 15))


def start_game():
    return "introduction1"

def move_to_intro2():
    return "introduction2"

def move_to_intro3():
    return "introduction3"

def move_to_room1():
    return "room1"

def move_to_mirror():
    return "mirror text"

def move_to_table():
    return "table objects"

def move_to_cupboard():
    return "cupboard objects"

def move_to_door():
    return "door key put"

def move_to_room2():
    return "room2"

def move_to_piano():
    return "piano text"

def move_to_book():
    return "book text"

def move_to_door2():
    return "door2"

def move_to_room3():
    return "room3"

def move_to_candle():
    return "candle"

def move_to_boat():
    return "boat"

def move_to_room4():
    return "room4"

def move_to_rubble():
    return "rubble"

def move_to_game_over():
    return "game_over"

def move_to_door3():
    return "door3"

current_state = "room3"
current_music = None
Game_state_2 = 0

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  
                if user_text.upper() == "JIGSAW" and current_state == "door2":
                    current_state = move_to_room3()
                if user_text.upper() != "JIGSAW" and current_state == "door2":
                    if current_music != 'incorrect password.mp3':
                       pygame.mixer.music.load('music/incorrect password.mp3')
                       current_music = 'incorrect password.mp3'
                    pygame.mixer.music.stop()  
                    pygame.mixer.music.play()              
            elif event.key == pygame.K_BACKSPACE: 
                user_text = user_text[:-1]
            else:
                if event.unicode.isprintable():
                    user_text += event.unicode  

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if current_state == "start":
                button_x, button_y, button_width, button_height = draw_text_button()
            
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    current_state = start_game()  

            elif current_state == "room1":
                if mirror_rect.collidepoint(mouse_x, mouse_y):
                    current_state = move_to_mirror()
                    mirror_dialogue_active = True 
                    mirror_message_index = 0  
                    mirror_dialogue_timer = pygame.time.get_ticks()

                if table_rect.collidepoint(mouse_x, mouse_y):
                    current_state = move_to_table()
                    table_dialogue_active = True  
                    table_message_index = 0 
                    table_dialogue_timer = pygame.time.get_ticks()

                if cupboard_rect.collidepoint(mouse_x, mouse_y):
                    current_state = move_to_cupboard()
                    cupboard_dialogue_active = True  
                    cupboard_message_index = 0  
                    cupboard_dialogue_timer = pygame.time.get_ticks()

                if door_rect.collidepoint(mouse_x, mouse_y):
                    if inventory[0] == "3 keys":
                        current_state = move_to_room2()
                    else:
                        current_state = move_to_door()
                        door_dialogue_active = True  
                        door_message_index = 0  
                        door_dialogue_timer = pygame.time.get_ticks()

            elif current_state == "mirror text":
                if key_mirror_rect.collidepoint(mouse_x, mouse_y):
                    if "key" not in inventory:
                        inventory[0] = "1 key"
                        current_state = move_to_room1()

            elif current_state == "table objects":
                if key_table_rect.collidepoint(mouse_x, mouse_y):
                    if "key" not in inventory:
                        inventory[0] ="2 keys"
                        current_state = move_to_room1()
                        

            elif current_state == "cupboard objects":
                if key_cupboard_rect.collidepoint(mouse_x, mouse_y):
                    if "key" not in inventory:
                        inventory[0] ="3 keys"
                        current_state = move_to_room1() 

            elif current_state == "room3":
                if candle_rect.collidepoint(mouse_x, mouse_y):
                    current_state = move_to_candle()

                if door3_rect.collidepoint(mouse_x, mouse_y):
                    if Game_state_2 == 3:
                       current_state = move_to_game_over()
                    
                    else:
                        current_state = move_to_door3()

                if rubble_rect.collidepoint(mouse_x, mouse_y):
                    current_state = move_to_rubble()

                if boat_rect.collidepoint(mouse_x, mouse_y):
                    current_state = move_to_boat()

            elif current_state == "door3":
                door3_dialogue_active = True
                door3_message_index = 0
                door3_dialogue_timer = pygame.time.get_ticks()

            elif current_state == "room4":
                if game_over_rect.collidepoint(mouse_x, mouse_y):
                    current_state = move_to_game_over()

            elif current_state == "room2":
                if piano_rect.collidepoint(mouse_x, mouse_y):
                    current_state = move_to_piano()  

                if book_rect.collidepoint(mouse_x, mouse_y):
                    current_state = move_to_book()    

                if door2_rect.collidepoint(mouse_x, mouse_y):
                    current_state = move_to_door2()

            room2_dialogue_active = True  
            room2_message_index = 0 
            room2_dialogue_timer = pygame.time.get_ticks()

        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RETURN:  
                if current_state == "introduction1":
                    current_state = move_to_intro2()
                elif current_state == "introduction2":
                    current_state = move_to_intro3()
                elif current_state == "introduction3":
                    current_state = move_to_room1()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: 
                if current_message_index < len(dialogue_messages) - 1:
                    current_message_index += 1
                    dialogue_timer = pygame.time.get_ticks()

                if current_message_index >= len(dialogue_messages):
                    dialogue_active = False

    if current_state == "start":         
        screen.blit(bg_beginning, (0, 0))
        draw_text_button()

        if current_music != 'bg for entry.mp3':
            pygame.mixer.music.load('music/bg for entry.mp3')
            pygame.mixer.music.set_volume(1.0)  
            pygame.mixer.music.play(-1)  
            current_music = 'bg for entry.mp3'

        
    elif current_state == "introduction1":
        screen.blit(introduction1, (0,0))        
        
    elif current_state == "introduction2":
        screen.blit(introduction2, (0, 0))
        
    elif current_state == "introduction3":
        screen.blit(introduction3, (0, 0))
        
    elif current_state == "room1":
        screen.blit(room1, (0, 0))
        if current_music != 'room1 new.mp3':
            pygame.mixer.music.load('music/room1 new.mp3')
            pygame.mixer.music.set_volume(1.0)  
            pygame.mixer.music.play(-1)  
            current_music = 'room1 new.mp3'

        draw_inventory()

        if not dialogue_active and current_message_index == 0:
            dialogue_active = True
            dialogue_timer = pygame.time.get_ticks()

        if dialogue_active:
           draw_dialogue_box()

        if dialogue_active and pygame.time.get_ticks() - dialogue_timer > dialogue_duration:
            if current_message_index < len(dialogue_messages) - 1:
                current_message_index += 1
                dialogue_timer = pygame.time.get_ticks() 
            else:
                dialogue_active = False 

    elif current_state == "mirror text":
        screen.blit(mirror_text, (0, 0))
        if mirror_dialogue_active:
            pygame.draw.rect(screen, (0, 0, 0), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))
            pygame.draw.rect(screen, (128, 128, 128), (dialogue_box_x + 5, dialogue_box_y + 5, dialogue_box_width - 10, dialogue_box_height - 10))

            mirror_message_text = font.render(mirror_dialogue_messages[mirror_message_index], True, (0, 0, 0))
            screen.blit(mirror_message_text, (dialogue_box_x + 10, dialogue_box_y + 30))

        if mirror_dialogue_active and pygame.time.get_ticks() - mirror_dialogue_timer > mirror_dialogue_duration:
            if mirror_message_index < len(mirror_dialogue_messages) - 1:
                mirror_message_index += 1
                mirror_dialogue_timer = pygame.time.get_ticks()
            else:
                mirror_dialogue_active = False
        screen.blit(key, (50, 400))
        draw_inventory()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                  current_state = "room1"

    elif current_state == "table objects":
        screen.blit(table_objects, (0,0))

        if table_dialogue_active:
            pygame.draw.rect(screen, (0, 0, 0), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))
            pygame.draw.rect(screen, (128, 128, 128), (dialogue_box_x + 5, dialogue_box_y + 5, dialogue_box_width - 10, dialogue_box_height - 10))

            table_message_text = font.render(table_dialogue_messages[table_message_index], True, (0, 0, 0))
            screen.blit(table_message_text, (dialogue_box_x + 10, dialogue_box_y + 30))

        if table_dialogue_active and pygame.time.get_ticks() - table_dialogue_timer > table_dialogue_duration:
            if table_message_index < len(table_dialogue_messages) - 1:
                table_message_index += 1
                table_dialogue_timer = pygame.time.get_ticks()
            else:
                table_dialogue_active = False

        screen.blit(key_table, (225,350))
        draw_inventory()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  
                  current_state = "room1"

    elif current_state == "cupboard objects":
        screen.blit(cupboard_objects, (0,0))

        if cupboard_dialogue_active:
            pygame.draw.rect(screen, (0, 0, 0), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))
            pygame.draw.rect(screen, (128, 128, 128), (dialogue_box_x + 5, dialogue_box_y + 5, dialogue_box_width - 10, dialogue_box_height - 10))

            cupboard_message_text = font.render(cupboard_dialogue_messages[cupboard_message_index], True, (0, 0, 0))
            screen.blit(cupboard_message_text, (dialogue_box_x + 10, dialogue_box_y + 30))

       
        if cupboard_dialogue_active and pygame.time.get_ticks() - cupboard_dialogue_timer > cupboard_dialogue_duration:
            if cupboard_message_index < len(cupboard_dialogue_messages) - 1:
                cupboard_message_index += 1
                cupboard_dialogue_timer = pygame.time.get_ticks()
            else:
                cupboard_dialogue_active = False

        screen.blit(key_table, (600,450))
        draw_inventory()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  
                  current_state = "room1"

    elif current_state == "door key put":
        screen.blit(door_message, (0,0))

        if door_dialogue_active:
            pygame.draw.rect(screen, (0, 0, 0), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))
            pygame.draw.rect(screen, (128, 128, 128), (dialogue_box_x + 5, dialogue_box_y + 5, dialogue_box_width - 10, dialogue_box_height - 10))

            door_message_text = font.render(door_dialogue_messages[door_message_index], True, (0, 0, 0))
            screen.blit(door_message_text, (dialogue_box_x + 10, dialogue_box_y + 30))

        
        if door_dialogue_active and pygame.time.get_ticks() - door_dialogue_timer > door_dialogue_duration:
            if door_message_index < len(door_dialogue_messages) - 1:
                door_message_index += 1
                door_dialogue_timer = pygame.time.get_ticks()
            else:
                door_dialogue_active = False
        
        draw_inventory()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                  current_state = "room1"

    elif current_state == "room2":
        screen.blit(room2, (0,0))
        if current_music != 'room2 better.mp3':
            pygame.mixer.music.load('music/room2 better.mp3')
            pygame.mixer.music.set_volume(1.0)  
            pygame.mixer.music.play(-1)  
            current_music = 'room2 better.mp3'

        if room2_dialogue_active:
            pygame.draw.rect(screen, (0, 0, 0), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))
            pygame.draw.rect(screen, (128, 128, 128), (dialogue_box_x + 5, dialogue_box_y + 5, dialogue_box_width - 10, dialogue_box_height - 10))

            room2_message_text = font.render(room2_dialogue_messages[room2_message_index], True, (0, 0, 0))
            screen.blit(room2_message_text, (dialogue_box_x + 10, dialogue_box_y + 30))

        
        if room2_dialogue_active and pygame.time.get_ticks() - room2_dialogue_timer > room2_dialogue_duration:
            if room2_message_index < len(room2_dialogue_messages) - 1:
                room2_message_index += 1
                room2_dialogue_timer = pygame.time.get_ticks()
            else:
                room2_dialogue_active = False

    elif current_state == "piano text":
        screen.blit(piano, (0,0))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  
                  current_state = "room2"

    elif current_state == "book text":
        screen.blit(book, (0,0))
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  
                  current_state = "room2"
        
    elif current_state == "door2":
        screen.blit(door2, (0,0))
        
        input_surface = font.render(user_text, True, (255,255,255))
        screen.blit(input_surface, (600, 520))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  
                  current_state = "room2"

    elif current_state == "room3":
        screen.blit(room3, (0,0))
        if current_music != 'room3 new.mp3':
            pygame.mixer.music.load('music/room3 new.mp3')
            pygame.mixer.music.set_volume(1.0) 
            pygame.mixer.music.play(-1) 
            current_music = 'room3 new.mp3'

    elif current_state == "candle":

        import sliding_game
        sliding_game

        if sliding_game.current_state_game =="room3":
            current_state = "room3"
            Game_state_2 += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  
                  current_state = "room3"

    elif current_state == "rubble":
        returned_state = spot_the_difference()
        
        if returned_state == "room3":
            current_state = "room3"
            Game_state_2 += 1
            pygame.mixer.music.load('music/room3 new.mp3')
            pygame.mixer.music.set_volume(1.0) 
            pygame.mixer.music.play(-1) 
            current_music = 'room3 new.mp3'

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  
                  current_state = "room3"

    elif current_state == "door3":
        screen.blit(door3, (0,0))

        if current_music != 'room4.mp3':
            pygame.mixer.music.load('music/room4.mp3')
            pygame.mixer.music.set_volume(1.0)  
            pygame.mixer.music.play(-1)  
            current_music = 'room4.mp3'  

        if door3_dialogue_active:
            pygame.draw.rect(screen, (0, 0, 0), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))
            pygame.draw.rect(screen, (128, 128, 128), (dialogue_box_x + 5, dialogue_box_y + 5, dialogue_box_width - 10, dialogue_box_height - 10))

            door3_message_text = font.render(door3_dialogue_messages[door3_message_index], True, (0, 0, 0))
            screen.blit(door3_message_text, (dialogue_box_x + 10, dialogue_box_y + 30))

        if door3_dialogue_active and pygame.time.get_ticks() - door3_dialogue_timer > door3_dialogue_duration:
            if door3_message_index < len(door3_dialogue_messages) - 1:
                door3_message_index += 1
                door3_dialogue_timer = pygame.time.get_ticks()
            else:
                door3_dialogue_active = False       

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  
                  current_state = "room3"     

    elif current_state == "boat":
        import memory_game
        memory_game

        if memory_game.current_room_state_game3 == "room3":
            current_state = "room3"
            Game_state_2 += 1
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  
                  current_state = "room3"

    elif current_state == "game_over":
        import game_over_screen
        game_over_screen

    pygame.display.update()