import fst

testN = [3,5,2]
testWords = [["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"],["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"],["hello", "one", "even", "never", "now", "world", "draw"]]

for i in range(len(testN)):
    print(fst.solution(testN[i], testWords[i]))