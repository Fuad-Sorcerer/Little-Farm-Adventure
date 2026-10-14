
import pygame
import random
from pathlib import Path

pygame.init()

WIDTH = 1000
HEIGHT = 700
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Little Farm Adventure")

clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 19, bold=True)
small_font = pygame.font.SysFont("arial", 16)
title_font = pygame.font.SysFont("arial", 29, bold=True)

rng = random.Random(15)

BASE = Path(__file__).resolve().parent / "Assets"

def find_asset(folder, name):
    folder = BASE / folder

    for file in sorted(folder.glob("*.png")):
        if file.stem.lower().startswith(name.lower()):
            return str(file)

    raise FileNotFoundError(
        f"Asset not found: {name} in {folder}"
    )


def get_sprite(folder, name, area, size):
    sheet = pygame.image.load(
        find_asset(folder, name)
    ).convert_alpha()

    image = sheet.subsurface(area)

    return pygame.transform.scale(image, size)


def load_animation(folder, name, cols, rows, size):
    sheet = pygame.image.load(
        find_asset(folder, name)
    ).convert_alpha()

    fw = sheet.get_width() // cols
    fh = sheet.get_height() // rows

    animations = []

    for row in range(rows):
        frames = []

        for col in range(cols):
            frame = sheet.subsurface(
                col * fw,
                row * fh,
                fw,
                fh
            )

            frame = pygame.transform.scale(
                frame, (size, size)
            )

            frames.append(frame)

        animations.append(frames)

    return animations

idle = load_animation(
    "Character", "Idle", 4, 3, 64
)

walk = load_animation(
    "Character", "Walk", 6, 3, 64
)

house = get_sprite(
    "Objects", "House",
    (148, 0, 76, 88),
    (170, 195)
)

tree = get_sprite(
    "Objects", "Maple Tree",
    (94, 0, 36, 48),
    (78, 104)
)

small_tree = get_sprite(
    "Objects", "Maple Tree",
    (69, 0, 25, 48),
    (54, 104)
)

chest = get_sprite(
    "Objects", "chest",
    (0, 0, 32, 16),
    (48, 24)
)

stone = get_sprite(
    "Objects", "Road",
    (0, 0, 16, 16),
    (32, 32)
)

crop_image = get_sprite(
    "Objects", "Spring Crops",
    (64, 16, 16, 16),
    (30, 30)
)

female_cow = load_animation(
    "Farm Animals", "Female Cow", 4, 3, 48
)

male_cow = load_animation(
    "Farm Animals", "Male Cow", 4, 3, 48
)

red_chicken = load_animation(
    "Farm Animals", "Chicken Red", 4, 2, 36
)

green_chicken = load_animation(
    "Farm Animals", "Chicken Blonde", 4, 2, 36
)

baby_chicken = load_animation(
    "Farm Animals", "Baby Chicken Yellow", 4, 3, 28
)

HOUSE_POS = (45, 65)
CHEST_POS = (64, 270)

SHOP = pygame.Rect(125, 320, 78, 48)

COW_PEN = pygame.Rect(270, 65, 290, 195)
CHICKEN_PEN = pygame.Rect(590, 65, 345, 195)

FIELD_RECTS = [
    pygame.Rect(345, 405, 250, 95),
    pygame.Rect(660, 405, 260, 95),
    pygame.Rect(345, 540, 250, 95)
]

# Main roads
ROADS = [
    pygame.Rect(225, 300, 725, 45),
    pygame.Rect(225, 300, 60, 380),
    pygame.Rect(285, 350, 660, 18)
]

# NEW - ANIMAL GATE CONNECTION ROADS
COW_ROAD = pygame.Rect(
    COW_PEN.centerx - 26,
    COW_PEN.bottom,
    52,
    42
)

CHICKEN_ROAD = pygame.Rect(
    CHICKEN_PEN.centerx - 26,
    CHICKEN_PEN.bottom,
    52,
    42
)

TREES = [
    (24, 385),
    (52, 540),
    (930, 535)
]

SMALL_TREES = [
    (5, 290),
    (930, 340),
    (155, 570)
]


GATE_WIDTH = 62


def gate_rect(rect, side="top"):
    if side == "bottom":
        y = rect.bottom - 3
    else:
        y = rect.top - 9

    return pygame.Rect(
        rect.centerx - GATE_WIDTH // 2,
        y,
        GATE_WIDTH,
        18
    )


