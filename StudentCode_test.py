import SCOPP_tester;
from IOWrapper import IOWrapper
testIO = IOWrapper()
expectedIO = IOWrapper()

def test_hello():
    XtestList = [6,-3,-2,4,0,3,0]
    YtestList = [-1,-4,5,3,-2,0,0]
    #[(6, -1),(-3, -4),(-2, 5),(4, 3),(0, -2),(3, 0),(0, 0)]
    expectedList = ["Quadrant IV","Quadrant III","Quadrant II","Quadrant I","Y-axis","X-axis","Origin"]
    i=0
    for expected in expectedList:
        testX = XtestList[i]
        testY = YtestList[i]
        print("Testing: Test case",testX,testY,"Expected",expected)
        #print("Testing: Test case","Expected",expected)
        expectedIO.print(expected)
        assert SCOPP_tester.test(testX, testY ,testIO = testIO,expectedIO = expectedIO)
        #assert SCOPP_tester.test(testIO = testIO,expectedIO = expectedIO)
        i+=1
        print("Test case Passed")
    print("Code is correct.All Test cases passed")
