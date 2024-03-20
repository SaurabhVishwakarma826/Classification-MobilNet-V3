import os
import random
import shutil 

splitsize = .85
categories = []

source_folder = "G:/desktop/project/sweetClassification/Dataset"
folders = os.listdir(source_folder)
print(folders)

for subfolder in folders:
    if os.path.isdir(source_folder + "/" + subfolder):
        categories.append(subfolder)

categories.sort()
print(categories)


# create a target folder
target_folder = "G:/desktop/project/sweetClassification/sweetDataset"

existDataSetPath = os.path.exists(target_folder)
if existDataSetPath==False:
    os.mkdir(target_folder)


# create a function for split the data for train and validation 

def split_data(SOURCE , TRAINING, VALIDATION, SPLIT_SIZE):
    files=[]

    for filename in os.listdir(SOURCE):
        file = SOURCE + filename
        print(file)
        if os.path.getsize(file) > 0 :
            files.append(filename)
        else:
            print(filename + " is 0 length , ignot it ....")
    print(len(files))


    trainingLength = int(len(files) * SPLIT_SIZE )
    shuffleSet = random.sample(files , len(files))
    trainingSet = shuffleSet[0:trainingLength]
    validSet = shuffleSet[trainingLength:]

    # copy the train images 
    for filename in trainingSet :
        thisFile = SOURCE + filename
        destination = TRAINING + filename
        shutil.copyfile(thisFile , destination)

    # copy the validation images
    for filename in validSet :
        thisFile = SOURCE + filename
        destination = VALIDATION + filename
        shutil.copyfile(thisFile , destination)       

trainPath = target_folder + "/train"
print(trainPath)
validatePath = target_folder + "/validate"

# create the target folders:
exitsDataSetPth = os.path.exists(trainPath)
print(exitsDataSetPth)
if not(exitsDataSetPth):
    os.mkdir(trainPath)

exitsDataSetPth = os.path.exists(validatePath)
if exitsDataSetPth==False:
    os.mkdir(validatePath)


# lets run the function for each of the folders
for category in categories:
    trainDestPath = trainPath + "/" + category
    validateDestPath = validatePath + "/" + category

    print(trainDestPath)

    if os.path.exists(trainDestPath)==False :
        os.mkdir(trainDestPath)
    if os.path.exists(validateDestPath)==False :
        os.mkdir(validateDestPath)

    sourePath = source_folder + "/" + category + "/"
    trainDestPath = trainDestPath + "/"
    validateDestPath = validateDestPath + "/"

    print("Copy from : "+sourePath + " to : " + trainDestPath + " and " +validateDestPath)

    split_data(sourePath , trainDestPath , validateDestPath , splitsize)
