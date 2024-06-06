import sys
import ast
import numpy as np
from PyQt5.QtWidgets import *

from PyQt5.QtGui import QPixmap
from nltk.corpus import wordnet as wn
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QScrollArea

hierarchical_data = {
    'directed graph': [
         ['Madagascar_cat', 'lynx'], ['pug', 'Madagascar_cat', 'lynx'], ['boxer', 'pug', 'Madagascar_cat', 'lynx'], ['Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], ['kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], ['fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['airliner', 'warplane'], ['orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['cab', 'limousine'], ['white_stork', 'airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['flamingo', 'white_stork', 'airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['space_shuttle', 'flamingo', 'white_stork', 'airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['American_coot', 'space_shuttle', 'flamingo', 'white_stork', 'airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['black_swan', 'American_coot', 'space_shuttle', 'flamingo', 'white_stork', 'airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['broccoli', 'cauliflower'], ['Persian_cat', 'black_swan', 'American_coot', 'space_shuttle', 'flamingo', 'white_stork', 'airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['tabby', 'Persian_cat', 'black_swan', 'American_coot', 'space_shuttle', 'flamingo', 'white_stork', 'airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['broccoli', 'cauliflower', 'tabby', 'Persian_cat', 'black_swan', 'American_coot', 'space_shuttle', 'flamingo', 'white_stork', 'airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['head_cabbage', 'broccoli', 'cauliflower', 'tabby', 'Persian_cat', 'black_swan', 'American_coot', 'space_shuttle', 'flamingo', 'white_stork', 'airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['Granny_Smith', 'head_cabbage', 'broccoli', 'cauliflower', 'tabby', 'Persian_cat', 'black_swan', 'American_coot', 'space_shuttle', 'flamingo', 'white_stork', 'airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['fig', 'Granny_Smith', 'head_cabbage', 'broccoli', 'cauliflower', 'tabby', 'Persian_cat', 'black_swan', 'American_coot', 'space_shuttle', 'flamingo', 'white_stork', 'airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['zucchini', 'fig', 'Granny_Smith', 'head_cabbage', 'broccoli', 'cauliflower', 'tabby', 'Persian_cat', 'black_swan', 'American_coot', 'space_shuttle', 'flamingo', 'white_stork', 'airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx'], 
         ['minivan', 'police_van'], ['jeep', 'minivan', 'police_van'], ['cab', 'limousine', 'jeep', 'minivan', 'police_van'], 
         ['zucchini', 'fig', 'Granny_Smith', 'head_cabbage', 'broccoli', 'cauliflower', 'tabby', 'Persian_cat', 'black_swan', 'American_coot', 'space_shuttle', 'flamingo', 'white_stork', 'airliner', 'warplane', 'gorilla', 'chimpanzee', 'lemon', 'orange', 'frying_pan', 'wok', 'coffeepot', 'teapot', 'trimaran', 'catamaran', 'spider_monkey', 'Crock_Pot', 'caldron', 'fireboat', 'container_ship', 'kuvasz', 'Norwich_terrier', 'boxer', 'pug', 'Madagascar_cat', 'lynx', 'cab', 'limousine', 'jeep', 'minivan', 'police_van']
         ]
    ,
    'undirected graph': [
         ['Norwich_terrier', 'kuvasz'], 
         ['Crock_Pot', 'Norwich_terrier', 'kuvasz'], ['catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], ['teapot', 'coffeepot'], ['wok', 'frying_pan'], 
         ['cab', 'limousine'], ['chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], ['orange', 'lemon'], 
         ['broccoli', 'cauliflower'], ['airliner', 'warplane'], ['Persian_cat', 'tabby'], ['minivan', 'cab', 'limousine'], 
         ['American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['Granny_Smith', 'broccoli', 'cauliflower'], ['caldron', 'wok', 'frying_pan'], ['space_shuttle', 'airliner', 'warplane'], 
         ['orange', 'lemon', 'Granny_Smith', 'broccoli', 'cauliflower'], 
         ['fig', 'orange', 'lemon', 'Granny_Smith', 'broccoli', 'cauliflower'], 
         ['pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['Persian_cat', 'tabby', 'boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['white_stork', 'Persian_cat', 'tabby', 'boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['flamingo', 'white_stork', 'Persian_cat', 'tabby', 'boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['police_van', 'minivan', 'cab', 'limousine'], ['Madagascar_cat', 'flamingo', 'white_stork', 'Persian_cat', 'tabby', 'boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['spider_monkey', 'Madagascar_cat', 'flamingo', 'white_stork', 'Persian_cat', 'tabby', 'boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['caldron', 'wok', 'frying_pan', 'spider_monkey', 'Madagascar_cat', 'flamingo', 'white_stork', 'Persian_cat', 'tabby', 'boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['head_cabbage', 'fig', 'orange', 'lemon', 'Granny_Smith', 'broccoli', 'cauliflower'], 
         ['teapot', 'coffeepot', 'caldron', 'wok', 'frying_pan', 'spider_monkey', 'Madagascar_cat', 'flamingo', 'white_stork', 'Persian_cat', 'tabby', 'boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['zucchini', 'head_cabbage', 'fig', 'orange', 'lemon', 'Granny_Smith', 'broccoli', 'cauliflower'], ['container_ship', 'space_shuttle', 'airliner', 'warplane'], 
         ['police_van', 'minivan', 'cab', 'limousine', 'teapot', 'coffeepot', 'caldron', 'wok', 'frying_pan', 'spider_monkey', 'Madagascar_cat', 'flamingo', 'white_stork', 'Persian_cat', 'tabby', 'boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['lynx', 'police_van', 'minivan', 'cab', 'limousine', 'teapot', 'coffeepot', 'caldron', 'wok', 'frying_pan', 'spider_monkey', 'Madagascar_cat', 'flamingo', 'white_stork', 'Persian_cat', 'tabby', 'boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['jeep', 'lynx', 'police_van', 'minivan', 'cab', 'limousine', 'teapot', 'coffeepot', 'caldron', 'wok', 'frying_pan', 'spider_monkey', 'Madagascar_cat', 'flamingo', 'white_stork', 'Persian_cat', 'tabby', 'boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['zucchini', 'head_cabbage', 'fig', 'orange', 'lemon', 'Granny_Smith', 'broccoli', 'cauliflower', 'jeep', 'lynx', 'police_van', 'minivan', 'cab', 'limousine', 'teapot', 'coffeepot', 'caldron', 'wok', 'frying_pan', 'spider_monkey', 'Madagascar_cat', 'flamingo', 'white_stork', 'Persian_cat', 'tabby', 'boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['container_ship', 'space_shuttle', 'airliner', 'warplane', 'zucchini', 'head_cabbage', 'fig', 'orange', 'lemon', 'Granny_Smith', 'broccoli', 'cauliflower', 'jeep', 'lynx', 'police_van', 'minivan', 'cab', 'limousine', 'teapot', 'coffeepot', 'caldron', 'wok', 'frying_pan', 'spider_monkey', 'Madagascar_cat', 'flamingo', 'white_stork', 'Persian_cat', 'tabby', 'boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz'], 
         ['fireboat', 'container_ship', 'space_shuttle', 'airliner', 'warplane', 'zucchini', 'head_cabbage', 'fig', 'orange', 'lemon', 'Granny_Smith', 'broccoli', 'cauliflower', 'jeep', 'lynx', 'police_van', 'minivan', 'cab', 'limousine', 'teapot', 'coffeepot', 'caldron', 'wok', 'frying_pan', 'spider_monkey', 'Madagascar_cat', 'flamingo', 'white_stork', 'Persian_cat', 'tabby', 'boxer', 'pug', 'black_swan', 'American_coot', 'gorilla', 'chimpanzee', 'trimaran', 'catamaran', 'Crock_Pot', 'Norwich_terrier', 'kuvasz']
    ],

    'distances graph': [
         ['limousine', 'jeep'], ['Granny_Smith', 'zucchini'], ['white_stork', 'flamingo'], ['minivan', 'police_van'], ['Persian_cat', 'tabby'], ['Madagascar_cat', 'lynx'], ['airliner', 'space_shuttle'], ['broccoli', 'head_cabbage'], ['spider_monkey', 'Madagascar_cat', 'lynx'], ['boxer', 'kuvasz'], ['American_coot', 'black_swan'], ['lemon', 'fig'], 
         ['teapot', 'coffeepot'], ['cauliflower', 'lemon', 'fig'], ['warplane', 'airliner', 'space_shuttle'], ['cab', 'limousine', 'jeep'], ['gorilla', 'spider_monkey', 'Madagascar_cat', 'lynx'], ['container_ship', 'fireboat'], ['wok', 'frying_pan'], ['catamaran', 'trimaran'], ['Granny_Smith', 'zucchini', 'cauliflower', 'lemon', 'fig'], ['container_ship', 'fireboat', 'catamaran', 'trimaran'],
         ['pug', 'boxer', 'kuvasz'], ['Crock_Pot', 'wok', 'frying_pan'], ['chimpanzee', 'gorilla', 'spider_monkey', 'Madagascar_cat', 'lynx'], ['cab', 'limousine', 'jeep', 'container_ship', 'fireboat', 'catamaran', 'trimaran'], ['caldron', 'teapot', 'coffeepot'], ['minivan', 'police_van', 'cab', 'limousine', 'jeep', 'container_ship', 'fireboat', 'catamaran', 'trimaran'],
         ['Persian_cat', 'tabby', 'pug', 'boxer', 'kuvasz'], ['Crock_Pot', 'wok', 'frying_pan', 'caldron', 'teapot', 'coffeepot'], ['warplane', 'airliner', 'space_shuttle', 'minivan', 'police_van', 'cab', 'limousine', 'jeep', 'container_ship', 'fireboat', 'catamaran', 'trimaran'], ['orange', 'Granny_Smith', 'zucchini', 'cauliflower', 'lemon', 'fig'],
         ['chimpanzee', 'gorilla', 'spider_monkey', 'Madagascar_cat', 'lynx', 'Persian_cat', 'tabby', 'pug', 'boxer', 'kuvasz'], ['broccoli', 'head_cabbage', 'orange', 'Granny_Smith', 'zucchini', 'cauliflower', 'lemon', 'fig'], ['Norwich_terrier', 'chimpanzee', 'gorilla', 'spider_monkey', 'Madagascar_cat', 'lynx', 'Persian_cat', 'tabby', 'pug', 'boxer', 'kuvasz'], ['white_stork', 'flamingo', 'American_coot', 'black_swan'], 
         ['broccoli', 'head_cabbage', 'orange', 'Granny_Smith', 'zucchini', 'cauliflower', 'lemon', 'fig', 'white_stork', 'flamingo', 'American_coot', 'black_swan'], ['Crock_Pot', 'wok', 'frying_pan', 'caldron', 'teapot', 'coffeepot', 'broccoli', 'head_cabbage', 'orange', 'Granny_Smith', 'zucchini', 'cauliflower', 'lemon', 'fig', 'white_stork', 'flamingo', 'American_coot', 'black_swan'], 
         ['Norwich_terrier', 'chimpanzee', 'gorilla', 'spider_monkey', 'Madagascar_cat', 'lynx', 'Persian_cat', 'tabby', 'pug', 'boxer', 'kuvasz', 'Crock_Pot', 'wok', 'frying_pan', 'caldron', 'teapot', 'coffeepot', 'broccoli', 'head_cabbage', 'orange', 'Granny_Smith', 'zucchini', 'cauliflower', 'lemon', 'fig', 'white_stork', 'flamingo', 'American_coot', 'black_swan'], 
         ['warplane', 'airliner', 'space_shuttle', 'minivan', 'police_van', 'cab', 'limousine', 'jeep', 'container_ship', 'fireboat', 'catamaran', 'trimaran', 'Norwich_terrier', 'chimpanzee', 'gorilla', 'spider_monkey', 'Madagascar_cat', 'lynx', 'Persian_cat', 'tabby', 'pug', 'boxer', 'kuvasz', 'Crock_Pot', 'wok', 'frying_pan', 'caldron', 'teapot', 'coffeepot', 'broccoli', 'head_cabbage', 'orange', 'Granny_Smith', 'zucchini', 'cauliflower', 'lemon', 'fig', 'white_stork', 'flamingo', 'American_coot', 'black_swan']
    ]
}

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./HomePage.ui", self)
        self.set_image('./images/logo.png', self.labelLogo, 10, 10)
        self.toolButton.clicked.connect(self.show_xai_interface)
        self.toolButton_2.clicked.connect(self.show_xai_query)

    def set_image(self, path, label_name, x, y):
        label = label_name  # Removed redundant QLabel creation
        label.setGeometry(x, y, 250, 250)
        # Load an image from the images folder
        pixmap = QPixmap(path)
        # Set the pixmap to the label and fit it
        label.setPixmap(pixmap)
        label.setScaledContents(True)

    def show_xai_interface(self):
        global widget
        widget.setCurrentIndex(1) 

    def show_xai_query(self):
        global widget
        widget.setCurrentIndex(2)

class XAIInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./XAIInterface.ui", self)
        self.next_button = self.findChild(QPushButton, 'pushButton')
        self.next_button.clicked.connect(self.go_to_naming_page)
        self.back_button.clicked.connect(self.back_function)

    def back_function(self):
        global widget
        widget.setCurrentIndex(0)

    def go_to_naming_page(self):
        category = self.findChild(QComboBox, 'categoryBox').currentText()
        graph = self.findChild(QComboBox, 'graphBox').currentText()
        # display_text = self.show_connections(category, graph)

        naming_page = Naming(category, graph)
        widget.addWidget(naming_page)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def show_connections(self, category, graph):
        if graph.lower() in hierarchical_data:
            paths = [path for path in hierarchical_data[graph.lower()] if category in path]
            if paths:
                formatted_paths = []
                for path in paths:
                    highlighted_path = ['<span style="color: red; font-size: 22px;"><b>{}</b></span>'.format(item) if item == category else item for item in path]
                    formatted_string = f"<span style='font-size: 20px;'>['{', '.join(highlighted_path)}']</span><br><br>"
                    formatted_paths.append(formatted_string)
                return "\n".join(formatted_paths)
            else:
                return f"No connections available for category '{category}' in the selected graph."
        else:
            return f"No data available for graph type '{graph}'."
        
class Naming(QMainWindow):
    def __init__(self, category, graph):
        super().__init__()
        uic.loadUi("./Naming.ui", self)
        self.back_button.clicked.connect(self.back_function)
        self.category = category
        self.graph = graph
        self.paths = [path for path in hierarchical_data[graph.lower()] if category in path]
        self.setupUI()

    def back_function(self):
        widget.removeWidget(widget.currentWidget())

    def setupUI(self):
        self.setWindowTitle("Naming Connections")  # Set window title
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("font-size: 20px;")
        widget = QWidget()
        vbox = QVBoxLayout()

        # Button and Header display for category and graph type
        button = QPushButton(f"Go Back")
        button.setMinimumHeight(50)
        button.setMinimumWidth(100)
        button.setMaximumHeight(50)
        button.setMaximumWidth(100)
        button.clicked.connect(self.back_function)
        vbox.addWidget(button)
        header = QLabel(f"Category: <b style='color: red; font-size: 20px;'>{self.category}</b> | Graph Type: <b>{self.graph}</b>")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 20px;")
        vbox.addWidget(header)

        for path in self.paths:
            hbox = QHBoxLayout()

            # Connection Label with category highlighted
            formatted_path = [f"<span style='color: red; font-size: 22px;'><b>{item}</b></span>" if item == self.category else item for item in path]
            connection_label = QLabel("Connection: " + " > ".join(formatted_path))
            connection_label.setTextFormat(Qt.TextFormat.RichText)
            hbox.addWidget(connection_label)

            # Suggested name based on the first common hypernym
            suggested_name = self.common_group(path)
            suggested_name_label = QLabel(f"Suggested Name: {suggested_name}")
            hbox.addWidget(suggested_name_label)

            # User name input
            user_name_edit = QLineEdit()
            user_name_edit.setPlaceholderText("Enter new name")
            hbox.addWidget(user_name_edit)

            # Send Button
            send_button = QPushButton("Send")
            send_button.clicked.connect(lambda checked, p=path, edit=user_name_edit: self.save_name(p, edit.text()))
            hbox.addWidget(send_button)

            vbox.addLayout(hbox)

        widget.setLayout(vbox)
        scroll.setWidget(widget)
        self.setCentralWidget(scroll)

    def common_group(self, groups):
        hierarchy = {}
        for group in groups:
            synsets = wn.synsets(group)
            if synsets:
                hypernyms = synsets[0].hypernym_paths()
                hierarchy[group] = [node.name().split('.')[0] for path in hypernyms for node in path]

        common_set = set(hierarchy[groups[0]])
        for group in groups[1:]:
            common_set.intersection_update(hierarchy[group])

        return next(iter(common_set), "No common hypernym found")

    def save_name(self, path, new_name):
        if new_name:
            try:
                # Read the current content of the file
                with open("./user_common_group.txt", 'r') as file:
                    lines = file.readlines()
            except FileNotFoundError:
                lines = []

            # Remove the existing entry if the path existsn and add the new entry
            new_lines = [line for line in lines if f"[{path}," not in line]
            new_lines.append(f"[{path}, {new_name}]\n")

            # Write the updated content back to the file
            with open("./user_common_group.txt", 'w') as file:
                file.writelines(new_lines)
            QMessageBox.information(self, "Saved", "Your name has been saved successfully!")
        else:
            QMessageBox.warning(self, "Error", "Please enter a name before saving.")


class XAIQuery(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./XAIQuery.ui", self)
        self.set_image('./images/pug_image.jpg', self.labelPug, 30, 80)
        self.set_image('./images/tabby_image.png', self.labelTabby, 400, 80)
        self.next_button = self.findChild(QPushButton, 'pushButton')
        self.next_button.clicked.connect(self.go_to_graph_res_page)
        self.back_button.clicked.connect(self.back_function)
        self.selected_category = None  # Initialize selected_category

        # Connect checkbox signals to a method to update selected_category
        self.checkBox.clicked.connect(self.update_category)
        self.checkBox2.clicked.connect(self.update_category)

    def update_category(self):
        if self.checkBox.isChecked():
            self.selected_category = 'pug'
        elif self.checkBox2.isChecked():
            self.selected_category = 'tabby'

    def set_image(self, path, label_name, x, y):
        label = label_name  # Removed redundant QLabel creation
        label.setGeometry(x, y, 350, 250)
        # Load an image from the images folder
        pixmap = QPixmap(path)
        # Set the pixmap to the label and fit it
        label.setPixmap(pixmap)
        label.setScaledContents(True)

    def back_function(self):
        global widget
        widget.setCurrentIndex(0)

    def go_to_graph_res_page(self, category):
        if self.selected_category:  # Check if a category is selected
            category = self.selected_category
        graph = self.findChild(QComboBox, 'comboBox').currentText()
        display_text = self.show_connections(category, graph)

        graph_res_page = TheGraphRes(graph, display_text)
        widget.addWidget(graph_res_page)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def show_connections(self, category, graph):
        # Load the user_common_group.txt file
        with open('./user_common_group.txt', 'r') as file:
            file_content = file.readlines()

        paths = hierarchical_data.get(graph.lower(), [])
        if paths:
            formatted_paths = []
            for path in paths:
                if category in path:
                    flag = 0
                    for line in file_content:
                        try:
                            # Strip whitespace and split the line into the list and group name
                            line = line.strip()
                            if line.startswith("[") and "], " in line:
                                list_part, group_name_part = line.split("], ", 1)
                                list_part += "]]"  # Add the closing bracket back to the list part
                                user_path = ast.literal_eval(list_part)
                                group_name = group_name_part.strip().replace(']', '')
                                if np.array_equal(path, user_path[0]):
                                    flag = 1
                                    highlighted_path = ['<span style="color: red; font-size: 20px;"><b>{}</b></span>'.format(item) if item == category else item for item in path]
                                    formatted_string = f"The {category} is a group of {group_name}: ['{', '.join(highlighted_path)}'].<br><br>"
                                    formatted_paths.append(formatted_string)
                                    break  # Stop searching after finding a match
                        except (ValueError, SyntaxError) as e:
                            print(f"Error parsing line: {line}. Error: {e}")
                            continue  # Ignore lines that can't be parsed

                    if flag == 0:
                        highlighted_path = ['<span style="color: red; font-size: 20px;"><b>{}</b></span>'.format(item) if item == category else item for item in path]
                        formatted_string = f"The {category} is a group of entity: ['{', '.join(highlighted_path)}'].<br><br>"
                        formatted_paths.append(formatted_string)
            return "\n".join(formatted_paths)
        else:
            return f"No data available for graph type '{graph}'."
        
    def common_group(self, groups):
        hierarchy = {}
        for group in groups:
            synsets = wn.synsets(group)
            if synsets:
                hypernyms = synsets[0].hypernym_paths()
                hierarchy[group] = [node.name().split('.')[0] for path in hypernyms for node in path]

        common_set = set(hierarchy[groups[0]])
        for group in groups[1:]:
            common_set.intersection_update(hierarchy[group])

        return next(iter(common_set), "No common hypernym found")

    # def get_common_hypernym(self, path):
    #     hierarchy = {}
    #     for group in path:
    #         synsets = wn.synsets(group)
    #         if synsets:
    #             hypernyms = synsets[0].hypernym_paths()
    #             for path in hypernyms:
    #                 for node in path:
    #                     hierarchy.setdefault(node.name().split('.')[0], 0)
    #                     hierarchy[node.name().split('.')[0]] += 1
    #     common_hypernym = max(hierarchy, key=hierarchy.get, default="No common hypernym found")
    #     return common_hypernym

    def wrap_text(self, text, max_len):
        words = text.split(", ")
        new_text = ""
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 2 > max_len:
                if current_line:
                    new_text += current_line[:-2] + ",\n" 
                current_line = word + ", "  
            else:
                current_line += word + ", "
        new_text += current_line[:-2]  
        return new_text

class TheGraphRes(QMainWindow):
    def __init__(self, graph_type, display_text):
        super().__init__()
        uic.loadUi("./TheGraphRes.ui", self)
        self.display_results(graph_type, display_text)
        self.back_button.clicked.connect(self.back_function)

    def back_function(self):
        widget.removeWidget(widget.currentWidget())

    def display_results(self, graph_type, display_text):
        label = self.findChild(QLabel, 'label')
        label.setStyleSheet("font-size: 20px;")
        label.setTextFormat(Qt.TextFormat.RichText)
        label.setText(f"<br><b>Selected Graph: {graph_type}</b><br><br><br><b>Hierarchical Data:</b><br><br>{display_text}")


app = QApplication(sys.argv)
widget = QStackedWidget()

home_page = HomePage()
xai_interface_page = XAIInterface()
xai_query_page = XAIQuery()

widget.addWidget(home_page)
widget.addWidget(xai_interface_page)
widget.addWidget(xai_query_page) 

widget.show()
sys.exit(app.exec_())