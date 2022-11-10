import math
import random
import pygame

FPS = 100

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (138, 127, 142)
COLORS = [BLUE, YELLOW, GREEN, MAGENTA, RED]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, x=20, y=550):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        Определяются положением пушки
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = random.choice(COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, сил гравитаций и сопротивления среды,
        действующей на мяч
        """

        self.x += self.vx * 50 / FPS
        self.y -= self.vy * 50 / FPS
        self.vy -= 0.9
        if self.vx >= 0:
            self.vx -= 0.001 * self.vx ** 2
        else:
            self.vx += 0.001 * self.vx ** 2
        if self.vy >= 0:
            self.vy -= 0.001 * self.vy ** 2
        else:
            self.vy += 0.001 * self.vy ** 2

    def draw(self):
        """ Рисует мяч-снаряд"""
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hit_test(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= (self.r + obj.r) ** 2

    def wall_hit(self):
        """Проверяет, есть ли столкновение с одной из 3х стен (кроме нижней) и сеняет направление движения снаряда
        с учётом потерь энергии при столкновении"""
        if self.x + self.vx - self.r < 0:
            self.vx = -self.vx + 0.002 * self.vx
        elif self.y - self.vy - self.r < 0:
            self.vy = - self.vy - 0.002 * self.vy
        elif self.x + self.vx + self.r > WIDTH:
            self.vx = -self.vx - 0.002 * self.vx

    def is_gone(self):
        """Проверяет, не упал ли снаряд вниз за пределы экрана."""
        return self.y - self.vy - 2 * self.r > HEIGHT

    def gun_hit(self, obj):
        """Проверяет, врезалась ли мишень в пушку"""
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) >= ((self.x + self.vx - obj.x) ** 2 +
                                                               (self.y - self.vy - obj.y) ** 2):
            return ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= (self.r + obj.r) ** 2
        else:
            return False


class Gun:
    def __init__(self):
        """Конструктор класса Gun"""
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 0
        self.color = GREY
        self.x = 20
        self.y = 550
        self.r = 10
        self.gun_l = 5

    def fire2_start(self):
        """Активирует апгрейд пушки."""
        self.f2_on = 1

    def fire2_end(self):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullets
        bullets += 1
        new_ball = Ball()
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self):
        """Прицеливание. Зависит от положения мыши."""
        if event and event.pos[0] != 20:
            self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 20))
        if self.f2_on:
            self.color = self.color
        else:
            self.color = GREY

    def draw(self):
        """Рисует 'базу' пушки - круг и ствол - прямоугольник"""
        pygame.draw.polygon(self.screen, self.color,
                            [(self.x - math.sin(self.an) * self.gun_l, self.y + math.cos(self.an) * self.gun_l),
                             (self.x + math.sin(self.an) * self.gun_l, self.y - math.cos(self.an) * self.gun_l), (
                                 self.x + math.sin(self.an) * self.gun_l + math.cos(self.an) * self.f2_power / 4,
                                 self.y - math.cos(self.an) * self.gun_l + math.sin(self.an) * self.f2_power / 4),
                             (
                                 self.x - math.sin(self.an) * self.gun_l + math.cos(self.an) * self.f2_power / 4,
                                 self.y + math.cos(self.an) * self.gun_l + math.sin(self.an) * self.f2_power / 4)])
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def power_up(self):
        """Увеличивает начальную скорость снаряда"""
        if self.f2_on:
            if self.f2_power < FPS * 2:
                self.f2_power += 1
                if self.color[0] <= 250 and self.color[1] >= 5 and self.color[2] >= 5:
                    self.color = (self.color[0] + GREY[0] / (FPS * 2), self.color[1] - GREY[1] / (FPS * 2),
                                  self.color[2] - GREY[2] / (FPS * 2))
        else:
            self.color = GREY


class Target:
    def __init__(self):
        """Конструктор класса Target"""
        self.screen = screen
        self.points = 0
        self.x = random.randint(30, 780)
        self.y = random.randint(30, 550)
        self.r = random.randint(10, 20)
        self.vx = random.randint(0, 3)
        self.vy = random.randint(0, 3)
        self.color = CYAN

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = random.randint(30, 780)
        self.y = random.randint(30, 550)
        self.r = random.randint(10, 20)
        self.vx = random.randint(0, 3)
        self.vy = random.randint(0, 3)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        """Рисует мишень"""
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def move(self):
        """Отвечает за движение мишени"""
        self.x += self.vx * 50 / FPS
        self.y -= self.vy * 50 / FPS

    def wall_hit(self):
        """Проверяет, есть ли столкновение с одной из стен"""
        if self.x + self.vx - self.r < 0:
            self.vx = -self.vx
        elif self.y - self.vy - self.r < 0:
            self.vy = - self.vy
        elif self.x + self.vx + self.r > WIDTH:
            self.vx = -self.vx
        elif self.y - self.vy + self.r > HEIGHT:
            self.vy = -self.vy

    def gun_hit(self, obj):
        """Проверяет, врезался ли снаряд в пушку"""
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) > (
                (self.x + self.vx - obj.x) ** 2 + (self.y + self.vy - obj.y) ** 2):
            return ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= (self.r + obj.r) ** 2
        else:
            return False


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gun Fight')
bullets = 0
score = 0
balls = []

clock = pygame.time.Clock()
gun = Gun()
target1 = Target()
target2 = Target()
finished = False

while not finished:
    screen.fill(BLACK)
    gun.draw()
    target1.draw()
    target2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end()
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting()

    target1.move()
    target2.move()
    if target1.gun_hit(gun) or target2.gun_hit(gun):
        finished = True
    target1.wall_hit()
    target2.wall_hit()
    for b in balls:
        b.wall_hit()
        b.move()
        if b.gun_hit(gun):
            finished = True
        if b.is_gone():
            del balls[balls.index(b)]
        if b.hit_test(target1):
            score += 1
            target1.hit()
            target1.new_target()
        if b.hit_test(target2):
            target2.hit()
            score += 1
            target2.new_target()
    gun.power_up()


print(f"You scored {score} points")
if bullets:
    print(f"Your accuracy was {round(score/bullets*100, 2)}%")
pygame.quit()
