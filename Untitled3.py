
# coding: utf-8

# In[1]:


from keras.datasets import mnist


# In[9]:


(X_train,Y_train),(X_test,Y_test) = mnist.load_data()


# In[3]:


import matplotlib.pyplot as plt 


# In[10]:


plt.imshow(X_train[0])


# In[7]:


X_train[0].shape


# In[11]:


#reshape data to fit model
X_train = X_train.reshape(60000,28,28,1)
X_test = X_test.reshape(10000,28,28,1)


# In[12]:


from keras.utils import to_categorical
#one-hot encode target column
Y_train = to_categorical(Y_train)
Y_test = to_categorical(Y_test)
Y_train[0]


# In[16]:


from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
#create model
model = Sequential()
#add model layers
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28,28,1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))


# In[17]:


#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


# In[18]:


#train the model
model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=3)


# In[19]:


#predict first 4 images in the test set
model.predict(X_test[:4])


# In[20]:


#actual results for first 4 images in test set
y_test[:4]

