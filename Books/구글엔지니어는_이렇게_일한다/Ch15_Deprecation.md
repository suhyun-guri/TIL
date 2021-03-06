<I style='color:gray;'> -- 본 내용은 구글 엔지니어는 이렇게 일한다(한빛미디어)를 요약한 내용입니다. -- </I>

# Ch15. 폐기 (Deprecation)
모든 시스템은 나이를 먹는다. 주변 환경이 끊임없이 변하기 때문에 기존의 시스템은 서서히 구식이 되는 것이다.

- **폐기**
    - 기존에 의존하던 낡은 생태계에서 떼어내 새로운 환경으로 이주하는 과정을 순차적으로 진행하여 궁극적으로는 낡은 시스템을 완전히 걷어내는 과정을 의미한다.

## 1. 폐기시키는 이유
"코드는 자산이 아니라 부채다" 라는 전제에서 시작한다.

가치를 만들어내는 것은 코드 '자체'가 아닌 '기능'이다. <br> 
똑같은 기능을 하는 두 코드가 있을 때, 1만 줄이나 되는 스파게티 코드보다는 이해하기 쉽게 짜여서 유지보수도 문제 없는 한 줄짜리를 더 선호할 것이다. <br> 이러한 지나친 코드나 더 이상 필요 없는 시스템들을 제거해야 한다.

폐기는 시대에 뒤처졌음을 보여줄 수 있고 비슷한 기능의 대체재가 존재하는 시스템에 적합하다. 

## 2. 폐기는 왜 그리 어려운가?
> **하이럼의 법칙** <br> 
API를 사용하는 유저가 충분히 많다면, 여러분이 어떤 의도를 가지고 API를 설계했든, 여러분의 시스템에서 관측 가능한 모든 행동들은 사용자에 의해 결정됩니다.
1. 하이럼의 법칙 <br>
    하이럼의 법칙에 의해 시스템은 사용자 수가 늘수록 설계자가 예상하지 못한, 전에 본 적 없는 방식을 이용될 가능성이 커져서 폐기 작업을 그만큼 어렵게 만든다. 

    즉, 사용자가 발견한 새로운 사용법은 '되니깐 쓰는 것'이지 시스템이 '보장하는 동작'이 아니다. 이런 맥락에서 시스템 하나를 제거한다는 것은 돌이킬 수 없는 변경이 될 수 있다.

2. 옛 시스템을 향한 애착 <br>
    엔지니어들에게 몇 년을 쏟아 구축한 무언가를 걷어내라고 설득하기란 쉽지 않다. 그러나 궁극적으로 스스로에게 피해가 돌아온다.

    구글은 코드 리포지토리에서 과거 이력까지 검색할 수 있도록 했으며 제거된 코드라도 언제든 다시 찾을 수 있게 하여 상실감을 줄여주었다.

3. 정치 <br>
    오래된 시스템을 제거하는 데에는 실제로 눈에 보이는 비용이 드는 반면, 아무것도 하지 않고 시스템을 방치해서 새어나가는 비용은 눈에 잘 띄지 않는다. 이를 이해관계자들에게 납득시키기가 어렵다.

완전히 대체하기보다는 시스템 이용자들이 각자의 업무 현장에서 점진적으로 개선시키는 편이 쉬울 때가 많다. <br>
현장에서 조금씩 리팩터링하여 폐기를 점진적으로 진행하면 기존 시스템을 계속 운영하면서도 이용자에게 더 쉽계 혜택을 제공할 수 있다.


### 설계 단계에서의 폐기
'언젠가는 폐기하게 될 시스템을 설계한다' 
> 원자력 발전소를 설계하려면 훗날 수명이 다한 원자로를 어떻게 해체하고 자금은 어떻게 조달할지도 반드시 고려해야 한다. 이를 인지하는 것이 실제로 설계에 큰 영향을 준다.

구글에서 엔지니어링 팀에 권장하는 고려사항
- 내 제품의 고객이 잠재적인 대체품으로 이주하기가 얼마나 쉬울까?
- 내 시스템을 한 부분씩 점진적으로 교체하려면 어떻게 해야 할까?

마지막으로, 프로젝트의 장기 지원 여부는 조직에서 프로젝트를 처음 승인할 때 결정된다는 것이다.

회사에서 기대 수명 동안 제대로 지원하지 못할 것 같은 프로젝트는 시작하지 마라. 폐기시키기로 결정한다 해도 여전히 비용이 든다. 하지만 잘 계획하고 적절한 도구와 정책 개발에 투자한다면 이 비용을 상당히 줄일 수 있다.

## 3. 폐기 유형
크게 '권고'와 '강제'로 구분한다.

### 권고 폐기
기한이 없고 조직에서도 우선순위가 높지 않은 (폐기 작업에 자원을 투입할 의지가 없는) 경우이다.


### 강제 폐기

### 폐기 경고


## 4. 폐기 프로세스 관리

