import pygame
import random
import time
import chem_names

pygame.init()
bgcolor = (36,255,0)
title_font = pygame.font.SysFont('Courier', 40)
main_font = pygame.font.SysFont('Courier',18,True)
pygame.mouse.set_cursor(*pygame.cursors.diamond)
screen = pygame.display.set_mode((1344,756))
pygame.display.set_caption("Organic Chemistry")

# Score object, evaluates score
class Score:

    def __init__(self):
        '''Stores score'''
        self.score = 0
        self.w_count = 0
        self.l_count = 0
        self.history = []

    def show_score(self):
        return str(self.score)

    def win_loss_ratio(self):
        if self.l_count == 0:
            return 'N/A'
        return str(round(self.w_count/self.l_count,2))

    def win(self):
        self.history.append('win')
        self.w_count += 1
        streak = False
        if len(self.history) >= 5:
            streak = True
            for score in self.history[len(self.history)-5:]:
                if score == 'loss':
                    streak = False
                    break
        if streak == True:
            self.score += 2
        else:
            self.score += 1

    def loss(self):
        self.history.append('loss')
        self.l_count += 1

    def reset(self):
        self.score = 0
        self.w_count = 0
        self.l_count = 0
        self.history = []    

# Displays main menu
def main_menu():
    print(chem_names.interpret('methyl ethanoate'))
    print(chem_names.interpret("2-bromo, 2,3-dichloro pent-4-ene"))
    print(chem_names.interpret('pent-2,4-diol'))
    screen.fill(bgcolor)
    start_button = pygame.rect.Rect(592, 185, 160, 80)
    inst_button = pygame.rect.Rect(527, 315, 300, 80)
    pygame.draw.rect(screen, (255,0,36), start_button)
    pygame.draw.rect(screen, (255,0,36), inst_button)
    texts = []
    for text in ["Organic chem","Start","Instrucions"]:
        texts.append(title_font.render(text,True,(0,0,0)))
    
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if start_button.collidepoint(ev.pos):
                    click_button(start_button)
                    diff_select()
                    break
                elif inst_button.collidepoint(ev.pos):
                    click_button(inst_button)
                    inst_page()
                    break
        for button in [start_button,inst_button]:
            if button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (208,0,36), button)
            else:
                pygame.draw.rect(screen, (255,0,36), button)
        for i,pos in enumerate([(527,50),(607,200),(542,330)]):
            screen.blit(texts[i],pos)
        pygame.display.flip()
    pygame.quit()

# Displays instruction page
def inst_page():
    screen.fill(bgcolor)
    inst_part1 = "The input is displayed on the left, drag processes onto the screen so that"
    inst_part2 = "it is converted to the output displayed on the right."
    inst_text = inst_part1+' '+inst_part2
    
    menu_button = pygame.rect.Rect(30,50,60,40)
    start_button = pygame.rect.Rect(592, 615, 160, 80)
    pygame.draw.rect(screen, (255,0,36), menu_button)
    pygame.draw.rect(screen, (255,0,36), start_button)
    lines = split_text(inst_text,1300,main_font)
    offset = 0
    for line in lines:
        inst_text = main_font.render(line,True,(0,0,0))
        screen.blit(inst_text,(50,120+offset))
        offset += main_font.get_height()

    texts = []
    for text,font in [["Instructions",title_font],["Start",title_font],["Menu",main_font]]:
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
                elif start_button.collidepoint(ev.pos):
                    click_button(start_button)
                    diff_select()
                    break
        for button in [start_button,menu_button]:
            if button.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (208,0,36), button)
            else:
                pygame.draw.rect(screen, (255,0,36), button)
        for i,pos in enumerate([(120,50),(607,630),(40,60)]):
            screen.blit(texts[i],pos)
        pygame.display.flip()
    pygame.quit()

# Allows player to select dificulty and starts game controller
def diff_select():
    screen.fill(bgcolor)
    title_text = title_font.render("Level Select",True,(0,0,0))
    screen.blit(title_text,(120,50))
    menu_button = pygame.rect.Rect(30,50,60,40)
    menu_text = main_font.render("Menu",True,(0,0,0))
    pygame.draw.rect(screen, (255,0,36), menu_button)
    buttons,button_texts = make_labled_buttons([[220, 165, 800, 120],[220, 355, 800, 120],[220, 545, 800, 120]],[levels[x]+' - '+level_descriptions[x] for x in range(3)],title_font)
    start = False
    
    while True:
        button_colors = [(255,0,36) for x in range(len(buttons))]
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if menu_button.collidepoint(ev.pos):
                    click_button(menu_button)
                    main_menu()
                    break
                elif buttons[0].collidepoint(ev.pos):
                    start = True
                    diff = 0
                elif buttons[1].collidepoint(ev.pos):
                    start = True
                    diff = 1
                elif buttons[2].collidepoint(ev.pos):
                    start = True
                    diff = 2
                if start:
                    click_button(buttons[diff])
                    main_control(diff)
                    break
        for i,button in enumerate(buttons):
            if button.collidepoint(pygame.mouse.get_pos()):
                button_colors[i] = (208,0,36)
        if menu_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (208,0,36), menu_button)
        else:
            pygame.draw.rect(screen, (255,0,36), menu_button)
        print_labled_buttons(buttons,button_texts,button_colors,[15,15])
        screen.blit(menu_text,(40,60))
        pygame.display.flip()
    pygame.quit()

