# this is a simple demo of the --tags feature in opsmop
#
# the '--tags' CLI argument runs only the part of a policy
# with matching tags. Matching one tag is enough to run any
# step.
#
# try the following:
#
# opsmop --apply tags.py --tags a
# opsmop --apply tags.py --tags a,b
# opsmop --apply tags.py --tags c
# opsmop --apply tags.py --tags d 
# opsmop --apply tags.py --tags e
# opsmop --apply tags.py
#
# what resources do you think will run in each invocation?

from opsmop.core.easy import *

class Role1(Role):

    def set_resources(self):
        return Resources(
            Echo("hi1", tags=['c']),
            Echo("hi2")
        )

class Role2(Role):

    def set_resources(self):
        return Resources(
            Echo("hi3"),
            Echo("hi4"),
            Shell("true", signals='demo_evt'),
            Echo("hi5", tags=['e']),
            Echo("hi6", tags=['any'])
        )

    def set_handlers(self):
        return Handlers(
            demo_evt1 = Echo("hi7"),
            demo_evt2 = Echo("hi8")
        )


class Demo(Policy):

    def set_variables(self):
        return dict()

    def set_roles(self):
        return Roles(
            Role1(tags=['a']),
            Role2(tags=['b'])
        )

def main():
    return [ Demo(tags=['d']) ]



