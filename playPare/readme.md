
## [플레이페어 암호](https://softeer.ai/practice/info.do?idx=1&eid=804)

<br/> 주어진 문자열의 왼쪽 부터 중복되지 않게 표시된다
<br/> 채워지지 않은 곳은 알파벳 순서대로 채워 넣는다
<br/> 암호화 할 문자를 2개씩 끊어주고 중복된는 문자열이면 사이에 X를 X가 안되면 사이에 Q를 넣고 나눈다
<br/> 마지막 한글자가 남을 때도 X를 넣어서 짝수개를 맞추고 만약 마지막 글자가 X여도 X를 넣는다
<br/> 2개씩 분리한 단어가 같은 행에 있으면 오른쪽으로 한칸씩
<br/> 같은 열에 있으면 아래로 한칸씩 
<br/> 두 조건 모두 해당 안되면 열 위치를 바꾼다

예제

```
 key : PLAYFAIRCIPHERKEY

HE Lx LO WO RL Dx -> ei yv rv vq br gw
                     EI YV RV VQ BR GW
PLAYF
IRCHE
Kbdgm
noqst
uvwxz
```

## 요소

- 입력 : 
    * 메세지
    * 키

- 출력 : 암호화된 메세지

## result

- [인덱스 번호로 순차적으로 서치](/playPare/playPare.py)
    <br/>ㅤㅤㅤㅤㅤㅤ

- [조건문으로만 해결](/wellFrog/solution.py)
    <br/>ㅤㅤㅤㅤㅤㅤ모범 답안