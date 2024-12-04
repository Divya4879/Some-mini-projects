import imageio.v3 as iio

filenames = ['download (1).jpg', 'download (4).jpg','download (5).jpg',
'download (7).jpg', 'download (8).jpg']

images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('my.gif', images, duration = 500, loop = 0)