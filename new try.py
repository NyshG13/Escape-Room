import pygame

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mystery Rooms")

# Load assets
ASSETS = {
    "bg_beginning": pygame.transform.scale(pygame.image.load("assets/MYSTERY ROOMS.png"), (800, 600)),
    "introduction": [
        pygame.transform.scale(pygame.image.load(f"assets/intro{i}.png"), (800, 600)) for i in range(1, 4)
    ],
    "room1": pygame.transform.scale(pygame.image.load("assets/best room1.png"), (800, 600)),
    "mirror_text": pygame.transform.scale(pygame.image.load("assets/painting hidden.png"), (800, 600)),
    "table_objects": pygame.transform.scale(pygame.image.load("assets/hidden obj bg1.jpg"), (800, 600)),
    "cupboard_objects": pygame.transform.scale(pygame.image.load("assets/cupboard 1-2.jpg"), (800, 600)),
    "door_message": pygame.transform.scale(pygame.image.load("assets/door 1-1.png"), (800, 600)),
    "room2": pygame.transform.scale(pygame.image.load("assets/room2 best.jpg"), (800, 600)),
    "piano": pygame.transform.scale(pygame.image.load("assets/piano better text.png"), (800, 600)),
    "book": pygame.transform.scale(pygame.image.load("assets/book text.png"), (800, 600)),
    "key": pygame.transform.scale(pygame.image.load("assets/key 1-1.png"), (50, 50)),
    "font": pygame.font.Font("assets/Zombified.ttf", 48),
}

# Rectangles for interactive objects
RECTS = {
    "mirror": pygame.Rect(650, 150, 60, 65),
    "table": pygame.Rect(300, 340, 100, 100),
    "cupboard": pygame.Rect(0, 150, 90, 150),
    "door": pygame.Rect(450, 200, 65, 180),
    "piano": pygame.Rect(370, 320, 50, 60),
    "book": pygame.Rect(30, 540, 75, 30),
    "door2": pygame.Rect(350, 80, 85, 220),
}

# Dialogue messages
DIALOGUES = {
    "intro": [
        "You are trapped in a haunted mansion...",
        "To get out of this room, you need to find 3 keys..",
        "Feel free to explore, but remember that your time is ticking",
    ],
    "mirror": [
        "This painting is so scary...",
        "Maybe the key is hidden somewhere inside this painting..?",
        "Can you search for it before it's too late..?",
    ],
    "table": [
        "What a mess this table is in...",
        "Maybe the key is hidden here..?",
        "But will you find it before the ghosts find you?",
    ],
    "cupboard": [
        "Everything here is a mess... even this cupboard",
        "Could a key be hidden somewhere in here..?",
        "How will you find it before the ghosts come for you?",
    ],
    "door": [
        "The door is locked..",
        "It won't open unless you find those 3 keys..",
        "Will you be able to find them? HA HA HA",
    ],
    "room2": [
        "You might have crossed the first room..",
        "But you are still trapped in this mansion..",
        "You won't get out of this room, especially since your time is limited",
    ],
}

# Inventory
inventory = set()

# Dialogue Manager
class DialogueManager:
    def __init__(self):
        self.active = False
        self.messages = []
        self.index = 0
        self.timer = 0
        self.duration = 3000

    def start(self, messages):
        self.active = True
        self.messages = messages
        self.index = 0
        self.timer = pygame.time.get_ticks()

    def update(self):
        if self.active and pygame.time.get_ticks() - self.timer > self.duration:
            if self.index < len(self.messages) - 1:
                self.index += 1
                self.timer = pygame.time.get_ticks()
            else:
                self.active = False

    def draw(self):
        if self.active:
            pygame.draw.rect(screen, (0, 0, 0), (10, 500, 780, 90))
            pygame.draw.rect(screen, (128, 128, 128), (15, 505, 770, 80))
            message = ASSETS["font"].render(self.messages[self.index], True, (0, 0, 0))
            screen.blit(message, (20, 520))

# State Management
class GameState:
    def __init__(self):
        self.state = "start"
        self.dialogue = DialogueManager()

    def change_state(self, new_state):
        self.state = new_state
        if new_state in DIALOGUES:
            self.dialogue.start(DIALOGUES[new_state])

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if self.state == "room1":
                if RECTS["mirror"].collidepoint(mouse_x, mouse_y):
                    self.change_state("mirror")
                elif RECTS["table"].collidepoint(mouse_x, mouse_y):
                    self.change_state("table")
                elif RECTS["cupboard"].collidepoint(mouse_x, mouse_y):
                    self.change_state("cupboard")

    def update(self):
        self.dialogue.update()

    def draw(self):
        # screen.fill((0, 0, 0))
        if self.state in ASSETS:
            screen.blit(ASSETS[self.state], (0, 0))
        self.dialogue.draw()

# Main game loop
state = GameState()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        state.handle_events(event)

    state.update()
    state.draw()
    pygame.display.update()

pygame.quit()
