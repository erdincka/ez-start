# Ranger configuration

## Install packages

https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/AdvancedInstallation/InstallingRanger.html

Check mysql if `ranger` db and user created, if not, follow the documentation to create them.

If Installer is used, these should be created already.


## Configure Ranger

https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/Ranger/ConfigureRanger.html

Change these:

```ini
rangerAdmin_password=CHANGEME
rangerTagsync_password=CHANGEME
rangerUsersync_password=CHANGEME
keyadmin_password=CHANGEME
```

And run:

`/opt/mapr/ranger/ranger-2.4.0/ranger-admin/setup.sh`

This will take few minutes to complete. Once ready, re-configure the cluster:

`/opt/mapr/server/configure.sh -R`


## Configure Ranger for HiveServer2

https://docs.ezmeral.hpe.com/datafabric-customer-managed/78/Ranger/Integrate_HiveServer2_with_Ranger.html

## Configure Policies

TBD.
