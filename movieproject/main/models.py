from django.db import models

class Movie(models.Model) :
    # 선택지
    ranks = [
        ('all','전체 관람가'),
        ('12','12세 이상 관람가'),
        ('15','15세 이상 관람가'),
        ('19','청소년 관람불가'),
    ]
    grades = [
        ('0.5','0.5'),
        ('1.0','1.0'),
        ('1.5','1.5'),
        ('2.0','2.0'),
        ('2.5','2.5'),
        ('3.0','3.0'),
        ('3.5','3.5'),
        ('4.0','4.0'),
        ('4.5','4.5'),
        ('5.0','5.0'),
    ]

    # 제목, 평점, 개봉 날짜, 상영 시간, 장르, 영상물 등급, 포스터 사진
    name = models.CharField(max_length = 30)
    grade = models.CharField(max_length = 10, choices = grades)
    pub_date = models.DateField()
    running_time = models.IntegerField(help_text = "시간 단위 : 분")
    category = models.CharField(max_length = 12)
    rank = models.CharField(max_length = 10, choices = ranks)
    image = models.FileField(upload_to = 'main/', null = True, blank = True)

    def __str__(self) :
        return self.name

        