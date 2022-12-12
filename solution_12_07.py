class FileSystemObject:
    size = 0
    parent = None

    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return(self.name)

    def get_parent(self):
        return self.parent
    
    def set_parent(self, obj):
        self.parent = obj
    
    def get_size(self):
        return self.size

    def __str__(self) -> str:
        return f'{self.name}'


class Directory(FileSystemObject):
    def __init__(self, name):
        self.name = name
        self.content = []

    def add_content(self, obj):
        obj.set_parent(self)
        self.content.append(obj)

    def get_content(self, name=None):
        if not name:
            return self.content
        
        for obj in self.content:
            if obj.get_name() == name:
                return obj
        return None

    def set_size(self, new_size: int):
        self.size = new_size
    
    def update_size(self):
        self.size = self.__calculate_size()

    def __str__(self) -> str:
        return "\n".join([obj.get_name() for obj in self.content])

    def __calculate_size(self):
        if not self.content:
            return 0

        new_size = 0   
        for obj in self.content:
            if type(obj).__name__ == "File":
                new_size += obj.get_size()
            else:
                new_size += obj.__calculate_size()
        
        self.set_size(new_size)
        return new_size

class File(FileSystemObject):
    def __init__(self, name, size: int):
        self.name = name
        self.size = size

    def __str__(self) -> str:
        return f'{self.name} ({self.size})'

def reconstruct_filesystem(command_history: list[str]):
    root = Directory("/")
    current_dir = root
    for line in command_history:
        if line[:4] == "$ ls":
            next
        elif line[:4] == "$ cd":
            arg = line[5:]
            if(arg == ".."):
                current_dir = current_dir.get_parent()
            elif(arg == "/"):
                current_dir = root
            else:
                current_dir = current_dir.get_content(arg)

        else:
            line_split = line.split(" ")
            if(line_split[0] == "dir"):
                obj = Directory(name = line_split[1] )
            else:
                obj = File(name = line_split[1], size = int(line_split[0]))

            current_dir.add_content(obj)

    root.update_size()

    return root

def sum_directory_size(dir: FileSystemObject, max_size = 100000): 
    subdirs = [obj for obj in dir.get_content() if type(obj).__name__ == "Directory"]
    if not dir.get_content():
        return 0
    
    if dir.get_size() < max_size:
        total_size = dir.get_size()
    else:
        total_size = 0
        
    for subdir in subdirs:
        total_size += sum_directory_size(subdir)

    return total_size

def collect_directory_sizes(dir: FileSystemObject, size_vector = []):
    size_vector.append( (dir.get_name(), dir.get_size()))
    subdirs = [obj for obj in dir.get_content() if type(obj).__name__ == "Directory"]
    if not dir.get_content() or len(subdirs) == 0:
        return
   
    for subdir in subdirs:
        collect_directory_sizes(subdir, size_vector)

    return(size_vector)

if __name__ == "__main__":
    data = open('data/data_12_07.txt', 'r').read().split('\n')
   
    root = reconstruct_filesystem(data)
    root.update_size()

    print(root.get_size())
    
    print(sum_directory_size(root))
