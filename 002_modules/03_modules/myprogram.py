# モジュールのimport
from mymodule import my_func, my_func2

# パッケージのimport
from my_package import some_main_script
from my_package.sub_package import some_sub_script


def main():
    my_func()
    my_func2()

    some_main_script.sub_report()
    some_sub_script.sub_report()


# ここから実行された場合のみ、mainを実行する
if __name__ == "__main__":
    main()
