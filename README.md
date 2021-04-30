# ia_dataset_enhancer
**A program to multiply the number of image you have in your dataset by adding noise, filters, deformations... Perfect to train AI(s)**

If you have to train some Artificial intelligences, datasets are the key and can change the succes rate of your AI. A poor dataset with a small amount of images can't train a good AI. But we don't have an infinite number of images ! What can we do ? We can create new images from the one we already have !
By example, if I flip an image on the x axis, for me it's obvious, but for an AI who only "sees" an array of numbers it's totally different !
So this is the main idea of this program, applying filters or transformations to have more images :
![example of transformations](https://cdn.discordapp.com/attachments/707337308994535457/837654372103749682/unknown.png)

For each image in the source folder, the programm will create 8 news images :
The original image just resized (400x400, *but you can change it line 18*) (all other images will be resized too)
An image with random noise above it
5 images randomly rotated
And one image flipped on the X axis

**Optimization :**
This program is designed to take advantage of all the cores of your CPU, it will detect this number automaticaly and launch one thread by core with the multiprocessing python library. *You can change the number of cores used line 16.*
By example if your CPU have 8 cores, it will proceed 8 images simultaneously !

**Crédits :**
The original idea for this program and the original image processing program was from my friend Ilan Mayeux. Optimisation and multiprocessing implementation is from me :D
