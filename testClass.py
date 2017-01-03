class TWFather:
	LastName="徐"
	def Lang(self):
		return "我會說中文"
	def LangNative(self):
		return "也會說台語"

class TWMother:
	LastName="曹"
	def Lang(self):
		return "我會說國語"
	def LangNative(self):
		return "也會說閔南語"

class Childs(TWMother,TWFather):
	FirstName="小毅"
	def StudyNewLang(self):
		return "學新的語言"

people = Childs()

print("繼承:", people.Lang())
print("繼承:", people.LangNative())
print("繼承姓:", people.LastName)
print("屬於自己的名:",people.FirstName)
print("自己的特性:", people.StudyNewLang())
