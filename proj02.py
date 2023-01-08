import pygame

# Initialize pygame
pygame.init()

# Set up the window
window_size = (600, 600)
window = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Rectangle Drawer")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (51, 65, 57)
OUTLINE = (30, 45, 36)
GREEN = (150, 230, 179)

# Set up the font
font = pygame.font.Font(None, 14)

# Set up the counter for the number of rectangles
rect_count = 0

# Set up the minimum and maximum size for the rectangles
min_rect_size = (40, 30)
max_rect_size = (100, 80)

# Set up a list to store the rectangles
rects = []

# Set up the main loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Store the starting position of the rectangle
            start_pos = event.pos
            print(start_pos)

        elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
            # display a preview of the rectangle as the mouse moves around the screen
            # Calculate the size of the rectangle using the starting position of MOUSEBUTTONDOWN
            if event.pos[0] > start_pos[0]:
                # RIGHT
                if event.pos[1] > start_pos[1]:
                # BOTTOM RIGHT
                    preview_width = event.pos[0] - start_pos[0]
                    preview_height = event.pos[1] - start_pos[1]
                    if preview_width < min_rect_size[0]:
                        preview_width = min_rect_size[0]
                    elif preview_width > max_rect_size[0]:
                        preview_width = max_rect_size[0]
                    if preview_height < min_rect_size[1]:
                        preview_height = min_rect_size[1]
                    elif preview_height > max_rect_size[1]:
                        preview_height = max_rect_size[1]
                    preview_rect = pygame.Rect(start_pos, (preview_width, preview_height))
                else:
                    # TOP RIGHT
                    preview_width = event.pos[0] - start_pos[0]
                    preview_height = start_pos[1] - event.pos[1]

                    print("preview_width: " + str(preview_width))
                    print("preview_height: " + str(preview_height))
                    
                    if preview_width < min_rect_size[0]:
                        preview_width = min_rect_size[0]
                    elif preview_width > max_rect_size[0]:
                        preview_width = max_rect_size[0]

                    if preview_height < min_rect_size[1]:
                        preview_height = min_rect_size[1]
                    elif preview_height > max_rect_size[1]:
                        preview_height = max_rect_size[1]
                    
                    preview_rect = pygame.Rect((start_pos[0], event.pos[1]), (preview_width, preview_height))

            else:
                if event.pos[1] > start_pos[1]:
                    # BOTTOM LEFT
                    preview_width = start_pos[0] - event.pos[0]
                    preview_height = event.pos[1] - start_pos[1]
                    if preview_width < min_rect_size[0]:
                        preview_width = min_rect_size[0]
                    elif preview_width > max_rect_size[0]:
                        preview_width = max_rect_size[0]
                    if preview_height < min_rect_size[1]:
                        preview_height = min_rect_size[1]
                    elif preview_height > max_rect_size[1]:
                        preview_height = max_rect_size[1]
                    preview_rect = pygame.Rect((event.pos[0], start_pos[1]), (preview_width, preview_height))

                else:
                    # TOP LEFT
                    preview_width = start_pos[0] - event.pos[0]
                    preview_height = start_pos[1] - event.pos[1]
                    if preview_width < min_rect_size[0]:
                        preview_width = min_rect_size[0]
                    elif preview_width > max_rect_size[0]:
                        preview_width = max_rect_size[0]
                    if preview_height < min_rect_size[1]:
                        preview_height = min_rect_size[1]
                    elif preview_height > max_rect_size[1]:
                        preview_height = max_rect_size[1]
                    preview_rect = pygame.Rect(event.pos, (preview_width, preview_height))

                
            
            # show the rectangle
            
        elif event.type == pygame.MOUSEBUTTONUP:
            # Calculate the size of the rectangle
            width = event.pos[0] - start_pos[0]
            height = event.pos[1] - start_pos[1]

            # Make sure the rectangle is within the minimum and maximum size
            if width < min_rect_size[0]:
                width = min_rect_size[0]
            elif width > max_rect_size[0]:
                width = max_rect_size[0]
            if height < min_rect_size[1]:
                height = min_rect_size[1]
            elif height > max_rect_size[1]:
                height = max_rect_size[1]

            # Create the rectangle
            rect = pygame.Rect(start_pos, (width, height))

            # Check if the rectangle overlaps with any existing rectangles
            overlaps = False
            for r in rects:
                if rect.colliderect(r):
                    overlaps = True
                    break

            # If the rectangle doesn't overlap, add it to the list
            if not overlaps:
                rects.append(rect)
                rect_count += 1

    # Clear the window
    window.fill(GREEN)

    if event.type == pygame.MOUSEMOTION and event.buttons[0]:
        # draw the preview rectangle
        pygame.draw.rect(window, OUTLINE, preview_rect, 2)

    # Draw the rectangles
    for rect in rects:
        pygame.draw.rect(window, GREY, rect)

        # Calculate the latitude, longitude, and area of the rectangle
        lat = rect.y / window_size[1]
        lon = rect.x / window_size[0]
        area = rect.width * rect.height

        # Create the text to display
        text = f"Lat: {lat:.2f} Lon: {lon:.2f} Area: {area}"

        # Render the text
        text_surface = font.render(text, True, BLACK)

        # Get the dimensions of the text
        text_width, text_height = text_surface.get_size()

        # Calculate the position of the text
        text_x = rect.x + (rect.width - text_width) / 2
        text_y = rect.y + (rect.height - text_height) / 2

        # Draw the text
        window.blit(text_surface, (text_x, text_y))

    # Draw the counter
    counter_text = f"Rectangle Count: {rect_count}"
    counter_surface = font.render(counter_text, True, BLACK)
    window.blit(counter_surface, (0, 0))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
