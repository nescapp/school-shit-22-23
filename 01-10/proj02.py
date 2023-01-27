import pygame
# bonne chance pour installer pygame
# j'ai utilisé python 3.10

# Initialize pygame
pygame.init()

# Set up the window
window_size = (800, 800)
window = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Rectangle Drawer")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (51, 65, 57)
OUTLINE = (30, 45, 36)
GREEN = (150, 230, 179)

# Set up the font
font = pygame.font.Font(None, 14)

# Set up the counter for the number of rectangles
rect_count = 5

# Set up the minimum and maximum size for the rectangles
min_rect_size = (60, 45)
max_rect_size = (150, 130)

# Set up a list to store the rectangles
rects = []

# Set up the main loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif rect_count > 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Store the starting position of the rectangle
                click_pos = event.pos

            elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
                mouse_pos = event.pos
                if mouse_pos[0] > click_pos[0]: # RIGHT
                    if mouse_pos[1] > click_pos[1]: # BOTTOM RIGHT
                        preview_width = mouse_pos[0] - click_pos[0]
                        preview_height = mouse_pos[1] - click_pos[1]
                        preview_rect = pygame.Rect(click_pos, (preview_width, preview_height))
                        # (x & y of click point), (calculated width & height)
                    else: # TOP RIGHT
                        preview_width = mouse_pos[0] - click_pos[0]
                        preview_height = click_pos[1] - mouse_pos[1]
                        preview_rect = pygame.Rect((click_pos[0], mouse_pos[1]), (preview_width, preview_height))
                        # (x of click point, y of mouse), (calculated width & height)
                else: # LEFT
                    if mouse_pos[1] > click_pos[1]: # BOTTOM LEFT
                        preview_width = click_pos[0] - mouse_pos[0]
                        preview_height = mouse_pos[1] - click_pos[1]
                        preview_rect = pygame.Rect((mouse_pos[0], click_pos[1]), (preview_width, preview_height))
                        # (x of mouse, y of click point), (calculated width & height)
                    else: # TOP LEFT
                        preview_width = click_pos[0] - mouse_pos[0]
                        preview_height = click_pos[1] - mouse_pos[1]                    
                        preview_rect = pygame.Rect(event.pos, (preview_width, preview_height))
                        # (x & y of mouse), (calculated width & height)

            elif event.type == pygame.MOUSEBUTTONUP:
                # determine what side of click_pos the mouse is on
                release_pos = event.pos
                if click_pos[0] > release_pos[0]: # LEFT
                    if click_pos[1] > release_pos[1]: # TOP LEFT
                        width = click_pos[0] - release_pos[0]
                        height = click_pos[1] - release_pos[1]
                        click_pos = release_pos
                    else: # BOTTOM LEFT
                        width = click_pos[0] - release_pos[0]
                        height = release_pos[1] - click_pos[1]
                        click_pos = (release_pos[0], click_pos[1])
                else: # RIGHT
                    if click_pos[1] > release_pos[1]: # TOP RIGHT
                        width = release_pos[0] - click_pos[0]
                        height = click_pos[1] - release_pos[1]
                        click_pos = (click_pos[0], release_pos[1])
                    else: # BOTTOM RIGHT
                        width = release_pos[0] - click_pos[0]
                        height = release_pos[1] - click_pos[1]

                # Calculate the size of the rectangle
                # Make sure the rectangle is within the minimum and maximum size
                if width < min_rect_size[0] or height < min_rect_size[1] or width > max_rect_size[0] or height > max_rect_size[1]:
                    continue
                # if width > max_rect_size[0]:
                #     width = max_rect_size[0]
                # if height > max_rect_size[1]:
                #     height = max_rect_size[1]
                
                rect = pygame.Rect(click_pos, (width, height))

                # Create the rectangle
                

                # Check if the rectangle overlaps with any existing rectangles
                overlaps = False
                for r in rects:
                    if rect.colliderect(r):
                        overlaps = True
                        break

                # If the rectangle doesn't overlap, add it to the list
                if not overlaps:
                    rects.append(rect)
                    rect_count -= 1

    # Clear the window
    window.fill(GREEN)

    if event.type == pygame.MOUSEMOTION and event.buttons[0] and rect_count > 0:
        # draw the preview rectangle
        preview_overlaps = False
        for r in rects:
            if preview_rect.colliderect(r):
                preview_overlaps = True

        if (preview_width < min_rect_size[0] or preview_height < min_rect_size[1] 
            or preview_width > max_rect_size[0] or preview_height > max_rect_size[1] or preview_overlaps):
            pygame.draw.rect(window, RED, preview_rect, 2)
        else:
            pygame.draw.rect(window, OUTLINE, preview_rect, 2)

    # Draw the rectangles
    for rect in rects:
        pygame.draw.rect(window, GREY, rect)
        pygame.draw.rect(window, WHITE, rect, 2)

        # Calculate the latitude, longitude, and area of the rectangle
        lat = rect.y / window_size[1]
        lon = rect.x / window_size[0]
        area = rect.width * rect.height

        # Create the text to display
        text = [f'Lat: {lat:.2f}', f'Lon: {lon:.2f}', f'Area: {area}']

        # Draw the text
        # window.blit(text_surface, (text_x, text_y))
        for line in text:
            window.blit((font.render(line, True, WHITE)),(rect.x + 3, rect.y + 3 + text.index(line) * 15 ))

    # Draw the counter
    counter_text = f"Rectangles left: {rect_count}"
    counter_surface = font.render(counter_text, True, BLACK)
    window.blit(counter_surface, (0, 0))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
