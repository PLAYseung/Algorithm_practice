
## [보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258)

진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

## 요소

- 입력 : 진열대 번호 순서대로 저장된 배열

- 출력 : [시작 진열대 번호, 끝 진열대 번호]

## result

- [전체 보석의 앞 뒤 순으로 요소 제거](/shoppingJewel/shoppingJewel.py)
<br/> 제공되는 리스트에서 하나씩 제거 하면서 비교?
<br/> 앞에서 부터 제거 하고 유니크 값을 얻다가 곗수가 적어지면 뒤에서부터 제거?
<br/> 정답률 50%    

- [위의 코드의 앞뒤 변경](/shoppingJewel/shoppingGems.py)
<br/> 제시된 테스트는 만족하지만 테스트 통과 X

- [새로운 list를 만들지 않고 뒤에 부터 증가](/shoppingJewel/twoPoint.py)
<br/> 증가값을 두개를 둬서 순차적으로 탐색
<br/> 샘플테스트 통과 제출 검사 통과 X
