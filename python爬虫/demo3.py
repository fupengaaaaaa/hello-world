import tensorflow as tf
from PIL import Image
import matplotlib.pyplot as plt
# mnist=tf.keras.datasets.mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train, x_test = x_train / 255.0, x_test / 255.0
# model = tf.keras.models.Sequential([
#   tf.keras.layers.Flatten(input_shape=(28, 28)),
#   tf.keras.layers.Dense(128, activation='relu'),
#   tf.keras.layers.Dropout(0.2),
#   tf.keras.layers.Dense(10, activation='softmax')
# ])

# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])


# model.fit(x_train, y_train, epochs=5, verbose=1)
# model.evaluate(x_test,  y_test, verbose=2)


# x=tf.constant([[4.0,5],[10,1]])
# y=tf.nn.softmax(x)


# li=(1,2,3)
# print(tf.convert_to_tensor(li))
# print(tf.Variable(li).shape)


# with tf.device('CPU:0'):
#   a = tf.Variable([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
#   b = tf.Variable([[1.0, 2.0, 3.0]])

# with tf.device('GPU:1'):
#   # Element-wise multiply
#   k = a * b
# print(k)


mnist=tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test)=mnist.load_data()
# print(x_train[0,0,0:28])
# print(x_train[:,tf.newaxis,:,:].shape)
# print(x_train.shape, y_train.shape)
# plt.imshow(x_train[1])

# df=tf.keras.layers.Conv2D(32,3)(x_train[:,:,:,tf.newaxis].astype('float32'))
# x_train=x_train[:,:,:,tf.newaxis][1].astype('float32')
# df=tf.keras.layers.Conv2D(1,3)
# ds=tf.keras.layers.Flatten()
# print(df(x_train[tf.newaxis,:,:,:]).shape)
# print(ds(x_train[tf.newaxis,:,:,:]))


# x_train=x_train[:,:,:,tf.newaxis].astype('float32')
# train_ds=tf.data.Dataset.from_tensor_slices((x_train,y_train)).shuffle(10000).batch(4000)
# for image, label in train_ds:
#     # print(image.shape, label.shape)
#     df=tf.keras.layers.Conv2D(23,3)
#     print(df(image).shape)



# print(x_train.shape)
# df=tf.keras.layers.Flatten()(x_train)
# print(df.shape)


# li=[1,2,3]
# lm=['a','b']
# for i in zip(li,lm):
#     print(i)



