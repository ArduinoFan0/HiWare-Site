import types


def custom_import(path:str, fetch_mode:bool = False, fetch_module:types.ModuleType=None):
    try:
        if not fetch_mode:
            import os
            my_path = os.path.dirname(os.path.abspath(path))
            if os.path.isfile(path):
                module_name = os.path.splitext(os.path.basename(path))[0]
            elif os.path.isdir(path):
                module_name = os.path.basename(path)
                my_path = os.path.join(path, "__init__.py")
            else:
                raise ImportError(f"Cannot import from directory {path}")
            with open(my_path, 'r') as f:
        else:
            if fetch_module is None:
                raise TypeError("fetch_module can't be None if importing using fetch")
            elif not isinstance(fetch_module, types.ModuleType):
                raise TypeError(f"fetch_module must be a module")
            else:
                fetch_module.fetch(path)

    except FileNotFoundError:
        raise ImportError(f"Cannot import from directory {path}")
print('My turn, then theirs')
custom_import('.\\my_module')
my_module.hello()