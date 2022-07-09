<I style='color:gray;'> -- 본 내용은 구글 엔지니어는 이렇게 일한다(한빛미디어)를 요약한 내용입니다. -- </I>

# Ch14. 더 큰 테스트 (Larger Testing)

In this chapter, we’ll discuss what we mean by “larger tests,” when we execute them, and best practices for keeping them effective. 

### 1. 더 큰 테스트란? (What is Larger Testing?)
구글은 테스트 범위(scope)라는 개념을 사용한다. <br>
더 큰 테스트들은 작은 테스트와 많은 면에서 다르다. 
- 느릴 수 있다. 구글에서 대규모 테스트의 기본 타임아웃은 15분이나 1시간이다. 몇 시간이나 며칠이 걸리는 테스트도 만들어 활용한다.
- 밀폐되지 않을 수 있다. 대규모 테스트는 다른 테스트나 최종 사용자와 자원 및 트래픽을 공유하기도 한다.
- 비결정적일 수 있다. 밀폐되지 않은 대규모 테스트라면 다른 테스트나 사용자 상태에 영향을 받을 수 있어서 완벽히 결정적이라고 보장하기가 거의 불가능하다.

이러한 단점에도 불구하고 더 큰 테스트를 이용하는 이유?
- 충실성(fidelity)
    - 테스트가 대상의 실제 행위를 얼마나 충실하게 반영했느냐