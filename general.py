import os


# Each website you crawl is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print(f"Creating project {directory}")
        os.makedirs(directory)


# Create queue and crawled
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + "\n")


# Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w') as f:
        pass


# Read a file and convert each line to set items
def file_to_set(path):
    s = set()
    with open(path, 'rt') as file:
        for line in file:
            s.add(line.replace('\n', ''))
    return s


# Convert a set of links to a file specified by PATH
def set_to_file(links, path):
    with open(path, "w") as f:
        for l in sorted(links):
            f.write(l + "\n")
