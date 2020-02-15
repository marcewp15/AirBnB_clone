#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """ the command interpreter of AirBnB project """
    prompt = '(hbnb) '

    def emptyline(self):
        """ Method called when an empty line is entered in response
        to the prompt. If this method is not overridden, it repeats
        the last non-empty command entered. """
        pass

    def do_EOF(self, line):
        """ Ctrl D - the program will exit cleanly"""
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
