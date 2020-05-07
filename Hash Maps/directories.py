'''
/foo
    /text
        /images.txt (1)
    /files
        /bar.txt (2)

    /car.bat (1)
    /yard.lat (2)
    /shard.tat (2)
    /one.yat (3)

Input: /foo
Output: [[/foo/text/images.txt, /foo/car.bat], []]

images.txt:
    "hi hello"

car.bat:
    "hi hello"

'''
# implement
def duplicate_files(root_dir):
    directories = mock_ls(root_dir)
    dirs = []
    while directories is not None:
        files = root_dir #/foo
        popped = directories.pop() #/text
        files = concat_file(files, popped) #/foo/text
        data = mock_ls(popped) #images.txt
        if data:
            tempfiles = files
            for val in data:
                files = concat_file(files, val)
                directories.append(files)
                files = tempfiles
        else:
            dirs.append(files)
    
    valuedict = {}
    duplicates = [] 
    for path in dirs:
        value = read_file(path)
        value = hash(value)
        if value in valuedict.keys():
            valuedict[value].append(path)
            #append to list that corresponds to key
            #output a list with the two directories 
        else:
            valuedict[value] = [path]

    for k,v in valuedict:
        if v.length > 1:
            duplicates.append(valuedict[value])
    return duplicates

def mock_ls(dir):
    pass

def concat_file(dir, sub_directory):
    # dir = /foo
    # sub_directory = /text
    # output -> /foo/text
    pass

def read_file(file):
    # "hi hello"
    # return string
    pass
    