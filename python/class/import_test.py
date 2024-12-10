import practice
import submodule.subpackage

def main():
    blah = practice.Practice()
    blah.add(1)
    print(blah)

    foo = submodule.subpackage.Foo()

if __name__ == "__main__":
    main()