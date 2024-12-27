import pygame
import ElectricFieldClasses
import sys

def main():
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((700, 700), 0, 32)
    screen.fill((255, 255, 255))

    click_mode = "positive"

    neg_charge_count = 0
    pos_charge_count = 0

    puck_start = (350, 350)

    puck = ElectricFieldClasses.Puck((350, 350))

    neg1 = ElectricFieldClasses.PointCharge(-1, (1000, 1000))
    neg2 = ElectricFieldClasses.PointCharge(-1, (1000, 1000))
    neg3 = ElectricFieldClasses.PointCharge(-1, (1000, 1000))

    pos1 = ElectricFieldClasses.PointCharge(1, (1000, 1000))
    pos2 = ElectricFieldClasses.PointCharge(1, (1000, 1000))
    pos3 = ElectricFieldClasses.PointCharge(1, (1000, 1000))

    play_area = pygame.Rect(85, 85, 530, 530)

    pos_charges = [pos1, pos2, pos3]
    neg_charges = [neg1, neg2, neg3]

    finished = False

    restart_button = ElectricFieldClasses.Button((10, 0), "dependencies/restart.png")

    level_indicator = ElectricFieldClasses.Button((200, 0), "dependencies/level_indicator.png")
    level_1_button = ElectricFieldClasses.Button((300, 0), "dependencies/level_1.png")
    level_2_button = ElectricFieldClasses.Button((350, 0), "dependencies/level_2.png")
    level_3_button = ElectricFieldClasses.Button((400, 0), "dependencies/level_3.png")

    positive_button = ElectricFieldClasses.Button((500, 0), "dependencies/positive_selected.png")
    negative_button = ElectricFieldClasses.Button((550, 0), "dependencies/negative.png")

    level_complete = ElectricFieldClasses.Button((200, 300), "dependencies/level_complete.png")
    finish = ElectricFieldClasses.Button((1000, 1000), "dependencies/finish.png")

    top_wall = ElectricFieldClasses.Obstacle((50, 50), (0, 255, 0), 600, 10)
    left_wall = ElectricFieldClasses.Obstacle((0, 50), (0, 255, 0), 60, 650)
    right_wall = ElectricFieldClasses.Obstacle((640, 50), (0, 255, 0), 60, 650)
    bottom_wall = ElectricFieldClasses.Obstacle((50, 640), (0, 255, 0), 600, 60)

    level_1_obstacle_1 = ElectricFieldClasses.Obstacle((50, 50), (0, 255, 0), 200, 400)
    level_1_obstacle_2 = ElectricFieldClasses.Obstacle((500, 300), (0, 255, 0), 200, 400)

    level_2_obstacle_1 = ElectricFieldClasses.Obstacle((0, 200), (0, 255, 0), 500, 30)
    level_2_obstacle_2 = ElectricFieldClasses.Obstacle((200, 400), (0, 255, 0), 500, 30)

    level_3_obstacle_1 = ElectricFieldClasses.Obstacle((300, 50), (0, 255, 0), 100, 530)

    Obstacles = [top_wall, bottom_wall, left_wall, right_wall]

    Buttons = [restart_button, level_indicator, level_1_button, level_2_button, level_3_button, positive_button, negative_button, finish]


    charges = [pos1, pos2, pos3, neg1, neg2, neg3]
    
    while True:
        screen.fill((255,255,255))

        #----------------------------------------------------------------------------------

        puck.display(screen)

        puck.updateVelocity(5)

        for Button in Buttons:
            Button.blit(screen)

        for Obstacle in Obstacles:
            Obstacle.display(screen)

        for Obstacle in Obstacles:
            puck.collideCheck(Obstacle)

        for i in range(neg_charge_count):
            neg_charges[i].display(screen)
            neg_charges[i].exertForce(puck)

        for i in range(pos_charge_count):
            pos_charges[i].display(screen)
            pos_charges[i].exertForce(puck)

        if pygame.Rect.colliderect(puck.rect, finish.rect):
            finished = True

        if finished:
            level_complete.blit(screen)

        puck.updateAttributes(5)


        #-----------------------------------------------------------------------------------

        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pygame.Rect.collidepoint(play_area, pos):
                    if click_mode == "negative":
                        if neg_charge_count < 3:
                            neg_charge_count += 1
                            neg_charges[neg_charge_count - 1].position = pos
                    if click_mode == "positive":
                        if pos_charge_count < 3:
                            pos_charge_count += 1
                            pos_charges[pos_charge_count - 1].position = pos
                if pygame.Rect.collidepoint(restart_button.rect, pos):
                    finished = False
                    puck.resetAttributes(puck_start)
                    for i in range(neg_charge_count):
                        neg_charges[i].position = (1000, 1000)
                    for i in range(pos_charge_count):
                        pos_charges[i].position = (1000, 1000)
                    neg_charge_count = 0
                    pos_charge_count = 0
                if pygame.Rect.collidepoint(positive_button.rect, pos):
                    click_mode = "positive"
                    positive_button.image = "dependencies/positive_selected.png"
                    negative_button.image = "dependencies/negative.png"
                if pygame.Rect.collidepoint(negative_button.rect, pos):
                    click_mode = "negative"
                    positive_button.image = "dependencies/positive.png"
                    negative_button.image = "dependencies/negative_selected.png"
                if pygame.Rect.collidepoint(level_1_button.rect, pos):
                    finished = False
                    Obstacles = [top_wall, bottom_wall, left_wall, right_wall, level_1_obstacle_1, level_1_obstacle_2]
                    finish.position = (500, 150)
                    puck_start = (150, 550)
                    puck.resetAttributes(puck_start)
                    for i in range(neg_charge_count):
                        neg_charges[i].position = (1000, 1000)
                    for i in range(pos_charge_count):
                        pos_charges[i].position = (1000, 1000)
                    neg_charge_count = 0
                    pos_charge_count = 0
                if pygame.Rect.collidepoint(level_2_button.rect, pos):
                    finished = False
                    Obstacles = [top_wall, bottom_wall, left_wall, right_wall, level_2_obstacle_1, level_2_obstacle_2]
                    finish.position = (500, 500)
                    puck_start = (150, 130)
                    puck.resetAttributes(puck_start)
                    for i in range(neg_charge_count):
                        neg_charges[i].position = (1000, 1000)
                    for i in range(pos_charge_count):
                        pos_charges[i].position = (1000, 1000)
                    neg_charge_count = 0
                    pos_charge_count = 0
                if pygame.Rect.collidepoint(level_3_button.rect, pos):
                    finished = False
                    Obstacles = [top_wall, bottom_wall, left_wall, right_wall, level_3_obstacle_1]
                    finish.position = (500, 150)
                    puck_start = (175, 175)
                    puck.resetAttributes(puck_start)
                    for i in range(neg_charge_count):
                        neg_charges[i].position = (1000, 1000)
                    for i in range(pos_charge_count):
                        pos_charges[i].position = (1000, 1000)
                    neg_charge_count = 0
                    pos_charge_count = 0


main()