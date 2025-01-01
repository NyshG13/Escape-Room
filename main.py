import pygame

pygame.init()

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

room1 = pygame.image.load("assets/empty room.jpg")
room1 = pygame.transform.scale(room1,(800,600))

mirror = pygame.image.load("assets/cropped mirror.png")
mirror = pygame.transform.scale(mirror,(90,150))

mirror_text = pygame.image.load("assets/mirror text.jpg")
mirror_text = pygame.transform.scale(mirror_text,(800,600))

door = pygame.image.load("assets/door 1-2.jpg")
door = pygame.transform.scale(door,(100,200))

sofa = pygame.image.load("assets/sofa 1.jpg")
sofa = pygame.transform.scale(sofa,(100,200))

mirror_rect = mirror.get_rect()
mirror_rect.topleft = (450, 150)

dialogue_box_width = 800-20
dialogue_box_height = 90
dialogue_box_x = 10
dialogue_box_y = 600-100

current_message_index = 0
dialogue_active = False  # Whether the dialogue box is active
dialogue_timer = 0  # Timer to control how long the dialogue is shown
dialogue_duration = 3000

mirror_message_index = 0
mirror_dialogue_active = False  # Whether the dialogue box is active in the mirror scene
mirror_dialogue_timer = 0
mirror_dialogue_duration = 3000

dialogue_messages = [
    "              You are trapped in a haunted mansion...",
    "         Solve the puzzles to escape before it's too late.",
    "              The ghosts are watching your every move..."
]

mirror_dialogue_messages = [
    "               This mirror is so scary...",
    "    There was first the reflection of a ghost, now a message....",
    "               What could this possibly mean...?"
]


def draw_dialogue_box():
    pygame.draw.rect(screen, (0, 0, 0), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))
    pygame.draw.rect(screen, (128,128,128), (dialogue_box_x + 5, dialogue_box_y + 5, dialogue_box_width - 10, dialogue_box_height - 10))
    
    # Render the current message
    message_text = font.render(dialogue_messages[current_message_index], True, (0, 0, 0))
    screen.blit(message_text, (dialogue_box_x + 10, dialogue_box_y + 30))

font = pygame.font.Font("assets/Zombified.ttf", 48)



def draw_text_button():
    button_text = font.render("ENTER", True, (255,255,255))  
    button_width = button_text.get_width()
    button_height = button_text.get_height()
    
    # Position the text in the center of the screen (or wherever you prefer)
    button_x = 360
    button_y = 440
    
    # Draw the text on the screen
    screen.blit(button_text, (button_x, button_y))
    return button_x, button_y, button_width, button_height


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

current_state = "start"

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if current_state == "start":
                button_x, button_y, button_width, button_height = draw_text_button()
            
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    current_state = start_game()  

            elif current_state == "room1":
                if mirror_rect.collidepoint(mouse_x, mouse_y):
                    current_state = move_to_mirror()
                    mirror_dialogue_active = True  # Activate the dialogue box in the mirror scene
                    mirror_message_index = 0  # Reset the dialogue index
                    mirror_dialogue_timer = pygame.time.get_ticks()

        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RETURN:  
                if current_state == "introduction1":
                    current_state = move_to_intro2()
                elif current_state == "introduction2":
                    current_state = move_to_intro3()
                elif current_state == "introduction3":
                    current_state = move_to_room1()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # When Enter is pressed
                if current_message_index < len(dialogue_messages) - 1:
                    current_message_index += 1
                    dialogue_timer = pygame.time.get_ticks()  # Reset the timer

                # If all messages are finished, hide the dialogue box
                if current_message_index >= len(dialogue_messages):
                    dialogue_active = False

    if current_state == "start":         
        screen.blit(bg_beginning, (0, 0))
        draw_text_button()
    elif current_state == "introduction1":
        screen.blit(introduction1, (0,0))
    elif current_state == "introduction2":
        screen.blit(introduction2, (0, 0))
    elif current_state == "introduction3":
        screen.blit(introduction3, (0, 0))
    elif current_state == "room1":
        screen.blit(room1, (0, 0))
        if dialogue_active:
           draw_dialogue_box()
        screen.blit(mirror, (450, 150))

    # If the dialogue box is not active and we are on the start screen, show the first message
        if not dialogue_active and current_message_index == 0:
            dialogue_active = True
            dialogue_timer = pygame.time.get_ticks()

    # Check if the current message has timed out (if the timer exceeds the duration)
        if dialogue_active and pygame.time.get_ticks() - dialogue_timer > dialogue_duration:
            if current_message_index < len(dialogue_messages) - 1:
                current_message_index += 1
                dialogue_timer = pygame.time.get_ticks()  # Reset the timer
            else:
                dialogue_active = False 

        screen.blit(door, (325, 150))
        # screen.blit(sofa, (700, 400))

    elif current_state == "mirror text":
        screen.blit(mirror_text, (0, 0))
        if mirror_dialogue_active:
            pygame.draw.rect(screen, (0, 0, 0), (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))
            pygame.draw.rect(screen, (128, 128, 128), (dialogue_box_x + 5, dialogue_box_y + 5, dialogue_box_width - 10, dialogue_box_height - 10))

            # Render the current dialogue message
            mirror_message_text = font.render(mirror_dialogue_messages[mirror_message_index], True, (0, 0, 0))
            screen.blit(mirror_message_text, (dialogue_box_x + 10, dialogue_box_y + 30))

        # Auto-progress the dialogue based on timer (optional)
        if mirror_dialogue_active and pygame.time.get_ticks() - mirror_dialogue_timer > mirror_dialogue_duration:
            if mirror_message_index < len(mirror_dialogue_messages) - 1:
                mirror_message_index += 1
                mirror_dialogue_timer = pygame.time.get_ticks()
            else:
                mirror_dialogue_active = False

    pygame.display.update()

