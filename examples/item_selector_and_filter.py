# -*- coding: utf-8 -*-

import dataclasses
from afwf_shell.api import Item, UI, debugger


@dataclasses.dataclass
class MyItem(Item):
    def enter_handler(self):
        print(f"enter: {self.title}")


def get_items():
    colors = ["blue", "green", "red", "yellow"]
    items = [
        MyItem(
            uid="id-1",
            title=color,
            subtitle=f"subtitle {color}",
            autocomplete=color,
            arg=color,
        )
        for color in colors
    ]
    return items


def handler(query: str):
    items = get_items()
    if query:
        return [item for item in items if query in item.title]
    else:
        return items


debugger.reset()
debugger.enable()
ui = UI(handler=handler)
ui.run()
