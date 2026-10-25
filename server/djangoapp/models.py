from django.db import models

class DealerReview(models.Model):
    dealer_id = models.IntegerField(db_index=True)
    reviewer = models.CharField(max_length=100)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for dealer {self.dealer_id} by {self.reviewer}"
