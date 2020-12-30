from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import os
import sys
import uuid
import base64
class TE(QTextEdit):
    def canInsertFromMimeData(self, source):
        # Returns true if the object can return an image
        if source.hasImage():
            return True
        else:
            return super(TE, self).canInsertFromMimeData(source)
    def insertFromMimeData(self, source):
        cursor = self.textCursor()
        document = self.document()
        if source.hasUrls():
            for u in source.urls():
                file_ext = splitext(str(u.toLocalFile()))
                if u.isLocalFile() and file_ext in IMAGE_EXTENSIONS:
                    image = QImage(u.toLocalFile())
                    document.addResource(QTextDocument.ImageResource, u, image)
                    cursor.insertImage(u.toLocalFile())

                else:
                    # If we hit a non-image or non-local URL break the loop and fall out
                    # to the super call & let Qt handle it
                    break
            else:
                # If all were valid images, finish here.
                return
        elif source.hasImage():
            image = source.imageData()
            uuid = hexuuid()
            document.addResource(QTextDocument.ImageResource, uuid, image)
            cursor.insertImage(uuid)
            return
        super(TE, self).insertFromMimeData(source)