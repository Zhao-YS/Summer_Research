# Packages Import

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from keras.callbacks import History, ReduceLROnPlateau
from keras.models import Model
from keras.layers import Input
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Concatenate
from keras.optimizers import adam_v2
from sklearn.model_selection import train_test_split



# one-hot encoder algorithm
def Encode(smiles):
        one_hot =  np.zeros((smiles.shape[0], Max_len , len(Allchar)),dtype=np.int8)
        for i,smile in enumerate(smiles):
            #encode the startchar
            one_hot[i,0,Dict_1["!"]] = 1
            #encode the rest of the chars
            for j,c in enumerate(str(smile)):
                one_hot[i,j+1,Dict_1[c]] = 1
            #Encode endchar
            one_hot[i,len(str(smile))+1:,Dict_1["E"]] = 1
        #Return two, one for input and the other for output
        return one_hot[:,0:-1,:], one_hot[:,1:,:]

#import Smiles
data = pd.read_csv("Drug_SMILEs.csv", delimiter = ",", names = ["Names","smiles"])
S_train, S_test = train_test_split(data["smiles"])

# Dictionarys for char_2_index and index_2_char
Smiles = list(data.smiles)
for i in range(0,len(Smiles)):
	Smiles[i] = str(Smiles[i])
Allchar = set("".join(Smiles)+"!E")
Dict_1 = dict((c,i) for i,c in enumerate(Allchar))
Dict_2 = dict((i,c) for i,c in enumerate(Allchar))
Max_len = max([len(smile) for smile in Smiles]) + 3

X_train, Y_train = Encode(S_train.values)
X_test,Y_test = Encode(S_test.values)


#Build RNN
input_shape = X_train.shape[1:]
output_dim = Y_train.shape[-1]
dim_1 = 64
dim_2 = 6
encoder_inputs = Input(shape=input_shape)
encoder = LSTM(dim_2, return_state=True,
                unroll=False)
encoder_outputs, state_h, state_c = encoder(encoder_inputs)
states = Concatenate(axis=-1)([state_h, state_c])
neck = Dense(dim_1, activation="relu")
neck_outputs = neck(states)
decode_h = Dense(dim_2, activation="relu")
decode_c = Dense(dim_2, activation="relu")
state_h_decoded =  decode_h(neck_outputs)
state_c_decoded =  decode_c(neck_outputs)
encoder_states = [state_h_decoded, state_c_decoded]
decoder_inputs = Input(shape=input_shape)
decoder_lstm = LSTM(dim_2,
                    return_sequences=True,
                    unroll=False
                   )
decoder_outputs = decoder_lstm(decoder_inputs, initial_state=encoder_states)
decoder_dense = Dense(output_dim, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
print(model.summary())

#Training set
opt=adam_v2.Adam(learning_rate=0.005) #Default 0.001
model.compile(optimizer=opt, loss='categorical_crossentropy')

h = History()
RP = ReduceLROnPlateau(monitor='val_loss')


model.fit([X_train,X_train],Y_train,
                    epochs=15,
                    batch_size=256,
                    shuffle=True,
                    callbacks=[h, RP],
                    validation_data=([X_test,X_test],Y_test))

#plot loss_function
plt.plot(h.history["loss"], label="Loss")
plt.plot(h.history["val_loss"], label="Val_Loss")
plt.yscale("log")
plt.legend()
plt.savefig('./loss.jpg')