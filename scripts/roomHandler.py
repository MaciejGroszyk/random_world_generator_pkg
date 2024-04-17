from drawRoom import RoomDrawCreator, DrawRoomHorizontal, DrawRoomVertical
from room import Room

class RoomHandler():
    def __init__(self) -> None:
        self.__rdc = RoomDrawCreator()
        self.__img = self.__rdc.img
        self.__draw = self.__rdc.draw
        
        self.__drh = DrawRoomHorizontal(self.__img, self.__draw)
        self.__drv = DrawRoomVertical(self.__img, self.__draw)
        
    def drawInitRoom(self, room : Room) -> None:
        self.__drh.drawWall(0)
        self.__drh.drawWall(room.getHeight())
        self.__drv.drawWall(0)
        self.__drv.drawWall(room.getWidth())

    def save(self) -> None:
        self.__rdc.saveImage()
