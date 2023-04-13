from utilities import *

if __name__ == "__main__":
    s = Style()
    i = Intro()

    s.style_font()

    a = i.intro_main()

    while True:
        if a == 1:
            print("Input File Type (INTEGER ONLY): ")
            print("1. PDF File (\".pdf\")")
            print("2. Word Document File (\".docx\")")
            print("3. Others (\"Experimental\")")
            tp = int(input())
            print()

            if tp == 1:
                file_type = ".pdf"
            elif tp == 2:
                file_type = ".docx"
            else:
                file_type = input("Enter File Extension (with '.' like \".pdf\", \".docx\", \".dat\"): ")

            file_name = input("File Name: ")
            print()

            file = file_name + file_type

            c = Corrupt(file)
            c.corrupt_func()
            file_path = os.getcwd() + '\\' + file
            print(f"{file} has been saved at {file_path}")
            time.sleep(1)
            print("File Path has been copied")
            pyperclip.copy(file_path)

            print()
            a = i.intro_main()

        else:
            print("Have a Nice Day ;-)")
            exit()