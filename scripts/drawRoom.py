from PIL import Image, ImageDraw
from roomParams import RoomParams
import os
import random

class RoomDrawCreator():
    def __init__(self):
        self.img_params = RoomParams()
        self.__current_file_path = os.path.abspath(os.path.dirname(__file__)) 
        
        self.img = self.getEmptyImg()
        self.draw = self.getDrawInstance()
        
    def getEmptyImg(self) -> Image:
        ecv = self.img_params.EMPTY_COLOR_VALUE
        empty_color = (ecv, ecv, ecv)
        return Image.new('RGB', self.img_params.IMG_SIZE, empty_color)

    def getDrawInstance(self) -> ImageDraw:
        return ImageDraw.Draw(self.img)

    def saveImage(self):
        IMG_NAME = "/test2.png"
        self.img.save(self.__current_file_path+IMG_NAME)

class DrawRoom():
    def __init__(self, img, draw): 
        self.img_params = RoomParams()
        self.img = img 
        self.draw = draw

    def drawWall(self):
        pass
    
    def drawRandomWall(self):
        pass

    def drawRandomWallWithDoor(self):
        pass

    def drawDoor(self):
        pass

    def getEmptyColor(self) -> tuple:
        ecv = self.img_params.EMPTY_COLOR_VALUE
        return (ecv, ecv, ecv)

    def getWallColor(self) -> tuple:
        wcv = self.img_params.WALL_COLOR_VALUE
        return (wcv, wcv, wcv)
    
    def getRandomValue(self, val) -> int:
        return random.randint(0, val)

    def getRandomWidthHeight(self) -> tuple:
        w = self.getRandomValue(self.img_params.IMG_SIZE[0])
        h = self.getRandomValue(self.img_params.IMG_SIZE[1])
        return w, h

class DrawRoomHorizontal(DrawRoom):
    def drawWall(self, height):
        w = self.img_params.IMG_SIZE[0]
        self.draw.line((0, height, w, height), fill=self.getWallColor(), width= self.img_params.WALL_SIZE)

    def drawDoor(self, height, door_pose):
        self.draw.line((door_pose, height, door_pose + self.img_params.DOOR_SIZE , height),
                        fill=self.getEmptyColor(), width= self.img_params.WALL_SIZE)

    def drawRandomWall(self):
        h = self.img_params.IMG_SIZE[1]
        self.drawWall(self.getRandomValue(h))

    def drawRandomWallWithDoor(self):
        w, h = self.getRandomWidthHeight()
        self.drawWall(h)
        self.drawDoor(h, w)

class DrawRoomVertical(DrawRoom):
    def drawWall(self, width):
        h =  self.img_params.IMG_SIZE[1]
        self.draw.line((width, 0, width, h), fill=self.getWallColor(), width= self.img_params.WALL_SIZE)

    def drawDoor(self, width, door_pose):
        self.draw.line((width, door_pose, width, door_pose + self.img_params.DOOR_SIZE ),
                        fill=self.getEmptyColor(), width= self.img_params.WALL_SIZE)

    def drawRandomWall(self):
        w = self.img_params.IMG_SIZE[0]
        self.drawWall(self.getRandomValue(w))

    def drawRandomWallWithDoor(self):
        w, h = self.getRandomWidthHeight()
        self.drawWall(w)
        self.drawDoor(w, h)