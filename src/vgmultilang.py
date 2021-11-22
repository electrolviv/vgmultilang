#!/usr/bin/python3

import sys
import os
import json
# import yaml


def loadfile(jfname: str) -> {}:
    """ Load JSON file """
    try:
        with open(jfname) as json_file:
            data = json.load(json_file)
            return data
    except BaseException as exc:
        print(exc)
    return {}


class ConverterV1:
    """ Version 1.0

    JSON fields:
        #ver == 1.0
        #pfx * Optional, MStr_ as default
        en : []
        de : []
        .. : []
        ru : []

    """

    def __init__(self, j : {}):
        """body of constructor"""
        self.jsrc = j
        self.jtxtres = {}
        self.maxidx = 0

    def __del__(self):
        """body of destructor"""
        print("Saving objects")
        pass

    def process(self) -> (int, str):
        """ Conversion main function
        :return: tuple - (errcode : int, errstr : str)
        """

        # Scan Max Lines
        # self.maxidx = self.ScanMaxLines()
        langs = []
        pfx = "MStr"
        jsrc = self.jsrc
        idx = 0

        for fld in jsrc:
            if fld == "#ver":
                pass
            elif fld == "#pfx":
                pfx = jsrc["#pfx"]
            else:
                jres = jsrc[fld]
                for jj in jres:
                    if jj == 'idx':
                        idx = jres['idx'] if 'idx' in jres else idx + 1
                    else:
                        print(jres[jj])

        return 0, "Done"

# --------------------------------------------------------------------
if __name__ == "__main__":

    cwdstr = os.getcwd()
    print("Running from : " + cwdstr)

    # Check parameter : source .json file
    if len(sys.argv) < 2:
        print("vgmultilang.py <mlangfile.json>")
        exit(1)

    srcjfile = sys.argv[1]
    print("Processing file : " + srcjfile)

    # Check file valid
    if not os.path.isfile(srcjfile):
        print("Invalid file : " + srcjfile)
        exit(2)

    jcontent = loadfile(srcjfile)
    if not jcontent:
        print("Not valid MLang .json file !")
        exit(3)

    if '#ver' not in jcontent:
        print("Invalid MLang version")
        exit(4)

    if jcontent['#ver'] == 1.0:
        cnvobj = ConverterV1(jcontent)
        retcode, retstr = cnvobj.process()
        # Call process, report execution status
        print("*** Error! " + retstr if retcode else retstr)
        exit(retcode)
    else:
        print("Invalid MLang version")
        exit(100)


# from yaml import load, dump
# try:
#     from yaml import CLoader as Loader, CDumper as Dumper
# except ImportError:
#     from yaml import Loader, Dumper
#
# # ...
#
# data = load(stream, Loader=Loader)
#
# # ...
#
# output = dump(data, Dumper=Dumper)

# def ScanMaxLines(self) -> int:
#     r = 0
#     return r
# def processFile(self, fname : str) -> (int, str):
