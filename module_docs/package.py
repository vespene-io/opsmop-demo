# MODULE:     package
# PURPOSE:    installs, removes, and upgrades packages
# CATEGORY:   general
# PROVIDERS:  package.apt, package.brew, package.yum, package.dnf, package.pacman
# RELATED:    file, service
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# The package module is used to install packages. The default provider for the operating
# system (for example, 'apt') is used unless the parameter 'method' is supplied to
# pick an alternate provider.  See :ref:`method`.
# =======================================================================================

from opsmop.core.easy import *
import getpass
USERNAME = getpass.getuser()

# --------------------------------------------------------------------------------------
# EXAMPLE: Basic Example
#
# DESCRIPTION:
#
# Installing and removing a package.
# =======================================================================================

class BasicExample(Role):

    def set_variables(self):
        return dict(a=1, b=5150, c="badwolf")

    def main(self):

        # explicit package provider selection works like this
        # Package(name='cowsay', method='yum')

        # uninstall
        Package(name='cowsay', absent=True)

        # install
        Package(name='cowsay')




# ---------------------------------------------------------------------------------------
# SETUP: a helper role that sets up for this demo
# =======================================================================================

class CommonSetup(Role):

    def main(self):
        pass

# ---------------------------------------------------------------------------------------
# POLICY: loads all of the above roles
# =======================================================================================

class Demo(Policy):

    def set_roles(self):
       return Roles(
           CommonSetup(),
           BasicExample(),
       )

if __name__ == '__main__':
    Cli(Demo())




 
