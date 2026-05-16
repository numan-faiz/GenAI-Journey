# python special methods and functions
class book:
    def __init__(self,title,author):
        self.__title=title
        self.__author=author

        # special methods
    def __str__(self):
        return f"'{self.__title}' by {self.__author}"
b=book("34545","george")
print(b)

class playlist:
    def __init__(self,songs):
        self.songs=songs
    def __len__(self):
        return len(self.songs)
    def __add__(self, other):
        return playlist(self.songs+other.songs)
p1=playlist(["song1","song2"])
p2=playlist(["song3"])
print(len(p1))
print(len(p2))



class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"{self.x},{self.y}"
    def __add__(self, other):
        if not isinstance(other,point):
            return NotImplemented
        return point(self.x+other.x,self.y+other.y)
p1=point(2,3)
p2=point(7,8)
print(p1+p2)