#!/usr/bin/python3
"""Console moduleu."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    class_list = ["BaseModel", "User"]

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
            elif args == "User":
                b = User()
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
        storage.save()

    def do_all(self, args):
        args = args.split()
        if len(args) == 0:
            for i in storage.all().values():
                print(str(i))
            return
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        for i in storage.all().values():
            if i.__class__.__name__ == args[0]:
                print(str(i))

    def do_update(self, args):
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
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objects[key]
        value = args[2]
        if isinstance(args[2], int):
            value = int(args[2])
        elif isinstance(args[2], float):
            value = int(args[2])
        setattr(obj, value, args[3])
        storage.save()

        if __name__ == '__main__':
            HBNBCommand().cmdloop()
