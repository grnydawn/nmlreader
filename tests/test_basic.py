import os
from microapp import MicroappProject

here = os.path.dirname(os.path.abspath(__file__))

prj = MicroappProject()

def test_basic():

    rdr = os.path.join(here, "..", "nmlreader.py")
    nml = os.path.join(here, "..", "res", "e3sm_atm_in")
    cmd = "%s %s" % (rdr, nml)

    ret = prj.main(cmd)

    assert ret == 0
#
#def test_print(capsys):
#
#    cmd = "-- input @1 --forward '@x=2' -- print @x @data[0]"
#    ret = prj.main(cmd)
#
#    assert ret == 0
#
#    captured = capsys.readouterr()
#    assert captured.out == "21\n"
#    assert captured.err == ""
