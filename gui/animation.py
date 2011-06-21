# -*- coding: utf-8 -*-
#
# This file is part of MyPaint.
# Copyright (C) 2007-2010 by Martin Renold <martinxyz@gmx.ch>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

import gtk
from gettext import gettext as _

class Animation(object):
    def __init__(self, doc):
        self.doc = doc
        self.model = doc.model.ani
    
    def get_init_actions(self):
        # name, stock id, label, accelerator, tooltip, callback
        actions = [
            ('PrevFrame', gtk.STOCK_GO_UP, _('Previous Frame'), 'Up', None, self.previous_frame_cb),
            ('NextFrame', gtk.STOCK_GO_DOWN, _('Next Frame'), 'Down', None, self.next_frame_cb),
            ('PrevKeyFrame', None, _('Previous Keyframe'), '<control>Up', None, self.previous_keyframe_cb),
            ('NextKeyFrame', None, _('Next Keyframe'), '<control>Down', None, self.next_keyframe_cb),
            ('PlayPausePenciltest', None, _('Play/Pause Penciltest'), '<control>p', None, self.playpause_penciltest_cb),
            ('StopPenciltest', None, _('Stop Penciltest'), None, None, self.stop_penciltest_cb),
            ('AddCel', gtk.STOCK_ADD, _('Add cel to this frame'), 'c', None, self.add_cel_cb),
            ('ToggleKey', gtk.STOCK_JUMP_TO, _('Toggle Keyframe'), 'k', None, self.toggle_key_cb),
            ('InsertFrames', gtk.STOCK_ADD, _('Insert frame'), None, None, self.insert_frames_cb),
            ('PopFrames', gtk.STOCK_REMOVE, _('Remove frame'), None, None, self.pop_frames_cb),
        ]
        return actions

    def previous_frame_cb(self, action):
        if self.model.frames.has_previous():
            self.model.previous_frame()
    
    def next_frame_cb(self, action):
        if self.model.frames.has_next():
            self.model.next_frame()

    def previous_keyframe_cb(self, action):
        if self.model.frames.has_previous_key():
            self.model.previous_keyframe()

    def next_keyframe_cb(self, action):
        if self.model.frames.has_next_key():
            self.model.next_keyframe()

    def add_cel_cb(self, action):
        self.model.add_cel()

    def playpause_penciltest_cb(self, action):
        self.model.playpause_penciltest()

    def stop_penciltest_cb(self, action):
        if self.model.penciltest_state == "play":
            self.model.stop_penciltest()

    def toggle_key_cb(self, action):
        self.model.toggle_key()

    def insert_frames_cb(self, action):
        self.model.insert_frames()

    def pop_frames_cb(self, action):
        self.model.pop_frames()
