from behave import fixture


@fixture
def start_mock_server():
    import subprocess
    list_files = subprocess.run(["ls", "-l"])
    print("The exit code was: %d" % list_files.returncode)
