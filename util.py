def check_quit(pygame):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
