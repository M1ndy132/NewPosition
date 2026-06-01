# NewPosition

> A narrative-driven math traversal game where position itself is unstable.

## Overview

Dr. Infinity has disappeared.

The reactor he maintained is destabilizing. Energy cells are scattering across the system, each one shifting according to hidden mathematical rules.

Your task is simple:

> Stabilize the reactor before the system collapses.

But nothing stays in place for long.

Every answer you give becomes the next state of the world.

---

## Gameplay

Each turn:

* You are given a **current position**
* A transformation is applied to an energy cell
* You calculate the new position
* Your answer becomes the next starting point

Progression is continuous — there are no resets between questions.

---

## Core Mechanics

### Transformations

* **Boost** → position + value
* **Drain** → position − value
* **Amplify** → position × value
* **Dissipate** → position ÷ value (rounded)

---

### Question Types

* **Regular** → standard interpretation of rules
* **Unknown** → inverted / altered logic patterns

Each level mixes these dynamically.

---

### Reactor System

* Limited stability per level
* Wrong answers reduce integrity
* At zero integrity → system failure
* Complete all cells → sector stabilized

---

## Structure

```
NewPosition/
│
├── main.py
├── questionfile.py
│
├── levels/
│   ├── level1.py
│   ├── level2.py
│   ├── ...
│   └── level20.py
│
└── README.md
```

Each level defines:

* allowed transformations
* difficulty settings
* story entries
* question types

---

## How to Play

```bash
python main.py
```

No installation required. Standard Python only.

---

## Story

Dr. Infinity left behind fragmented journal entries inside the reactor system.

At first, the patterns seem mathematical.

Then they start to feel… intentional.

Something is changing how the system behaves.

---

## Roadmap (Optional)

* Improved UI formatting
* Sound effects for reactor events
* Hard mode (larger numbers, multi-step transforms)
* Optional multiplayer classroom challenge mode

---

## 📌 Version

**v0.0.1 — First Stable Build**

* Fully playable from Level 1–20
* Core mechanics complete
* Story progression implemented
* Level-based difficulty scaling

---

## ⚙️ Notes

This project is designed as a learning-driven puzzle game blending:

* arithmetic
* state progression
* narrative fragments

---

## ⭐ Credit

Built as an experimental learning project exploring:

> math as movement, and answers as world state.

---