#!/usr/bin/python3
"""Console to begin my application"""
import cmd
import sys
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Console class begins"""

    prompt = '(hbnb) '
    __classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

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
            if_true = False
            for obj_id in obj.keys():
                if obj_id == stt:
                    print(obj[obj_id])
                    if_true = True
            if if_true is False:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """

        args = line.split()
        to_del = None
        found = False
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
                    to_del = obj_id
                    found = True
            if found is False:
                print("** no instance found **")
            if to_del is not None:
                del obj[to_del]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or
        not on the class name."""

        found = False
        insts = storage.all()
        alll = []
        if not line:
            for k in insts.keys():
                alll.append(str(insts[k]))
                found = True
            print(alll)
        else:
            for obj_id in insts.keys():
                arr = obj_id.split(".")
                if arr[0] == line:
                    alll.append(str(insts[obj_id]))
                    found = True
            if len(alll) > 0:
                print(alll)
        if found is False:
            print("** class doesn't exist **")

    def default(self, line):
        """Handle defaults stuff."""

        d_line = line.split(".")
        if d_line[1] == "all()":
            self.do_all(d_line[0])
        if d_line[1] == "count()":
            self.count(d_line[0])
        if d_line:
            fir = d_line[1].split("(")
            if fir[0] == "show":
                lst = fir[1].split(")")
                self.do_show(d_line[0] + " " + lst[0])
        if d_line:
            fir = d_line[1].split("(")
            if fir[0] == "destroy":
                lst = fir[1].split(")")
                self.do_destroy(d_line[0] + " " + lst[0])

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""

        args = line.split()
        found = False
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            for obj_id in obj.keys():
                arr = obj_id.split(".")
                if arr[1] == args[1]:
                    ins = obj[obj_id]
                    found = True
            if found is False:
                print("** no instance found **")
            if len(args) == 2:
                print("** attribute name missing **")
            if len(args) == 3:
                print("** value missing **")
            if len(args) == 4 and found is True:
                a = args[3]
                b = a.split("\"")
                setattr(ins, args[2], b[1])
    def count(self, line):
        """Prints total instance based on class"""

        found = False
        insts = storage.all()
        tol = 0
        for obj_id in insts.keys():
            arr = obj_id.split(".")
            if arr[0] == line:
                tol = tol + 1
                found = True
        if found is True:
            print(tol)
        if found is False:
            print("** class doesn't exist **")

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
