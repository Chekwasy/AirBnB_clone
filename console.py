#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """quit commadn to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of a given class, saves it, and prints the id"""
        if arg:
            try:
                instance = eval(arg)()
                instance.save()
                print(instance.id)
            except NameError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
            return

    def do_show(self, arg):
        """show string representation of an instance based on the class name and id"""
        args = arg.split()
        objdict = storage.all()

        if args:
            className = args[0]
            if className == "BaseModel":
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = className + "." + instance_id
                    if key in objdict:
                        print(objdict[key])
                    else:
                        print("** no instance found **")

            else:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        objdict = storage.all()

        if args:
            className = args[0]
            if className == "BaseModel":
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = className + "." + instance_id
                    if key in objdict:
                        del objdict[key]
                        storage.save()
                    else:
                        print("** no instance found **")

            else:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if arg == "BaseModel":
            objdict = storage.all()
            listrep = []
            for obj in objdict.values():
                listrep.append(str(obj))
            print(listrep)

        else:
            print("** class doesn't exist **")

    def do_EOF(self, arg):
        """Descriptions: Exits the program"""
        return True

    def emptyline(self):
        """No change to the program"""
        pass

    def run_commands(self, commands):
        for command in commands:
            self.onecmd(command)


    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        objdict = storage.all()

        if args:
            className = args[0]
            if className == "BaseModel":
                if len(args) < 2:
                    print("** instance id missing **")
                    return

                instance_id = args[1]
                key = className + "." + instance_id
                if key not in objdict:
                    print("** no instance found **")
                    return

                if len(args) < 3:
                    print("** attribute name missing **")
                    return

                if len(args) < 4:
                    print("** value missing **")
                    return

                attribute_name = args[2]
                attribute_value = args[3]

                instance = objdict[key]
                setattr(instance, attribute_name, attribute_value)
                instance.save()

            else:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")


if __name__ == '__main__':
    hbnb = HBNBCommand()

    " Check if command-line arguments are provided "
    if len(sys.argv) > 1:
        # Non-interactive mode"            '
        commands = sys.argv[1:]
        hbnb.run_commands(commands)
    else:
        # Interactive mode
        hbnb.cmdloop()

