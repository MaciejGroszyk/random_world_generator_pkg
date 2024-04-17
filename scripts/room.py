
class Room():
    def __init__(self, point : tuple,  width : int, height : int, door : tuple = None) -> None:
        self.__point = point
        self.__height = height
        self.__width = width
        self.__door = door

    def getPoint(self) -> tuple:
        return self.__point

    def getHeight(self) -> int:
        return self.__height

    def getWidth(self) -> int:
        return self.__width
    
    def getDoor(self) -> tuple:
        return self.__door
    
    def setDoor(self, w, h) -> None:
        self.__door = (w, h)
    
    def isDoor(self) -> bool:
        return (self.__door is None)
