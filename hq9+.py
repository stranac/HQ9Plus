"""
A simple implementation of the HQ9+ programming language.
http://esolangs.org/wiki/HQ9%2B

Ignores everything except the four valid commands(case insensitive):
    H   Prints "Hello, world!"
    Q   Prints the entire text of the source code file.
    9   Prints the complete canonical lyrics to "99 Bottles of Beer on the Wall"
    +   Increments the accumulator.
"""

import sys
import re

import bottles


class HQ9PlusProgram(object):
    def __init__(self, src):
        self.src = src
        self.acc = 0
        self.commands = {
        'H': self.hello,
        'Q': self.quine,
        '9': self.nine,
        '+': self.plus,
        }

    def hello(self):
        print 'Hello, world!'

    def quine(self):
        print self.src

    def nine(self):
        print '\n'.join(bottles.verses())

    def plus(self):
        self.acc += 1

    def run(self):
        for letter in re.findall(r'[HQ+9]', self.src.upper(), re.MULTILINE):
            self.commands[letter]()


def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        in_file = sys.stdin
    else:
        in_file = open(filename)

    with in_file:
        program = HQ9PlusProgram(in_file.read())
    program.run()

main()
