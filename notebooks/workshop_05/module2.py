from .subpackage.module3 import function3

def function2():
    print(f"""this is print stmt from
        module: {__name__}
        in file: {__file__}
    """)

function2()
