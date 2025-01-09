import pygame 


pygame.init()

def room2(screen):
    
    room2 = pygame.image.load("assets/room2 best.jpg")
    room2 = pygame.transform.scale(room2, (800,600))

    piano = pygame.image.load("assets/piano better text.png")
    piano = pygame.transform.scale(piano, (800,600))

    book = pygame.image.load("assets/book text.png")
    book = pygame.transform.scale(book, (800,600))  

    door2 = pygame.image.load("assets/door 1-1.png")
    door2 = pygame.transform.scale(door2, (800,600))

    piano_rect = pygame.Rect(370, 320, 50, 60)
    book_rect = pygame.Rect(30, 540, 75, 30)
    door2_rect = pygame.Rect(350, 80, 85, 220)
    player_input = input()

    room2_message_index = 0
    room2_dialogue_active = False
    room2_dialogue_timer = 0
    room2_dialogue_duration = 3000

    correct_password = "JIGSAW"  # The correct password
    player_input = ""          # Stores the current input from the player
    puzzle_active = True       # Whether the puzzle is active
    door_unlocked = False

    room2_dialogue_messages = [
    "          you might have crossed the first room..",
    "        but you are still trapped in this mansion..",
    "and you wont get out of this room, especially since your time is limited"
    ]

    font = pygame.font.Font("assets/Zombified.ttf", 48)

    def draw_dialogue():
        """Handles drawing the dialogue box."""
        if room2_dialogue_active:
            pygame.draw.rect(screen, (0, 0, 0), (100, 400, 600, 150))  # Dialogue box background
            pygame.draw.rect(screen, (128, 128, 128), (105, 405, 590, 140))  # Inner box
            message_text = font.render(room2_dialogue_messages[room2_message_index], True, (0, 0, 0))
            screen.blit(message_text, (110, 430))

    def draw_puzzle():
         pygame.draw.rect(screen, (0, 0, 0), (200, 300, 400, 100))  # Input box
         pygame.draw.rect(screen, (255, 255, 255), (205, 305, 390, 90))  # White border

    # Render input text
         input_text = font.render(player_input, True, (0, 0, 0))
         screen.blit(input_text, (220, 330))

    # Render instructions
         instructions = font.render("Enter the password:", True, (0, 0, 0))
         screen.blit(instructions, (200, 250))

    def move_to_room2():
       return "room2"

    def move_to_piano():
       return "piano text"

    def move_to_book():
       return "book text"

    def move_to_door2():
       return "door2"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if current_state == "door2":
                    if puzzle_active:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                if player_input.upper() == correct_password
                                    door_unlocked = True
                                    puzzle_active = False
                                else:
                                    player_input = ""
                            elif event.key == pygame.K_BACKSPACE:
                                player_input = player_input[:-1]
                            elif event.unicode.isalpha():
                                player_input += event.unicode.upper()

                if current_state == "room2":
                    if piano_rect.collidepoint(mouse_x, mouse_y):
                        current_state = move_to_piano()  

                    if book_rect.collidepoint(mouse_x, mouse_y):
                        current_state = move_to_book()    

                    if door2_rect.collidepoint(mouse_x, mouse_y):
                        current_state = move_to_door2()

                room2_dialogue_active = True  # Activate the dialogue box in the cupboard scene
                room2_message_index = 0  # Reset the dialogue index
                room2_dialogue_timer = pygame.time.get_ticks()

        if current_state == "room2":
             screen.blit(room2, (0, 0))
             

        if current_state == "piano text":
            screen.blit(piano, (0,0))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Check if the Escape key is pressed
                      current_state = "room2"

        elif current_state == "book text":
            screen.blit(book, (0,0))
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Check if the Escape key is pressed
                     current_state = "room2"
        
        elif current_state == "door2":
             screen.blit(door2, (0,0))

             if puzzle_active:
                 draw_puzzle()

       


    