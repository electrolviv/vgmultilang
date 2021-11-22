#!/usr/bin/python3

import sys
import os
import json
# import yaml

# Main resources object
#  '#ver'
#  'en' : []
#  'de' : []
#  'ru' : []


class ConverterClass:

    def __init__(self):
        self.jsrc = {}
        self.jtxtres = {}
        self.maxidx = 0


    # def ScanMaxLines(self) -> int:
    #     r = 0
    #     return r

    @staticmethod
    def loadfile(jfname : str) -> {}:
        """ Load JSON file """
        try:
            with open(jfname) as json_file:
                data = json.load(json_file)
                return data
        except BaseException as exc:
            print(exc)
        return {}


    def processFile(self, fname : str) -> (int, str):
        """ Conversion main function
        :param fname file to process
        :return: tuple - (errcode : int, errstr : str)
        """

        # Check file valid
        if not os.path.isfile(fname):
            errstr = "Invalid file : " + fname
            return 1, errstr

        print("Processing file : " + fname)

        self.jsrc = self.loadfile(fname)
        if not self.jsrc:
            return 2, "Not valid MLang .json file !"

        if '#ver' not in self.jsrc:
            return 3, "Invalid MLang version"

        if self.jsrc['#ver'] == 1.0:
            return self.processVer1P0(self.jsrc)

        return 100, "Invalid MLang version"

    def processVer1P0(self, jsrc : {}) -> (int, str):

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
                jres = self.jsrc[fld]
                for jj in jres:
                    if jj == 'idx':
                        idx = jres['idx'] if 'idx' in jres else idx + 1
                    else:
                        print(jres[jj])


        return 0, "Done"


if __name__ == "__main__":

    cwdstr = os.getcwd()
    print("Running from : " + cwdstr)

    # Check parameter : source .json file
    if len(sys.argv) < 2:
        print("vgmultilang.py <mlangfile.json>")
        exit(1)

    # Call process, report execution status
    cnvobj = ConverterClass()
    retcode, retstr = cnvobj.processFile(str(sys.argv[1]))
    print("*** Error! " + retstr if retcode else retstr)
    exit(retcode)


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
