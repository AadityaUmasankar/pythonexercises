import os

os.chdir(r'C:\Users\U Aaditya\Downloads\Lynda - Python 3 Essential Training')

print(os.getcwd())
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    f_1, f_2, f_3, f_4, f_5 = file_name.split('_')
    new_name = '{}-{}-{}{}'.format(f_2,f_3,f_5,file_ext)

    os.rename(f,new_name)
