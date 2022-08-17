#!/usr/bin/python3
import sys, argparse

class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

def print_usage():
    print(' Usage: ' + sys.argv[0] + ' \'text to encode\'')

def print_help():
    print_usage()
    parser.print_help()

if __name__ == '__main__':
    print(bcolors.HEADER + '*************************************************' + bcolors.ENDC)
    print(bcolors.HEADER + '**          MORSE STRING (EN/DE)CODER          **' + bcolors.ENDC)
    print(bcolors.HEADER + '*************************************************' + bcolors.ENDC)
    print(bcolors.HEADER + '**          Author: David Shahbazyan           **' + bcolors.ENDC)
    print(bcolors.HEADER + '**         Version: 1.0                        **' + bcolors.ENDC)
    print(bcolors.HEADER + '**    Release Date: 17 Jan, 2019               **' + bcolors.ENDC)
    print(bcolors.HEADER + '*************************************************' + bcolors.ENDC)

    parser=argparse.ArgumentParser()
    parser.add_argument('-e', '--encode', help='String to encode')
    parser.add_argument('-d', '--decode', help='String to decode (separate symbols with spaces)')

    if len(sys.argv) == 1:
        print_help()
        sys.exit(1)
    else:
        args = parser.parse_args()
        if args.encode:
            alphabet = {
                'A':'.-',       'B':'-...',     'C':'-.-.',    'D':'-..',     'E':'.',       'F':'..-.',
                'G':'--.',      'H':'....',     'I':'..',      'J':'.---',    'K':'-.-',     'L':'.-..',
                'M':'--',       'N':'-.',       'O':'---',     'P':'.--.',    'Q':'--.-',    'R':'.-.',
                'S':'...',      'T':'-',        'U':'..-',     'V':'...-',    'W':'.--',     'X':'-..-',
                'Y':'-.--',     'Z':'--..',     '1':'.----',   '2':'..---',   '3':'...--',   '4':'....-',
                '5':'.....',    '6':'-....',    '7':'--...',   '8':'---..',   '9':'----.',   '0':'-----',
                ' ':'  ',       '.':'.-.-.-',   ',':'--..--',  '+':'.-.-.',   '-':'-....-',  '/':'-..-.',
                '*':'*',        '=':'-...-',    '_':'..--.-',  ':':'---...',  ';':'-.-.-.',  '?':'..--..',
                '!':'-.-.--',   '\'':'.----.',  '"':'.-..-.',  '(':'-.--.',   ')':'-.--.-',  '&':'.-...',
                '$':'...-..-',  '@':'.--.-.'
            }
            result = ''
            for key in list(args.encode):
                key = key.upper()
                if key in alphabet:
                    result += alphabet[key] + ' '
            print(result)
        elif args.decode:
            alphabet = {
                '.-':'A',       '-...':'B',     '-.-.':'C',    '-..':'D',     '.':'E',       '..-.':'F',
                '--.':'G',      '....':'H',     '..':'I',      '.---':'J',    '-.-':'K',     '.-..':'L',
                '--':'M',       '-.':'N',       '---':'O',     '.--.':'P',    '--.-':'Q',    '.-.':'R',
                '...':'S',      '-':'T',        '..-':'U',     '...-':'V',    '.--':'W',     '-..-':'X',
                '-.--':'Y',     '--..':'Z',     '.----':'1',   '..---':'2',   '...--':'3',   '....-':'4',
                '.....':'5',    '-....':'6',    '--...':'7',   '---..':'8',   '----.':'9',   '-----':'0',
                '  ':' ',       '.-.-.-':'.',   '--..--':',',  '.-.-.':'+',   '-....-':'-',  '-..-.':'/',
                '*':'*',        '-...-':'=',    '..--.-':'_',  '---...':':',  '-.-.-.':';',  '..--..':'?',
                '-.-.--':'!',   '.----.':'\'',  '.-..-.':'"',  '-.--.':'(',   '-.--.-':')',  '.-...':'&',
                '...-..-':'$',  '.--.-.':'@'
            }
            result = ''
            for key in args.decode.split(' '):
                if key in alphabet:
                    result += alphabet[key]
            print(result)
        else:
            print_help()
