#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, re, math, time, random
import Tkinter, Tkdnd, tkFileDialog
from Tkconstants import PAGES, UNITS, NORMAL, RAISED, SUNKEN, HORIZONTAL, RIGHT, BOTH, LEFT, BOTTOM, TOP, NW, HIDDEN, X, Y, ALL, CENTER
import tkSnack
import wave


#### Files ####
config_file="./Spanish-lettersnumbers/config_spanish.py"
results_file = "resultsRAN.txt"
data_path = "dataRAN"



class MainFrame(Tkinter.Frame):
  def __init__(self, master, *scripts, **opts):

    # build gui:
    Tkinter.Frame.__init__(self, master, **opts)
    master.title("RAN")
    self.scripts = list(scripts)
    self.opts = {}

    self.display_var = Tkinter.StringVar("")
    width = master.winfo_screenwidth()
    self.display = Tkinter.Message(self, justify=LEFT, textvar=self.display_var,
                     font=(fontname, fontsize),
                     width=width-(width/10), bg="white")
    self.display.pack(fill=BOTH, expand=1)

    self.entry_var = Tkinter.StringVar("")
    self.entry = Tkinter.Entry(self, font=(fontname, fontsize),
                               textvar=self.entry_var)
    self.entry.pack(fill=X)
#    self.entry.bind('<Return>', lambda e:self.key_pressed('<Return>'))

    self.bind('<space>', lambda e:self.key_pressed('<space>'))
    # Lexical closures suck:
    def event_handler_creator(frame, key):
      return lambda e:frame.key_pressed(key)

    self.focus_set()

    self.key_pressed(None)

  def key_pressed(self, key):
    if self.scripts:
      self.scripts[0].next(self, key, **self.opts)
    else:
      sys.exit(0)

  def next_script(self, **opts):
    self.opts.update(opts)
    self.scripts.pop(0)

  def set_text(self, text, justify=None, new_fontsize=None):
    if new_fontsize:
                    self.display["font"] = "%s %d" %( fontname, new_fontsize)
    else:
                    self.display["font"] = "%s %d" %( fontname, fontsize)          
                    
    if justify:
        self.display["justify"] = justify
    self.display_var.set(text)
    

class Text(object):
          
  
  def __init__(self, text, align=LEFT):
    self.text = text
    self.align = align
  def next(self, frame, key=None, **opts):
    frame.set_text(self.text, self.align)
    frame.next_script()


    
class RAN(object):
  def __init__(self, items_to_display,type_item,practice=False):
    self.type_item=type_item
    self.reading_items = self.items_obj(items_to_display[self.type_item])
    self.reading_items_len =len(items_to_display[self.type_item])
    self.text =""
    # data strctures for collecting the results:
    self.practice = practice
    self.audiofile= "none"
    self.save_audio= save_audio and not(practice)
    self.number = 0
    self.times = []
    self.time = 0
    self.acumulated_time=0
    self.recorder = tkSnack.Sound()

    self.next = self.before_show_element

  def items_obj(self, items_list):
    for i in items_list :
       yield i

  def before_show_element(self, frame, key=None, **opts):
    #before the actual item, I want to show with _ what they would have to read
    self.text = make_serie(self.reading_items.next())
    preview= re.sub('[^\s]',"_",self.text)
    frame.set_text(preview,new_fontsize= fontsize_test)
    self.next = self.show_element
  
  
                                
  def show_element(self, frame, key=None, **opts):
    if key != None and key != "<space>":
      return
    #element, self.desired_answer = [s.strip() for s in reading_items.next().split('\t')]
    #self.times.append(time.time())
    
    frame.set_text(self.text, new_fontsize= fontsize_test)
    print "reading:\n"
    print self.text
    if self.save_audio:
                    self.audiofile= data_path+"/s_%s_type_%s_n_%d.wav" % (subject_id, self.type_item,self.number)
                    self.recorder = tkSnack.Sound(file=self.audiofile,
                                                  channels=use_channels,
                                                  frequency=use_frequency,encoding="Lin16")#,,encoding=use_encoding
                                                  #fileformat=use_fileformat,
                                                  #)
                    self.recorder.record()
                    print "Recording... "+ self.audiofile+ "\n"
    self.time=time.time()  #initial time
    
    self.number += 1
    self.next = self.store_results

  def store_results(self, frame, key, **opts):

    
   #self.times.append([self.time,time.time()] )  #intitial, final time
    if self.save_audio:
                    self.recorder.stop()
                    print "End  of "+ self.audiofile +" \n"
          #save acumlated time
    self.acumulated_time = self.acumulated_time + (time.time()- self.time)
          
          ##RAW data:
          #item number, practice, type, audio file, initial time, final time, practice self.practice, item text splitted with |
    resultLine= "%d, %s, %s, %s, %f, %f, %f, %s" % (self.number, 
                                            self.practice, 
                                            self.type_item,
                                            self.audiofile,
                                            self.time, 
                                            time.time(),
                                            (time.time()- self.time),
                                            self.text.replace("\n","||")) 
                                            
    store_line(resultLine, results_file_raw)
                    
    if self.number == self.reading_items_len: 
     frame.after(0, lambda:self.show_results(frame, **opts))
    else:
     frame.after(0,lambda:self.before_show_element(frame, **opts))
    
  
  def show_results(self, frame, **opts):

   

