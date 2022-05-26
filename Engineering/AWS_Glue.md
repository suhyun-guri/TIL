# 1. AWS Glue 개요


`keyword` : 간편, 유연하며 비용 효율적인, 완전 관리형, 서버리스, ETL 서비스, 개발자 친화적, Apache Spark 환경, Python과 Scala 코드 지원

AWS Glue는 까다롭고 시간이 많이 소요되는 데이터 검색, 변환, 작업 일정 조정 등과 같은 작업을 간소화 및 자동화하는 **종합 관리형 데이터 카탈로그 및 ETL(Extract, Transform, Load) 서비스**이다.

데이터 소스를 크롤링하고 CSV, Apache Parquet, JSON 등의 데이터 형식과 데이터 유형에 대해 사전 구축된 분류자를 사용하여 데이터 카탈로그를 생성한다.

<aside>
💡 **데이터 카탈로그 ?**

[https://www.tibco.com/ko/reference-center/what-is-a-data-catalog](https://www.tibco.com/ko/reference-center/what-is-a-data-catalog)


**메타데이터들을 모아 한눈에 여러 데이터들을 확인할 수 있도록 해주는 기능.**

즉, **사용자가 필요한 정보를 빠르게 찾을 수 있도록 하는 회사의 데이터 자산 목록이다.** 카탈로그는 대부분 다른 데이터에 대한 기본 정보를 제공하고 그것이 무엇인지 설명하는 메타 데이터이다.

데이터 카탈로그는 **데이터 관리의 핵심 요소**이며 데이터 카탈로그를 사용하여 분산적이어서 탐색하기 어려울 수 있는 조직의 전체 소스에서 필요한 데이터 자산을 검색한다.

- Glue에서는 Table이라는 이름으로 데이터 카탈로그가 존재하며, 저장된 모든 메타데이터들을 확인할 수 있다. 스키마 수정 등 메타데이터에 대한 간단한 작업을 할 수 있다.
</aside>

<aside>
💡 **메타데이터 ?**

- 데이터의 특성을 나타낸 것으로 크롤링된 데이터의 크기, 형식, 스키마 등으로 원본 데이터를 표현한 데이터이다.
- **데이터에 관한 구조화된 데이터로, 다른 데이터를 설명해주는 데이터를 의미한다.**
</aside>

AWS Glue 데이터 카탈로그는 Apache Hive 메타스토어와 호환되며 Hive, Presto, Apache Spark, Apache Pig 등 널리 사용되는 도구를 지원한다.

- 사용 편의성과 데이터 관리 기능을 지원하기 위해 다음의 확장 제공
    - 검색을 통해 데이터 찾기
    - 분류를 통해 파일 식별 및 구문 분석
    - 버전 관리를 통해 변화하는 스키마 관리

## 1-1. 장점

1. 보다 빠른 데이터 통합
    1. 조직 전체의 여러 그룹이 확장 가능한 ETL 워크플로우 실행 등의 **데이터 통합 작업을 함께 수행**
    2. → 시간 단축
2. 대규모 데이터 통합 자동화
    1. 데이터 통합에 필요한 많은 작업을 자동화
    2. 데이터 원본 크롤링, 데이터 형식 파악, 데이터 저장을 위한 스키마 제안
    3. 수천 개의 ETL 작업을 쉽게 실행 및 관리
    4. SQL을 사용하는 여러 데이터 저장소 간에 데이터 조합 및 복제 가능
3. 서버리스
    1. 관리할 인프라가 없으며 데이터 확장 작업을 실행하는 데 필요한 리소스를 프로비저닝, 구성 및 확장함.
    2. *프로비저닝(provisioning) : 사용자의 요구에 맞게 시스템 자원을 할당, 배치, 배포해 두었다가 필요시 시스템을 즉시 사용할 수 있는 상태로 미리 준비해두는 것을 의미.*
    3. 사용되는 리소스에 대해서만 비용을 지불 (pay-as-you-go 서비스)

## 1-2. Glue 관련 용어 (+AWS 관련 용어)

- Data Store
    - 데이터를 영구적으로 저장하기 위한 저장소 (Amazon S3 버킷 및 관계형 데이터베이스)
    - *버킷 : Amazon S3에 저장된 객체에 대한 컨테이너. S3에 데이터를 업로드하려면 우선 하나의 AWS 리전에 S3 버킷을 만들어야 한다. - `객체들을 그룹핑한 최상위 디렉토리`*
- 크롤러(Crawler)
    - 데이터 스토어(소스 또는 대상)에 연결하는 프로그램은 Classifier의 우선 순위 지정 목록을 통해 데이터의 스키마를 결정한 다음 AWS Glue Data Catalog에 메타데이터 테이블을 생성한다.
- 분류자(Classifier)
    - 데이터 스키마를 결정. 일반 파일 형식(CSV, JSON, XML 등)에 대한 분류자
- Glue Data Catalog
    - Glue의 영구적 메타데이터 스토어. 테이블 정의, 작업 정의 및 기타 관리 정보를 포함하여 AWS Glue 환경을 관리한다.
- Job
    - ETL 작업을 수행하는 데 필요한 비지니스 로직
    - 변환 스크립트 (Transform Script), Data Source, Data targets으로 구성
- Connection
    - 특정 데이터 스토어에 연결하는 데 필요한 속성을 포함하는 데이터 카탈로그 객체

---

- Amazon VPC(Virtual Private Cloud)
    - 논리적으로 격리된 가상의 네트워크. 사용자가 정의한 가상 네트워크로 AWS 리소스를 시작할 수 있다.
- AWS IAM (Identity and Access Management)
    - AWS 리소스에 대한 엑세스를 안전하게 제어할 수 있는 웹 서비스
    - IAM을 사용하여 리소스를 사용하도록 인증(로그인) 및 권한 부여된 대상을 제어한다.
- Amazon EC2(Elastic Compute Colud)
    - AWS에서 제공하는 클라우드 컴퓨팅 서비스.
    - AWS 클라우드에서 확장 가능 컴퓨팅 용량을 제공
    - 용량의 탄력성(늘리거나 줄일 수 있음), 사용한만큼 지불, 사용자가 인스턴스를 완전히 제어, 보안 및 네트워크 구성/스토리지 관리가 효과적
    

# 2. AWS Glue 구성요소

## 2-1. AWS Glue Console

AWS Glue 콘솔을 사용하여 ETL 워크플로우 정의 및 관리

- AWS Glue Data Catalog & AWS Glue Jobs system에서 API를 호출하여 다음 작업을 실행
    - jobs, tables, crawlers, and connections과 같은 AWS Glue 객체 정의
    - 크롤러가 실행되는 시간을 예약
    - 작업 트리거에 대한 이벤트/일정 정의
    - AWS Glue 객체 목록 검색 및 필터링
    - 변환 스크립트 편집

## 2-2. AWS Glue Data Catalog

AWS Glue Data Catalog는 AWS Cloud의 영구 기술 메타데이터 저장소이다.

[**데이터 카탈로그 ?**](https://www.notion.so/d6993d7b6afa41ceb56305bb00d502e1) 

## 2-3. AWS Glue Crawlers and Classifiers

크롤러를 사용하여 모든 종류의 레포에서 데이터를 스캔, 분류, 스키마 정보를 추출, 데이터 카탈로그에 메타데이터를 자동으로 저장할 수 있다. 그 다음 데이터 카탈로그를 사용하여 ETL 작업을 안내할 수 있다.

[Defining Crawlers](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)

## 2-4. AWS Glue ETL Operations

데이터 카탈로그의 메타데이터를 사용하여 다양한 ETL 작업을 수행하기 위해 AWS Glue 확장이 포함된 Scala or PySpark(Apache Spark용 Python API) 스크립트를 자동으로 생성할 수 있다.

ex)  raw data를 추출, 정리 및 변환한 다음 결과를 분석할 수 있는 다른 레포에 저장할 수 있다. 이러한 스크립트는 CSV 파일을 관계형 형식으로 변환하여 Amazon Redshift에 저장할 수 있다.

[Programming ETL Scripts](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming.html)

## 2-5. Streaming ETL in AWS Glue

지속적으로 실행되는 작업을 사용하여 스트리밍 데이터에서 ETL 작업을 수행할 수 있다.

## 2-6. The AWS Glue Jobs System

ETL 워크플로우를 조정하는 관리형 인프라를 제공.

데이터를 추출, 변환 및 다른 위치로 전송하는 데 사용하는 스크립트를 자동화하는 작업을 AWS Glue에서 생성할 수 있다. 작업을 예약 및 연결하거나 새 데이터 도착과 같은 이벤트에 의해 작업을 트리거할 수 있다.

# ?. Data Crawling

- ****[Hands On]AWS Glue Studio로 ETL작업 - Crawling 부분 참고****
    
    [[Hands On]AWS Glue Studio로 ETL작업](https://tech.cloud.nongshim.co.kr/2021/08/19/hands-on-aws-glue-studio-etl/)
    

Glue에서는 데이터를 직접 가져오는 것이 아닌, 데이터의 메타데이터만을 가져와서 데이터 카탈로그에 저장한다.

데이터의 메타데이터를 가져오는 작업은 Glue Crawler를 통해 할 수 있다.

# ?. Amazon S3 + AWS Glue → Data Lake

[Amazon S3 및 AWS Glue를 이용한 데이터 레이크 구축하기 | Amazon Web Services](https://aws.amazon.com/ko/blogs/korea/build-a-data-lake-foundation-with-aws-glue-and-amazon/)