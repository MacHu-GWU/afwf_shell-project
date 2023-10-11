# -*- coding: utf-8 -*-

import afwf_shell.api as afwf_shell


def handler(query: str, ui: afwf_shell.UI):
    raise ValueError("this handler raises an error")


afwf_shell.debugger.reset()
afwf_shell.debugger.enable()
ui = afwf_shell.UI(handler=handler)
ui.run()
