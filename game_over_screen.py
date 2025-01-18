import pygame
import cv2  

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('music/game over music.mp3')
pygame.mixer.music.play(-1)

WHITE = (255, 255, 255)

current_state_out = 'game_over'  

video_path = "C:/Users/naysh/Escape_Room/videos/out_of_the_mansion.mp4" 

screen = pygame.display.set_mode((800, 600))

font_title = pygame.font.Font('memory game/fonts/HallowenInline.ttf', 64)
font_content = pygame.font.Font('memory game/fonts/Halloween.ttf', 30)

game_over_text = font_title.render('GAME COMPLETE', True, WHITE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (800//2, 600//2)

congrats_text = font_content.render('You saved the souls and now you are free', True, WHITE)
congrats_rect = congrats_text.get_rect()
congrats_rect.center = (800//2, 600//2 + 50)

thank_you_text = font_content.render('Thank you for playing', True, WHITE)
thank_you_rect = thank_you_text.get_rect()
thank_you_rect.center = (800//2, 600//2 + 100)

# Function to play the video using OpenCV
def play_video():
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Couldn't open the video file.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)

    # Play the video frame by frame
    while cap.isOpened():
        ret, frame = cap.read()  # Read the next frame
        
        if not ret:
            break  # If no frames left, exit the loop

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        frame_surface = pygame.surfarray.make_surface(frame)

        rotated_surface = pygame.transform.rotate(frame_surface, -90)  

        screen.blit(rotated_surface, (0, 0))

        screen.blit(game_over_text, game_over_rect)
        screen.blit(congrats_text, congrats_rect)
        screen.blit(thank_you_text, thank_you_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                quit()

        pygame.time.Clock().tick(fps) 

    # Release the video capture when done
    cap.release()


running = True
while running:
    # Check game state
    if current_state_out == 'game_over':
        play_video()  # Play the video when game is over
        current_state_out = 'playing'  # Reset state after video finishes
        break  # Exit the loop after the video finishes

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
