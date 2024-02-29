#!/usr/bin/python3
"""Console module"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    class_list = ["BaseModel"]

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

    def do_create(self, args):
        """Do create"""
        if args:
            if args == "BaseModel":
                b = BaseModel()
                print(b.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        storage.save()

    def do_show(self, args):
        """Do show"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        id = args[1]
        key = "{}.{}".format(class_name, id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, args):
        """Do destroy"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
                class_name = args[0]
        id = args[1]
        key = "{}.{}".format(class_name, id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]

    def do_all(self, arg):
        result_list = []
        if arg is None:
            return storage.all()
        if arg not in class_list:
            print("** class doesn't exist **")
            return
        keys = storage.all().keys()
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
