class Practice:
    class_var = []
    
    def __init__(self):
        self.instance_var = []

    def add(self, value):
        self.class_var.append(value)
        self.instance_var.append(value)

    def __str__(self):
        return f"class_var: {self.class_var} instance_var: {self.instance_var}"


def main():
    instance = Practice()
    instance.add(1)

    instance2 = Practice()
    instance2.add(2)

    print(instance)
    print(instance2)

if __name__ == "__main__":
    main()