import glob
import os

def getFilename(userName):
    dirname = "DataBase/" + userName + "/*"
    filelist = glob.glob(dirname)
    return filelist

def getLabel(fileName):
    index = ["JOY", "ACC", "FEA", "SUR", "SAD", "DIS", "ANG", "ANT", "NEU", "OTH"]
    label = {"JOY": 0, "ACC": 1, "FEA": 2, "SUR": 3, "SAD": 4, "DIS": 5, "ANG": 6, "ANT": 7, "NEU": 8, "OTH": 9}

    for elem in index:
        if elem in fileName:
            return label[elem]

if __name__ == '__main__':
    raw_dir = "Raw/"
    labelIndex = ["JOY", "ACC", "FEA", "SUR", "SAD", "DIS", "ANG", "ANT"]
    label = {"JOY": 0, "ACC": 1, "FEA": 2, "SUR": 3, "SAD": 4, "DIS": 5, "ANG": 6, "ANT": 7}
    for feel in labelIndex:
        file_list = glob.glob(raw_dir + feel + "/*")
        for fname in file_list:
            mfccName = "mfcc/" + feel + "/" + fname.split("/")[2].split(".")[0] + ".mfcc"
            print(mfccName)
            os.system("x2x +sf < '%s' | frame -l 441 -p 441 |mfcc -l 441 -f 44.1 -m 12 -n 20 -a 0.97 > '%s'" %(fname, mfccName))