def fence_walls(rect, opened=False, side="top"):
    left = rect.left - 9
    right = rect.right + 9
    top = rect.top - 9
    bottom = rect.bottom - 3

    gate = gate_rect(rect, side)

    walls = [
        pygame.Rect(
            left, top, 12,
            rect.height + 20
        ),
        pygame.Rect(
            rect.right - 3, top,
            12, rect.height + 20
        )
    ]

    if side == "bottom":
        # Solid top
        walls.append(
            pygame.Rect(
                left, top,
                rect.width + 18, 12
            )
        )

        if opened:
            walls.append(
                pygame.Rect(
                    left, bottom,
                    gate.left - left, 12
                )
            )

            walls.append(
                pygame.Rect(
                    gate.right, bottom,
                    right - gate.right, 12
                )
            )
        else:
            walls.append(
                pygame.Rect(
                    left, bottom,
                    rect.width + 18, 12
                )
            )

    else:
        # Solid bottom
        walls.append(
            pygame.Rect(
                left, bottom,
                rect.width + 18, 12
            )
        )

        if opened:
            walls.append(
                pygame.Rect(
                    left, top,
                    gate.left - left, 12
                )
            )

            walls.append(
                pygame.Rect(
                    gate.right, top,
                    right - gate.right, 12
                )
            )
        else:
            walls.append(
                pygame.Rect(
                    left, top,
                    rect.width + 18, 12
                )
            )

    return walls


def horizontal_fence(x1, x2, y):
    if x2 <= x1:
        return

    pygame.draw.rect(
        screen, (79, 43, 28),
        (x1, y + 7, x2 - x1, 8)
    )

    pygame.draw.rect(
        screen, (162, 94, 52),
        (x1, y + 8, x2 - x1, 4)
    )

    for x in range(x1, x2 + 1, 32):
        pygame.draw.rect(
            screen, (68, 38, 26),
            (x - 5, y, 11, 29)
        )

        pygame.draw.rect(
            screen, (170, 98, 54),
            (x - 3, y + 2, 7, 25)
        )


def vertical_fence(x, y1, y2):
    pygame.draw.rect(
        screen, (75, 42, 27),
        (x + 7, y1, 9, y2 - y1)
    )

    pygame.draw.rect(
        screen, (164, 92, 48),
        (x + 9, y1, 4, y2 - y1)
    )

    for y in range(y1, y2 + 1, 32):
        pygame.draw.rect(
            screen, (65, 37, 26),
            (x, y - 5, 27, 11)
        )

        pygame.draw.rect(
            screen, (170, 98, 54),
            (x + 2, y - 3, 23, 7)
        )


def draw_fence(rect, opened=False, side="top"):
    left = rect.x - 8
    right = rect.right + 8

    top = rect.y - 26
    bottom = rect.bottom + 2

    gate = gate_rect(rect, side)

    if side == "bottom":
        # Top fence fully closed
        horizontal_fence(left, right, top)

        # Bottom fence with gate
        horizontal_fence(left, gate.left, bottom)
        horizontal_fence(gate.right, right, bottom)

        if not opened:
            pygame.draw.rect(
                screen, (105, 60, 36),
                (gate.left, bottom + 7, gate.width, 8)
            )

            pygame.draw.rect(
                screen, (180, 112, 61),
                (gate.left + 2, bottom + 9,
                 gate.width - 4, 3)
            )

        else:
            pygame.draw.rect(
                screen, (220, 190, 109),
                (gate.left + 3, bottom + 21,
                 gate.width - 6, 3)
            )

    else:
        # Top fence with gate
        horizontal_fence(left, gate.left, top)
        horizontal_fence(gate.right, right, top)

        if not opened:
            pygame.draw.rect(
                screen, (105, 60, 36),
                (gate.left, top + 7, gate.width, 8)
            )

            pygame.draw.rect(
                screen, (180, 112, 61),
                (gate.left + 2, top + 9,
                 gate.width - 4, 3)
            )

        else:
            pygame.draw.rect(
                screen, (220, 190, 109),
                (gate.left + 3, rect.y - 6,
                 gate.width - 6, 3)
            )

        horizontal_fence(left, right, bottom)

    vertical_fence(
        left, top + 10, bottom + 10
    )

    vertical_fence(
        right - 26, top + 10, bottom + 10
    )

