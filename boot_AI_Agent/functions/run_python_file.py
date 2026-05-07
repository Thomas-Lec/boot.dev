import os, subprocess
from config import *

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, absolute_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", absolute_file_path]
        if args is not None:
            command.extend(args)
        

        result_subproc = subprocess.run(command,cwd=abs_working_dir,
                                        capture_output=True,
                                        text=True,
                                        timeout=30)
        
        result = [] 
        if result_subproc.returncode != 0:
            result.append(f"Process exited with code {result_subproc.returncode}")

        if result_subproc.stderr == "" and result_subproc.stdout == "":
            result.append(f"No output produced")

        if result_subproc.stdout:
            result.append(f"STDOUT: {result_subproc.stdout}")

        if result_subproc.stderr:
            result.append(f"STDERR: {result_subproc.stderr}")

        return  "\n".join(result)

    except Exception as e:
        return f"Error: executing Python file: {e}"
