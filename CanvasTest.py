import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((640,480))
    colour = pygame.display.set_mode((640,480))

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,0,0))

    canvas = pygame.Surface((600,400))
    canvas = canvas.convert()
    canvas.fill((255,255,255))

    bk = pygame.Surface(colour.get_size())
    bk = bk.convert()
    bk.fill((0,0,255))

    clock = pygame.time.Clock()
    preview = False
    viewer = False
    keepGoing = True
    LineStart = (0,0)
    LineEnd = (0,0)
    
    while (keepGoing):
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                lineStart = pygame.mouse.get_pos()
                preview = True
            elif event.type == pygame.MOUSEBUTTONUP:
                lineEnd = pygame.mouse.get_pos()
                pygame.draw.line(canvas, (0, 0, 0), lineStart, lineEnd, 3)
                preview = False
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    viewer = True
                elif event.key == pygame.K_RIGHT:
                    viewer = False
                
            
        screen.blit(background, (0, 0))
        screen.blit(canvas, (0,0))
        if preview:
            pygame.draw.line(screen, (100, 100, 100), lineStart, lineEnd, 1)
        if viewer:
            colour.blit(bk, (0,0))

        pygame.display.flip()

if __name__ == "__main__": main()
