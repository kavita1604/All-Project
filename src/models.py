from django.db import models

# Create your models here
class Question(models.Model):
	#question_text is a 
	question_text = models.CharField(max_length = 150)
	date_published = models.DateTimeField('date published')

	def when_published_date(self):
		return self.date_published  >= (timezone.now() - datetime.timedelta(day = 1))


	def __str__(self):
		return self.question_text + " Created on" +str(self.date_published)



#Question & Answer is two tables but have no relation so we use ForeignKey
class Answer(models.Model):
	question = models.ForeignKey(Question)#when one to many re
	answer_text = models.CharField(max_length = 150)
	no_of_votes = models.IntegerField(default = 0)



	def __str__(self):
		return self.answer_text + " have "+ str(self.no_of_votes) + "Number of votes" +" belongs to question"+ str(self.question_id)