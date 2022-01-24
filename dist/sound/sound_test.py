import pygame

pygame.display.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800,600))
done = False

pygame.mixer.music.load("trak1.wav")
pygame.mixer.music.play()

paused = False
snds = [pygame.mixer.Sound("jump1.wav"), pygame.mixer.Sound("land1.wav")]

while not done:
    eList = pygame.event.get()
    for e in eList:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_1:
                snds[0].play()
            elif e.key == pygame.K_2:
                snds[1].play()
            elif e.key == pygame.K_p:
                paused = not paused
                if paused:
                    pos = pygame.mixer.music.get_pos()
                    pygame.mixer.music.load("menu.wav")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("trak1.wav")
                    pygame.mixer.music.play(1, pos)


    pygame.display.flip()


pygame.mixer.quit()