class Animal:
    def __init__(
        self, frames, x, y, pen, product=None
    ):
        self.frames = frames
        self.x = float(x)
        self.y = float(y)

        self.pen = pen
        self.product = product

        self.size = frames[0][0].get_width()

        self.direction = rng.choice([-1, 1])
        self.speed = rng.uniform(0.25, 0.65)

        self.frame = 0.0
        self.timer = rng.randint(35, 100)
        self.moving = False

        self.last_collected = -30000

    def update(self):
        self.timer -= 1

        if self.timer <= 0:
            self.timer = rng.randint(35, 100)

            self.direction = rng.choice([-1, 1])

            self.moving = rng.choice(
                [True, True, False]
            )

        if self.moving:
            nx = self.x + self.direction * self.speed

            minimum = self.pen.x + 35
            maximum = (
                self.pen.right - self.size - 20
            )

            if minimum <= nx <= maximum:
                self.x = nx
            else:
                self.direction *= -1

            self.frame = (self.frame + 0.08) % 4

        else:
            self.frame = 0

    def draw(self):
        image = self.frames[0][int(self.frame)]

        if self.direction < 0:
            image = pygame.transform.flip(
                image, True, False
            )

        screen.blit(
            image,
            (round(self.x), round(self.y))
        )

    def center(self):
        return pygame.Vector2(
            self.x + self.size / 2,
            self.y + self.size / 2
        )


animals = [
    Animal(
        female_cow, 315, 125, COW_PEN, "milk"
    ),
    Animal(
        male_cow, 405, 125, COW_PEN
    ),
    Animal(
        female_cow, 485, 125, COW_PEN, "milk"
    ),
    Animal(
        male_cow, 350, 185, COW_PEN
    ),
    Animal(
        female_cow, 450, 185, COW_PEN, "milk"
    ),

    Animal(
        red_chicken, 635, 110,
        CHICKEN_PEN, "eggs"
    ),
    Animal(
        green_chicken, 710, 110,
        CHICKEN_PEN, "eggs"
    ),
    Animal(
        red_chicken, 785, 110,
        CHICKEN_PEN, "eggs"
    ),
    Animal(
        green_chicken, 860, 110,
        CHICKEN_PEN, "eggs"
    ),
    Animal(
        baby_chicken, 655, 185, CHICKEN_PEN
    ),
    Animal(
        red_chicken, 730, 185,
        CHICKEN_PEN, "eggs"
    ),
    Animal(
        green_chicken, 805, 185,
        CHICKEN_PEN, "eggs"
    ),
    Animal(
        baby_chicken, 865, 185, CHICKEN_PEN
    )
]

class Crop:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.planted = True
        self.planted_at = -12000

    def ready(self, now):
        return (
            self.planted
            and now - self.planted_at >= 8500
        )

    def draw(self, now):
        pygame.draw.rect(
            screen, (143, 100, 60),
            (self.x, self.y, 34, 27)
        )

        if self.ready(now):
            screen.blit(
                crop_image,
                (self.x + 2, self.y - 4)
            )

        elif self.planted:
            progress = min(
                1.0,
                max(
                    0,
                    (now - self.planted_at) / 8500
                )
            )

            height = 5 + int(15 * progress)

            pygame.draw.line(
                screen, (50, 109, 39),
                (self.x + 17, self.y + 23),
                (self.x + 17,
                 self.y + 23 - height),
                3
            )

            pygame.draw.ellipse(
                screen, (79, 170, 62),
                (self.x + 17,
                 self.y + 17 - height, 9, 7)
            )


class Field:
    def __init__(self, rect):
        self.rect = rect
        self.open = False

        self.crops = [
            Crop(
                rect.x + 20 + c * 42,
                rect.y + 11 + r * 35
            )
            for r in range(2)
            for c in range(5)
        ]

    def draw(self, now):
        pygame.draw.rect(
            screen, (105, 74, 46),
            self.rect
        )

        for crop in self.crops:
            crop.draw(now)

        draw_fence(
            self.rect, self.open, "top"
        )


fields = [
    Field(rect) for rect in FIELD_RECTS
]

cow_gate_open = False
chicken_gate_open = False

inventory = {
    "crops": 0,
    "seeds": 20,
    "coins": 0,
    "milk": 0,
    "eggs": 0
}

storage = {
    "crops": 0,
    "milk": 0,
    "eggs": 0
}

menu = None

message = "Welcome to Little Farm Adventure!"
message_until = 0

player_x = 245.0
player_y = 345.0

