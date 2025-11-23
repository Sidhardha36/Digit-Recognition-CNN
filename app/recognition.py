import os
import pygame
import numpy as np
from tensorflow.keras.models import load_model

# Window position
os.environ['SDL_VIDEO_WINDOW_POS'] = "300,100"

pygame.init()

# Load trained CNN model
model = load_model("../model/model.h5")

# Window settings
WIDTH, HEIGHT = 650, 550
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Handwritten Digit Recognizer")

# Colors
BG = (30, 30, 30)
CANVAS_BG = (0, 0, 0)
WHITE = (255, 255, 255)
BUTTON_COLOR = (60, 60, 60)
BUTTON_HOVER = (90, 90, 90)

# Canvas
canvas = pygame.Surface((300, 300))
canvas.fill(CANVAS_BG)

font = pygame.font.SysFont("Segoe UI", 26)
small_font = pygame.font.SysFont("Segoe UI", 20)

# Fixed brush size
BRUSH_SIZE = 12


# PREDICTION — FIXED WITH PROPER RESIZE

def predict_digit():
    arr = pygame.surfarray.array3d(canvas)

    # Convert to grayscale
    arr = np.dot(arr[..., :3], [0.2989, 0.5870, 0.1140])

    # Rotate and flip to match MNIST orientation
    arr = np.rot90(arr, -1)
    arr = np.fliplr(arr)

    # Convert numpy → pygame surface → resize to 28x28 → numpy
    surface = pygame.surfarray.make_surface(arr)
    surface_28 = pygame.transform.scale(surface, (28, 28))
    arr_28 = pygame.surfarray.array3d(surface_28)

    arr_28 = np.dot(arr_28[..., :3], [0.2989, 0.5870, 0.1140])
    arr_28 = arr_28.reshape(1, 28, 28, 1) / 255.0

    pred = model.predict(arr_28)[0]
    return np.argmax(pred)


# BUTTON COMPONENT

def draw_button(text, x, y, w, h):
    mouse = pygame.mouse.get_pos()
    rect = pygame.Rect(x, y, w, h)

    color = BUTTON_HOVER if rect.collidepoint(mouse) else BUTTON_COLOR
    pygame.draw.rect(WIN, color, rect, border_radius=10)

    WIN.blit(font.render(text, True, WHITE), (x + 10, y + 5))
    return rect


# MAIN LOOP

running = True
prediction = ""

print("App running...")

while running:
    WIN.fill(BG)

    # Header
    WIN.blit(font.render("Digit Recognizer", True, WHITE), (20, 20))

    # Canvas border
    pygame.draw.rect(WIN, WHITE, (20, 80, 302, 302), 2)
    WIN.blit(canvas, (21, 81))

    # Buttons
    reset_btn = draw_button("Reset", 350, 120, 140, 40)
    predict_btn = draw_button("Predict", 350, 180, 140, 40)

    # Prediction text
    WIN.blit(font.render(f"Prediction: {prediction}", True, WHITE), (350, 250))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Drawing on canvas
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            if 21 < x < 321 and 81 < y < 381:
                pygame.draw.circle(canvas, WHITE, (x - 21, y - 81), BRUSH_SIZE)

        # Button click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_btn.collidepoint(event.pos):
                canvas.fill(CANVAS_BG)
                prediction = ""

            if predict_btn.collidepoint(event.pos):
                prediction = predict_digit()

    pygame.display.update()

pygame.quit()
