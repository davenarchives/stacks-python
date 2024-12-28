## Overview
This Python script provides a simple implementation of a stack data structure and demonstrates its use by reversing a user-provided paragraph.

## Features
- **Stack Class**: Implements a stack with the following methods:
  - `is_empty`: Checks if the stack is empty.
  - `push`: Adds an item to the stack.
  - `pop`: Removes and returns the top item from the stack.
  - `peek`: Returns the top item without removing it.
  - `size`: Returns the number of items in the stack.
- **Paragraph Reversal**: Uses the stack to reverse the characters of a given paragraph.

## How It Works
1. **Input**: The user provides a paragraph of text.
2. **Processing**: Each character of the paragraph is pushed onto a stack. Then, the characters are popped from the stack to build the reversed paragraph.
3. **Output**: The reversed paragraph is displayed to the user.

## Usage
### Prerequisites
- Python 3.x

### Steps to Run
1. Save the script in a file, e.g., `reverse_paragraph.py`.
2. Open a terminal or command prompt.
3. Run the script using the command:
   ```
   python reverse_paragraph.py
   ```
4. Enter a paragraph when prompted.
5. View the reversed paragraph as the output.

### Example
**Input:**
```
Hello, World!
```

**Output:**
```
!dlroW ,olleH
```

## Code Structure
### Stack Class
- Implements the core stack functionality.
- Uses a list (`self.items`) to store elements.

### `reverse_paragraph` Function
- Accepts a string (paragraph) as input.
- Uses the `Stack` class to reverse the characters of the paragraph.

### `main` Function
- Handles user input and displays the reversed paragraph.

## Customization
- The script can be modified to reverse words instead of characters by splitting the paragraph into words and pushing each word onto the stack.
- Additional error handling can be added for edge cases, e.g., empty input.

## License
This script is provided "as-is" for educational purposes. Feel free to modify and use it in your projects.

