import subprocess
import os

def run_cpp(program, *inputs):
    """
    Run a compiled C++ executable and pass inputs via stdin.
    program: full path to .exe file
    inputs: each argument is one line of input
    """
    cpp_path = program

    if not os.path.exists(cpp_path):
        raise FileNotFoundError(f"Executable not found: {cpp_path}")

    stdin_input = "\n".join(map(str, inputs)) + "\n"

    result = subprocess.run(cpp_path, input=stdin_input, capture_output=True, text=True)
    return result.stdout.strip()
