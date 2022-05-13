import glob
import os
#
#
# # Exercise 1
# initial_path = os.getcwd()
#
# # v1
# os.mkdir('outdir')
# os.chdir('outdir')
# os.mkdir('innerdir')
#
# file_path = os.path.join('innerdir', 'empty.txt')
#
# with open(file_path, 'w'):
#     pass
#
# for path, dirnames, filenames in os.walk('.'):
#     print(path, dirnames, filenames)
#
# os.remove(file_path)
#
# # v1.1
# # os.rmdir('innerdir')
# # os.rmdir(os.getcwd())
#
# # v.1.2
# os.removedirs(os.path.join(os.getcwd(), 'innerdir'))
#
#
# # v2
# os.chdir(initial_path)
#
# outdir_path = 'outdir'
# innerdir_path = os.path.join(outdir_path, 'innerdir')
# empty_file_path = os.path.join(innerdir_path, 'empty.txt')
#
# os.makedirs(innerdir_path)
#
# with open(empty_file_path, 'w'):
#     pass
#
# for path, dirnames, filenames in os.walk(outdir_path):
#     print(path, dirnames, filenames)
#
# os.remove(empty_file_path)
# os.removedirs(innerdir_path)
#


# Exercise 2

def get_directory_tree(path, extension, intermediate_dirs=False,
                       recursive=False):
    path_components = [path, f'*.{extension}']
    print('1. path_components:', path_components)
    if intermediate_dirs:
        path_components.insert(1, '**')
    print('2. path_components:', path_components)

    pattern = os.path.join(*path_components)
    # os.path.join(path_components[0], path_components[1])
    print('3. pattern:', pattern)

    return glob.glob(pattern, recursive=recursive)


print(get_directory_tree('.', 'py'), end='\n\n')
print(get_directory_tree('..', 'py', intermediate_dirs=True), end='\n\n')
print(get_directory_tree('..', 'py', intermediate_dirs=True, recursive=True), end='\n\n')


