"""
This file contains formatting functions.
"""

'''
Text formatting
-------------------------------------------------------------------------------
'''

#This class creates text boxes when a string is passed into it.
class text_box_maker():
    
    def __init__(self, width=0):
        self.width = width

    def remove_space(self, text):
        self.text = text
        lines = self.text.splitlines()
        for s in lines:
            if len(s) == 1:
                del(s)
        width = max(len(s) for s in lines)
        self.width = width

    def bordered(self, text):
        lines = self.text.splitlines()
        num_lines = (len(lines) - 1)
        x = 0
        while x <= num_lines:
            lines[x] = ('{}'.format((' '*5)) + lines[x] + '{}'.format((' '*5)))
            x = x + 1
        width = self.width+10
        res = ['┌' + '─' * width + '┐']
        for s in lines:
            res.append('│' + (s + ' ' * width)[:width] + '│')
        res.append('└' + '─' * width + '┘')
        return '\n'.join(res)
        
    def make_text_box(self, text):
        self.remove_space(text)
        if self.width > 2:
            half_width = ( int( (self.width / 2) ) + 10 )
        return '\n' + ('* ' * (half_width)) + "\n" + (self.bordered(text))

#This object creates text boxes.
boxer = text_box_maker()