import os
import json
import sys

"""
dict = {}
path = '/var/lib/docker/image/overlay2/layerdb/sha256/'
directory='sha256'
def file_traversal():
    for root,dir_name,file_name in os.walk(path):
        if (file_name = 'diff'):
            content = file_name.read()
            print (content)
"""
def file_traversal():
layers_root = "/var/lib/docker/image/overlay2/layerdb/sha256/"

result = {}
for layer_dir in os.listdir(layers_root):
    path = "{}/{}/diff".format(layers_root, layer_dir) 
    with open(path, "r") as lfp:
        key = lfp.read()
        result[key] = "{}/{}".format(layers_root, layer_dir)


def read(dir_name):
   #dir_name.file_traversal()
   main_path="/var/lib/docker/image/overlay2/imagedb/sha256/"
   with open("/var/lib/docker/image/overlay2/layerdb/sha256/+"dir_name"):
        
    reqd=json.loads(key) 


def tarsplit_decoder():
    with gzip.open('tar-split.json.gz', 'r') as fin, open('layer.tar', 'wb') as fout:
    for line in fin.readlines():
        entry = json.loads(line)
        if entry['type'] == 2 and entry['payload'] and len(entry['payload']) > 0:
            decoded = base64.b64decode(entry['payload'])
            fout.write(decoded)
        elif entry['type'] == 1 and entry['payload'] and len(entry['payload']) > 0:
            with open(image_path +"/"+entry['name'], "rb") as fin:
                content = fin.read()
                print("Read {} bytes".format(len(content)))
                fout.write(content)

def read_diff():
    image_path = "/var/lib/docker/image/overlay2/imagedb/content/sha256"
with open("{}/{}".format(image_path, sys.argv[1]), "r") as fin:
    image_info = json.loads(fin.read())
    for layer_id in image_info['rootfs']['diff_ids']:
        print(layer_id)
        key1=diff_ids
        if key1 in result.key():
            print (result.get(key1))

#mapping path with diff idß
def read_cache(dir_name):
    with open ("var/lib/docker/image/overlay2/layerdb/sha256/" + "dir_name" +"diff" + "cache_id"):
        print (read(cache_id))