import SCOPP_tester;
from IOWrapper import IOWrapper
testIO = IOWrapper()
expectedIO = IOWrapper()

def test_hello():
    expectedList = []
    XtestList = []
    YtestList = []
    i=0
    for expected in expectedList:
        testX = XtestList[i]                                                                  # use these lOCs while using list object
        testY = YtestList[i]
        print("Testing: Test case",testX,YtestList,"Expected",expected)
        #print("Testing: Test case","Expected",expected)
        expectedIO.print(expected)
        assert SCOPP_tester.test(testX, testY ,testIO = testIO,expectedIO = expectedIO)
        #assert SCOPP_tester.test(testIO = testIO,expectedIO = expectedIO)
        i+=1
        print("Test case Passed")
    print("Code is correct.All Test cases passed")
