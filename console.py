#!/usr/bin/python3
"""Console to begin my application"""
import cmd, sys
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console class begins"""

    prompt = '(hbnb) '
    __classes = ["BaseModel"]
    def do_create(self, line):
        """This create new instance, saves it to json file and prints the id"""

        try:
            if not line:
                print("** class name missing **")
            else:
                new_ins = eval(line)()
                new_ins.save()
                print(new_ins.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of an instance\
        based on the class name and id"""

        args = line.split()
        if len(args) > 2 or len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            stt = args[0] + "." + args[1]
            for obj_id in obj.keys():
                if obj_id == stt:
                    ob = obj[obj_id].copy()
                    for k, v in ob.items():
                        if k == "updated_at" or k == "created_at":
                            ob[k] = datetime.fromisoformat(v)
                    del ob["__class__"]
                    st = "[" + args[0] + "]" + \
                        "(" + args[1] + ")" + str(ob)
                    print(st)
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """

        args = line.split()
        to_del = None
        if len(args) > 2 or len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            stt = args[0] + "." + args[1]
            for obj_id in obj.keys():
                if obj_id == stt:
                    to_del = obj[obj_id]
                else:
                    print("** no instance found **")
            if to_del is not None:
                del to_del
                storage.save()
    def do_quit(self, arg):
        "Quit command to exit the program"

        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        """Pass or do nothing via emptyline"""

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
