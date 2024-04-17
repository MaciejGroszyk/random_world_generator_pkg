
from roomHandler import RoomHandler
from roomParams import RoomParams

from room import Room

from PIL import Image, ImageDraw

class WorldMapPngGenerator():
    def __init__(self) -> None:
        self.room_list = []
        self.roomParams = RoomParams()
        self.roomHandler = RoomHandler()
        
    def initRoom(self) -> None:
        init_point = (0, 0)
        width = self.roomParams.IMG_SIZE[0]
        height = self.roomParams.IMG_SIZE[1]
        room = self.__getNewRoom(init_point, width, height)
        self.roomHandler.drawInitRoom(room)
        self.room_list.append(room)

    def __getNewRoom(self, point, width, height, room = None) -> Room:
        return Room(point, width, height, room)

    def saveWorldMapPng(self):
        self.roomHandler.save()

if __name__ == "__main__":
    wmpg = WorldMapPngGenerator()
    wmpg.initRoom()
    wmpg.saveWorldMapPng()
    