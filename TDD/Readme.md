### git
- 1단계 : git init ~ commit
- 2단계 : checkout, git log view
- 3단계 : git branch, merge
- 4단계 : github, push, pull, clone


### command
- git log --oneline --graph --all
- git add .
- git commit -m 'test'
- git push
- git pull

### TDD
- RED : 실패하는 단계
  - todo 리스트 작성
  - 명확한 스펙 확정
- GREEN : 기능 구현
  - 어떻게든 동작하도록.
  - 딱 테스트를 통과할 만큼만 구현
  - 죄악을 저질러도 좋다 (나중에 만회를 할 것이기 때문에)
- BLUE : 리팩토링 단계


> Baby step은 꼭 거쳐야 하나?
> - 꼭 그렇지는 않지만, 작은 단계 작업을 배우면 저절로 적절한 크기의 단계 작업이 가능하다.


### Test Double
- Double : 대역
- SUT를 대역하는 게 아니라 SUT가 의존하고 있는 대상에 대해서 대역 생성
- 어떤 경우 사용?
  1.  테스트 단순화
      - 의존/하위의존이 너무 많을 경우. 준비물들이 많아지게 된다. 
      - 부수효과를 제외하고 테스트 하고 싶을 때
      - 의존하고 있는 대상이 너무 느릴 경우
  2. 실제 세계에 영향을 미칠 경우 (테스트 -> 실제 세계)
  3. 실제 세계가 영향을 미칠 경우 (테스트 <- 실제 세계)
      - 비결정적인 상황들 (ex. 랜덤값 반환)

- 종류
  1. Stub
     - 특정 파라미터에 미리 정해둔 값을 return 해주도록 세팅할 수 있는 객체
     - stubbing 한다
     - SUT 내부에서 동작
  2. Mock object
     - 실제 객체와 똑같은 메서드를 가지고 있지만, 
     - 실제 코드는 들어 있지 않다.
     - 특정 메서드가 호출 되었는지 기록하는 객체
     - 단점 : 실제 코드가 아니라 테스트 놓치는 부분 있음
     - SUT 내부에서 동작
  3. Spy
     - 실제 객체 코드가 존재하는 mock object
     - 단점 : 동작이 무거워진다
  4. Fake object
     - 실제 객제와 같지만 경량화 시킴
  
### Patching
- 실제 객체의 일부 메서드를 가짜로 변경
- 게릴라 -> 고릴라 -> 몽키
- 