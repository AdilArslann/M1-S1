# Chess Piece Analyzer

## Overview

This repository contains a Python program developed as part of Turing College's Web Development Module 1 Sprint 1. The project's objective is to create a program that can answer a specific question related to chess: given a board state with one white piece and up to 16 black pieces, which black pieces can the white piece take?

## Project Requirements

The program must meet the following criteria:

1. **Adding the White Piece**: The program should ask the user to input a white chess piece and its location on the board. The user can choose between two predefined white pieces (e.g., pawn and rook) and provide input in a specific format (e.g., "knight a5"). After successfully adding the white piece, the program proceeds to the next step.

2. **Adding Black Pieces**: The user is then prompted to enter the black pieces, one by one, using the same format as for the white piece. The user can add at least one black piece and up to 16. They can also type "done" to indicate that no more black pieces will be added.

3. **Input Validation**: The program should handle valid input formats ("piece coordinates") and report any errors clearly.

4. **Analyzing Moves**: After adding all pieces, the program should determine which black pieces the white piece can take.

## Usage

To run the program, execute the Python file (e.g., `chess_analyzer.py`). Follow the on-screen prompts to input the white and black pieces as described above.
