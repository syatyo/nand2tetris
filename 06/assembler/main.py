#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
from parser import Parser, CommandType
from code import Code

def main():
    args = sys.argv
    filepath = args[1]

    parser = Parser(filepath=filepath)

    path, ext = os.path.splitext(os.path.basename(filepath))
    hack_file_name = path + '.hack'
    hack_file = open(hack_file_name, 'w')

    # ファイルオープン(書き込み)
    while parser.has_more_commands:
        parser.advance()

        commnad_type = parser.command_type()

        if commnad_type == CommandType.A_COMMAND:
            symbol = parser.symbol()
            a_bin = Code.a_bin(symbol)
            hack_file.write(a_bin)

        elif commnad_type == CommandType.C_COMMAND:
            comp_mnemonic = parser.comp()
            dest_mnemonic = parser.dest()
            jump_mnemonic = parser.jump()

            comp_bin = Code.comp(comp_mnemonic)
            dest_bin = Code.dest(dest_mnemonic)
            jump_bin = Code.jump(jump_mnemonic)

            c_instruction = '100' + comp_bin + dest_bin + jump_bin
            hack_file.write(c_instruction)
    
    hack_file.close()
            
if __name__ == '__main__':
    main()