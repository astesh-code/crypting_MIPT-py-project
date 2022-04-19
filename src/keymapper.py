def key_map(in_fun):
    def g_args(self, key=None):
        if self.key==None:
            self.key = self.__gen_key__()
        if key==None:
            key = self.key
        return in_fun(self, key)
    g_args.__name__ = in_fun.__name__
    g_args.__doc__ = in_fun.__doc__
    g_args.__module__ = in_fun.__module__
    return g_args