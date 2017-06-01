class Router(object):
    """
    A router to control all database operations on models in the
    auth application.
    """


    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to rolodex.
        """
        
        if model._meta.app_label == 'rolodex':
            return 'rolodex_db'

        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write rolodex models go to rolodex.
        """
        if model._meta.app_label == 'rolodex':
            return 'rolodex_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if the two objects are from the same app
        """

        if obj1._meta.app_label == obj2._meta.app_label:
            return True

        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the auth app only appears in the 'auth'
        database.
        """
        if app_label == 'rolodex':
            return db == 'rolodex_db'
        else:
            return db == 'default'
            
        return None

