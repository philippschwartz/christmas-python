import os
import random
import time
from colorama import init, Fore, Back, Style
import shutil

# Initialize colorama
init(autoreset=True)

def clear_screen():
    """Clear screen using OS-specific command"""
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Unix/Linux/MacOS
        os.system('clear')

def create_christmas_art():
    """Create minimalist Christmas tree art with floating words"""
    width, height = shutil.get_terminal_size()
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Calculate tree dimensions
    tree_height = min(height - 4, 35)
    max_width = min(width - 10, tree_height * 2)
    start_x = (width - max_width) // 2
    start_y = (height - tree_height) // 2

    # Draw minimal tree with geometric shapes
    for y in range(tree_height):
        row_width = int(max_width * ((y + 1) / tree_height))
        for x in range(row_width):
            if random.random() < 0.4:  # Make tree more sparse
                symbols = ['△', '▲', '◇', '□', '○']
                symbol = random.choice(symbols)
                pos_x = start_x + x + (max_width - row_width) // 2
                pos_y = start_y + y
                if 0 <= pos_y < height and 0 <= pos_x < width:
                    canvas[pos_y][pos_x] = Fore.GREEN + symbol

    # Add floating words at random positions
    words = ['HOPE', 'JOY', 'PEACE', 'WONDER', 'NOEL', 'MAGIC']
    for word in random.sample(words, 3):  # Only use 3 random words
        x = random.randint(0, width - len(word))
        y = random.randint(0, height - 1)
        color = random.choice([Fore.CYAN, Fore.YELLOW, Fore.RED])
        
        # Check if space is available
        if all(canvas[y][x + i] == ' ' for i in range(len(word))):
            for i, char in enumerate(word):
                canvas[y][x + i] = color + char

    # Add scattered stars in the background
    for _ in range(width * height // 100):  # Adjust density of stars
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if canvas[y][x] == ' ':
            color = random.choice([Fore.BLUE, Fore.WHITE, Fore.CYAN, Fore.MAGENTA])
            symbol = random.choice(['*', '·', '+', '✧', '⋆'])
            canvas[y][x] = color + symbol

    # Convert canvas to string with black background
    return '\n'.join([''.join([Back.BLACK + pixel if pixel != ' ' 
                              else Back.BLACK + ' ' for pixel in row]) 
                     for row in canvas])

def main():
    try:
        while True:
            clear_screen()
            art = create_christmas_art()
            print(art, end='')
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(Style.RESET_ALL)
        os.system('clear')

if __name__ == "__main__":
    main()
