# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory:
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description 
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate    


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        phrase = phrase.lower()
        self.phrase = phrase 
    def is_phrase_in(self, text):
        for punctuation in string.punctuation:
            text = text.replace(punctuation, " ")
        textWords = text.lower().split()
        phraseWords = self.phrase.split() 
        
        for i in range(len(textWords) + 1 - len(phraseWords)):
            isIn = False 
            for j in range(len(phraseWords)):
                if phraseWords[j] == textWords[i+j]:
                    isIn = True 
                else:
                    isIn = False 
                    break     
            if isIn:
                return True 
        return False             



# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        text = story.title
        return self.is_phrase_in(text)


# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        text = story.description
        return self.is_phrase_in(text)

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
#        "3 Oct 2016 17:00:10 ".
class TimeTrigger(Trigger):
    def __init__(self, time):
        dt = datetime.strptime(time, "%d %b %Y %H:%M:%S")
        dt = dt.replace(tzinfo=pytz.timezone("UTC"))
        self.time = dt 


# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.pubdate.replace(tzinfo=pytz.timezone("UTC")) < self.time:
            return True 
        else:
            return False     

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.pubdate.replace(tzinfo=pytz.timezone("UTC")) > self.time:
            return True 
        else:
            return False     

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, T):
        self.trigger = T
    def evaluate(self, story):
        return not self.trigger.evaluate(story)    

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, T1, T2):
        self.trigger1 = T1
        self.trigger2 = T2 
    def evaluate(self, story):
        return (self.trigger1.evaluate(story) and self.trigger2.evaluate(story))

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self.trigger1 = T1
        self.trigger2 = T2 
    def evaluate(self, story):
        return (self.trigger1.evaluate(story) or self.trigger2.evaluate(story))

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filtered_stories.append(story)
                break 
    return filtered_stories            



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    triggers_list = []
    triggers_dict = {}

    for line in lines:
        arguments = line.split(',')
        if arguments[0] == "ADD":
            for trigger_name in arguments[1:]:
                triggers_list.append(triggers_dict[trigger_name])
        else:
            trigger_name = arguments[1]
            name = arguments[0]
            if trigger_name == "TITLE":
                phrase = arguments[2]
                triggers_dict[name] = TitleTrigger(phrase)
            elif trigger_name == "DESCRIPTION":
                phrase = arguments[2]
                triggers_dict[name] = DescriptionTrigger(phrase)    
            elif trigger_name == "AFTER":
                date = arguments[2]
                triggers_dict[name] = AfterTrigger(date)   
            elif trigger_name == "BEFORE":
                date = arguments[2]
                triggers_dict[name] = BeforeTrigger(date)       
            elif trigger_name == "NOT":
                T1 = arguments[2]
                triggers_dict[name] = NotTrigger(triggers_dict[T1])
            elif trigger_name == "AND":
                T1, T2 = arguments[2], arguments[3]
                triggers_dict[name] = AndTrigger(triggers_dict[T1], triggers_dict[T2]) 
            elif trigger_name == "OR":
                T1, T2 = arguments[2], arguments[3]
                triggers_dict[name] = OrTrigger(triggers_dict[T1], triggers_dict[T2])          
            else:
                pass


    return triggers_list



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        # t1 = TitleTrigger("SAF")
        # t2 = DescriptionTrigger("aloysius")
        # t3 = DescriptionTrigger("Singapore")
        # t4 = AndTrigger(t2, t3)
        # triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('debate_triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

