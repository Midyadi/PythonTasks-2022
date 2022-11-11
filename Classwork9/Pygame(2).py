import pygame
from pygame.draw import circle
from random import randint
from math import cos, sin, radians

pygame.init()

# Настройка экрана
FPS = 100
display_size = (900, 600)
screen = pygame.display.set_mode(display_size)
pygame.display.set_caption('Catch me if you can!')

# Настройка размеров шаров
max_figure_size = 80
min_figure_size = 30

# Настройка цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
VIOLET = (127, 0, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GOLDEN = (212, 175, 55)
COLORS = [RED, BLUE, VIOLET, GREEN, MAGENTA, CYAN]


# Определение необходимых функций
def new_ball():
    """
    Создаёт новый шарик со случайным радиусом в случайном месте

    Returns:
        params - возвращает параметры созданного шара:
            color - цвет шара
            [x_b, y_b] - начальные иксовая и игрековая координаты центра шара
            r_b - радиус шара
            alpha - угол, задающий направление движения
        """

    x_b = randint(max_figure_size, display_size[0] - max_figure_size)
    y_b = randint(max_figure_size, display_size[1] - max_figure_size)
    r_b = randint(min_figure_size, max_figure_size)
    alpha = randint(0, 359)
    color = COLORS[randint(0, 5)]
    params = [color, [x_b, y_b], r_b, alpha]
    return params


def new_snitch():
    """
    Создаёт особую мишень - золотой "снитч" - в случайном месте.
    Снитч меньше любого шара не менее чем 3 раза и движется в 3 раза быстрее
    За поимку снитча даётся 3 очка

    Returns:
        params - возвращает параметры созданного снитча:
            color - цвет снитча
            [x_b, y_b] - начальные иксовая и игрековая координаты центра снитча
            r_b - радиус снитча
            alpha - угол, задающий направление движения
        """

    x_s = randint(min_figure_size // 3, display_size[0] - min_figure_size // 3)
    y_s = randint(min_figure_size // 3, display_size[1] - min_figure_size // 3)
    r_s = min_figure_size // 3
    alpha = randint(0, 359)
    color = GOLDEN
    params = [color, [x_s, y_s], r_s, alpha]
    return params


def get_starting_objects(object_count=3):
    """
    Создаёт список первых "obj_count" ШАРОВ (снитч не может появиться на старте) для отрисовки

    Args:
        object_count: количество шаров, отрисовываемых на экране

    Returns:
        starting objs: список шаров для отрисовки на экране
        """

    starting_objects = []
    for _ in range(object_count):
        ball = new_ball()
        starting_objects.append(ball)
    return starting_objects


def objects_draw():
    """
    Рисует объекты (шары и возможно снитч) из списка на экране
    Ничего не принимает и не возвращает
        """

    for thing in objects_on_screen:
        circle(screen, *thing[:-1])


def balls_list():
    """
    Возвращает лист УЖЕ отрисованных объектов

    Returns:
        objects_on_screen - список шаров
        """

    return objects_on_screen


def is_hit(x_o, y_o, r_o):
    """
    Проверяет, есть ли попадание по объекту

    Args:
        x_o - иксовая координата центра объекта
        y_o - игрековая координата центра объекта
        r_o - радиус объекта

    Returns:
        True, если клик мыши произошёл внутри шарика,
        Else иначе
        """

    x_cl, y_cl = pygame.mouse.get_pos()
    return (x_o - x_cl) ** 2 + (y_o - y_cl) ** 2 <= r_o ** 2


# В данной версии игры объекты отскакивают от стенок реалистично,
# поэтому следующая функция используется только при создании нового объекта
def get_phi(min_phi=0, max_phi=359):
    """
    Возвращает случайный угол в градусах

    Args:
        min_phi: минимальный угол
        max_phi: максимальный угол

    Returns:
        phi: угол, задающий новое направление движения шара
    """

    phi = randint(min_phi, max_phi)
    return phi


def is_close_to_wall(something):
    """
    Проверяет, сталкивается ли объект 'something' со стеной (краем экрана)
    и изменяет направление его движения согласно закону отражения

    Args:
        something: объект, который проверяем на столкновение со стеной

    Функция ничего не возвращает
     """

    if something[1][0] + cos(radians(something[3])) - something[2] < 0:
        something[3] = 180 - something[3]
    elif something[1][0] + cos(radians(something[3])) + something[2] > display_size[0]:
        something[3] = 180 - something[3]
    elif something[1][1] + sin(radians(something[3])) + something[2] > display_size[1]:
        something[3] = -something[3]
    elif something[1][1] + sin(radians(something[3])) - something[2] < 0:
        something[3] = -something[3]


def moving_objects():
    """
    Перемещает объекты в направлении, заложенном в параметрах объекта.
    Функция ничего не принимает и не возвращает
    """

    for j in range(len(objects_on_screen)):
        is_close_to_wall(objects_on_screen[j])
        x_move = 100 / FPS * cos(radians(objects_on_screen[j][3]))  # Множитель 100/FPS нужен, чтобы для любого FPS
        y_move = 100 / FPS * sin(radians(objects_on_screen[j][3]))  # скорость перемещения объекта была одинаковой
        if objects_on_screen[j][2] >= min_figure_size:  # Если объект - это шар, а не снитч
            objects_on_screen[j][1][0] += x_move
            objects_on_screen[j][1][1] += y_move
        else:  # Если объект - это снитч
            objects_on_screen[j][1][0] += x_move * 3
            objects_on_screen[j][1][1] += y_move * 3


pygame.display.update()
clock = pygame.time.Clock()
finished = False
escape = False

# Счётчики попаданий и промахов
hit_counter = 0
snitch_counter = 0
ball_counter = 0
miss_counter = 0

# Счётчик для заливки фона на несколько кадров при промахе или поимке снитча (при больших FPS)
# При больших FPS заливка только одного кадра недостаточна
miss_fill = -1
snitch_fill = -1

objects_on_screen = get_starting_objects()

while (not finished) and (not escape):
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                escape = True
        elif event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for obj in reversed(objects_on_screen):  # Чтобы при наложении объектов попадание считалось по верхнему
                x, y, r = obj[1][0], obj[1][1], obj[2]
                if is_hit(x, y, r):
                    if r >= min_figure_size:  # Если объект - это шар
                        hit_counter += 1
                        ball_counter += 1
                    else:  # Если объект - это снитч
                        hit_counter += 3
                        snitch_counter += 1
                        snitch_fill = FPS // 20
                    decider = randint(0, 9)  # Вероятность появления снитча -  0,1
                    if decider == 0 and all(body[2] >= min_figure_size for body in objects_on_screen):
                        # Второе условие не допускает несколько снитчей одновременно на экране
                        new_object = new_snitch()
                    else:
                        new_object = new_ball()
                    objects_on_screen[objects_on_screen.index(obj)] = new_object
                    break
            else:
                miss_counter += 1
                screen.fill(RED)
                miss_fill = FPS // 20
    if miss_fill >= 0:
        miss_fill -= 1
    if snitch_fill >= 0:
        snitch_fill -= 1
    moving_objects()
    objects_draw()
    pygame.display.update()
    if miss_fill >= 0:
        screen.fill(RED)
    elif snitch_fill >= 0:
        screen.fill(GOLDEN)
    else:
        screen.fill(BLACK)

if finished:
    pygame.quit()
elif escape:
    escape = False
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    total = font.render("Total:", True, WHITE)
    points = font.render(f'You got {hit_counter} points', True, WHITE)
    hit = font.render(f'You hit {ball_counter} balls and {snitch_counter} snitches', True, WHITE)
    miss = font.render(f'You missed {miss_counter} times', False, WHITE)
    if (ball_counter + snitch_counter + miss_counter) != 0:
        accuracy_number = round((ball_counter + snitch_counter) / (ball_counter + snitch_counter + miss_counter) * 100, 2)
    else:
        accuracy_number = 0
    accuracy = font.render(f'Your accuracy was '
                           f'{accuracy_number}%',
                           True, WHITE)
    texts = (total, points, hit, miss, accuracy)
    for i in range(len(texts)):
        screen.blit(texts[i], (display_size[0] // 2, display_size[1] // 2 + 40 * i))
        pygame.display.update()
    while (not finished) and (not escape):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                finished = True
pygame.quit()
