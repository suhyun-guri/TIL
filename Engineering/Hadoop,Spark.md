# Hadoop?

- Hadoop은 **다수의 컴퓨터에서 대량의 데이터를 처리하기 위한 자바 기반의 오픈 소스 프레임워크**이다.
- 방대한 데이터를 저장해둘 스토리지와 데이터를 순차적으로 처리할 수 있는 구조가 필요하다. 이를 위해서는 수백 수천 대의 컴퓨터가 이용되어야 하며 이를 관리하는 것이 Hadoop이다.
- 구글에서 개발된 분산 처리 프레임워크인 MapReduce를 참고하여 제작되었다.
- SQL과 같은 쿼리 언어를 Hadoop에서 실행하기 위한 소프트웨어로 Hive가 개발되었다. Hive의 도입으로 프로그래밍 없이 데이터를 집계할 수 있게 함으로써 많은 사람이 사용할 수 있게 되었다.
### Hadoop의 분산처리 단계
하둡에서 분산처리를 위해 사용하는 기술인 MapReduce는 단계별로 데이터를 처리한다.
- 클러스터에서 데이터 읽기 -> 동작 실행 -> 클러스터에 결과 기록 -> 데이터 업데이트된 내용 읽기 -> 다음 동작 실행 -> 클러스터에 결과 기록
- 위와 같이 5단계에 걸쳐 데이터 처리를 진행한다. 

### Hadoop을 사용하는 이유?
- 기존의 관계형 데이터베이스 관리 시스템(RDBMS)는 비싼 비용이 든다. 그에 비해 하둡은 오픈소스로 비용이 거의 들지 않는다.
- 하둡은 분산 컴퓨팅 방식으로 구축 비용이 저렴하며 그 비용 대비 데이터 처리가 빠르다.
- 장애를 대비하여 매번 운영한 이후의 결과들을 디스크에 기록하기 때문에 문제가 발생했을 때, 기록된 결과들을 활용하여 문제를 파악하고 해결하기 쉽다.


# Apache Spark?
- Spark는 분산처리 시스템이며 오픈소스이다.
- 빠른 성능을 위해 인 메모리 캐싱과 최적화된 실행을 사용하고 일반 배치처리, 스트리밍 분석, 머신러닝, 그래프 데이터베이스 및 임시 쿼리를 지원한다.
- 하둡은 map함수가 모두 종료되어야 reduce 함수가 실행되며 성능 손실이 크다는 문제가 있다. map 함수의 결과가 디스크에 저장되고, 이를 reduce 함수가 다시 읽어오는 데에 있어서 성능 손실이 큰 것이다.
- 그러나 Spark는 map함수가 전부 종료되지 않았더라도 map의 결과를 스트리밍하는 방식으로, map의 결과가 다 나와야만 reduce를 수행한다는 전제를 깨버렸다.
- Spark는 초기 MapReduce의 성능 한계를 극복하고 하둡의 10배 빠른 속도를 보인다.
- but 하둡은 Spark가 제공하지 않는 HDFS와 같은 분산 파일 시스템을 제공하는 등 차이점이 있다. 스파크 자체가 하둡 기반으로 구동하는 것을 목적으로 만들어졌으므로 하둡 기반으로 돌아가는 것을 추천한다.

### Spark의 분산처리 단계
- 클러스터에서 데이터 읽기 -> 애널리틱스 운영 수행 및 결과값 클러스터 입력 동작과 같은 전 과정이 동시 진행
- Hadoop과 달리 2단계로 진행, 일반적인 상황에서 데이터 처리 속도가 Hadoop에 비해 훨씬 빠르다.

## Hadoop and Spark
- Hadoop은 데이터 일괄처리를 최선으로 하며 페타바이트급의 데이터를 저렴한 비용으로 저장 및 처리할 수 있다.
- Spark는 스트리밍 데이터로의 전환을 편리하게 할 수 있다는 장점이 있다.
- *Spark는 하둡과 쓰기 위해 개발되었기에 하둡과 함께 쓰면 더 좋다*




## References
- [Velog:하둡(hadoop)과 스파크(Spark)](https://velog.io/@cha-suyeon/%ED%95%98%EB%91%A1hadoop%EA%B3%BC-%EC%8A%A4%ED%8C%8C%ED%81%ACSpark)
- [Naver Blog:[빅데이터] 하둡(Hadoop)과 아파치 스파크(Spark) 파헤치기](https://m.blog.naver.com/acornedu/221083892521)