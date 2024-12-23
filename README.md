# Terminal Christmas Art Animation

A sophisticated terminal-based artistic installation that reimagines the traditional Christmas tree through algorithmic art. This Python application generates an abstract, ever-evolving visualization using Unicode characters and dynamic color patterns.

![Christmas Tree Animation Demo](demo.gif)

## Concept

This project explores the intersection of holiday tradition and digital art, transforming the utilitarian command-line interface into a canvas for festive expression. Through geometric abstraction and programmatic animation, it challenges our perception of both terminal capabilities and traditional holiday decorations.

## Technical Implementation

The animation employs several key technical approaches:
- Dynamic Unicode character mapping for artistic representation
- Algorithmic pattern generation using Python's random module
- Real-time terminal size adaptation for responsive display
- Color manipulation through the Colorama library
- Efficient screen buffer management for smooth animation

## Features

The installation creates an immersive experience through:
- Geometric abstraction of traditional Christmas tree elements
- Ambient floating seasonal messages that create depth and context
- Dynamic star field generation that responds to terminal dimensions
- Responsive scaling that maintains artistic integrity across different terminal sizes
- Full-screen utilization with intelligent border management

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

## Design Philosophy

This project demonstrates how programming can transform everyday tools into vehicles for artistic expression. By combining geometric patterns with seasonal elements, it creates a contemplative space that bridges traditional holiday imagery with contemporary digital art.

## Technical Requirements

- Python 3.9+
- Terminal with Unicode support
- Colorama library

## Author

Philipp Schwartz

## License

MIT License

Copyright (c) 2024 Philipp Schwartz

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
