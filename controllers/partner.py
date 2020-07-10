# -*- coding: utf-8 -*-


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def signup(self, values, token=None):
        """ signup a user, to either:
            - create a new user (no token), or
            - create a user for a partner (with token, but no user for partner), or
            - change the password of a user (with token, and existing user).
            :param values: a dictionary with field values that are written on user
            :param token: signup token (optional)
            :return: (dbname, login, password) for the signed up user
        """


    @api.model
    def _signup_create_user(self, values):
        """ signup a new user using the template user """



    def _create_user_from_template(self, values):
        """ create a new user using the template user """