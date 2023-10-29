import pathlib

p_file = pathlib.Path('test/test2.txt')
print(p_file.exists())

p_file = pathlib.Path('test/test3.txt')
print(p_file.exists())

p_dir = pathlib.Path('test')
print(p_dir.exists())
print(list(p_dir.iterdir()))

p_dir = pathlib.Path('test2')
if not p_dir.exists():
    p_dir.mkdir()
