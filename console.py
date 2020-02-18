#!/usr/bin/python3

import cmd
#from models.storage import FileStorage
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ the command interpreter of AirBnB project """
    prompt = '(hbnb) '
    classes = ['BaseModel']
    def do_create(self, args):
        """ """
        classes = ['BaseModel']
        if len(args) == 0:
            print("** class name missing **")
        elif args not in classes:
            print("** class doesn't exist **")
        else:
            a = BaseModel()
            print(a.id)
            a.save()
        pass

    def do_show(self, args):
        """ """
        classes = ['BaseModel']
        words = args.split(' ')
        if len(args) == 0:
            print("** class name missing **")
            return
        elif words[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(words) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        s = 'BaseModel' + '.' + words[1]
        for key , value in all_objs.items():
            if s  in key:
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    print(obj)
                    return
        print("** no instance found **")
        pass

    def do_all(self, args):
        """

        """
        classes = ['BaseModel']
        if len(args) == 0:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        elif args not in classes:
            print("** class doesn't exist **")
        elif 'BaseModel' in classes:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)


    def do_destroy(self, args):
        """

        """
        classes = ['BaseModel']
        words = args.split(' ')
        if len(args) == 0:
            print("** class name missing **")
            return
        elif words[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(words) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        s = 'BaseModel' + '.' + words[1]
        for key , value in all_objs.items():
            if s in key:
                del all_objs[str(s)]
                storage.save()
                return
        print("** no instance found **")

    def do_update(self):
        """

        """
        print("I am UPDATE")

    def emptyline(self):
        """ Method called when an empty line is entered in response
        to the prompt."""
        pass

    def do_EOF(self, line):
        """ Ctrl D - the program will exit cleanly"""
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
