import sys

def main():
    if "--help" in sys.argv:
        print("Використання: python src/sys_tool.py [опції]")
        print("Опції:")
        print("\t--help\tпоказати цю підказку")
        sys.exit(0)

    print("командна строка")


if __name__ == "__main__":
    main()
