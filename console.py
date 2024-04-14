#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
import cmd, sys
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """this command marks the end of command"""
        return True
    
    def emptyline(self):
        """Do"""
        pass

    def do_create(self, arg):
        """command to create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        if arg in globals():
            model = eval(arg)()
            model.save()
            print(model.id)
        else:
            print("** class doesn't exist **")
    def do_show(self, args):
        cls = args.split()
        if not cls:
            print("** class name missing **")
            return
        cls_name = cls[0]
        if cls_name not in globals():
                print("** class doesn't exist **")
                return
        if len(cls) < 2:
            print('** instance id missing **')
            return
        all_obj = storage.all()
        found_inst = False
        for key in all_obj.keys():
            key_name, key_id = key.split('.')
            if key_id == cls[1]:
                print(all_obj[key])
                found_inst = True
                break
        if not found_inst:
            print("** no instance found **")
    def do_destroy(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in globals():
            print("** class doesn't exist **")
            return
        all_obj = storage.all()
        found_inst = False
        for key in all_obj.keys():
            key_name, key_id = key.split('.')
            if key_id == args[1]:
                del all_obj[key]
                model = eval(key_name)(**all_obj)
                model.save()
                found_inst = True
                break
        if not found_inst:
            print("** no instance found **")
    
    def do_all(self, arg):
        all_li = []
        all_obj = storage.all().values()
        if not arg:
            for key in all_obj:
                all_li.append(str(key))
            print(all_li)
        else:
            if arg not in globals():
                print("** class doesn't exist **")
            else:
                for key in all_obj:
                    all_li.append(str(key))
            print(all_li)
        
    def do_update(self, arg):
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        if len(args) == 4:
            cls_name, cls_id, atr_name, atr_val = args[0:]
            if atr_name in ['id', 'created_at', 'updated_at']:
                return
            if cls_name not in globals():
                print("** class doesn't exist **")
            else:
                found = False
                all_objs = storage.all()
                for keys in all_objs:
                    key_name, key_id = keys.split('.')
                    if key_id == cls_id:
                        setattr(all_objs[keys], atr_name, eval(atr_val))
                        model = eval(cls_name)(**all_objs)
                        model.save()
                        found = True
                if not found:
                     print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
