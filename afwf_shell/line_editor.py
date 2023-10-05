# -*- coding: utf-8 -*-

import blessed


class LineEditor:
    """
    Simulate a user input line editor. User can type characters, move cursor,
    backspace, delete, clear line, etc ...

    :param chars: a list of characters, representing the current line.
    :param cursor_position: the current cursor position. 0 means the cursor is
        at the beginning of the line. 1 means it is after the first character.
        when cursor_position == len(chars), it means the cursor is at the end.
    """
    def __init__(self):
        self.chars = []
        self.cursor_position = 0

    def enter_text(self, text: str):
        for char in text:
            self.press_key(key=char)

    def _press_key(self, key: str):
        self.chars.append(key)
        self.cursor_position += 1

    def press_key(self, key: str, n: int = 1):
        for _ in range(n):
            self._press_key(key)

    def _press_backspace(self):
        if self.cursor_position == 0:
            pass
        elif self.cursor_position == len(self.chars):
            self.chars.pop()
            self.cursor_position -= 1
        else:
            self.cursor_position -= 1
            self.chars.pop(self.cursor_position)

    def press_backspace(self, n: int = 1):
        for _ in range(n):
            self._press_backspace()

    def _press_left(self):
        if self.cursor_position != 0:
            self.cursor_position -= 1

    def press_left(self, n: int = 1):
        for _ in range(n):
            self._press_left()

    def press_home(self):
        self.cursor_position = 0

    def _press_delete(self):
        if self.cursor_position == len(self.chars):
            pass
        else:
            self.chars.pop(self.cursor_position)

    def press_delete(self, n: int = 1):
        for _ in range(n):
            self._press_delete()

    def _press_right(self):
        if self.cursor_position != len(self.chars):
            self.cursor_position += 1

    def press_right(self, n: int = 1):
        for _ in range(n):
            self._press_right()

    def press_end(self):
        self.cursor_position = len(self.chars)

    def clear_line(self):
        self.chars.clear()
        self.cursor_position = 0

    def clear_backward(self):
        self.chars = self.chars[self.cursor_position:]
        self.cursor_position = 0

    def clear_forward(self):
        self.chars = self.chars[:self.cursor_position]
        self.cursor_position = len(self.chars)

    @property
    def line(self) -> str:
        """
        Example: ``ali|ce`` -> line = alice
        """
        return "".join(self.chars)

    @property
    def value(self) -> str:
        """
        Example: ``ali|ce`` -> value = ali
        """
        return "".join(self.chars[: self.cursor_position])
