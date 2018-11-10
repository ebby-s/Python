import pygame
import threading

pygame.init()
global title_font
global main_font
title_font = pygame.font.SysFont('Courier', 40)
main_font = pygame.font.SysFont('Courier',18)

class Window:

    def __init__(self):
        print("window initialising...")
        self.bgcolor = (36,255,0)
        self.ans_buttons = []
        for i in range(5):
            self.ans_buttons.append(pygame.rect.Rect(176, 134, 17, 17))
        self.drag = [False,0]
        

    def activate(self):
        self.screen = pygame.display.set_mode((800,450))
        pygame.display.set_caption("Organic Chemistry")
        self.thread = threading.Thread(None,self.active)
        self.thread.start()

    def close(self):
        print("closing window...")
        pygame.display.quit()
        pygame.quit()
        print("window closed...")
    
    def active(self):
        print("window activating...")
        
        self.screen.fill(self.bgcolor)
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break

            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    for i,button in enumerate(self.ans_buttons):
                        if button.collidepoint(ev.pos):
                            self.drag = [True,i]
                            mouse_x, mouse_y = ev.pos
                            offset_x = button.x - mouse_x
                            offset_y = button.y - mouse_y

            elif ev.type == pygame.MOUSEBUTTONUP:
                if ev.button == 1:            
                    self.drag[0] = False
            elif ev.type == pygame.MOUSEMOTION:
                if self.drag[0]:
                    mouse_x, mouse_y = ev.pos
                    self.ans_buttons[self.drag[1]].x = mouse_x + offset_x
                    self.ans_buttons[self.drag[1]].y = mouse_y + offset_y

            self.screen.fill(self.bgcolor)
            for button in self.ans_buttons:
                pygame.draw.rect(self.screen, (0,36,255), button)
            pygame.display.flip()

test = Window()
test.activate()
