import pygame
import qrcode
import random
from io import BytesIO
from PIL import Image

# Initialize Pygame
pygame.init()

#  display Milako
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("QR Code Dare Game")

# bg color adujst gareko
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)

score = 0

# Dare haru ko vandaar
dares = [
    "Sing a song!",
    "Dance for 30 seconds!",
    "Do 10 push-ups!",
    "Tell a funny joke!",
    "Imitate an animal!",
    "Run around the room!",
    "Pretend you're invisible!"
]

# dare nikalne ninja technique using functions
def generate_qr_code(dare_text):
    # QR code library use garera generate gareko dares
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(dare_text)  
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white').convert('RGB')
    
    size = img.size
    data = img.tobytes()
    
    qr_surface = pygame.image.frombuffer(data, size, "RGB")
    
    return qr_surface

# text dekhaune ninja technique
def display_text(text, position, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def display_qr_code(qr_surface):
    screen.fill(WHITE)
    
    
    qr_rect = qr_surface.get_rect(center=(screen_width // 2, screen_height // 3))
    screen.blit(qr_surface, qr_rect)

def display_score():
    screen.fill(WHITE)
    display_text(f"Your score: {score}", (50, 50))
    pygame.display.update()
    pygame.time.wait(2000) 

def player_round():
    global score
    dare_text = random.choice(dares)
    qr_surface = generate_qr_code(dare_text)
    
    dare_completed = False
    input_submitted = False
    
    while not input_submitted:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # Player submits whether they completed the dare
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:  # 'Y' for "Yes, completed"
                    dare_completed = True
                    input_submitted = True
                elif event.key == pygame.K_n:  # 'N' for "No, didn't complete"
                    dare_completed = False
                    input_submitted = True
        
        # naya QR code dekhauna ko lagi
        display_qr_code(qr_surface)
        display_text(f"Scan the QR code to see your dare!", (50, screen_height - 100))
        
        pygame.display.update()

    # Update score based on whether the dare was completed
    if dare_completed:
        score += 1

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # counting rounds
    player_round()
    
    # round pachi score dekhauna
    display_score()

# Quit Pygame
pygame.quit()
