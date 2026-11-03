import pygame
import subprocess
# 1. Initialize Pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Object-Oriented Button Class")

clock = pygame.time.Clock()


# 2. Define the Reusable Button Class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action):
        """
        Initializes a custom button object.
        action: Pass a function name here to execute when clicked.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action  # This holds the click function reference
        self.is_hovering = False

        # Set up text font, surface, and position
        self.font = pygame.font.SysFont("Arial", 28, bold=True)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, surface):
        """Draws the button onto the given surface with proper hover state colors."""
        current_color = self.hover_color if self.is_hovering else self.color
        pygame.draw.rect(surface, current_color, self.rect, border_radius=8)
        surface.blit(self.text_surface, self.text_rect)

    def check_hover(self, mouse_pos):
        """Updates the button's internal hover tracking state."""
        self.is_hovering = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        """Checks for mouse click triggers specifically within this button's boundary."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovering and self.action:
                self.action()  # Execute the passed callback function


# 3. Define Callback Functions (What happens when buttons are clicked)
def print_hello():
    print("Hello from the button object!")

def print_goodbye():
    print("Goodbye World!")

def run_game():
    subprocess.Popen(Slots.jar)

# 4. Instantiate Button Objects
# You can now cleanly add as many buttons as you want in one line!
button_1 = Button(300, 200, 200, 60, "Say Hello", (0, 150, 255), (0, 200, 255), print_hello)
button_2 = Button(300, 320, 200, 60, "Say Goodbye", (230, 50, 50), (255, 80, 80), print_goodbye)

# Keep track of all button objects in a clean list
buttons = [button_1, button_2]


# 5. Main Loop
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Route events cleanly through every button object
        for button in buttons:
            button.handle_event(event)

    # --- GAME LOGIC ---
    # Continuously check hover states for accurate visual responsiveness
    for button in buttons:
        button.check_hover(mouse_pos)

    # --- DRAWING ---
    screen.fill((30, 30, 40))

    # Cleanly draw every button object stored in our register
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
