import glob
import os

def getFilename(userName):
    dirname = "Raw/" + userName + "/*"
    filelist = glob.glob(dirname)
    return filelist

def getLabel(fileName):
    index = ["JOY", "ACC", "FEA", "SUR", "SAD", "DIS", "ANG", "ANT", "NEU", "OTH"]
    label = {"JOY": 0, "ACC": 1, "FEA": 2, "SUR": 3, "SAD": 4, "DIS": 5, "ANG": 6, "ANT": 7, "NEU": 8, "OTH": 9}

    for elem in index:
        if elem in fileName:
            return label[elem]

if __name__ == '__main__':
    database_dir = "Database/"
    labelIndex = ["JOY", "ACC", "FEA", "SUR", "SAD", "DIS", "ANG", "ANT"]
    label = {"JOY": 0, "ACC": 1, "FEA": 2, "SUR": 3, "SAD": 4, "DIS": 5, "ANG": 6, "ANT": 7}

    for feel_name in labelIndex:
        fol_name = database_dir + feel_name + "/*"
        file_list = glob.glob(fol_name)
        for file_name in file_list:
            raw_name = "Raw/" + feel_name + "/" +  file_name.split("/")[2].split(".")[0] + ".raw"
            print(raw_name)
            os.system("sox '%s' '%s'" %(file_name, raw_name))


    """
    for user in people:
        print(user)
        filename = getFilename(user)
        for fname in filename:
            print(fname)
            rawname = "F0/" + user[:-2] + "/" + labelIndex[getLabel(fname)] + fname[8:-3] + "raw"
            print(f0name)
            os.system("sox '%s' '%s'" %(fname, rawname))
    """
