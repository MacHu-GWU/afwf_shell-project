# -*- coding: utf-8 -*-

import dataclasses
from fuzzywuzzy import process
from afwf_shell.item import Item
from afwf_shell.ui import UI, debugger


@dataclasses.dataclass
class MyItem(Item):
    def enter_handler(self):
        print(f"enter: {self.title}")

    def ctrl_a_handler(self):
        print(f"ctrl_a: {self.title}")

    def ctrl_w_handler(self):
        print(f"ctrl_w: {self.title}")

    def ctrl_p_handler(self):
        print(f"ctrl_p: {self.title}")


def get_items():
    zen_of_python = [
        "Beautiful is better than ugly.",
        "Explicit is better than implicit.",
        "Simple is better than complex.",
        "Complex is better than complicated.",
        "Flat is better than nested.",
        "Sparse is better than dense.",
        "Readability counts.",
        "Special cases aren't special enough to break the rules.",
        "Although practicality beats purity.",
        "Errors should never pass silently.",
        "Unless explicitly silenced.",
        "In the face of ambiguity, refuse the temptation to guess.",
        "There should be one-- and preferably only one --obvious way to do it.",
        "Although that way may not be obvious at first unless you're Dutch.",
        "Now is better than never.",
        "Although never is often better than *right* now.",
        "If the implementation is hard to explain, it's a bad idea.",
        "If the implementation is easy to explain, it may be a good idea.",
        "Namespaces are one honking great idea -- let's do more of those!",
    ]
    items = [
        MyItem(
            uid=f"id-{str(ith).zfill(2)}",
            title=zen,
            subtitle=f"subtitle {str(ith).zfill(2)}",
            autocomplete=zen,
            arg=zen,
        )
        for ith, zen in enumerate(zen_of_python, start=1)
    ]
    return items


def handler(query: str):
    items = get_items()
    if query:
        if len(query) >= 3:
            raise ValueError("Hello World")
        else:
            mapper = {item.title: item for item in items}
            title_list = list(mapper.keys())
            result = process.extract(query, title_list, limit=len(items))
            return [mapper[title] for title, score in result]
    else:
        return items


debugger.reset()
debugger.enable()
ui = UI(handler=handler)
ui.run()
