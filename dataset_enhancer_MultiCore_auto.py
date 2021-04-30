from numpy import fliplr
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import random
from skimage import exposure
from skimage.util import random_noise
from skimage import transform
from cv2 import resize
from glob import glob
import os

from multiprocessing import Pool
# Pool nous permet de lancer une fonction plusieurs fois dans un core différent en même temps avec une liste d'arguments
# We will use Pool to open a function in many cores of our CPU with a list of arguments (core1 will have the first argument, core 2 the 2nd...)

cpus = os.cpu_count()
imgSize = (400,400) # Size (x,y) of the news images created


# IMAGE PROCESSING FUCTION, take a list of images to process. Output folder is just output/
def processImages(images):
    dossierOutput = "output\\"

    # Text to add to the modified images names: 
    rotated_img = "rot_"
    noise_img = "noise_"
    vert_img = "rvrsd_"

    print("PROCESSING OF ",len(images), "IMAGES.")

    # Creating output folder if needed
    if not os.path.exists(dossierOutput):
        os.makedirs(dossierOutput)

    for nom_actuel in images:  

        nom_actuel1 = mpimg.imread(nom_actuel)

        nom_actuel = nom_actuel.split("\\")[-1] # Just taking the name of the image and not the complete path with folders

        # Image resize to 400x400
        img_rescale = resize(nom_actuel1,imgSize) # (X, Y)

        # Random rotation (5 times)
        for i in range(5):
            trans = transform.rotate(img_rescale, random.uniform(-20,20)) # -20 et 20 sont les degrés max de rotations pour l'image
            mpimg.imsave(dossierOutput + rotated_img + str(i) + nom_actuel, trans)
        
        # Add noise
        img_nos = random_noise(img_rescale, mode="s&p", clip=True)

        # Vertical flip 
        vertFlip = fliplr(img_rescale)

        # Sauvegarde toutes les variantes de l'image dans son emplacement miroir
        mpimg.imsave(dossierOutput+nom_actuel, img_rescale)
        mpimg.imsave(dossierOutput + noise_img + "0" + nom_actuel, img_nos)
        mpimg.imsave(dossierOutput + vert_img + "0" + nom_actuel, vertFlip)
    
    print("endThread")
        
if __name__ == '__main__': # We will do that only if we are the main program (prevent threads to launch threads the recursive way)
    print("Your CPU have",cpus,"cores.")
    # Taking the list of images
    dossier_training = glob(input("nom du dossier : ") + "/*")

    def autoSplit(l,elements):
        """
        Will split the whole list into n (elements) number of little lists
        Will try to have all lists lenght equal while it can add more elements
        So the difference of lenght between two new lists can't be superior to one
        """

        output = []
        for i in range(elements):
            output.append([])

        for i in range(len(l)): # We'll alternatively add one image to each small new list (use the modulo to cycle in the number of new lists)
            output[i % elements].append(l[i])

        return output    

    print("Your CPU have",cpus, "cores, as many images will be processed at the same time!")
    print(len(dossier_training), "images to proceed...")
    mainListe = autoSplit(dossier_training,cpus) # Creating lists of images for each future thread

    # We'll create as many threads as the lenght of the mainList of tasks, defined by the number of cores counted
    with Pool(len(mainListe)) as p:
        p.map(processImages, mainListe)