import subprocess

folder_in = "/home/zerg/tst"
folder_out = "/home/zerg/out"
folder_ext = "/home/zerg/folder1"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    # Test 1
    res1 = checkout("cd {}; 7z a {}/arx2".format(folder_in, folder_out), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_out), "arx2.7z")
    assert res1 and res2, "Test 1 FAIL"


def test_step2():
    # Test 2
    res1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(folder_out, folder_ext), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_ext), "test1")
    res3 = checkout("ls {}".format(folder_ext), "test2")
    assert res1 and res2 and res3, "Test 2 FAIL"


def test_step3():
    # Test 3
    assert checkout("cd /home/zerg/tst; 7z -t arx2.7z", "Everything is Ok"), "Test 3 FAIL"


def test_step4():
    # Test 4
    assert checkout("cd {}; 7z -u arx2.7z".format(folder_in), "Everything is Ok"), "Test 4 FAIL"


def test_step5():
    # Test 5
    assert checkout("cd {}; 7z -d arx2.7z".format(folder_in), "Everything is Ok"), "Test 5 FAIL"


def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False


def test_checkout_negative_ls():
    # Test 6
    assert checkout_negative("ls /nonexistent_directory", "No such file or directory"), "Test 6 FAIL"


def test_checkout_negative_x():
    # Test 7
    assert checkout_negative("7z x /nonexistent_file.7z -o/nonexistent_directory", "Error:"), "Test 7 FAIL"


def test_checkout_hash():
    # Test 8
    hash_output = subprocess.run("7z h arx2.7z", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    hash_lines = hash_output.stdout.splitlines()
    hash_line = hash_lines[-1]
    crc32_hash = hash_line.split()[-1]
    assert crc32_hash == "calculated_crc32_hash", "Test 8 FAIL"