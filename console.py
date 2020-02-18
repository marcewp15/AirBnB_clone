#!/usr/bin/python3

import cmd
#from models.storage import FileStorage
from models import storage
from models.base_model import BaseModel

classes = ['BaseModel']


class HBNBCommand(cmd.Cmd):
    """ the command interpreter of AirBnB project """
    prompt = '(hbnb) '
    classes = ['BaseModel']

    def do_create(self, args):
        """ create a new instance of a class and prints the id """
        #classes = ['BaseModel']
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
        """ Prints the json file of an instance of a class name and id """
        #classes = ['BaseModel']
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
        for key, value in all_objs.items():
            if s in key:
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    print(obj)
                    return
        print("** no instance found **")
        pass

    def do_all(self, args):
        """ Prints all string representation of all instances """
        #classes = ['BaseModel']
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
        """  """
        #classes = ['BaseModel']
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
        for key, value in all_objs.items():
            if s in key:
                del all_objs[str(s)]
                storage.save()
                return
        print("** no instance found **")

    def do_update(self, args):
        """ """
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
        if len(words) == 2:
            print("** attribute name missing **")
            return
        if len(words) == 3:
            print("** value missing **")
            return
        s1 = 'BaseModel' + '.' + words[1]
        all_objs = storage.all()
        for key, value in all_objs.items():
            if s1 in key:
                up = BaseModel.to_dict(self)
                up[words[2]] = words[3]
                storage.save()
                return
        print("** no instance found **")

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
