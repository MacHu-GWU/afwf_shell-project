# -*- coding: utf-8 -*-

import typing as T
import time
import dataclasses
from pathlib import Path
from fuzzywuzzy import process
import afwf_shell.api as afwf_shell


@dataclasses.dataclass
class Item(afwf_shell.Item):
    pass


path = Path(__file__).parent / "first_run_waiter_example_tracker.txt"


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
        Item(
            uid=f"id-{str(ith).zfill(2)}",
            title=zen,
            subtitle=f"subtitle {str(ith).zfill(2)}",
            autocomplete=zen,
            arg=zen,
        )
        for ith, zen in enumerate(zen_of_python, start=1)
    ]
    return items


def search(query: str) -> T.List[Item]:
    items = get_items()
    if query:
        mapper = {item.title: item for item in items}
        title_list = list(mapper.keys())
        result = process.extract(query, title_list, limit=len(items))
        return [mapper[title] for title, score in result]
    else:
        return items


def handler(query: str, ui: afwf_shell.UI):
    if path.exists():
        return search(query)
    else:
        items = [
            Item(
                uid="uid",
                title="Creating index ...",
                subtitle="please wait, don't press any key.",
            )
        ]
        ui.print_items(items=items)
        time.sleep(3)
        path.write_text("done")
        ui.move_to_end()
        ui.clear_items()
        ui.clear_query()
        ui.print_query()
        return search(query)


path.unlink(missing_ok=True)
afwf_shell.debugger.reset()
afwf_shell.debugger.enable()
ui = afwf_shell.UI(handler=handler)
ui.run()
