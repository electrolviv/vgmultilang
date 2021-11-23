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


class StringsArray:

    def __init__(self, defpfx='en'):
        self.pfx = defpfx
        self.arr = []

    def append(self, varprops : []):
        self.arr.append(varprops)


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

        # Source JSON
        self.jsrc = j
        # Output JSON
        self.jresult = {}

        self.curidx = 0
        self.pfx = "MStr"

        self.langs = []
        self.db = []


    def __del__(self):
        """body of destructor"""
        print("Saving objects")

    def process(self) -> (int, str):
        """ Conversion main function
        :return: tuple - (errcode : int, errstr : str)
        """

        # Scan Max Lines
        # self.maxidx = self.ScanMaxLines()
        jsrc = self.jsrc

        # first loop
        for varname in jsrc:
            if varname == "#ver":
                pass
            elif varname == "#pfx":
                self.pfx = jsrc["#pfx"]
            else:
                ret = self.insert(varname, jsrc[varname])
                if not ret:
                    return 5, f"Insert failed on variable '{varname}'"

        return 0, "Completed"

    def GetStringsBank(self, langpfx : str) -> StringsArray:
        dbidx = self.langs.index(langpfx)
        return self.db[dbidx]

    def insert(self, varname : str, j : {}) -> bool:

        for langpfx in j:
            if langpfx == 'idx':
                if j['idx'] < self.curidx:
                    return False
                self.curidx = j['idx']
            else:
                if langpfx not in self.langs:
                    self.langs.append(langpfx)
                    strarr = StringsArray(langpfx)
                    self.db.append(strarr)

                # Insert record into local dedicated db
                strarr = self.GetStringsBank(langpfx)
                strarr.append([varname, j[langpfx], self.curidx])

        self.curidx += 1

        return True

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
        print(("*** Error! " if retcode else "Done. ") + retstr)
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