direction = "down"
animation_index = 0.0

COOLDOWN = 20000

def notify(text, now):
    global message, message_until

    message = text
    message_until = now + 2500


def player_feet(x=None, y=None):
    if x is None:
        x = player_x

    if y is None:
        y = player_y

    return pygame.Rect(
        int(x + 22),
        int(y + 48),
        20,
        12
    )


def player_center():
    return pygame.Vector2(
        player_feet().center
    )


static_obstacles = [
    pygame.Rect(70, 214, 130, 47),

    pygame.Rect(
        CHEST_POS[0] + 5,
        CHEST_POS[1] + 7,
        38,
        16
    ),

    SHOP
]

for x, y in TREES:
    static_obstacles.append(
        pygame.Rect(
            x + 26, y + 80, 26, 20
        )
    )

for x, y in SMALL_TREES:
    static_obstacles.append(
        pygame.Rect(
            x + 17, y + 80, 20, 20
        )
    )


def can_move(x, y):
    feet = player_feet(x, y)

    for obstacle in static_obstacles:
        if feet.colliderect(obstacle):
            return False

    pen_walls = (
        fence_walls(
            COW_PEN, cow_gate_open, "bottom"
        )
        +
        fence_walls(
            CHICKEN_PEN,
            chicken_gate_open,
            "bottom"
        )
    )

    for wall in pen_walls:
        if feet.colliderect(wall):
            return False

    for field in fields:
        for wall in fence_walls(
            field.rect, field.open, "top"
        ):
            if feet.colliderect(wall):
                return False

    return True

def distance_to(rect):
    return player_center().distance_to(
        pygame.Vector2(rect.center)
    )


def near_chest():
    return distance_to(
        pygame.Rect(
            CHEST_POS[0],
            CHEST_POS[1],
            48,
            24
        )
    ) < 80


def near_shop():
    return distance_to(SHOP) < 90


def nearest_crop():
    choices = []

    for field in fields:
        if not field.open:
            continue

        for crop in field.crops:
            distance = player_center().distance_to(
                (crop.x + 17, crop.y + 14)
            )

            if distance < 48:
                choices.append(
                    (distance, crop)
                )

    if choices:
        return min(
            choices,
            key=lambda item: item[0]
        )[1]

    return None


def nearest_animal():
    choices = []

    for animal in animals:
        if animal.product is None:
            continue

        distance = player_center().distance_to(
            animal.center()
        )

        if distance < 65:
            choices.append(
                (distance, animal)
            )

    if choices:
        return min(
            choices,
            key=lambda item: item[0]
        )[1]

    return None


def switch_gate(now):
    global cow_gate_open
    global chicken_gate_open

    candidates = [
        (
            distance_to(
                gate_rect(COW_PEN, "bottom")
            ),
            "cow"
        ),

        (
            distance_to(
                gate_rect(CHICKEN_PEN, "bottom")
            ),
            "chicken"
        )
    ]

    for i, field in enumerate(fields):
        candidates.append(
            (
                distance_to(
                    gate_rect(field.rect, "top")
                ),
                i
            )
        )

    nearby = [
        item for item in candidates
        if item[0] < 66
    ]

    if not nearby:
        notify(
            "Move closer to a gate.",
            now
        )
        return

    _, selected = min(
        nearby,
        key=lambda item: item[0]
    )

    if selected == "cow":
        rect = COW_PEN
        side = "bottom"
        opened = cow_gate_open

    elif selected == "chicken":
        rect = CHICKEN_PEN
        side = "bottom"
        opened = chicken_gate_open

    else:
        rect = fields[selected].rect
        side = "top"
        opened = fields[selected].open

    gate = gate_rect(rect, side)

    if opened and player_feet().colliderect(gate):
        notify(
            "Move away from the gate first!",
            now
        )
        return

    new_state = not opened

    if selected == "cow":
        cow_gate_open = new_state

    elif selected == "chicken":
        chicken_gate_open = new_state

    else:
        fields[selected].open = new_state

    notify(
        "Gate opened!" if new_state
        else "Gate closed!",
        now
    )


