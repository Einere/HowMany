HowMany
컴퓨터언어
윤소정교수님
2013726058 최형준

1. 설명
    본 프로젝트의 프로그램인 “HowMany”는 기본적으로 “3줄 요약기”에서 영감을 얻었습니다.
    알고리즘과 로직, 구현방법의 한계 등으로 인해 온전한 “3줄 요약기”라기 보다는, 최다 빈도수 단어들을 추출하여 해당 단어가 제일 많이 포함된 문장을 출력하는 “3줄 요약기”의 열화판입니다.
    본 앱은 텍스트 파일을 입력 받아서 단어로 분해합니다. 분해한 단어들의 개수를 세어 빈도수 순으로 정렬합니다. 제일 많은 빈도수를 가진 단어 2개를 선정합니다. 해당 단어들을 하나라도 포함하는 문장을 출력하거나 둘 다 포함하는 문장을 출력하도록 동작합니다.
    추가적인 기능으로서, 단어들 중에서 최대 빈도수 상위 10개의 단어를 추출하여 파이형 그래프를 그려줍니다. 이로 인해, 사용자는 좀 더 직관적으로 단어의 빈도수를 인지할 수 있습니다.


2. 구성요소
    (1) howmany.py
        앱을 실행시키기 위한 코드파일입니다.
    (2) form.ui
        앱의 GUI를 담당하는 파일입니다.
    (3) baseball.txt, ktfire.txt, report.txt, star.txt
        UTF-8로 인코딩된 테스트용 텍스트 파일입니다. 각각의 파일은 영문 또는 한글로 이루어져 있습니다.
    (4) crow.txt
        ANSI(cp949)로 인코딩된 테스트용 텍스트 파일입니다. 해당 파일은 한글로 이루어져 있습니다.
        

3. 시작하기
    3-1. 요구사항
        HowMany앱은 PyQt5와 matplotlib을 필요로 합니다.
        
    3-2. 설치
        압축받은 zip파일 내의 howmany.py를 파이썬 IDE로 연 뒤, run하면 됩니다.

    3-3. 실행
        (1) HowMany 앱이 실행된 상태에서, open 버튼을 클릭하여 분석할 텍스트 파일을 엽니다.
        (2) input 텍스트 브라우저에 텍스트 파일의 내용이 출력됩니다.
        (3) analyze 버튼을 눌러 내용을 분석합니다.
        (4) output 텍스트 브라우저에 분석한 내용이 출력됩니다. (paragraph, sentences, words, 
        (5) draw 버튼을 눌러 최대 빈도수 상위 10개의 단어를 파이형 차트로 그립니다.
        (6) 다른 파일을 분석하고 싶다면, open 버튼을 클릭하여 분석할 다른 텍스트 파일을 엽니다.

    3-4. 실행 예시
        baseball.txt를 분석한 경우, 최대 빈도수 상위 2개 word는 "Heroes", "first"입니다.
        또한, "3줄 요약" 결과로는 
        "Song Sung-mun drove in the go-ahead run with a sacrifice fly in the top of the fifth inning, and starter Han Hyun-hee was solid in 5 1/3 innings for the Heroes’ first win of the best-of-five series"
        "9 hitter Joo Hyo-sang, making his first start of the series, rolled a single down the right field line to bring both runners home and put the Heroes ahead 2-1'
        가 됩니다.

4. 사용된 도구
    pycharm
    anaconda
    
5. 수정하지 못한 오류 
    (1) 현재 UTF-8과 ANSI(cp949)로 인코딩된 텍스트 파일은 정상적으로 읽혀지는 것을 확인했습니다만, 그 외의 인코딩으로 된 텍스트 파일은 확인하지 못하였습니다.

