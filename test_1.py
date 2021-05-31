import unittest

from shapes import Rectangle,Triangle,Circle

class ArithmethicsTest(unittest.TestCase):

    def testSummation(self):
        result = Rectangle(2,2).__add__(Triangle(5,2))
        self.assertEquals(9.0,result)
    
    def testSubtraction(self):
        result = Rectangle(5,2).__sub__(Triangle(5,2))
        self.assertEquals(5.0,result)

        result = Rectangle(6,2).__sub__(Triangle(5,2))
        self.assertEquals(7.0,result)
    
    def testEqual(self):
        falseResult = Rectangle(5,2).__eq__(Triangle(5,2))
        self.assertEquals(False,falseResult)

        trueResult = Rectangle(1,1).__eq__(Triangle(1,2))
        self.assertEquals(True,trueResult)

    def testColor(self):
        temp = Rectangle(1,2,"red")
        result = temp.getColor()
        self.assertEquals("red",result)


if __name__ == "__main__":
    unittest.main()



