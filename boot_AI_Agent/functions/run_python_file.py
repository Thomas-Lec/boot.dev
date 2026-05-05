import os, subprocess
from config import *

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, target_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_path]
        if args is not None:
            command.extend(args)
        

        result_subproc = subprocess.run(command,cwd=target_path,
                                        capture_output=True,
                                        text=True,
                                        timeout=30, 
                                        check=True)
        
        if result_subproc.returncode > 0:
            result += f"Process exited with code {result_subproc.returncode}"
        elif result_subproc.stderr == None or result_subproc.stdout == None:
            result += f"No output produced"
        else:
            result +=f"STDOUT: {result_subproc.stdout} STDERR: {result_subproc.stderr}"

        return result

    except Exception as e:
        return f"Error: executing Python file: {e}"
