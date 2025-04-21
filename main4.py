import pygame
import sys
import json
pygame.init()

#
white =(255, 255, 255)
black =(0, 0, 0)
width = 400
height = 400
screen = pygame.display.set_mode((width, height))
timer = 0

upgrade_button = pygame.Rect(25,25,25,25)
# click_button = pygame.Rect(50,50,50,50)
upgrade_cost = [25,75,125,175,225,275,325,375,425]
ui=0
clicks_per_second = [1,3,5,7,9,11,13,15,17]
# upgrade_increase = 4
enemy = 0
moneyi = 0
enemies = [100, 200, 300, 400, 500, 750, 1000, 1200, 1500,]
money2 = [10, 15, 25, 50, 75, 125, 175, 275, 350]
score = enemies[enemy]
money = 0

pygame.display.set_caption('Clicker Game')

def save_game(score):
    game_state = {
        "score": score,
        "enemy": enemy,
        "moneyi": moneyi,
        "money": money
    }
    with open("save.json", "w") as f:
        json.dump(game_state, f)

def load_game():
    with open("save.json", "r") as f:
        game_state = json.load(f)
    return game_state["score"], game_state["enemy"], game_state["moneyi"]

score, enemy, moneyi = load_game()
#anim_main_char =[pygame.transform.scale(pygame.image.load(""), size = (400, 300))]

font = pygame.font.Font(None, 36)
#главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #проверка и нажатие кнопок мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #лкм
                score -= 1

            if upgrade_button.collidepoint(event.pos) and money >= upgrade_cost[ui]:
                money -= upgrade_cost[ui]
                ui+=1
            #     добавть само улучшение


            #         moneyi -= upgrade_cost
            #     clicks_per_second += upgrade_increase
            #     upgrade_cost = int(upgrade_cost * 1.5)
            #
            #     upgrade_button = pygame.draw.rect(screen, black, (300, 350, 200, 50))
            #     #pygame(f"улучшить ({upgrade_cost})", font, black, screen, 320, 360)


    timer += 1
    if timer > 600:
        save_game(score)
        save_game(money)
        save_game(enemy)
        timer=0
        
    if score <= 0:
        enemy += 1
        score = enemies[enemy]
        money += money2[moneyi]
        moneyi += 1
        # upgrade_increase += upgrade_cost[upgrade_button]

#отрисовка экрана
    screen.fill(white)
    #screen.blit (anim_main_char[0])
    text = font.render(f'score: {score}', True, black)
    screen.blit(text, (150,130))
    text = font.render(f'money: {money}', True, black)
    screen.blit(text, (150,200))
    pygame.draw.rect(screen,(0,0,0),upgrade_button)






    pygame.display.flip()

    pygame.time.Clock().tick(60)


