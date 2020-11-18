#!/usr/bin/env python
import os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

print("Welcome to PDBmutator - create structural variants from PDB and alignment")
cmd = 'gedit README.md'
os.system(cmd)

class PDBMUTATORApp(App):
#    kv_directory = 'kivy_templates'
    def build(self):
        return MyLayout()
   
class MyLayout(Widget):
    
      
    # define buttons and actions
    def btn1(self):
        print("running PDBmutator - amino acid replacements") 
        cmd = 'perl PDBmutator1.pl'
        os.system(cmd)
    def btn2(self):
        print("running PDBmutator - DNA substitution/polymorphism") 
        cmd = 'perl PDBmutator2.pl'
        os.system(cmd)
    def btn3(self):
        print("running PDBmutator - variants from protein alignment") 
        cmd = 'perl PDBmutator3.pl'
        os.system(cmd)
       


if __name__ == '__main__':
    PDBMUTATORApp().run()