def draw_shop():
    x, y, w, h = SHOP

    pygame.draw.rect(
        screen, (85, 50, 32),
        (x, y + 18, w, h - 18),
        border_radius=4
    )

    pygame.draw.rect(
        screen, (205, 153, 90),
        (x - 4, y + 13, w + 8, 15),
        border_radius=3
    )

    pygame.draw.rect(
        screen, (71, 46, 30),
        (x + 5, y - 20, w - 10, 28),
        border_radius=4
    )

    label = small_font.render(
        "SHOP", True, (255, 210, 90)
    )

    screen.blit(
        label,
        (
            x + w // 2 - label.get_width() // 2,
            y - 15
        )
    )


blocked = [
    COW_PEN.inflate(55, 55),
    CHICKEN_PEN.inflate(55, 55),

    *[
        rect.inflate(90, 90)
        for rect in FIELD_RECTS
    ],

    *[
        rect.inflate(20, 20)
        for rect in ROADS
    ],

    COW_ROAD.inflate(10, 10),
    CHICKEN_ROAD.inflate(10, 10),

    pygame.Rect(35, 50, 195, 245),
    SHOP.inflate(20, 20)
]

decorations = []

for _ in range(230):
    x = rng.randrange(12, WIDTH - 12)
    y = rng.randrange(25, HEIGHT - 12)

    point = pygame.Rect(x, y, 6, 6)

    if not any(
        point.colliderect(rect)
        for rect in blocked
    ):
        decorations.append(
            (x, y, rng.randrange(4))
        )


def draw_animal_roads():
    color = (188, 157, 108)

    # Cow Farm gate road
    pygame.draw.rect(
        screen,
        color,
        COW_ROAD
    )

    # Chicken Farm gate road
    pygame.draw.rect(
        screen,
        color,
        CHICKEN_ROAD
    )

    # Decorative stones on roads
    for road in [COW_ROAD, CHICKEN_ROAD]:
        center_x = road.centerx - 16

        screen.blit(
            stone,
            (center_x, road.y + 4)
        )

        screen.blit(
            stone,
            (center_x, road.y + 27)
        )


def draw_world(now):
    # Grass ground
    screen.fill((102, 183, 99))

    # Decorations
    for x, y, kind in decorations:
        if kind == 0:
            pygame.draw.line(
                screen, (55, 140, 68),
                (x, y + 5),
                (x - 2, y), 2
            )

        elif kind == 1:
            pygame.draw.circle(
                screen, (241, 130, 158),
                (x, y), 2
            )

        else:
            pygame.draw.circle(
                screen, (83, 160, 76),
                (x, y), 2
            )

    # Main roads
    for road in ROADS:
        pygame.draw.rect(
            screen,
            (188, 157, 108),
            road
        )

    # NEW - Animal road connections
    draw_animal_roads()

    # Stone road decoration
    for i in range(9):
        screen.blit(
            stone,
            (315 + i * 48, 305)
        )

    for i in range(7):
        screen.blit(
            stone,
            (240, 360 + i * 44)
        )

    # House yard
    pygame.draw.rect(
        screen,
        (190, 158, 110),
        (55, 255, 160, 35)
    )

    screen.blit(house, HOUSE_POS)
    screen.blit(chest, CHEST_POS)

    draw_shop()

    # Trees
    for pos in TREES:
        screen.blit(tree, pos)

    for pos in SMALL_TREES:
        screen.blit(small_tree, pos)

    # Animal ground
    pygame.draw.rect(
        screen,
        (121, 186, 103),
        COW_PEN
    )

    pygame.draw.rect(
        screen,
        (129, 191, 111),
        CHICKEN_PEN
    )

    # Natural dirt patches
    for x, y in [
        (360, 100),
        (470, 195),
        (670, 105),
        (815, 200)
    ]:
        pygame.draw.ellipse(
            screen,
            (158, 135, 95),
            (x, y, 28, 13)
        )

    # Crop fields
    for field in fields:
        field.draw(now)


def draw_panel(title, lines):
    rect = pygame.Rect(
        250, 145, 500, 415
    )

    pygame.draw.rect(
        screen,
        (78, 54, 37),
        rect,
        border_radius=12
    )

    pygame.draw.rect(
        screen,
        (183, 125, 70),
        rect, 4,
        border_radius=12
    )

    heading = title_font.render(
        title,
        True,
        (255, 210, 90)
    )

    screen.blit(
        heading,
        (
            rect.centerx - heading.get_width() // 2,
            rect.y + 19
        )
    )

    for i, line in enumerate(lines):
        label = font.render(
            line,
            True,
            (255, 245, 210)
        )

        screen.blit(
            label,
            (285, 220 + i * 37)
        )


