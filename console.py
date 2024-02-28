#!/usr/bin/python3
"""Console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command"""
        return True

    def do_EOF(self, arg):
        """EOF command"""
        print()
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_help(self, args):
        """Help function"""
        cmd.Cmd.do_help(self, args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
