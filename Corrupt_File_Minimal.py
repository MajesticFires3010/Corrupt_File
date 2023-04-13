from utilities import *

if __name__ == "__main__":
    s = Style()
    a = sys.argv[1]
    i = Intro()

    s.style_font()

    if a == "-h":
        i.intro_minimal()

    else:
        c = Corrupt(a)
        c.corrupt_func()
        file_path = os.getcwd() + '\\' + a
        print(f"{a} has been saved at {file_path}")
        time.sleep(1)
        print("File Path has been copied")
        pyperclip.copy(file_path)