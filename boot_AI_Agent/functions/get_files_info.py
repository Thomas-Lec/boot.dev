import os

def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs,directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if os.path.isdir(target_dir) == False:
        return f'Error: "{target_dir}" is not a directory'

    try:

        results = []
        for target_dir_item in os.listdir(target_dir):
            file_size = os.path.getsize(os.path.join(target_dir, target_dir_item))
            is_dir = os.path.isdir(os.path.join(target_dir, target_dir_item))
            results.append(f"- {target_dir_item}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(results)

    except Exception as e:
        return f"Error: unexpected Error occured {e}" 

