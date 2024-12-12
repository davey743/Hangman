hangman_figure = [
    """
----------------------
                     |
                     |
""",
"""
----------------------
                     |
                     |
                     O
""",
"""
----------------------
                     |
                     |
                     O
                     |                    
""",
"""
----------------------
                     |
                     |
                     O
                    \|
""",
"""
----------------------
                     |
                     |
                     O
                    \|/
""",
"""
----------------------
                     |
                     |
                     O
                    \|/
                     |
""",
"""
----------------------
                     |
                     |
                     O
                    \|/
                     |
                    /
""",
"""
----------------------
                     |
                     |
                     O
                    \|/
                     |
                    / \ 
"""
]

def get_hangman_figure(attempts):
    return hangman_figure[7 - attempts]