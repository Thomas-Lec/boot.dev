import os

def get_files_info("calculator", directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs,directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if os.path.isdir(working_dir_abs) == False:
        return f'Error: "{working_dir_abs}" is not a directory'

    try:

        for target_dir_item in target_dir:
            file_size = os.path.getsize(target_dir_item)
            is_dir = os.path.isdir(target_dir_item)
        return f"- {target_dir_item}: file_size={file_size} bytes, is_dir={isdir}"

    except Exception as e:
        return f"Error: unexpected Error occured {e}" 

