import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from random import randint
import textwrap

version = 'v0.1.0'

bingo_df = pd.read_csv('bingo.csv', sep=';')
ones = bingo_df[bingo_df.odds == 1].text.tolist()
twos = bingo_df[bingo_df.odds == 2].text.tolist()
threes= bingo_df[bingo_df.odds == 3].text.tolist()

def make_bingo_sheet(plot_name):
    rand = []
    for i in range(25):
        rand.append(randint(1,3))
    rand = np.array(rand)
    rand[12]=0
    rand.reshape(5,5)

    num_ones = len(np.argwhere(rand == 1))
    num_twos = len(np.argwhere(rand == 2))
    num_threes = len(np.argwhere(rand == 3))
    text1 = np.random.choice(ones, num_ones, replace=False )
    text2 = np.random.choice(twos, num_twos, replace=False)
    text3 = np.random.choice(threes, num_threes, replace=False)

    bingo_sheet = np.empty(25, dtype='|S1000')

    used_list = ['babalabl']
    used_list = np.array(used_list)

    for i,element in enumerate(rand):
        #print(i, element)
        if element == 0:
            text=np.array("(free square) Justyn, Vik and Stu aren't at CAPER")
        if element == 1:
            text = 'babalabl'
            while np.any(used_list == text):
                text = random.choice(ones)  

        if element == 2:
            text = 'babalabl'
            while np.any(used_list == text):
                text = random.choice(twos)  

        if element == 3:
            text = 'babalabl'
            while np.any(used_list == text):
                text = random.choice(threes)  

        used_list = np.append(used_list, text)
        bingo_sheet[i] = text

    bingo_sheet = bingo_sheet.reshape(5,5)

    f, ax = plt.subplots(5,5, figsize = (20,20))
    plt.subplots_adjust(hspace=0, wspace=0)


    for i in range(5):
        for j in range(5):
            mytext = bingo_sheet[i,j]
            mytext = textwrap.fill(mytext, 17)
            """
            mytext = mytext.split()
            total_char = 0
            lines = 1
            inds=[]
            for word_index in len(mytext):
                total_char += len(mytex[word_index])
                if total_char > lines*20:
                    inds.append(word_index)

            inds.reverse()
            for ind in inds:
                wrappedtext = mytext.insert()

            #if len(mytext) > 20:
            #    mytext = "\n".join([mytext[i:i+20] for i in range(0, len(mytext), 20)])
            """    
            #print mytext
            ax[i,j].text(0.1, 0.4, mytext, wrap=True, fontsize=18, transform=ax[i,j].transAxes)
            ax[i,j].xaxis.set_visible(False)
            ax[i,j].yaxis.set_visible(False)

    plt.suptitle('BINGO SHEET version '+version, fontsize=40)
    plt.savefig(plot_name)
    #plt.show()

for i in range(20):
    plot_name = "bingo_sheet_N"+str(i)
    make_bingo_sheet(plot_name)