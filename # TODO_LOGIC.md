# TODO_LOGIC.md

# Reactor Math Game — Core Logic Completion Checklist

This file defines the "logic finish line" for the game.
When all boxes are checked, the core system is considered complete.

---

## 🧠 Core Game Loop

- [X] Position generates correctly or carries over correctly
- [X] Keyword is selected without breaking rules
- [X] Movement value is generated correctly
- [X] Player input is requested each round
- [X] Correct answer is calculated accurately
- [X] Game state updates correctly after each round
- [X] Loop runs continuously without bugs or resets

---

## ⚙️ Game State Stability

- [ ] Position always reflects last correct result
- [ ] Cells collected increments only on success
- [ ] Reactor integrity decreases only on failure
- [ ] Level progression resets state correctly
- [ ] No unintended variable resets or overwrites

---

## 🔢 Math System

- [ ] Boost = position + n
- [ ] Drain = position - n
- [ ] Amplify = position * n (controlled difficulty)
- [ ] Dissipate = position / n (consistent rounding rule)
- [ ] No operation produces unplayable numbers
- [ ] Answers are mentally solvable (no excessive complexity)

---

## 🎮 Keyword System

- [ ] All keywords behave consistently
- [ ] No keyword breaks game balance
- [ ] No keyword dominates gameplay unfairly
- [ ] Dynamic keyword removal does not break flow
- [ ] New keyword can be added without rewriting core loop

---

## 📊 Level System

- [ ] Levels defined in separate files/modules
- [ ] Each level defines:
  - [ ] keywords
  - [ ] cells required
  - [ ] story text
- [ ] Main loop does not depend on hardcoded level logic
- [ ] Level switching does not break state
- [ ] New level can be added without modifying core loop

---

## 💀 Win / Lose Conditions

- [ ] Win condition triggers correctly (cells collected)
- [ ] Lose condition triggers correctly (reactor integrity = 0)
- [ ] Game stops immediately on win or loss
- [ ] No ability to continue playing after game ends

---

## 🔁 Session Flow

- [ ] Start prompt works correctly
- [ ] Game loop runs cleanly
- [ ] Level transition prompt works
- [ ] End state displays clearly (win or loss)
- [ ] Game exits cleanly back to terminal

---

## ✨ COMPLETION RULE

Core logic is considered COMPLETE when ALL checkboxes above are ticked.

At that point:

- Game is stable
- Systems are reusable
- Expansion (graphics, sounds, algebra mode) can be added safely

---
