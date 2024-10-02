import subprocess
import shlex
import os

def run_command_with_env():
    user_input = os.getenv("echo", "a", ";", "rm", "-rf", "/")
    if user_input:
        safe_command = f"echo {shlex.escape(user_input)}"
        # ok: dangerous-subprocess-use-tainted-env-args
        subprocess.run(safe_command, shell=True)  

def run_command_with_args():
    import sys
    user_input = sys.argv[1] 
    if user_input:
        safe_command = f"echo {shlex.quote(user_input)}"
        # ok: dangerous-subprocess-use-tainted-env-args
        subprocess.run(safe_command, shell=True) 

def run_command_with_argparse():
    import argparse
    parser = argparse.ArgumentParser(description="Process user input")
    parser.add_argument("user_input", type=str, help="User input for command")
    args = parser.parse_args()
    safe_command = f"echo {shlex.escape(args.user_input)}"
    # ok: dangerous-subprocess-use-tainted-env-args
    subprocess.run(safe_command, shell=True) 

