"""
You are implementing a class that handles text editing operations, but currently it is not complete and might have some issues. Your task is to refactor it, fix the issues and add the missing parts.

The following methods should be supported:

onPressLeft() - the cursor moves left by 1 character. If there are no characters on the left side of the cursor, does nothing.
onPressRight() - the cursor moves right by 1 character. If there are no characters on the right side of the cursor, does nothing.
onPressHome() - the cursor moves to the beginning of the text.
onPressEnd() - the cursor moves to the end of the text.
onPressDelete() - deletes the character (if there is one) adjacent to the right side of the cursor.
onPressBackspace() - deletes the character (if there is one) adjacent to the left side of the cursor.
onInputCharacter(character) - inserts character on the right side of the cursor.
Example

For commands = ["S", "S", "i", "g", "g", "backspace", "n", "a", "l", "left", "left", "left", "left", "left", "backspace", "left", "C", "o", "d", "e"], the output should be
solution(commands) = ["S", "SS", "SSi", "SSig", "SSigg", "SSig", "SSign", "SSigna", "SSignal", "SSignal", "SSignal", "SSignal", "SSignal", "SSignal", "Signal", "Signal", "CSignal", "CoSignal", "CodSignal", "CodeSignal"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string commands

commands[i] is either a string from the set {"left", "right", "home", "end", "delete", "backspace"}, or a string consisting of exactly one English letter character.

Guaranteed constraints:
1 ≤ commands.length ≤ 250.

[output] array.string

An array where the ith element is equal to the result of the ith operation.
"""
class Editor:

    def __init__(self):
        self.text = ""
        self.cursor = 0

    def onPressLeft(self):
        if self.cursor > 0:
            self.cursor -= 1
        return self.text

    def onPressRight(self):
        if self.cursor < len(self.text):
            self.cursor += 1
        return self.text

    def onPressHome(self):
        self.cursor = 0
        return self.text

    def onPressEnd(self):
        self.cursor = len(self.text)
        return self.text

    def onPressDelete(self):
        if self.cursor == len(self.text):
            return self.text
        self.text = "".join(self.text[x] for x in range(len(self.text)) if x != self.cursor)
        return self.text

    def onPressBackspace(self):
        if self.cursor <= len(self.text) and self.cursor > 0:
            self.text = self.text[:self.cursor - 1] + self.text[self.cursor:]
            self.cursor -= 1
        return self.text

    def onInputCharacter(self, character):
        self.text = self.text[:self.cursor] + character + self.text[self.cursor:]
        self.cursor += 1
        return self.text


def solution(commands):
    editor = Editor()
    result = []
    for command in commands:
        if command == "left":
            result.append(editor.onPressLeft())
        elif command == "right":
            result.append(editor.onPressRight())
        elif command == "home":
            result.append(editor.onPressHome())
        elif command == "end":
            result.append(editor.onPressEnd())
        elif command == "delete":
            result.append(editor.onPressDelete())
        elif command == "backspace":
            result.append(editor.onPressBackspace())
        else:
            result.append(editor.onInputCharacter(command))

    return result
