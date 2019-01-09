# MODULE: network
# PURPOSE: configures network interfaces
# CATEGORY: general
# PROVIDERS: network.sysconfig
# FYI: See the online documentation for the full parameter list
#
# DESCRIPTION:
#
# The network module is used to either generate configuration files, or directly configure
# network interface cards. The default provider for the OS (I.E. Sysconfig for
# Centos/RHEL/Fedora)  is used unless the parameter 'method' is supplied to the Interfaces
# resource. Note that Interface cannot be directly returned as a resource,
# all Interface objects must be added to an Interfaces object, which is then returned as a resource.

from opsmop.core.easy import *
import getpass
USERNAME = getpass.getuser()

# --------------------------------------------------------------------------------------
# EXAMPLE: Basic Example
#
# DESCRIPTION:
#
# Setting up an interface with static IP and DNS servers.
# Warning: Running this example could cause your system to loose it's connection!
# =======================================================================================

class BasicExample(Role):

    def set_resources(self):
        inter = Interface(
            device='eth0',
            ipv4_address='192.168.1.1',
            ipv4_netmask='255.255.255.0',
            dns=['8.8.8.8', '8.8.4.4'],
            on_boot=True,
            boot_proto='static'
        )
        return Resources(
            Interfaces(
                inter,
                auto_reload=True,
                force=False
            )
        )

# ---------------------------------------------------------------------------------------
# SETUP: a helper role that sets up for this demo
# =======================================================================================

class CommonSetup(Role):

    def set_resources(self):
        return Roles(
        )

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
