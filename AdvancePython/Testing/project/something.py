from subprocess import check_output

def print_content_of_cwd():
    return check_output(['ls']).split()
