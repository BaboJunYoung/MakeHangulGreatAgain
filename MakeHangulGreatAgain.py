import sys

def main(sentenceList: list):
    sentence = " ".join(sentenceList)
    result = ""

    jungsungLength = 21
    jongsungLength = 28

    for char in sentence:
        if ord("가") <= ord(char) <= ord("힣"):
            # char는 한글
            pureHangul = ord(char) - ord("가")
            
            chosungIndex = pureHangul // (jungsungLength * jongsungLength)
            jungsungIndex = (pureHangul % (jungsungLength * jongsungLength) // jongsungLength)

            changedHangul = (chosungIndex * jungsungLength * jongsungLength) + (jungsungIndex * jongsungLength) + 18 + ord("가")
            
            result += chr(changedHangul)
        else: result += char
    print(result)
    return result            

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Run) python3 MakeHangulGreatAgain.py <Any Sentence You Want>")
        print("Ex) python3 MakeHangulGreatAgain.py 모든 인간은 태어날 때부터 자유로우며 그 존엄과 권리에 있어 동등하다.")
        print("    몺듮 잆값읎 탮없낪 땞붒텂 잢윲롮웂몂 긊 좂없괎 궚릾엢 잆없 돖듮핪닶.")
    else:
        main(sys.argv[1:])