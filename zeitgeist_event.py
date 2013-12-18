#"python taken from # from http://bazaar.launchpad.net/~zeitgeist-dataproviders/zeitgeist-datasources/git/view/head:/vim/zeitgeist.vim
#"zeitgeist.vim - a Zeitgeist logger for Vim
#"Author : Jonathan Lambrechts <jonathanlambrechts@gmail.com>

import os
import time
import dbus
import sys

# Extract | prompt | command | args | from raw input.
if(sys.argv[1]):
  
  MY_PROMPT = '$ '
  prompt = ''
  cmd = ''
  args = ''
  # output = ''
  
  line = sys.argv[1].strip()
  prompt_index = line.find(MY_PROMPT)
  
  if ( prompt_index > -1 ):
    args_index = prompt_index + len(MY_PROMPT)
    prompt = line[:args_index]
    args = line[args_index:].strip().split(" ")
    cmd = args[0]
  
  # TODO add more commands. For now only command cd triggers event.  
  if(cmd == 'cd'):

    try:
      from zeitgeist.client import ZeitgeistClient
      from zeitgeist.datamodel import Subject, Event, Interpretation, Manifestation
      zeitgeistclient = ZeitgeistClient()
      got_zeitgeist = True
    except (RuntimeError, ImportError, dbus.exceptions.DBusException):
      got_zeitgeist = False
     
    precond = os.getuid() != 0 and os.getenv('DBUS_SESSION_BUS_ADDRESS') != None
     
    if got_zeitgeist and precond:
      
      uri            = 'file:///home/saasbook/typescript.txt' # must exist
      mimetype       = 'text/plain'
      event_actor    = 'app://somefakestring.desktop'
      event_interp   = 'new'
      event_manif    = 'user'
      subject_interp = 'document'
      subject_manif  = 'file_data_object'
     
     
      subject_interpretation = {
        'todo'     : Interpretation.TODO,
        'document' : Interpretation.DOCUMENT }[subject_interp]
          
      subject_manifestation = {
        'software_item'    : Manifestation.SOFTWARE_ITEM,
        'file_data_object' : Manifestation.FILE_DATA_OBJECT }[subject_manif]
        
      event_interpretation = {
        'accept'  : Interpretation.ACCEPT_EVENT,
        'deny'    : Interpretation.DENY_EVENT,
        'send'    : Interpretation.SEND_EVENT,
        'receive' : Interpretation.RECEIVE_EVENT,
        'expire'  : Interpretation.EXPIRE_EVENT,
        'leave'   : Interpretation.LEAVE_EVENT,
        'read'    : Interpretation.ACCESS_EVENT,
        'new'     : Interpretation.CREATE_EVENT,
        'write'   : Interpretation.MODIFY_EVENT,
        'move'    : Interpretation.MOVE_EVENT,
        'delete'  : Interpretation.DELETE_EVENT }[event_interp]
     
      event_manifestation = {
        'user'      : Manifestation.USER_ACTIVITY,
        'heuristic' : Manifestation.HEURISTIC_ACTIVITY,
        'scheduled' : Manifestation.SCHEDULED_ACTIVITY,
        'world'     : Manifestation.WORLD_ACTIVITY,
        'system'    : Manifestation.SYSTEM_NOTIFICATION }[event_manif] 
     
      
      subject = Subject.new_for_values(
        uri=unicode(uri),
        text=unicode(uri.rpartition('/')[2]),
        interpretation=unicode(subject_interpretation),
        manifestation=unicode(subject_manifestation),
        origin=unicode(uri.rpartition('/')[0]),
        mimetype=unicode(mimetype)
      )
      
      # print "subject: %r" % subject
      event = Event.new_for_values(
        timestamp=int(time.time()*1000),
        interpretation=unicode(event_interpretation),
        manifestation=unicode(event_manifestation),
        actor=unicode(event_actor),
        subjects=[subject,]
      )
      
      # print "event: %r" % event
      zeitgeistclient.insert_event(event)
      # print "insert done"