def draw_ui(now):
    pygame.draw.rect(
        screen,
        (37, 60, 42),
        (8, 7, 730, 38),
        border_radius=8
    )

    stats = (
        f"Crops {inventory['crops']}   "
        f"Seeds {inventory['seeds']}   "
        f"Milk {inventory['milk']}   "
        f"Eggs {inventory['eggs']}   "
        f"Coins {inventory['coins']}"
    )

    label = font.render(
        stats,
        True,
        (255, 245, 210)
    )

    screen.blit(label, (18, 15))

    if now < message_until:
        info = message
    else:
        info = (
            "G Gate | E Collect/Chest | "
            "R Plant | F Shop | I Inventory"
        )

    pygame.draw.rect(
        screen,
        (37, 60, 42),
        (10, HEIGHT - 35, 790, 29),
        border_radius=6
    )

    label = small_font.render(
        info,
        True,
        (255, 245, 210)
    )

    screen.blit(
        label,
        (20, HEIGHT - 28)
    )


running = True

while running:
    clock.tick(FPS)
    now = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            key = event.key

            # ESCAPE
            if key == pygame.K_ESCAPE:
                if menu:
                    menu = None
                else:
                    running = False

            # INVENTORY
            elif menu == "inventory":
                if key == pygame.K_i:
                    menu = None

            # SHOP
            elif menu == "shop":
                if key == pygame.K_f:
                    menu = None

                elif key == pygame.K_1:
                    if inventory["crops"] > 0:
                        inventory["crops"] -= 1
                        inventory["coins"] += 5

                        notify(
                            "Sold crop for 5 coins!",
                            now
                        )
                    else:
                        notify(
                            "No crops to sell.",
                            now
                        )

                elif key == pygame.K_2:
                    if inventory["coins"] >= 2:
                        inventory["coins"] -= 2
                        inventory["seeds"] += 1

                        notify(
                            "Bought 1 seed!",
                            now
                        )
                    else:
                        notify(
                            "Need 2 coins.",
                            now
                        )

                elif key == pygame.K_3:
                    if inventory["milk"] > 0:
                        inventory["milk"] -= 1
                        inventory["coins"] += 12

                        notify(
                            "Sold milk for 12 coins!",
                            now
                        )
                    else:
                        notify(
                            "No milk to sell.",
                            now
                        )

                elif key == pygame.K_4:
                    if inventory["eggs"] > 0:
                        inventory["eggs"] -= 1
                        inventory["coins"] += 7

                        notify(
                            "Sold egg for 7 coins!",
                            now
                        )
                    else:
                        notify(
                            "No eggs to sell.",
                            now
                        )

            # CHEST
            elif menu == "chest":
                if key == pygame.K_e:
                    menu = None

                else:
                    actions = {
                        pygame.K_1: ("crops", 1),
                        pygame.K_2: ("crops", -1),
                        pygame.K_3: ("milk", 1),
                        pygame.K_4: ("milk", -1),
                        pygame.K_5: ("eggs", 1),
                        pygame.K_6: ("eggs", -1)
                    }

                    if key in actions:
                        item, amount = actions[key]

                        if amount == 1:
                            source = inventory
                            dest = storage
                        else:
                            source = storage
                            dest = inventory

                        if source[item] > 0:
                            source[item] -= 1
                            dest[item] += 1

                            notify(
                                "Item moved!",
                                now
                            )
                        else:
                            notify(
                                "Nothing to move.",
                                now
                            )

            # NORMAL GAME
            else:
                if key == pygame.K_i:
                    menu = "inventory"

                elif key == pygame.K_f:
                    if near_shop():
                        menu = "shop"
                    else:
                        notify(
                            "Get closer to Shop.",
                            now
                        )

                # OPEN/CLOSE GATES
                elif key == pygame.K_g:
                    switch_gate(now)

                # COLLECT/HARVEST
                elif key == pygame.K_e:
                    if near_chest():
                        menu = "chest"

                    else:
                        animal = nearest_animal()
                        crop = nearest_crop()

                        if (
                            animal is not None
                            and (
                                crop is None
                                or player_center().distance_to(
                                    animal.center()
                                ) < player_center().distance_to(
                                    (crop.x + 17, crop.y + 14)
                                )
                            )
                        ):
                            if (
                                now - animal.last_collected
                                >= COOLDOWN
                            ):
                                inventory[animal.product] += 1
                                animal.last_collected = now

                                notify(
                                    "Collected 1 "
                                    + animal.product + "!",
                                    now
                                )

                            else:
                                seconds = (
                                    COOLDOWN
                                    - (
                                        now
                                        - animal.last_collected
                                    )
                                    + 999
                                ) // 1000

                                notify(
                                    f"Wait {seconds} seconds.",
                                    now
                                )

                        elif crop and crop.ready(now):
                            crop.planted = False
                            inventory["crops"] += 1

                            notify(
                                "Harvested 1 crop!",
                                now
                            )

                        else:
                            notify(
                                "Move closer to a ready crop "
                                "or adult animal.",
                                now
                            )

                # PLANT SEEDS
                elif key == pygame.K_r:
                    crop = nearest_crop()

                    if crop is None:
                        notify(
                            "Approach a plot in an open field.",
                            now
                        )

                    elif crop.planted:
                        notify(
                            "Plot already planted.",
                            now
                        )

                    elif inventory["seeds"] < 1:
                        notify(
                            "Buy more seeds.",
                            now
                        )

                    else:
                        inventory["seeds"] -= 1

                        crop.planted = True
                        crop.planted_at = now

                        notify(
                            "Seed planted!",
                            now
                        )



    keys = pygame.key.get_pressed()

    dx = 0
    dy = 0

    if menu is None:
        dx = (
            int(keys[pygame.K_d])
            - int(keys[pygame.K_a])
        ) * 4

        dy = (
            int(keys[pygame.K_s])
            - int(keys[pygame.K_w])
        ) * 4

        if dy < 0:
            direction = "up"

        elif dy > 0:
            direction = "down"

        elif dx < 0:
            direction = "left"

        elif dx > 0:
            direction = "right"

        new_x = max(
            0,
            min(player_x + dx, WIDTH - 64)
        )

        new_y = max(
            0,
            min(player_y + dy, HEIGHT - 64)
        )

        if can_move(new_x, player_y):
            player_x = new_x

        if can_move(player_x, new_y):
            player_y = new_y

        # Animals remain inside their pens
        for animal in animals:
            animal.update()


    if direction == "down":
        row = 0
    elif direction == "up":
        row = 1
    else:
        row = 2

    if dx or dy:
        animation_index = (
            animation_index + 0.12
        ) % 6

        character = walk[row][
            int(animation_index)
        ]

    else:
        animation_index = 0
        character = idle[row][0]

    if direction == "left":
        character = pygame.transform.flip(
            character, True, False
        )


    draw_world(now)

    for animal in animals:
        animal.draw()

    # Cow Gate faces Main Road
    draw_fence(
        COW_PEN,
        cow_gate_open,
        "bottom"
    )

    # Chicken Gate faces Main Road
    draw_fence(
        CHICKEN_PEN,
        chicken_gate_open,
        "bottom"
    )

    screen.blit(
        character,
        (round(player_x), round(player_y))
    )

    draw_ui(now)



    if menu:
        overlay = pygame.Surface(
            (WIDTH, HEIGHT),
            pygame.SRCALPHA
        )

        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))

        if menu == "inventory":
            draw_panel(
                "INVENTORY",
                [
                    f"Crops: {inventory['crops']}",
                    f"Seeds: {inventory['seeds']}",
                    f"Milk: {inventory['milk']}",
                    f"Eggs: {inventory['eggs']}",
                    f"Coins: {inventory['coins']}",
                    "I / ESC = Close"
                ]
            )

        elif menu == "chest":
            draw_panel(
                "FARM CHEST",
                [
                    f"Crops: {inventory['crops']} "
                    f"(stored {storage['crops']})",

                    f"Milk: {inventory['milk']} "
                    f"(stored {storage['milk']})",

                    f"Eggs: {inventory['eggs']} "
                    f"(stored {storage['eggs']})",

                    "1/2: Store/Take Crop",
                    "3/4: Store/Take Milk",
                    "5/6: Store/Take Egg",
                    "E / ESC = Close"
                ]
            )

        elif menu == "shop":
            draw_panel(
                "FARM SHOP",
                [
                    f"Coins: {inventory['coins']}",
                    "1 - Sell Crop: +5 Coins",
                    "2 - Buy Seed: -2 Coins",
                    "3 - Sell Milk: +12 Coins",
                    "4 - Sell Egg: +7 Coins",
                    "F / ESC = Close"
                ]
            )

    pygame.display.flip()

pygame.quit()
