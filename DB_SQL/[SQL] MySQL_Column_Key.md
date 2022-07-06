## [MySQL] COLUMN KEY
MySQL에는 column key로 PRI, UNI, MUL이 있다.

### 1. PRI
PRI는 `Primary Key`로 주로 알고 있는 기본키이다. <br>
PRI를 설정하면, 해당 필드는 NOT NULL, UNIQUE 제약 조건의 특징을 가진다. <br>
If Key is PRI, the column is a PRIMARY KEY or is one of the columns in a multiple-column PRIMARY KEY. [MySQL 공식문서] 
### 2. UNI
UNI는 `Unique Key`로 고유 키를 의미한다. <br>
UNI를 설정하면, 해당 필드는 UNIQUE 제약 조건을 가진다. 즉, 중복된 값을 가질 수 없다. <br>
If Key is UNI, the column is the first column of a UNIQUE index. (A UNIQUE index permits multiple NULL values, but you can tell whether the column permits NULL by checking the Null field.) [MySQL 공식문서] 
### 3. MUL
MUL은 `Multiple Key`로 중복 가능한 컬럼을 나타낸다.  <br>
다른 테이블의 기본 키를 참조하는 외래키를 MUL로 표현한다. 여러 행이 동일한 값을 가질 수 있다. <br>
If Key is MUL, the column is the first column of a nonunique index in which multiple occurrences of a given value are permitted within the column. [MySQL 공식문서] 

### # 참고자료
- http://www.tcpschool.com/mysql/mysql_constraint_primaryKey
- https://www.wake-up-neo.com/ko/mysql/sql-%ED%82%A4-mul-%EB%8C%80-pri-%EB%8C%80-uni/971474861/amp/
- https://dev.mysql.com/doc/refman/8.0/en/show-columns.html
- https://velog.io/@hyoniii_log/DatabaseMySQL