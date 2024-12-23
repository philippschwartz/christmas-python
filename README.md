# Terminal Christmas Art Animation

Initial Thoughts:
- Inspired by wanting to create a festive, digital decoration that's both minimal and artistic
- Aimed to transform the boring terminal into something different and holiday-themed
- Wanted to explore how simple characters could create engaging visual art

Process:
- What worked:
  * Using Unicode characters instead of basic ASCII for better visuals
  * Creating a black background for better contrast
  * Adding floating words for an artistic touch
  * Random placement of stars and decorations
  * The virtual environment setup for clean dependency management

- What didn't:
  * Initial screen clearing had issues on macOS
  * First attempts at centering weren't perfect
  * Early versions had white background bleeding
  * Some terminal compatibility challenges needed fixing

- Unexpected discoveries:
  * Terminal size detection makes it adaptable
  * Colorama library makes color management much easier
  * Simple geometric shapes can create compelling abstract art
  * Animation can be achieved with basic timing loops

Learnings:
- Technical insights:
  * How to manage terminal displays
  * Virtual environment importance
  * Color handling in terminal applications
  * Screen buffer management
  * Python's random module for artistic purposes

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/philippschwartz/christmas-python.git
    cd christmas-python
    ```

2. Create and activate virtual environment:

    For Unix/Mac:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    For Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate.bat
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Windows-Specific Setup
If you're using PowerShell and encounter script execution restrictions, open PowerShell as Administrator and run:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

## Usage

Launch the animation:
```bash
python christmas_tree.py
```
    
Exit gracefully with Ctrl+C

