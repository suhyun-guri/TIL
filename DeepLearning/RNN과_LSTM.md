# RNN과 LSTM
## 1. RNN (Recurrent Neural Network)
RNN(Recurrent Neural Network)은 CNN과 함께 대표적인 딥러닝 모델이다. 시계열 데이터같은 **순차 데이터(Sequential Data)** 처리를 위한 모델이다.
> 순차 데이터란? <br>
순서를 가지고 나타나는 데이터로, 데이터 내 각 개체 간의 순서가 중요하다. <br>
ex) 날짜에 따른 기온 데이터, 단어들로 이루어진 문장 등 <br>

### 연산 과정
- 모델에 들어오는 각 시점의 데이터 x마다 연산 수행
- 입력값에 따라 반복해서 출력값과 hidden state를 계산
- **이전 시점에 생성된 hidden state를 다음 시점에 사용**

### RNN의 문제점
- RNN은 출력값이 시간 순서에 따라 생성
- 각 시점의 출력값과 실제값을 비교하여 손실(Loss)값을 계산
- 역전파 알고리즘이 시간에 따라 작동 (Back-propagation Through Time (BPTT))
- So, 입력값의 길이가 매우 길어질 경우, 초기 입력값과 나중 출력값 사이에 전파되는 기울기 값이 매우 작아질 가능성이 높음
- 즉, 기울기 소실(Vanishing Gradient)문제가 발생하기 쉬움. (다른 말로 장기 의존성(Long-term Dependency)를 다루기 어려움.)

## LSTM (Long-Short Term Memory)
RNN의 기울기 소실 문제를 해결하고자 등장하였다.
LSTM은 RNN의 hidden state에 cell-state를 추가한 구조이다.
- cell state
  - 기울기 소실 문제를 해결하기 위한 핵심 장치
  - 장기적으로 기억할 정보를 조절

LSTM은 3종류의 게이트를 4개의 FC Layer로 구성한다.
- forget gate, input gate, output gate
