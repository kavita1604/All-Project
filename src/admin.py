from django.contrib import admin
from src.models import Question , Answer

# Register your models here.

class AnswerInLine(admin.TabularInline):
	model = Answer
	extra = 2



class QuestionDisplay(admin.ModelAdmin):
	#fields=['date_published','question_text']
	fieldsets = [
	("Question Info", {'fields' : ['question_text']}),
	("Date Information", {'fields' : ['date_published']})
	]
	inlines = [AnswerInLine]
	search_fields = ['question_text']


admin.site.register(Question, QuestionDisplay)
# admin.site.register(Answer)


