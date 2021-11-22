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
        self.jtxtres = {}
        self.maxidx = 0

    def ScanMaxLines(self):
        pass

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

        jcontent = self.loadfile(fname)
        if not jcontent:
            return 2, "Not valid MLang .json file !"

        for fld in jcontent:
            if fld == "#ver":
                pass
            elif fld == "#pfx":
                pass
            else:
                print(jcontent[fld])

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
