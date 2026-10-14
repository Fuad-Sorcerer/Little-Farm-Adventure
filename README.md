
<div align="center">

# 🌾 Little Farm Adventure 🐄

### A Cozy 2D Farming Adventure Built with Python & Pygame

**Plant Crops • Raise Animals • Collect Resources • Earn Coins**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?style=for-the-badge)
![Game](https://img.shields.io/badge/Genre-Farming_RPG-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Prototype-purple?style=for-the-badge)

---

**A peaceful pixel-art farming game where you can grow crops, interact with animals, collect resources, and manage your own little farm!**

</div>

## 📖 About the Game

**Little Farm Adventure** is a 2D pixel-art farming game developed using **Python and Pygame**.

The game offers a relaxing farming experience where players can explore a colorful farm, harvest crops, raise animals, collect milk and eggs, and earn coins by selling products.

This project was created to practice Python programming, game development, sprite animation, collision detection, and interactive gameplay systems.

## ✨ Features

### 🌍 Farm World
- Beautiful 2D pixel-art environment
- Smooth character movement
- Animated player sprites
- Trees, grass, pathways, and decorations
- Farmhouse and wooden fences
- Multiple farming areas
- Connected roads and farm gates

### 🌱 Farming System
- Plant seeds in farming plots
- Watch crops grow over time
- Harvest fully grown crops
- Manage available seeds
- Grow crops repeatedly

### 🐄 Animal System
- 5 cows with animated movement
- 8 chickens with animated movement
- Separate animal enclosures
- Interactive animal gates
- Collect milk from female cows
- Collect eggs from adult chickens
- Animal resource collection cooldown

### 🎒 Inventory System
- Store harvested crops
- Manage seeds and coins
- Track collected milk and eggs
- View resources through the inventory menu

### 📦 Chest Storage
- Store harvested crops
- Store milk and eggs
- Withdraw stored resources
- Manage your farm supplies

### 🏪 Farm Shop
- Sell crops to earn coins
- Sell milk and eggs
- Purchase additional seeds
- Manage your farming economy

### 🚧 Interactive Gates
- Open and close farm gates
- Separate cow and chicken enclosures
- Roads connected to animal farm entrances
- Collision detection around fences

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pygame | Game development framework |
| Pathlib | Asset file management |
| Random | Animal movement and decorations |
| Pixel Art | Game characters and environment |

## 🎮 Controls

| Key | Action |
|-----|--------|
| W | Move Up |
| A | Move Left |
| S | Move Down |
| D | Move Right |
| G | Open / Close Gates |
| E | Harvest / Collect / Open Chest |
| R | Plant Seeds |
| I | Open / Close Inventory |
| F | Open / Close Shop |
| 1–6 | Shop and Chest Actions |
| ESC | Close Menu / Exit Game |

## 📁 Project Structure

```text
Little-Farm-Adventure/
│
├── main.py
│
├── Assets/
│   │
│   ├── Character/
│   │   ├── Idle.png
│   │   └── Walk.png
│   │
│   ├── Objects/
│   │   ├── House.png
│   │   ├── Maple Tree.png
│   │   ├── chest.png
│   │   ├── Road.png
│   │   └── Spring Crops.png
│   │
│   └── Farm Animals/
│       ├── Female Cow.png
│       ├── Male Cow.png
│       ├── Chicken Red.png
│       ├── Chicken Blonde.png
│       └── Baby Chicken Yellow.png
│
└── README.md
```

> **Note:** Some sprite files may have longer filenames. The game automatically searches for assets using their filename prefixes.

## 🚀 Installation

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

Make sure Python is added to your system PATH.

### Step 2: Download the Project

Clone this repository:

```bash
git clone https://github.com/YOUR-USERNAME/Little-Farm-Adventure.git
```

Or download the repository as a ZIP file and extract it.

### Step 3: Open the Project

Open the extracted folder in **Visual Studio Code** or another code editor.

### Step 4: Install Pygame

Open a terminal and run:

```bash
python -m pip install pygame
```

### Step 5: Run the Game

Execute the following command:

```bash
python main.py
```

The game window should now open!

> If Python is installed as `py` on Windows, you can use `py main.py` instead.

## 🌾 How to Play

### 1. Explore Your Farm

Use the WASD keys to move around the farm.

Explore the farmhouse, animal enclosures, crop fields, and shop.

### 2. Grow Crops

- Walk toward a crop field.
- Press `G` near the gate to open it.
- Enter the field.
- Press `E` near a mature crop to harvest it.
- Press `R` near an empty plot to plant a new seed.

### 3. Collect Animal Products

**Cows:**
- Open the cow enclosure gate.
- Approach a female cow.
- Press `E` to collect milk.

**Chickens:**
- Open the chicken enclosure gate.
- Approach an adult chicken.
- Press `E` to collect an egg.

Animals need time before they can provide another resource.

### 4. Visit the Farm Shop

Approach the shop and press `F`.

You can sell your harvested resources or buy additional seeds.

### 5. Manage Your Inventory

Press `I` to view your inventory.

Check your collected crops, seeds, milk, eggs, and coins.

### 6. Use the Storage Chest

Approach the chest and press `E`.

Store resources for later or withdraw previously stored items.

## 💰 Game Economy

| Item | Action | Coins |
|------|--------|-------|
| Crop | Sell | +5 |
| Seed | Buy | -2 |
| Milk | Sell | +12 |
| Egg | Sell | +7 |

Earn more coins by managing your farming activities efficiently!

## 🧠 Programming Concepts

This project demonstrates several important programming concepts:

- Variables and data types
- Functions and classes
- Object-oriented programming
- Lists and dictionaries
- Conditional statements
- Loops and event handling
- Sprite sheet animation
- Collision detection
- Game loops and frame rates
- Player movement
- Resource management
- Interactive game objects
- Basic game economy

It is a practical learning project for beginner Python developers interested in creating 2D games.

## ⚙️ Current Limitations

Little Farm Adventure is a learning prototype.

- Game progress is not permanently saved.
- The game currently uses keyboard controls.
- The game is designed for desktop Python.
- Multiplayer is not supported.

## 🐛 Troubleshooting

**Problem: `No module named pygame`**

Install Pygame:

```bash
python -m pip install pygame
```

**Problem: Asset not found**

Make sure the `Assets` folder is located in the same directory as `main.py`.

Also verify the sprite filenames and folder names.

**Problem: Game does not launch**

Check that Python and Pygame are installed correctly and that you are running the project with the intended Python interpreter.

## 🎯 Project Goals

The main goal of this project is to learn how a complete 2D farming game works using Python.

The project focuses on:

1. Writing organized Python code
2. Learning Pygame fundamentals
3. Understanding animation systems
4. Creating interactive gameplay
5. Building inventory and economy systems
6. Practicing object-oriented programming

## 👨‍💻 Developer

**Mofasser Ahmed Fuad**

Python Developer | Web Developer | UI/UX Designer

Interested in Python programming, game development, and building creative digital experiences.

### Connect With Me

- **GitHub:** [Visit My GitHub](https://github.com/)
- **Facebook:** [My Facebook](https://www.facebook.com/Xkingxtar)
- **Email:** mdfuad310281@gmail.com

## 🎨 Asset Credits

This project uses pixel-art assets for characters, animals, and environmental objects.

Credit belongs to the respective asset creators.

Please review the original asset licenses before redistributing or reusing them.

## 📜 License

The source code and third-party game assets may have different usage permissions.

No open-source license has been specified for this repository.

Please contact the developer regarding code reuse, and refer to the original creators' licenses for asset usage.

---

<div align="center">

### 🌿 Built with Python & Pygame

**Made with ❤️ by Mofasser Ahmed Fuad**

*Thanks for visiting Little Farm Adventure!*

⭐ **If you like this project, consider giving it a star!**

</div>
