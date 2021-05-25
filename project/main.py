# -*- coding: utf-8 -*-

from mvc.model import Model
from mvc.view import View
from mvc.controller import Controller


if __name__ == '__main__':
    model = Model()
    view = View()
    controller = Controller(view, model)
    controller.parse_user_input()
