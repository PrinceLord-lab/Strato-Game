import os

width = os.get_terminal_size().columns

def level_one():
    output = []
    output.append('     /¡\        '.center(width))
    output.append('    |━0━|       '.center(width))
    output.append('_____\!/___     '.center(width))
    output.append('____CHIEF__\____'.center(width))
    output.append('---(ʘ)--(ʘ)-\   '.center(width))
    output.append('      ‿      \  '.center(width))
    return output

def level_two():
    output = []
    output.append('   __________   '.center(width))
    output.append(' <|┻━┻━━━━┻━┻|> '.center(width))
    output.append(' <| [Ò]  [Ó] |> '.center(width))
    output.append(' /|  |╬╬╬╬|  |\ '.center(width))
    output.append('| |  |╬╬╬╬|  | |'.center(width))
    output.append('[ |__________| ]'.center(width))
    return output

def level_three():
    output = []
    output.append('                          '.center(width))
    output.append('     ⠀⠀⠀⢀⣀⣀⣤⣤⣤⣀        '.center(width))
    output.append('     ⠀⣴⠛⠉⠉⠉⠉⠉⠉⢻        '.center(width))
    output.append('     ⣿⣿⠀⠀*    *⠘⣷       '.center(width))
    output.append(' /\/\⣿⣿⣀⣀⣀⣀⣀⣀⣀⣤⣿/\/\  '.center(width))
    output.append('/ /  ⠈⠛⠉⠉⠉⠉⠉⠉⠉⠉⠉  \ \ '.center(width))
    return output