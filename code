
class Point2D:
    def __init__(self, x:float, y:float):
        self.coord=(x,y)



class Polygon:
    def __init__(self, pt_list:[Point2D],color:str):
        self.points=pt_list
        self.color=color



class Polygons():

    def __init__(self):

        self.polygons=[]# lists of lists, each sublist of the form [polygon,name]


    def add_polygon(self,poly:Polygon,name:str):
        info=[poly,name]
        self.polygons.append(info)

    def remove_polygon(self,name:str):
        if len(self.polygons)==0:
            return
        else:
            for i in self.polygons:
                if self.polygons[1]==name:
                    self.polygons.remove(i)

    def save_to_file(self,filename=str):
        file=open(filename,"w")

        if len(self.polygons)==0:
            file.write("")

        else:
            for poly in self.polygons:
                line=f''
                #getting the points; poly[0] contains a list of points, each of which contains it's coordinates;
                
                pts=[]
                for pt2d in poly[0].points:
                    
                    pts.append(pt2d.coord)
                
                line+=f'{pts}'

                line+=','
                    
                #getting the color

                line+=poly[0].color

                line+=','

                #getting the name

                line+=poly[1]

                file.write(line+'\n')

        file.close()


                 



        file.close()

    #def load_from_file(filename:str):
        #file=open(filename)



ponto1=Point2D(0,0)

ponto2=Point2D(0,1)

ponto3=Point2D(1,0)

triangulo=Polygon([ponto1,ponto2,ponto3],'red')    

segmento=Polygon([ponto1,ponto2],'blue')

catetos=Polygons()

catetos.add_polygon(triangulo,'tri')
catetos.add_polygon(segmento,'segmento')


catetos.save_to_file('poly_info2.txt')

