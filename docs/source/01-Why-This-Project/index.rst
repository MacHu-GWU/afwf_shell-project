Why This Project
==============================================================================


The Idea
------------------------------------------------------------------------------
我非常喜欢 `Alfred Workflow <https://www.alfredapp.com/workflows/>`_ 这款效率工具, 它的编程可扩展性使得我可以创建各种我需要的工具. 但是这款工具只能在 Mac 上使用, 并且 Workflow 功能是收费功能, 需要至少 34 英镑购买 `Powerpack <https://www.alfredapp.com/shop/>`_ 后才能使用.

受到 Alfred 的启发, 我希望能创建一款类似的效率工具, 能够跨平台, 免费. 于是我选择了用 Terminal 作为 App 的载体, 用 Terminal 界面作为 UI, 用跨平台的 Python 作为底层实现. 于是就有了这个项目.


User Interaction Logics
------------------------------------------------------------------------------
我们以 `Google Search <https://www.google.com/>`_ 为例, 来介绍如果用 ``afwf_shell`` 重新实现 Google Search, 用户界面的交互逻辑是怎样的.


CLI Command and UI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
要使用 Google Search, 用户需要输入 www.google.com 进入网页界面. 然后用户会看到一个 Search bar 可以输入文本, 并且会根据用户的输入自动出现提示.

用户在 Terminal 中输入 CLI 命令, 进入一个交互式的 UI. 这个 CLI 的命令就类似于 Alfred 中的 `Keyword <https://www.alfredapp.com/help/workflows/inputs/keyword/>`_, 决定了了这个 UI 的功能. 既然我们是用 CLI 命令, 那么自然也能支持参数, 可以用 ``--param value`` 的形式改变这个 UI 的功能.

本质上这个 CLI 命令的作用就是将用户带到特定 App, 它和 www.google.com 之于 Google Search 的关系是一样的, 就是一个 App 的入口. 而这个 UI 就相当于 Google Search 的 Search Bar.

举个例子, 基于 ``afwf_shell`` 的 Google Search UI 可能长得像这个样子:

.. code-block:: bash

    code



User Input Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
进入 UI 之后, 用户就可以输入文本了. 这个输入的文本就是 User Input Query, 简称 Query. 我们限制用户的输入文本只有一行, 因为这个 App 的设计哲学就是用最简单的命令来做复杂的事.

[Search on ]


Dropdown Menu and Item
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
当用户输入了 Query 之后, 就会以这个 Query 作为 Input, 并运行一段代码, 然后返回 Output. 这个 Output 在 UI 界面上







Software Architecture
------------------------------------------------------------------------------
