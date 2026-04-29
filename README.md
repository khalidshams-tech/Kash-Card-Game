# Kash Card Game

A Flask web application for tracking rounds, scores, roles, and card-swap instructions in a three-player Kash card game.

## Project Description

Kash Card Game is a small Python/Flask project that turns a manual card-game scoring process into a browser-based tool. The app tracks player names, rotating dealer roles, required trick counts, actual tricks won, round results, total scores, and next-round swap instructions.

This project shows practical web development skills, session-based state management, route handling, form processing, and game logic organization.

## Technologies Used

- Python 3
- Flask
- HTML
- CSS
- Jinja templates
- Browser sessions

## Features

- Start a new three-player game
- Rotate dealer and role responsibilities by round
- Track required tricks for each player
- Enter actual tricks won during each round
- Calculate missing tricks and update player scores
- Generate card-swap instructions for the next round
- End the game when a player reaches the score limit
- Reset the game and start over
- Responsive browser-based interface

## Project Structure

```text
Kash-Card-Game/
+-- app.py
+-- game_logic.py
+-- requirements.txt
+-- README.md
+-- static/
+-- templates/
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/khalidshams-tech/Kash-Card-Game.git
```

2. Open the project folder:

```bash
cd Kash-Card-Game
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the app:

```bash
python app.py
```

6. Open the local site in your browser:

```text
http://127.0.0.1:5000
```

## Screenshots

Add screenshots here showing:

- Start game screen
- Round entry screen
- Score/results screen
- Game-over screen

Example:

```markdown
![Kash Card Game screen](static/screenshots/kash-card-game.png)
```

## What I Learned

- How to build a Flask app with multiple routes
- How to use sessions to keep game state between requests
- How to separate game logic from web route code
- How to process forms and validate player input
- How to turn real-world rules into program logic
- How to document setup steps for another user

## Future Improvements

- Add automated tests for game scoring rules
- Add stronger input validation and user-friendly error messages
- Add screenshots or a short demo video
- Add a deployed version using Render, PythonAnywhere, or another hosting platform
- Improve accessibility and mobile layout
- Add game history export for completed rounds

## Status

Active portfolio project. The next improvement should be adding tests and screenshots.