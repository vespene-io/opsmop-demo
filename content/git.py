from opsmop.core.easy import *

# cd thisdir
# python3 git.py --local --check
# python3 git.py --local --apply

class GitRole(Role):

    def set_variables(self):
        return dict()

    def set_resources(self):
        return Resources(
            Git(action="clone", repository="https://github.com/opsmop/opsmop"),
        )

    def set_handlers(self):
        return Handlers(
            file_changed = Echo("repo cloned")
        )

class Demo(Policy):

    def set_variables(self):
        return dict()

    def set_roles(self):
        roles = [ GitRole() ]
        return Roles(*roles)

if __name__ == '__main__':
    Cli(Demo())

