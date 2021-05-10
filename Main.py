import pygame
import time
import math

'''
print("\t Dati valorile celor 4 puncte intre 0 si 11 pe axa xOy: ")
p0_x = int(input("P0_x = "))
p0_y = int(input("P0_y = "))
p1_x = int(input("P1_x = "))
p1_y = int(input("P1_y = "))
p2_x = int(input("P2_x = "))
p2_y = int(input("P2_y = "))
p3_x = int(input("P3_x = "))
p3_y = int(input("P3_y = "))

'''
# Varianta de puncte:
p0_x = 2
p0_y = 10
p1_x = 1
p1_y = 1
p2_x = 10
p2_y = 1
p3_x = 8
p3_y = 10


pygame.init()
pygame.display.set_caption('Curbe Bezier')

screen_size = (1200, 800)
screen = pygame.display.set_mode(screen_size)

x, y = 500.0, 500.0
width, height = 70, 70
speed = 0.001

font = pygame.font.SysFont(None, 25)

position_text1 = font.render("P0", True, (255, 255, 255), (0, 0, 0))
position_text2 = font.render("P1", True, (255, 255, 255), (0, 0, 0))
position_text3 = font.render("P2", True, (255, 255, 255), (0, 0, 0))
position_text4 = font.render("P3", True, (255, 255, 255), (0, 0, 0))
position_textT = font.render("^", True, (0, 140, 255), (0, 0, 0))

text_rect1 = position_text1.get_rect()
text_rect2 = position_text2.get_rect()
text_rect3 = position_text3.get_rect()
text_rect4 = position_text4.get_rect()
text_rectT = position_textT.get_rect()

path_position = [(p0_x * 100, p0_y * 70), (p1_x * 100, p1_y * 70), (p2_x * 100, p2_y * 70), (p3_x * 100, p3_y * 70)]

t = 0
aux = 0

running = True

while running:
    screen.fill((0, 0, 0))
    pygame.time.delay(100)

    P0 = path_position[0]
    P1 = path_position[1]
    P2 = path_position[2]
    P3 = path_position[3]
    P4 = path_position[0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    while t < 1:
        t += speed
        aux += 1

        # calculul valorilor curbei in punctele t
        P0_x = pow((1-t), 3) * P0[0]
        P0_y = pow((1-t), 3) * P0[1]

        P1_x = 3 * t * pow((1-t), 2) * P1[0]
        P1_y = 3 * t * pow((1-t), 2) * P1[1]

        P2_x = 3 * pow(t, 2) * (1-t) * P2[0]
        P2_y = 3 * pow(t, 2) * (1 - t) * P2[1]

        P3_x = pow(t, 3) * P3[0]
        P3_y = pow(t, 3) * P3[1]

        p0_x = pow((1-t), 4) * P0[0]
        p0_y = pow((1-t), 4) * P0[1]

        p1_x = 4 * t * pow((1-t), 3) * P1[0]
        p1_y = 4 * t * pow((1-t), 3) * P1[1]

        p2_x = 6 * pow(t, 2) * pow((1-t), 2) * P2[0]
        p2_y = 6 * pow(t, 2) * pow((1-t), 2) * P2[0]

        p3_x = 4 * pow(t, 3) * (1-t) * P3[0]
        p3_y = 4 * pow(t, 3) * (1-t) * P3[1]

        p4_x = pow(t, 4) * P0[0]
        p4_y = pow(t, 4) * P0[1]

        formular = ((P0_x + P1_x + P2_x + P3_x), (P0_y + P1_y + P2_y + P3_y))
        formular_2 = ((p0_x + p1_x + p2_x + p3_x + p4_x), (p0_y + p1_y + p2_y + p3_y + p4_y))
        T = formular
        """
        # calcul ecuatia tangentei la curba in punctul t
        bt1_x = 3 * pow((1 - t), 2) * (P1_x - P0_x)
        bt1_y = 3 * pow((1 - t), 2) * (P1_y - P0_x)

        bt2_x = 6 * t * (1 - t) * (P2_x - P1_x)
        bt2_y = 6 * t * (1 - t) * (P2_y - P1_y)

        bt3_x = 3 * pow(t, 2) * (P3_x - P2_x)
        bt3_y = 3 * pow(t, 2) * (P3_y - P2_y)

        # vectorul normal
        bt = ((bt1_x + bt2_x + bt3_x), (bt1_y + bt2_y + bt3_y))

        # norma vectorului normal
        norma_bt = math.sqrt(pow(bt[0], 2) + pow(bt[1], 2))

        # versorul normalei
        nt = ((bt[0] / norma_bt), (bt[1] / norma_bt))

        # Curbura cu semn
        k_t = math.sqrt(pow(formular[0], 2) + pow(formular[1], 2))

        # clacul de scala
        s = (1/k_t)

        vector = ((abs(-s * k_t * nt[0]) * T[0]), (abs(-s * k_t * nt[1]) * T[1]))
        """
        x, y = formular
        a, b = formular_2

        text_rect1 = P0
        text_rect2 = P1
        text_rect3 = P2
        text_rect4 = P3
        test_rect1 = P4
        # text_rectT = vector

        screen.blit(position_text1, text_rect1)
        screen.blit(position_text2, text_rect2)
        screen.blit(position_text3, text_rect3)
        screen.blit(position_text4, text_rect4)

        pygame.draw.line(screen, (0, 255, 0), P0, P1, 1)
        pygame.draw.line(screen, (0, 255, 0), P2, P3, 1)
        # pygame.draw.line(screen, (0, 255, 0), P1, P2, 1)
        """
        if aux % 40 == 0:
            pygame.draw.line(screen, (0, 255, 255), T, vector, 1)
            screen.blit(position_textT, text_rectT)
        """
        pygame.draw.circle(screen, (255, 255, 255), (round(x), round(y)), 1)
        pygame.draw.circle(screen, (255, 140, 0), (round(a), round(b)), 1)
        pygame.display.update()

pygame.quit()
