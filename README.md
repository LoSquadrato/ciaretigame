# 🃏 CIARETI

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-in%20development-orange)]()
[![Ciao ❤️ Toffa](https://img.shields.io/badge/Ciao%20❤️%20Toffa-purple)]()

**Ciareti** is a mysterious card game of *doubtful origin*, passed from friend to friend somewhere along the river **Brenta**, in northern Italy.  

It's a game whose *simple rules can be understood even by a child*, but whose strategy is incredibly complex.

---

## 🂡 The Deck

Ciareti uses a **traditional 40-card Italian deck**, divided into four suits:

**BASTONI (Clubs)**, **COPPE (Cups)**, **DENARI (Coins)**, and **SPADE (Swords)** —  
each suit contains cards from **1 to 10**.

![cards](https://github.com/LoSquadrato/ciaretigame/blob/main/assets/cards.jpg)
>Treviso-style decks are bright and colorful —  
> every number corresponds to a group of cups, coins, clubs, or swords.

---

## 🎲 Rules of the Game

1. **Deal the entire deck** evenly among the players.  
   Each player may look at all their cards.

2. The **first player** plays a card — this sets the **leading suit** for that round.

3. On each turn:
   - You **must play a card of the same suit** if you have one.  
   - If you don’t, play *any* card.  
   - To **win the trick**, play a card of the same suit with a **higher value** than the leading card.

4. Once all players have played, the **highest card of the leading suit** wins the round.  
   The winner collects the cards into their personal pile.

5. The winner of the trick **leads the next round**.

6. After all cards are played, count the **DENARI (Coins)** cards you’ve collected:  
   Each DENARI card gives **points equal to its value** 

7. The player who **won no tricks at all** scores **55 points**.

---

## 🏆 Winning the Game

Here’s where *Ciareti* stands apart:

### 🌀 **The player with the FEWEST points wins!**

Your goal is to **avoid scoring**, not to chase points.  
Try to win hands *without collecting any DENARI*, or dodge victory altogether.

You can play a **single round** or set a **target score** (e.g. “first to reach 200 points loses”).

---

## 💻 How to Play (Digital Version)

To play the Python version of *Ciareti*:

```bash
# 1. Install Python 3.12+
https://www.python.org/downloads/

# 2. Clone this repository
git clone https://github.com/your-username/ciareti.git
cd ciareti

# 3. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# 4. Run the game
python main.py
```

Enjoy your descent into strategic madness! 😁

🔮 Roadmap

Planned features and improvements:

🧠 AI opponents with adaptive logic

🔁 Turn and round management

🧾 Automatic scoring and winner declaration

🖼️ Graphical interface (GUI)

❤️ Author’s Note

Ciareti isn’t an official, traditional card game —
but it could be. It was born from laughter, storytelling, and long nights along the Brenta.
It’s a tribute to friendship, chaos, and the strange beauty of trying not to win.

📜 License

This project is released under the MIT License
.
Feel free to fork, improve, and share — just don’t forget to play fair 😉

⭐️ If you enjoy this project...

Give it a star on GitHub!
It helps others discover Ciareti and keeps the Brenta legend alive ✨