# Minecraft Survival Mode: Choose Your Own Adventure

This is a text-based interactive adventure game inspired by Minecraft, written in Python. The game features a modern, friendly narrative style, a fast typewriter effect for immersive storytelling, and background music using Pygame. Choices are presented using a clean, interactive command-line interface powered by the `questionary` library.

## Features
- **Interactive Story:** Make choices that affect the outcome of your adventure.
- **Typewriter Effect:** Smooth, quick typewriter animation for all story text.
- **Background Music:** Looped music playback with Pygame (requires `song.wav` in the same directory).
- **Modern CLI:** User-friendly prompts and navigation with `questionary`.

## Requirements
- Python 3.7+
- `pygame`
- `questionary`

## Setup
1. **Clone or download this repository.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   If you do not have `pip`, install it with:
   ```bash
   sudo apt update && sudo apt install python3-pip
   ```
3. **Ensure you have a `song.wav` file** in the project directory for background music.

## Running the Game
Run the following command in your terminal:
```bash
python minecraft_adventure.py
```

## Notes
- If you encounter issues with sound, make sure your system audio is working and `pygame` is installed correctly.
- The game is best experienced in a terminal that supports Unicode and fast output.

## License
This project is for educational and entertainment purposes only and is not affiliated with Mojang or Microsoft.

Enjoy your adventure!

