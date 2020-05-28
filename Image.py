train_data = scipy.io.loadmat('extra_32*32.mat)
X = train_data['X']
y = train_data['y']
img_index = 25
plt.imshow(x[:,:,:,img_index])
plt.show()
print (y[img_index])
