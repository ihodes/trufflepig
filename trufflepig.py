# -*- coding: utf-8 -*-
'''
TrufflePig
~~~~~~~~~~

Search (and maybe replace) text in an HTML. Select with CSS+ selectors.

See the README.md for examples.

Author: Isaac Hodes
License: MIT 

           _
           ((`)_.._     ,'-. _..._ _._
           \,'    '-._.-\   '     ` .-'
           .'            /          (
          /             |     _   _ \
         |              \     e   e  |
         ;                     .-.   /
         ;       ',       '-.( '')-'
         '.      |           ;-'
           \    /           /
           /   /-._  __,  7 |
           \  `\  \``  |  | |
            \   \_,\   |  |_,\
             '-`'      \_,\
'''
import sys

from argparse import ArgumentParser, FileType
from pyquery import PyQuery as pq



parser = ArgumentParser(description="Search/replace html truffles.",
                        epilog=("For more information, check "
                                "http://github.com/ihodes/trufflepig."))

parser.add_argument('selector',
                    help="css selector to search for (JQuery syntax)")
parser.add_argument('mod_files', # TODO  allow multiple files to be output
                    metavar='output file(s)',
                    nargs='*',
                    help="file to modify")
parser.add_argument('-i', '--input',
                    metavar='text',
                    default=sys.stdin,
                    help="text with which to replace selection with")
parser.add_argument('--dry',
                    action='store_true',
                    help=("instead of modifying the input files, "
                          "print results of the transformation"))

parser.add_argument('--replace', action='store_true', default=True,
                    help="(default) replace selection")
parser.add_argument('--remove', action='store_true',
                    help="remove selection")
parser.add_argument('--append', action='store_true',
                    help="insert inside selection, after existing content")
parser.add_argument('--prepend', action='store_true',
                    help="insert inside selection, before existing content")
parser.add_argument('--after', action='store_true',
                    help="append to selection")
parser.add_argument('--before', action='store_true',
                    help="prepend to selection")

def run(args):
    for mod_file in args.mod_files:
        with open(mod_file, 'rb') as i:
            d = pq(i.read(), parser='html')

        if isinstance(args.input, file):
            args.input = args.input.read()

        if args.remove:
            d(args.selector).remove()
        elif args.append:
            d(args.selector).append(args.input)
        elif args.prepend:
            d(args.selector).prepend(args.input)
        elif args.after:
            pq(args.input).insertAfter(d(args.selector))
        elif args.before:
            pq(args.input).insertBefore(d(args.selector))
        else: # args.replace is true/assumed true (is the default)
            d(args.selector).html(args.input)

        if not args.dry:
            with open(mod_file, 'wb') as o:
                o.write(str(d))
        else:
            print(d)

def main():
    args = parser.parse_args()
    run(args)
    


