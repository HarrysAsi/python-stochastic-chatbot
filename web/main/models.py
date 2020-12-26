from django.db import models

class Tag(models.Model):
    """
    Tag models actually describes the AI tags that the bot will categorize the data with
    """
    class Meta:
        db_table = 'tag'
        verbose_name = "tag"
        verbose_name_plural = "tags"

    name = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tag {self.name}"

class Question(models.Model):
    """ Question model represents the question-answer that the bot will trained with"""

    class Meta:
        db_table = "question"
        verbose_name = "question"
        verbose_name_plural = "questions"
    
    tags = models.ManyToManyField(Tag)
    question = models.TextField(blank=False, null=False)
    answer = models.TextField(blank=False, null=False)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def tags_as_str(self):
        return "-".join([t.name for t in self.tags.all()])

    def __str__(self):
        return f"Qstn: {self.question[:4]} \n Ansr: {self.answer[:4]}"
