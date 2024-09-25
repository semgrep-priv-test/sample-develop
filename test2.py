import json
import subprocess
import sys
import django

def a(request):
    ip = request.POST.get("ip")
    # ruleid:subprocess-injection
    subprocess.run("ping "+ ip)

def b(request):
    host = request.headers["HOST"]
    # ruleid:subprocess-injection
    subprocess.run("echo {} > log".format(host))
