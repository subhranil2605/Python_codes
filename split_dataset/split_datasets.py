import splitfolders


# input folder dir
input_folder = r"F:\Project_CNN\axial_t2_all\input"

# output folder dir
output = r"F:\Project_CNN\axial_t2_all\output" 


# ratio of split are in order of train/val/test. You can change to whatever you want.
# For train/val sets only, you could do .75, .25 for example.
splitfolders.ratio(input_folder, output=output, seed=42, ratio=(.8, .1, .1))
