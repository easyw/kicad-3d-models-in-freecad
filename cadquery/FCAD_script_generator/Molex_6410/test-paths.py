import os


destination_dir="/Molex_6410"


full_path=os.path.realpath(__file__)
print('full_path: \n{:s}\n'.format(full_path))


"""
script_dir=os.path.dirname(os.path.realpath(__file__))
print('script_dir: \n{:s}\n'.format(script_dir))
"""

script_dir_name =full_path.split(os.sep)[-2]
print('script_dir_name: \n{:s}\n'.format(script_dir_name))

parent_path = full_path.split(script_dir_name)[0]
print('parent_path: \n{:s}\n'.format(parent_path))


"""
models_dir=sub_path+"_3Dmodels"
print('models_dir:\n{:s}\n'.format(models_dir))

script_dir=os.path.dirname(os.path.realpath(__file__))
print('script_dir:\n{:s}\n'.format(script_dir))

out_dir=models_dir+destination_dir
print('out_dir:\n{:s}\n'.format(out_dir))
"""

my_out_dir = parent_path +"_3Dmodels" + destination_dir
print('my_out_dir:\n{:s}\n'.format(my_out_dir))


my_out_dir = parent_path +"_3Dmodels" + "/" + script_dir_name
print('my_out_dir:\n{:s}\n'.format(my_out_dir))

