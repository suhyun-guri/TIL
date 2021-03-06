<I style='color:gray;'> -- 본 내용은 구글 엔지니어는 이렇게 일한다(한빛미디어)를 요약한 내용입니다. -- </I>

# Ch14. 더 큰 테스트 (Larger Testing)
- what we mean by “larger tests” 
- when we execute them
- best practices for keeping them effective. 

## 1. 더 큰 테스트란? (What is Larger Testing?)
구글은 테스트 범위(scope)라는 개념을 사용한다. <br>
더 큰 테스트들은 작은 테스트와 많은 면에서 다르다. 
- 느릴 수 있다. 구글에서 대규모 테스트의 기본 타임아웃은 15분이나 1시간이다. 몇 시간이나 며칠이 걸리는 테스트도 만들어 활용한다.
- 밀폐되지 않을 수 있다. 대규모 테스트는 다른 테스트나 최종 사용자와 자원 및 트래픽을 공유하기도 한다.
- 비결정적일 수 있다. 밀폐되지 않은 대규모 테스트라면 다른 테스트나 사용자 상태에 영향을 받을 수 있어서 완벽히 결정적이라고 보장하기가 거의 불가능하다.

### 이러한 단점에도 불구하고 더 큰 테스트를 이용하는 이유? <br>
단위 테스트는 개별 함수, 객체, 모듈에 대한 확신을 심어준다. 반면 더 큰 테스트는 시스템 '전체'가 의도대로 동작한다는 확신을 더해주는 역할을 한다. 이들을 자동화해두면 다양하게 확장할 수 있다.

- 충실성(fidelity)
    - 테스트가 대상의 실제 행위를 얼마나 충실하게 반영했느냐를 나타내는 속성
    - <img src=https://user-images.githubusercontent.com/70987343/178109388-0d627e00-2406-4aff-9181-42bd5f443cd7.png> (SUT : System Under Test)
    - 단위 테스트 (Unit Tests)는 대상 코드를 검증해주지만 프로덕션 환경에서와는 매우 다르게 동작할 것이며 오른쪽 끝의 프로덕션은 당연히 테스트 충실성이 가장 높은 환경이다.
    - 더 큰 테스트의 핵심은 이 사이에서 가장 적합한 지점을 찾는 것. 충실성이 높아질수록 비용이 커져서 테스트 실패 시 입는 손해도 크기 때문이다.
- 단위 테스트가 손 대기 어려운 영역 (Common Gaps in Unit Tests)
    - 부정확한 테스트 대역 (Unfaithful doubles)
    - 설정 문제 (Configuration issues)
    - 과부하 시 나타나는 문제 (Issues that arise under load)
    - 예기치 못한 동작, 입력, 부작용 (Unanticipated behaviors, inputs, and side effects)
    - 창발적 행위와 진공 효과 (Emergent behaviors and the "vacuum effect")

## 2. 더 큰 테스트 @Google
### 수명
어떤 테스트가 가장 적합한지는 코드의 기대 수명에 따라 달라진다.

단위 테스트는 기대 수명이 몇 시간 이상만 되면 충분히 가치가 있다. 나머지 더 큰 테스트들 모두 수명이 더 긴 소프트웨어에 유용하다. 하지만 수명이 길어질수록 주 관심사가 테스트의 유지보수로 옮겨간다.

<img src=https://user-images.githubusercontent.com/70987343/178110355-f944104a-3259-432e-92e5-6f378d18c434.png height=350px>


건강한 상태를 오래 유지하는 '핵심'은 개발 시작 후 며칠 안으로 단위 테스트를 만들어 테스트 피라미드를 쌓기 시작하는 것이다. 그 후 수동으로 수행하던 종단간 테스트를 자동화된 통합 테스트로 대체해 피라미드 위층으로 올린다.

구글은 코드를 서브밋하려면 반드시 단위 테스트를 포함하도록 규정하여 해결했다. 단위 테스트와 수동 테스트 사이의 간극을 매우는 데 소홀해서는 안된다.

### 구글 규모에서의 더 큰 테스트
다음과 같은 테스트 대상(SUT)이 있다고 해보자.

<img src=https://user-images.githubusercontent.com/70987343/178127891-f2eec655-beb6-4947-a050-78b88c883b34.png height=350px>

사용자, 소셜 그래프, 소셜 스트림, 광고 등이 혼합된 사회 관계망 서비스용 시스템이다. 

종단간 테스트가 필요한 개별 시나리오 수는 SUT 구조에 따라 기하급수적으로 혹은 조합의 수만큼 늘어나므로 이런 식의 성장은 확장하는 데 한계가 분명하다. 따라서 성장에 맞춰 더 큰 테스트들도 지속해서 관리할 수 있으려면 새로운 전략이 필요하다.

더 큰 테스트들은 원하는 규모에서 잘 작동하면서도 충실성이 상당히 높게 구현하는 게 관건이다. 

## 3. 더 큰 테스트의 구조
큰 테스트를 진행하는 일반적인 흐름
1. 테스트 대상 시스템 확보
2. 필요한 테스트 데이터 준비
3. 대상 시스템을 이용해 동작 수행
4. 행위 검증

### 테스트 대상 시스템(System Under Test, SUT)
대규모 테스트에서의 SUT는 하나 이상의 독립된 프로세스에서 수행된다.

구글에는 다양한 형태의 SUT가 존재하며, SUT의 범위가 대규모 테스트 자체의 범위를 규정하는 주된 요소이다.

SUT의 형태는 주로 `밀폐성`, `충실성`에 의해 결정된다.

