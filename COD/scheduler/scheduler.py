from datetime import date, timedelta
from functools import partial
import pickle
from tkinter import *


class Scheduler:

    def __init__(self):
        self.day = date.today()

        self.root = Tk()
        self.root.title('스케줄러 프로그램')
        self.root.geometry('600x600+400+150')

        self._initialize()
        self._load_data()
        self.root.protocol("WM_DELETE_WINDOW", self._close_root)
        self.root.mainloop()

    def _initialize(self):
        self.day_lbl = Label(self.root, text=self.day)
        self.day_lbl.grid(row=1, column=1)

        self.todo = []
        self.index = 4

        add = Button(self.root, text='추가', width=5, command=self._add_click)
        add.grid(row=1, column=3, pady=5)

        add = Button(self.root, text='◀', width=3, command=self._before_day)
        add.grid(row=1, column=4, pady=5)

        add = Button(self.root, text='▶', width=3, command=self._next_day)
        add.grid(row=1, column=5, pady=5)

    def _add_click(self):
        self.index += 1
        i = self.index

        self.todo.append({'text': Entry(self.root)})
        self.todo[i - 5]['text'].grid(row=i, column=1, ipadx=100, ipady=5, padx=20, pady=3)

        complete = partial(self._button_complete, i - 5)
        self.todo[i - 5]['btn_complete'] = Button(self.root, text='수행중', width=5, command=complete)
        self.todo[i - 5]['btn_complete'].grid(row=i, column=3, padx=3)
        self.todo[i - 5]['is_complete'] = False

        delete = partial(self._button_delete, i - 5)
        self.todo[i - 5]['btn_delete'] = Button(self.root, text='삭제', width=5, command=delete)
        self.todo[i - 5]['btn_delete'].grid(row=i, column=4, padx=3)

    def _button_complete(self, num):
        todo = self.todo

        complete = partial(self._button_complete, num)
        if not todo[num]['is_complete']:
            todo[num]['text'].config(state=DISABLED)
            todo[num]['btn_complete'].destroy()
            todo[num]['btn_complete'] = Button(self.root, text='완료', width=5, command=complete)
            todo[num]['btn_complete'].grid(row=num + 5, column=3, padx=3)
            todo[num]['is_complete'] = True

        else:
            todo[num]['text'].config(state=NORMAL)
            todo[num]['btn_complete'].destroy()
            todo[num]['btn_complete'] = Button(self.root, text='수행중', width=5, command=complete)
            todo[num]['btn_complete'].grid(row=num + 5, column=3, padx=3)
            todo[num]['is_complete'] = False

    def _button_delete(self, num):
        self.index -= 1
        for a in self.todo[num].values():
            if not isinstance(a, bool):
                a.destroy()
        del self.todo[num]

    def _save_data(self):
        data = [[todo['text'].get(), todo['is_complete']] for todo in self.todo]
        with open('schedule_' + str(self.day), 'wb') as f:
            pickle.dump(data, f)

    def _load_data(self):
        try:
            with open('schedule_' + str(self.day), 'rb') as f:
                data_list = pickle.load(f)
        except:
            self._add_click()
            return
        self.index = 4

        for data in data_list:
            self.index += 1
            i = self.index
            self.todo.append({'text': Entry(self.root)})
            self.todo[i - 5]['text'].grid(row=i, column=1, ipadx=100, ipady=5, padx=20, pady=3)
            self.todo[i - 5]['text'].insert(0, data[0])
            self.todo[i - 5]['text'].config(state=DISABLED if data[1] else NORMAL)

            complete = partial(self._button_complete, i - 5)
            self.todo[i - 5]['btn_complete'] = Button(self.root, text='수행중' if not data[1] else '완료', width=5, command=complete)
            self.todo[i - 5]['btn_complete'].grid(row=i, column=3, padx=3)
            self.todo[i - 5]['is_complete'] = data[1]

            delete = partial(self._button_delete, i - 5)
            self.todo[i - 5]['btn_delete'] = Button(self.root, text='삭제', width=5, command=delete)
            self.todo[i - 5]['btn_delete'].grid(row=i, column=4, padx=3)

    def _before_day(self):
        self._save_data()

        for a in self.todo:
            for b in a.values():
                if not isinstance(b, bool):
                    b.destroy()
        del self.todo
        self.day -= timedelta(days=1)
        self.day_lbl.destroy()

        self._initialize()
        self._load_data()

    def _next_day(self):
        self._save_data()

        for a in self.todo:
            for b in a.values():
                if not isinstance(b, bool):
                    b.destroy()
        del self.todo
        self.day += timedelta(days=1)
        self.day_lbl.destroy()

        self._initialize()
        self._load_data()

    def _close_root(self):
        self._save_data()
        self.root.destroy()

Scheduler()