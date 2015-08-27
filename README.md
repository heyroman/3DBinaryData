# 3DBinaryData

This project creates a 3D-visualization of files of any kind. It was inspired by this TED video:
[*The 1s and 0s behind cyber warfare*](https://www.ted.com/talks/chris_domas_the_1s_and_0s_behind_cyber_warfare)

To use this program one has to put the file one wants to visualise into 'input_data_examples' directory and run main.py script, then type the name of this file.
This code treats files differently. For files that's size is less than 4kB it uses simple algorithm which is just reading 3 consequent bytes as x, y and z coordinate of a point to be visualise.
The color of this point is then being set according to the number of matching bits in these 3 bytes.

If file size is greater than 4kB, the PCA gets into action. We assume we only want 1000 points to plot, so we divide out file into 1000 pieces.
Each piece then containes file_size/1000 bytes, ie dimensions of a point represented by this piece. So, we have a matrix of 1000 rows and file_size/1000 columns (dimensions).
Then PCA is applied to that matrix reducing dimensionality to the number of 4. These 4 dimensions are x, y, z and color of each point.