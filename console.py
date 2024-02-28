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
        """Empty"""
        return False

    def postcmd(self, stop, line):
        """Post cmd function"""
        self.doc_header = "Commands (type help <topic>):"
        self.misc_header = "Miscellaneous help topics:"
        self.undoc_header = "Undocumented commands:"
        return stop


if __name__ == '__main__':
    HBNBCommand().cmdloop()