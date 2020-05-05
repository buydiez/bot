import postgresql
db = postgresql.open('pq://postgres:'+'@localhost:5432/icq_bot')


"""
Запись по chatId
"""
def getMember(chatId:int):
	#print("GET MEMBER CHATID: " +  chatId)
	member = db.query('SELECT * FROM members WHERE "chatId" =' + "'752217372'")
	if member[0]:
		return member


"""
Проверка юзера
"""

def getMemberCheck(chatId: int):
	member = getMember(chatId)[0]
	if member["chatId"]:
		print(member)
		return False
	elif not "":
		print("-")
		return True

"""
Добавление нового юзера
"""

def setMember(chatId: int):
		insert_member = db.prepare("INSERT INTO members('chatId') VALUES ($1)")
		insert_result = insert_member(chatId)
		return insert_result


"""
Все юзеры
"""
def allMember():
	member = db.query('SELECT * FROM members')
	print(member[0]["chatId"])