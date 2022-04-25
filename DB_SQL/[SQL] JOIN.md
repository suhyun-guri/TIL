## 1. JOIN
- 두 개 이상의 테이블들을 연결 또는 결합하여 데이터를 출력하는 것
- 연산자에 따라 EQUI JOIN, Non EQUI JOIN로 분류

### 1.1 EQUI JOIN (등가 교집합)
- 두 개의 테이블 간에 **서로 정확하게 일치하는 경우**를 활용하는 조인
- 등가 연산자(=)를 사용한 조인을 의미
- 대부분 기본키-외래키 관계를 기반으로 발생하나, 모든 조인이 그런 것은 아니다.

### 1.1 Non EQUI JOIN (비등가 교집합)
- 두 개의 테이블 간에 **서로 정확하게 일치하지 않는 경우**를 활용하는 조인
- 등가 연산자 이외의 연산자들을 사용한 조인을 의미 (>, >=, <, <=, BETWEEN)


## 2. FROM절 JOIN 형태
### 2.1 INNER JOIN
- 내부 JOIN이라고 하며, JOIN 조건에서 동일한 값이 있는 행만 반환
- JOIN의 기본값으로 'INNER' 생략 가능

```sql
-- INNER JOIN구로 테이블 정의
SELECT * FROM TABLE1 [INNER] JOIN TABLE2
-- ON구를 사용해 조인 조건 지정
ON TABLE1.column = TABLE2.column;
```
- ON 조건절을 사용하면 칼럼명이 다르더라도 JOIN 조건을 사용 가능
- WHERE문을 사용하여 조건을 걸 수 있다.
### 2.2 USING
- 같은 이름을 가진 칼럼들 중 원하는 칼럼에 대해서만 선택적으로 틍가 조인 가능
- SQL Server에서는 지원 X
```sql
SELECT * FROM TABLE1 JOIN TABLE2
USING(기준칼럼);
-- USING 조건절 사용시에는 칼럼이나 테이블에 별칭을 붙일 수 없다.
```
- 여러 개 조인할 때
```sql
SELECT name, class_name, score_avg FROM student
INNER JOIN class USING(class_id)
INNER JOIN score USING(student_id);
```
### 2.3 NATURAL JOIN 
- 두 테이블 간의 **동일한 이름을 갖는 모든 칼럼들에 대해** 등가 조인을 수행
- 실무에서 많이 쓰이지는 않음
```sql
SELECT * FROM TABLE1 NATURAL JOIN TABLE2;
-- 추가로 ON 조건절이나 USING 조건절, WHERE절에서 JOIN 조건 정의 불가
```
<img src='../img/[SQL]JOIN.PNG' alt='natural_join'>

### 2.4 CROSS JOIN 
- JOIN 조건이 없는 경우 생길 수 있는 **모든 데이터의 조합을 조회**
```sql
SELECT * FROM student 
[CROSS] JOIN class;
-- CROSS 생략 가능
```
> INNER JOIN은 ON 또는 USING이 반드시 있어야 한다. <br> 만약 없다면 CROSS JOIN으로 간주된다.

<img src='../img/[SQL]JOIN2.PNG' alt='cross_join'>

### 2.5 OUTER JOIN 
- 두 개의 테이블 간에 교집합을 조회하고 한쪽 테이블에만 있는 데이터도 포함시켜서 조회한다.
- 빈 곳은 NULL 값으로 출력된다.
- WHERE 조건절에서 한쪽에만 있는 데이터를 포함시킬 테이블 쪽으로 (+)를 위치

```sql
-- WHERE 조건절 사용할 경우
SELECT * FROM student, class
WHERE student.class_id (+)= class.class_id;
```
- 표준 OUTER JOIN (LEFT, RIGHT, FULL)
```sql
--LEFT
SELECT * FROM student LEFT OUTER JOIN class
ON student.class_id = class.class_id;
--RIGHT
SELECT * FROM student RIGHT OUTER JOIN class
ON student.class_id = class.class_id;
--FULL
SELECT * FROM student FULL OUTER JOIN class
ON student.class_id = class.class_id;
```
- FULL OUTER JOIN은 Oracle에서만 쓰인다. MySQL, MariaDB의 경우 지원하지 않는다. 대신 UNION 연산자를 사용한다. (중복 데이터를 제거함)

### 2.6 SELF JOIN
- 동일 테이블 사이의 조인을 의미한다.
- 동일 테이블 사이의 조인을 수행하면 테이블과 칼럼 이름이 모두 같기 때문에 **식별을 위해 별칭이 필수이다.**

```sql
SELECT a.name, b.class
FROM student AS a, student AS b;
--예시
SELECT ALPHA.사원번호, ALPHA.관리자
FROM 직원 ALPHA, 직원 BETA
WHERE ALPHA.관리자 = BETA.사원번호;
```

