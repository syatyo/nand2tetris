#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum

class CommandType(Enum):
    A_COMMAND = 0
    C_COMMAND = 1
    L_COMMAND = 2

class Parser:

    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.lines = file.readlines()
            self.cursor = 0
            self.command = ""
    
    def has_more_commands(self):
        return self.cursor + 1 < len(self.lines)
    
    def advance(self):
        if self.has_more_commands():
            self.cursor += 1
            command = self.lines[self.cursor]

            # 空白文字のストリップ
            self.command = command.strip()

            if self.command.startswith('//'):
                self.advance()
            elif not self.command:
                self.advance()

    def command_type(self):
        if self.command.startswith('@'):
            return CommandType.A_COMMAND
        elif self.command.startswith('('):
            return CommandType.L_COMMAND
        else:
            return CommandType.C_COMMAND
    
    def symbol(self):
        if self.command_type == CommandType.A_COMMAND:
            return self.command[1:]
        else:
            last_char_index = len(self.command) - 1
            return self.command[1:last_char_index-1]
    
    def dest(self):
        dest_index = self.command.find('=')
        if dest_index == -1:
            return "null"
        
        mnemonic = self.command[:dest_index-1]
        return mnemonic
    
    def comp(self):
        # destかcompか、どちらか一方は空かもしれない。
        dest_index = self.command.find('=')
        comp_index = self.command.find(';')

        if dest_index == -1:
            return self.command[:comp_index-1]
        
        if comp_index == -1:
            return self.command[comp_index+1:]
    
    def jump(self):
        jump_index = self.command.find(';')
        if jump_index == -1:
            return 'null'
        else:
            return self.command[jump_index+1:]
    


