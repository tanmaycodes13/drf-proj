from django.db import models


class rating:
    RATING_CHOICES = (
        ("1", "Poor"),
        ("2", "Below Average"),
        ("3", "Good"),
        ("4", "Hit"),
        ("5", "Blockbuster"),
    )


class tv_series(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    detail = models.TextField()
    rating = models.CharField(max_length=1, choices=rating.RATING_CHOICES, default="3")
    creator = models.ForeignKey(
        "auth.User", related_name="tv_series", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["-id"]


class netflix_seires_model(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    detail = models.TextField()
    rating = models.CharField(max_length=1, choices=rating.RATING_CHOICES, default="3")
    creator = models.ForeignKey(
        "auth.User", related_name="netflix_series", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["-id"]
