#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Code:

    def a_bin(a_instruction):
        return a_instruction.format('016b')

    def dest(mnemonic):

        if mnemonic == 'null':
            return '000'
        elif mnemonic == 'M':
            return '001'
        elif mnemonic == 'D':
            return '010'
        elif mnemonic == 'MD':
            return '011'
        elif mnemonic == 'A':
            return '100'
        elif mnemonic == 'AM':
            return '101'
        elif mnemonic == 'AD':
            return '110'
        elif mnemonic == 'AMD':
            return '111'

    def comp(mnemonic):
        if mnemonic == '0':
            return '101010'
        elif mnemonic == '1':
            return '111111'
        elif mnemonic == '-1':
            return '111010'
        elif mnemonic == 'D':
            return '001100'
        elif mnemonic == 'A':
            return '110000'
        elif mnemonic == 'M':
            return '110000'
        elif mnemonic == '!D':
            return '001101'
        elif mnemonic == '!A':
            return '110001'
        elif mnemonic == '!M':
            return '110001'
        elif mnemonic == '-D':
            return '001111'
        elif mnemonic == '-A':
            return '110011'
        elif mnemonic == '-M':
            return '110011'
        elif mnemonic == 'D+1':
            return '011111'
        elif mnemonic == 'A+1':
            return '110111'
        elif mnemonic == 'M+1':
            return '110111'
        elif mnemonic == 'D-1':
            return '001110'
        elif mnemonic == 'A-1':
            return '110010'
        elif mnemonic == 'M-1':
            return '110010'
        elif mnemonic == 'D+A':
            return '000010'
        elif mnemonic == 'D+M':
            return '000010'
        elif mnemonic == 'D-A':
            return '010011'
        elif mnemonic == 'D-M':
            return '010011'
        elif mnemonic == 'A-D':
            return '000111'
        elif mnemonic == 'M-D':
            return '000111'
        elif mnemonic == 'D&A':
            return '000000'
        elif mnemonic == 'D&M':
            return '000000'
        elif mnemonic == 'D|A':
            return '010101'
        elif mnemonic == 'D|M':
            return '010101'

    def jump(mnemonic):

        if mnemonic == 'null':
            return '000'
        elif mnemonic == 'JGT':
            return '001'
        elif mnemonic == 'JEQ':
            return '010'
        elif mnemonic == 'JGE':
            return '011'
        elif mnemonic == 'JLT':
            return '100'
        elif mnemonic == 'JNE':
            return '101'
        elif mnemonic == 'JLE':
            return '110'
        elif mnemonic == 'JMP':
            return '111'
