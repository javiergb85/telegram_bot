class Todo:
    def __init__(self, title) -> None:
        self.title = title
        self.is_completed = False

    def set_completed(self):
        self.is_completed = True

from Controllers.TodoController import TodoController
application.add_handler(CommandHandler("add", TodoController.add_todo ))
application.add_handler(CommandHandler("list", TodoController.list_todo ))
application.add_handler(CommandHandler("check", TodoController.check_todo ))
application.add_handler(CommandHandler("clear", TodoController.clear_todos ))