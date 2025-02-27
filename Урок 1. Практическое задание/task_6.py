"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskBoard:
    def __init__(self):
        self.cur_queue = QueueClass()
        self.revision_queue = QueueClass()
        self.log = []

    def resolve_task(self):
        task = self.cur_queue.from_queue()
        self.log.append(task)

    def to_revision_task(self):
        task = self.cur_queue.from_queue()
        self.revision_queue.to_queue(task)

    def to_current_queue(self, item):
        self.cur_queue.to_queue(item)

    def from_revision(self):
        task = self.revision_queue.from_queue()
        self.cur_queue.to_queue(task)

    def current_task(self):
        return self.cur_queue.elems[len(self.cur_queue.elems) - 1]

    def current_revision(self):
        return self.revision_queue.elems[len(self.revision_queue.elems) - 1]


if __name__ == '__main__':
    task_board = TaskBoard()
    task_board.to_current_queue('Task1')
    task_board.to_current_queue('Task2')
    task_board.to_current_queue('Task3')
    print(task_board.cur_queue.elems)
    print(task_board.current_task())
