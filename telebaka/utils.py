import importlib
import pkgutil


def get_plugins():
    return {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in pkgutil.iter_modules()
        if name.startswith('telebaka_')
    }
