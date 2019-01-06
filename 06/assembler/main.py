import sys, os
from parser import Parser
from code import Code

if __name__ == '__main__':
    main()

def main():
    args = sys.argv
    filepath = args[1]

    parser = Parser(filepath=filepath)

    path, ext = os.path.splitext(os.path.basename(filepath))
    binary_file_name = path + '.hack'
    binary_file = open(binary_file_name, 'w')
    # ファイルオープン(書き込み)
    while parser.has_more_commands:
        parser.advance()

        commnad_type = parser.command_type()


