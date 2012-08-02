#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myportfolio.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jonathanschen.settings")
>>>>>>> 4cc0ec98ecb2e35229d526e02e296f73a0cebafd

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
