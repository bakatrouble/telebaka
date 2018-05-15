import pkg_resources
import importlib
import pkgutil


def prepare_key(key):
    return key.replace('-', '_')


def get_plugins():
    plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in pkgutil.iter_modules()
        if name.startswith('telebaka_')
    }
    keys = [prepare_key(pkg.key) for pkg in pkg_resources.working_set]
    plugins.update({
        key: importlib.import_module(key)
        for key in keys
        if key.startswith('telebaka_')
    })
    return plugins
