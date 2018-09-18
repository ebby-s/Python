import pygame
import time

pygame.init()
bgcolor = (147,166,180)
button_color = (255,255,255)
hover_color = (216,216,216)
press_color = (192,192,192)
logo = pygame.image.load("ciswhitemalehort.png")
pattern = pygame.image.load("line.png")
title_font = pygame.font.SysFont('Courier', 40)
small_font = pygame.font.SysFont('Courier',18)
main_font = pygame.font.SysFont('Courier',18,True)
pygame.mouse.set_cursor(*pygame.cursors.diamond)
screen = pygame.display.set_mode((1344,756))
pygame.display.set_caption("ECG Sim")

# Displays main menu
def main_menu():
    screen.fill(bgcolor)
    
    screen.blit(pattern, (0, 350))
    screen.blit(pattern, (519, 350))
    screen.blit(pattern, (824, 350))
    screen.blit(logo, (519, 120))
    start_button = pygame.rect.Rect(592, 565, 160, 80)
    pygame.draw.rect(screen, button_color, start_button)
    credits_button = pygame.rect.Rect(612, 675, 120, 60)
    pygame.draw.rect(screen, button_color, credits_button)
    texts = []
    for text in ["ECG Sim","Start"]:
        texts.append(title_font.render(text,True,(0,0,0)))
    texts.append(small_font.render("Credits",True,(0,0,0)))
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if start_button.collidepoint(ev.pos):
                    click_button(start_button)
                    level_select()
                    break
                elif credits_button.collidepoint(ev.pos):
                    click_button(credits_button)
                    credits_page()
                    break
        for button in [start_button,credits_button]:
            if button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, hover_color, button)
            else:
                pygame.draw.rect(screen, button_color, button)
        for i,pos in enumerate([(588,50),(607,580),(634,695)]):
            screen.blit(texts[i],pos)
        pygame.display.flip()
    pygame.quit()

# Displays credits page
def credits_page():
    screen.fill(bgcolor)
    offset = 0
    credits_texts = []
    for text in ["Programming: ","Design: ","Everything else: "]:
        credits_texts.append(small_font.render(text,True,(0,0,0)))
    for text in credits_texts:
        screen.blit(text,(50,120+offset))
        offset += small_font.get_height() + 50
    
    menu_button = pygame.rect.Rect(30,50,60,40)
    
    texts = []
    for text,font in [["Instructions",title_font],["Menu",main_font]]:
        texts.append(font.render(text,True,(0,0,0)))    

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if menu_button.collidepoint(ev.pos):
                    click_button(menu_button)
                    main_menu()
                    break
        for button in [menu_button]:
            if button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, hover_color, button)
            else:
                pygame.draw.rect(screen, button_color, button)
        for i,pos in enumerate([(120,50),(40,60)]):
            screen.blit(texts[i],pos)
        pygame.display.flip()
    pygame.quit()

# Allows player to select a level and starts game controller
def level_select():
    screen.fill(bgcolor)
    title_text = title_font.render("Level Select",True,(0,0,0))
    screen.blit(title_text,(120,50))
    menu_button = pygame.rect.Rect(30,50,60,40)
    menu_text = main_font.render("Menu",True,(0,0,0))
    pygame.draw.rect(screen, button_color, menu_button)
    level_buttons,button_texts = make_labled_buttons([[100, 165+110*x, 315, 80] for x in range(0,5)] ,["Level "+str(x)+' - '+"Level description." for x in range(0,5)],main_font)
    mid_buttons,mid_texts = make_labled_buttons([[515, 165+110*(x%5), 315, 80] for x in range(5,10,1)] ,["Level "+str(x)+' - '+"Level description." for x in range(5,10,1)],main_font)
    right_buttons,right_texts = make_labled_buttons([[930, 165+110*(x%5), 315, 80] for x in range(10,15,1)] ,["Level "+str(x)+' - '+"Level description." for x in range(10,15,1)],main_font)    
    level_buttons += mid_buttons + right_buttons
    button_texts += mid_texts + right_texts
    start = False
    
    while True:
        button_colors = [button_color for x in range(len(level_buttons))]
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if menu_button.collidepoint(ev.pos):
                    click_button(menu_button)
                    main_menu()
                    break
                for button in level_buttons:
                    if button.collidepoint(ev.pos):
                        start = True
                        level = level_buttons.index(button)
                if start:
                    click_button(level_buttons[level])
                    main_control(level)
                    break
        for i,button in enumerate(level_buttons):
            if button.collidepoint(pygame.mouse.get_pos()):
                button_colors[i] = hover_color
        if menu_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, hover_color, menu_button)
        else:
            pygame.draw.rect(screen, button_color, menu_button)
        print_labled_buttons(level_buttons,button_texts,button_colors,[15,15])
        screen.blit(menu_text,(40,60))
        pygame.display.flip()
    pygame.quit()

# Game controller
def main_control(level):
    stop = False
    while not stop:
        question = generate(level)
        stop = game(question)

# Creates buttons, a button is a rectangle and text together
def make_labled_buttons(coordinates,texts,font=main_font,pos_only=False):
    buttons = []
    button_texts = []
    if pos_only:
        for x in coordinates:
            buttons.append(pygame.rect.Rect(x,600,160,80))
    else:
        for x,y,sx,sy in coordinates:
            buttons.append(pygame.rect.Rect(x,y,sx,sy))
    for i,text in enumerate(texts):
        max_length = buttons[i].width
        if font.size(text)[0] > max_length-40:
            lines = []
            text = split_text(text,max_length,font)
            for line in text:
                lines.append(font.render(line,True,(0,0,0)))
            button_texts.append(lines)
        else:
            button_texts.append(font.render(text,True,(0,0,0)))
    return buttons,button_texts

#Prints buttons onto the screen, a button is a rectangle and text together
def print_labled_buttons(buttons,texts,colors,offset):
    if type(colors) != type([]):
        color = colors
        colors = [color for x in range(len(buttons))]
    for i,button in enumerate(buttons):
        pygame.draw.rect(screen, colors[i], button)
        if type(texts[i]) == type([]):
            line_offset = 0
            for line in texts[i]:
                screen.blit(line,(button.x+offset[0],button.y+offset[1]+line_offset))
                line_offset += line.get_height()
        else:
            screen.blit(texts[i],(button.x+offset[0],button.y+offset[1]))

# Splits a line into several smaller lines which are smaller than max length
def split_text(text,max_length,font):
    text = text.split()
    lines = []
    line = ''
    for word in text:
        if font.size(line+' '+word)[0] >= max_length-40 and line != '':
            lines.append(line)
            line = ''
        if line != '':
            line = " ".join([line,word])
        else:
            line = word
    if line != '':
        lines.append(line)
    return lines

# Generates questions from contents of questions file
def generate(diff):
    try:
        i,o,p,allp = question_files[diff]
        if len(i) == 0:
            return False
    except:
        return False

    ps = []
    if level_modes[diff] == 'random':
        val = random.randint(0,len(i)-1)
        
        for j in p[val]:
            ps.append(j)
        while len(ps) < 5:
            k = random.choice(allp)
            if k not in ps:
                ps.append(k)

        random.shuffle(ps)
    return [i[val],o[val],p[val],ps]

def click_button(button):
    pygame.draw.rect(screen, press_color, button)
    pygame.display.flip()
    time.sleep(0.15)

if __name__ == '__main__':
    main_menu()