# Opens a screen that warns the user when something goes wrong
def warning_screen(text):
    screen = pygame.display.set_mode((400,225))
    screen.fill(bgcolor)
    lines = split_text(text,360,main_font)
    offset = 0
    for line in lines:
        warning_text = main_font.render(line,True,(0,0,0))
        screen.blit(warning_text,(20,20+offset))
        offset += main_font.get_height()
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        pygame.display.flip()
    pygame.quit()

# Game controller
def main_control(diff):
    score.reset()
    stop = False
    while not stop:
        question = generate(diff)
        if question == False:
            warning_screen('The file "'+level_files[diff]+'" either cannot be found or is empty, please make sure that it exists, is in the same directory and has content.')
            break
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

# One round of the game
def game(question):
    drag = [False,0]
    buttons,button_texts = make_labled_buttons([[50,300,160,100],[1130,300,160,100],[30,50,60,40],[50,630,80,40],[1216,630,80,40]],[question[0],question[1],'Menu','Reset','Submit'])
    ans_buttons,ans_texts = make_labled_buttons([190,390,590,790,990],question[-1],main_font,True)
    ans_colors = [(0,102,255) for x in range(5)]
    
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                
                for i,button in enumerate(buttons):
                    if button.collidepoint(ev.pos):
                        if i == 2:
                            click_button(button)
                            main_menu()
                            return True
                        elif i == 3:
                            click_button(button)
                            for i,x in enumerate([190,390,590,790,990]):
                                ans_buttons[i].x = x
                                ans_buttons[i].y = 600
                        elif i == 4:
                            click_button(button)
                            ans = []
                            for i,button in enumerate(ans_buttons):
                                if button.y < 470:
                                    ans.append([i,button.x])
                            if not correct(question[2],question[3],ans):
                                view_ans_text = main_font.render(' -> '.join(question[2]),True,(0,0,0))
                                unpause_text = main_font.render('--Click anywhere to continue--',True,(0,0,0))
                                screen.blit(view_ans_text,(672-main_font.size(' -> '.join(question[2]))[0]*0.5,175))
                                screen.blit(unpause_text,(507,125))
                                pygame.display.flip()
                                while True:
                                    ev = pygame.event.poll()
                                    if ev.type == pygame.QUIT:
                                        pygame.quit()
                                        return True
                                    elif ev.type == pygame.MOUSEBUTTONDOWN:
                                        break
                            return False
                for i,button in enumerate(ans_buttons):
                    if button.collidepoint(ev.pos):
                        ans_colors[i] = (236,236,0)
                        drag = [True,i]
                        mouse_x, mouse_y = ev.pos
                        offset_x = button.x - mouse_x
                        offset_y = button.y - mouse_y
        elif ev.type == pygame.MOUSEBUTTONUP:
            if ev.button == 1:            
                drag[0] = False
        elif ev.type == pygame.MOUSEMOTION:
            if drag[0]:
                mouse_x, mouse_y = ev.pos
                if 220 < mouse_x + offset_x < 960:
                    ans_buttons[drag[1]].x = mouse_x + offset_x
                if 200 < mouse_y + offset_y < 650:
                    ans_buttons[drag[1]].y = mouse_y + offset_y

        for i,button in enumerate(ans_buttons):
            if not drag[0]:
                if button.y < 470:
                    ans_colors[i] = (236,0,55)
                elif button.y >= 470:
                    ans_colors[i] = (0,102,255)
        screen.fill(bgcolor)
        screen.fill((255,0,36),(0,550,1344,20))
        print_labled_buttons(buttons,button_texts,(255,0,36),[10,10])
        print_labled_buttons(ans_buttons,ans_texts,ans_colors,[10,10])
        score_text = title_font.render("Score: "+score.show_score()+"   W/L Ratio: "+score.win_loss_ratio(),True,(0,0,0))
        screen.blit(score_text,(120,50))
        pygame.display.flip()
    pygame.quit()
    return True

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

# Corrects the answer entered by the player and changes the score
def correct(correct_ans,ans_order,ans):
    ans = sort(ans)
    correct_numbers = []
    for p in correct_ans:
        correct_numbers.append(ans_order.index(p))
    ans_list = []
    for a in ans:
        ans_list.append(a[0])
    if correct_numbers == ans_list:
        score.win()
        return True
    else:
        score.loss()
        return False

# Just a bubble sort
def sort(things):
    done = False
    while not done:
        done = True
        for i in range(len(things)-1):
            if things[i][1] > things[i+1][1]:
                done = False
                j = things[i]
                things[i] = things[i+1]
                things[i+1] = j
    return things

# Loads contents of a file
def load_text(filename,questions=False):
    if questions:
        inputs = []
        outputs = []
        processes = []
        all_processes = []
    else:
        levels = []
    file = open(filename,'r')
    lines = file.readlines()
    for line in lines:
        if "%" in line:
            continue
        if '\n' in line:
            line = line[:-1]
        line = line.split(';')
        if questions:
            inputs.append(line[0])
            outputs.append(line[1])
            processes.append(line[2:])
        else:
            for i,part in enumerate(line):
                try:
                    levels[i].append(part)
                except:
                    levels.append([])
                    levels[i].append(part)
    if not questions:
        return levels
    for i in processes:
        for process in i:
            if process not in all_processes:
                all_processes.append(process)
    return [inputs,outputs,processes,all_processes]

def click_button(button):
    pygame.draw.rect(screen, (255,255,0), button)
    pygame.display.flip()
    time.sleep(0.15)

score = Score()
settings = load_text('settings.txt')
[levels,level_descriptions,level_files,level_modes] = settings[0:4]
question_files = [load_text(level_files[y],True) for y in range(3)]

if __name__ == '__main__':
    main_menu()
