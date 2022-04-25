## 1. Standard SQL
- 관계형 대수
  - 관계형 데이터베이스에서 **원하는 정보를 유도하기 위한** 기본 연산 집합
  - 일반 집합 연산 (합집합 - UNION, 교집합 - INTERSECT, 차집합 - EXCEPT, 카디션 곱 - CROSS JOIN)
  - 순수 관계 연산 (셀렉션 - WHERE, 프로젝션 - SELECT, 조인 - 다양한 JOIN, 디비전)

```sql
-- student 테이블의 구조 나타내기
DESC student; 
-- 순수 관계 연산자 사용하여 테이블 조회
SELECT * FROM student;
-- 순수 관계 연산자 사용하여 조건 검색
SELECT *
FROM student
WHERE grade=3;
```

## 2. 집합 연산자
- 두 개 이상의 테이블에서 조인을 사용하지 않고 연관된 데이터를 조회하는 방법 중 하나. 
- 테이블에서 SELECT한 컬럼 수와 각 컬럼의 데이터 타입이 테이블 간 상호 호환 가능해야 한다.
- UNION, UNION ALL, INTERSECT, EXCEPT

### 2.1 UNION
- 두 개의 테이블을 하나로 만드는 연산. 합집합
- 합친 후에 테이블에서 **중복된 데이터는 제거**
- 이를 위해 UNION은 테이블을 합칠 때 정렬 과정을 발생시킨다.
```sql
SELECT * FROM A WHERE ~
UNION
SELECT * FROM B WHERE ~
--ORDER BY ~
```
### 2.2 UNION ALL
- UNION과 거의 같은 기능 수행
- 단, **중복 제거와 정렬을 하지 않음**
```sql
SELECT * FROM A WHERE ~
UNION ALL
SELECT * FROM B WHERE ~
--ORDER BY ~
```
### 2.3 INTERSECT
- 두 개의 테이블에 대해 겹치는 부분을 추출하는 연산. 교집합
- 추출 후에는 중복된 결과를 제거
- Oracle/Maria Database에서는 지원되지만 MySQL에서는 지원되지 않음. JOIN 등을 활용해야 함.
```sql
SELECT a FROM A
INTERSECT
SELECT b FROM B;
```
### 2.4 EXCEPT(MINUS)
- 두 개의 테이블에서 겹치는 부분을 앞의 테이블에서 제외하여 추출하는 연산. 차집합
- 추출 후에는 중복된 결과를 제거
- Oracle Database에서는 지원 (MINUS로 지원), Maria Database에서는 10.3 version부터 EXCEPT 키워드로 지원
- MySQL에서는 지원되지 않음. JOIN 등을 활용해야 함.
```sql
SELECT a FROM A
EXCEPT
SELECT b FROM B;
```

