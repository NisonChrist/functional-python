# functional-python

A small, practical playground for learning functional programming concepts in Python through concise examples and incremental exercises.

## Why this repo?

Functional programming (FP) can feel abstract when presented only as theory or toy examples. This repository focuses on **small, concrete, and reusable patterns** that you can apply in real projects. The goal is to show how FP ideas improve code clarity, safety, and composability—without requiring a new language.

## Goals

- Provide **minimal, readable implementations** of core FP concepts in Python.
- Explain *why* and *when* each concept is useful.
- Offer **hands-on examples** you can run and modify quickly.
- Keep the code small enough to study in one sitting.

## What’s inside

Current modules:

- `functor.py` — a basic `Functor` with `map`
- `maybe.py` — a `Maybe` type to represent optional values safely
- `either.py` — an `Either` type for success/error-style modeling

Each module includes a small `main()` demonstrating usage.

## Requirements

- **Python 3.12.10+**

<!--## Getting started

1. Clone the repository:

   ```/dev/null/commands.txt#L1-1
   git clone <your-repo-url>
   ```

2. Run a module:

   ```/dev/null/commands.txt#L1-1
   python functor.py
   ```

   or

   ```/dev/null/commands.txt#L1-1
   python maybe.py
   ```

3. Read the code and experiment. Try replacing lambdas or values to see how behavior changes.-->

## Suggested learning path

1. **Functor** — Learn how `map` applies a transformation without changing the container.
2. **Maybe** — Avoid `None` checks scattered across your code.
3. **Either** — Model success/failure explicitly without exceptions.

<!--## Contributing ideas

If you have a practical example or a small FP pattern that helped you in real work, feel free to open a PR or issue. The focus is always on **clarity and usefulness**.-->

<!--## License

This project is provided for learning and experimentation. Add a license if you plan to share or reuse it widely.-->
