🧬 Evolutionary Game Solver (AI Project 2 – Genetic Algorithms)

This project was implemented as part of the Artificial Intelligence (Spring 2021) course at Amirkabir University of Technology (Tehran Polytechnic).
The goal is to design a Genetic Algorithm (GA) that can solve procedurally generated game levels similar to Super Mario, determining whether a level is solvable and estimating the maximum achievable score.

🎯 Problem Statement

Nintendo has developed a procedural level generator that produces random levels, but occasionally some are unsolvable.
The task is to create an algorithm that:

Determines if a level is solvable or not, and

Estimates the maximum possible score that a player can achieve.

The algorithm should simulate a simplified 2D platformer where the agent (Luigi) moves rightward and performs three possible actions at each step:

Action Code	Description
0	Move Right
1	Jump + Move Right
2	Dodge + Move Right

Each level is represented as a text string (e.g. "____G_M__L_"), where each symbol represents an element:

Symbol	Meaning
_	Empty Ground
G	Goomba (Ground Enemy)
M	Mushroom (Collectible)
L	Lakitu (Air Enemy)
F	Flag (Goal)

Luigi starts at the leftmost position and must reach the flag without dying.

🧩 Game Rules and Scoring
Event	Score
Move forward	+1
Eat a Mushroom	+2
Kill a Goomba by jumping	+2
Jump unnecessarily	−0.5
Collide with enemy / lose	−10
Finish level	Bonus

The agent’s fitness is calculated based on its survival and score, forming the basis of the Genetic Algorithm’s evaluation.

🧠 Algorithm Overview

The Genetic Algorithm optimizes Luigi’s action sequence to maximize score.
It evolves through several generations using selection, crossover, and mutation operations.

Steps:

Initialize Population:
Randomly generate action sequences (chromosomes).

Evaluate Fitness:
Use the game’s scoring function to compute each chromosome’s fitness.

Selection:
Select parents probabilistically (fitness-weighted or elite-based).

Crossover:
Combine parents to produce offspring using either:

Single-point crossover

Double-point crossover

Mutation:
Randomly change an action (0, 1, or 2) with predefined probabilities.

Termination:
Stop when:

Generations reach a fixed limit (e.g. 200), or

The average fitness converges.

🏗️ Project Structure
File	Description
game.py	Defines game logic, Luigi’s states, and scoring.
ga.py	Implements the Genetic Algorithm class.
visualizer.py	Handles map visualization and result plotting with matplotlib.
levels/	Contains 10 pre-defined levels in .txt format.
main.py	Entry point for running the GA simulation.
📊 Visualization and Output

The project generates:

Fitness Plots: Min, Avg, Max fitness per generation

Level Snapshots: Visual representation of maps

GIF Animations: Luigi’s gameplay generated via ffmpeg

Example:

python main.py


Output folders:

/output/configs        → Map configurations
/output/plots          → Fitness evolution plots
/output/images         → Luigi movement frames
/output/animations     → Final GIFs

⚙️ Example Results
Setting	Population	Crossover	Mutation	Runs	Selection Power
1	200	Single-point	0.1	100	1
2	400	Double-point	0.5	100	3
3	100	Single-point	0.6	200	1
4	400	Double-point	0.6	200	3
🧠 Concepts Used

Genetic Algorithms

Fitness-based optimization

State machines

Game simulation and visualization

Python data handling and plotting

📄 License

Developed by Mohammad Mottaghi
as part of the Artificial Intelligence (Spring 2021) course
at Amirkabir University of Technology (Tehran Polytechnic).
© 2024 Mohammad Mottaghi
