import os

width = os.get_terminal_size().columns

def level_one():
    output = ['Do you like my hat?'.center(width), 'Custom made from the CAA.'.center(width),
              'What does CAA mean?'.center(width), 'Cute Awesome Alliance.'.center(width)]
    return output

def level_two():
    output = ['Have you come to challenge me?'.center(width), 'I did not think such a novice would have the guts.'.center(width),
              'Very well. Challenge accepted.'.center(width)]
    return output

def level_three():
    output = ['...'.center(width), '...'.center(width), '...'.center(width), 'Welcome.'.center(width)]
    return output