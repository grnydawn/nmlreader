import os
import f90nml

from microapp import App

class NMLReader(App):
    _name_ = "nmlreader"
    _version_ = "0.1.1"
    _description_ = "Fortran namelist reader microapp"
    _long_description_ = "Fortran namelist reader microapp"
    _author_ = "Youngsung Kim"
    _author_email_ = "youngsung.kim.act2@gmail.com"

    def __init__(self, mgr):

        self.add_argument("nmlpath", help="Fortran namelist file")
        self.register_forward("namelist")

    def perform(self, args):

        nmlpath = args.nmlpath['_']
        if os.path.exists(nmlpath):
            self.add_forward(namelist=f90nml.read(nmlpath))

        else:
            raise Exception("'%s' does not exist." % nmlpath)
