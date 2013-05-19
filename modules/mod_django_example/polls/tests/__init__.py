from os import path
import glob
import os


# code to test selection
def get_tests(dirname):
    tests = [os.path.basename(f)[:-3] for f in glob.glob(os.path.join(dirname, "tests_*.py"))]
    enabled_modules = []
    for test in tests:
        tokens = test.split("_")
        module = ".".join(dirname.split(os.path.sep)[-2:]) + "." + test
        enabled_modules.append(__import__(module, globals(), locals(), ['*']))

    return enabled_modules

# __file__ is the name of current file in python, always filled
test_modules = get_tests(path.dirname(__file__))

for test_ in test_modules:
    for k in dir(test_):
        locals()[k] = getattr(test_, k)
