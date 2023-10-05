# -*- coding: utf-8 -*-

"""
通过学习 inquirer 的源码来研究如何实现一个类似的功能.
"""

import inquirer

questions = [
    inquirer.Text("name", message="What's your name?"),
]
answers = inquirer.prompt(questions)

print(answers)