#    frame.set_text(practice_summary % {
#      "total":reading_items,
#      "time":self.times})

#    store_line("# Practice processing items: %d"
#                      % practice_processing_items)
    #print ">", self.times, diff(self.times), sd(self.times)
#    time_out = int(1000 * (mean(diff(self.times[measure_time_after_trial:]))
#          + time_out_factor * sd(diff(self.times[measure_time_after_trial:]))))
#    store_line("# Mean rt: %.02f" % mean(diff(self.times)))
#    store_line("# Accuracy of answers: %.02f" %
#                           (float(self.correct)/practice_processing_items))

#calcular el av y guardarlo
    av = self.acumulated_time / self.number
    #subject id, date, number of items, average time
    store_line("%s, %s, %s, %s, %d, %f" % (subject_id, self.type_item, self.practice, time.asctime(), self.number, av),results_file)

    frame.set_text(end_set)
    frame.next_script( **opts)



class GoodbyeScript(object):
  def next(self, frame, key=None, **opts):
    frame.set_text(good_bye_text)
#    store_line("phase\tsid\tlevel\tmemory\tverification\tmean_rt\tmax_rt")
#    store_line('\n'.join(opts["results"]))
    frame.next_script()

def make_serie(text_to_conv):   ##Norton Wolf 2012 style
    newtext =text_to_conv.strip()
    newtext = re.sub(' ',"  ",newtext)
    newtext = re.sub('\n',"\n\n",newtext)            
    return newtext
    

def store_line(s, filename, mode='a'):
  if not os.path.exists(data_path):  #I want to save the data always in dataRAN
    os.makedirs(data_path)           
  f = file(data_path+"/"+filename, mode)
  #os.path.isfile(path)
  if(os.path.getsize(data_path+"/"+filename)==0):
    f.write("# RAN test" + '\n')
    f.write("# written by Bruno Nicenboim <bruno.nicenboim@uni-potsdam.de> (adapted from script of Titus v.d. Malsburg <malsburg@uni-potsdam.de>)"+ '\n')
    f.write("# University of Potsdam, 2012"+ '\n')
  f.write(s + '\n')
  f.close()


def request_subject_id():
  print "Please enter a subject id consisting of numbers and letters: ",
  sid = sys.stdin.readline()[:-1]
  mo = re.match('[a-zA-Z0-9]+', sid)
  if mo and mo.group() == sid:
    return sid
  else:
    return request_subject_id()
    
    





#ask for subject
subject_id = request_subject_id() 
results_file_raw = subject_id + ".ran.dat"



while os.path.exists(data_path+"/"+results_file_raw):
   print "A results file for this subject id already exists."
   print "Shall I overwrite it? (y/n)"
   if sys.stdin.readline().strip() == "y":
     f = file(data_path+"/"+results_file_raw, 'w')
     f.close()
     break
   else:
     results_file_raw = request_subject_id()


store_line("item_number, practice, self.type_item, audio_file, initial_time, final_time, reading_loud_time,  item_text", results_file_raw)
if not os.path.exists(data_path+"/"+results_file):
             store_line("subject_id, type_item, practice, time, number_of_items, average",results_file)

exec file(config_file)



  # Setup GUI and take off:
root = Tkinter.Tk()
tkSnack.initializeSnack(root)
  
  
main_frame = MainFrame(root, Text(instructions), Text(before_practice), RAN(practice_items,type_item="letters",practice=True),
                         Text(before_test1), RAN(items,"letters")
                        ,Text(before_test2), RAN(items,"numbers"), GoodbyeScript())
main_frame.pack(fill=BOTH, expand=1)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set() # <-- move focus to this widget
root.bind("<Escape>", lambda e: e.widget.quit())
root.mainloop()
