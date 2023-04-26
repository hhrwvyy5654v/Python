import os
import sys

def delete_document(path):
    for root, _, floder in os.walk(path):
        for file in floder:
            if file.endswith('.tmp') or file.endswith('.log') or file.endswith('.obj') or file.endswith('.txt'):
                os.remove(os.path.join(root, file))
                print(root+"/"+file, " is being removed")

path = sys.argv[1]
delete_document(path)
