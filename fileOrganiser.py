import os,shutil

# NOTE: You can write every single extensions inside tuples

dict_extension = {
    'audio_extensions' : {'.mp3','.m4a','wav','flac'},
    'video_extensions' : {'.mp4','.mkv','MKV','flav','mpeg'},
    'document_extensions' : {'.doc','.pdf','.txt'},
    'image_extension' : {'.jfif','.jpg','.png'},
}

folderpath = input('Enter folder path : ')

def file_finder(folder_path, file_extension):
    files=[]
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files

for extension_type,extension_tuple in dict_extension.items():
    # print('calling file finder')
    # print(file_finder(folderpath,extension_tuple))
    folder_name = extension_type.split('_')[0]+'files'
    folder_path = os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath,extension_tuple):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)
