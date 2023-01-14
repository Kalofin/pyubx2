"""
Helper, Property and Static method tests for pyubx2.UBXMessage

Created on 3 Oct 2020

*** NB: must be saved in UTF-8 format ***

@author: semuadmin
"""
# pylint: disable=line-too-long, invalid-name, missing-docstring, no-member

import os
import unittest

from pyubx2 import UBXMessage, UBXReader, UBX_CLASSES, POLL
import pyubx2.ubxtypes_core as ubt
import pyubx2.ubxtypes_get as ubg
import pyubx2.ubxtypes_set as ubs
import pyubx2.ubxtypes_poll as ubp
from pyubx2.ubxhelpers import (
    calc_checksum,
    isvalid_checksum,
    key_from_val,
    get_bits,
    itow2utc,
    gnss2str,
    dop2str,
    gpsfix2str,
    msgstr2bytes,
    val2bytes,
    bytes2val,
    cfgkey2name,
    cfgname2key,
    protocol,
    hextable,
    att2idx,
    att2name,
    deg2dms,
    deg2dmm,
    latlon2dms,
    latlon2dmm,
    ecef2llh,
    llh2ecef,
    haversine,
)


class StaticTest(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        dirname = os.path.dirname(__file__)
        self.streamNAV = open(os.path.join(dirname, "pygpsdata-NAV.log"), "rb")

    def tearDown(self):
        self.streamNAV.close()

    # def testDefinitions(self):  # DEBUG test for possible missing payload definitions
    #     for msg in ubt.UBX_MSGIDS.values():
    #         if (
    #             msg not in (ubp.UBX_PAYLOADS_POLL)
    #             and msg not in (ubg.UBX_PAYLOADS_GET)
    #             and msg not in (ubs.UBX_PAYLOADS_SET)
    #         ):
    #             print(f"Possible missing payload definition {msg}")
    #     for msg in ubg.UBX_PAYLOADS_GET:
    #         if msg not in ubt.UBX_MSGIDS.values():
    #             print(f"Possible missing core definition {msg} GET")
    #     for msg in ubs.UBX_PAYLOADS_SET:
    #         if msg not in ubt.UBX_MSGIDS.values():
    #             print(f"Possible missing core definition {msg} SET")
    #     for msg in ubp.UBX_PAYLOADS_POLL:
    #         if msg not in ubt.UBX_MSGIDS.values():
    #             print(f"Possible missing core definition {msg} POLL")

    def testFill_CFGMSG2(self):  # test msg_cls in bytes property
        EXPECTED_RESULT = "b'\\x06'"
        res = UBXMessage("CFG", "CFG-MSG", POLL, msgClass=240, msgID=5)
        self.assertEqual(str(res.msg_cls), EXPECTED_RESULT)

    def testFill_CFGMSG3(self):  # test msg_id in bytes property
        EXPECTED_RESULT = "b'\\x01'"
        res = UBXMessage("CFG", "CFG-MSG", POLL, msgClass=240, msgID=5)
        self.assertEqual(str(res.msg_id), EXPECTED_RESULT)

    def testFill_CFGMSG4(self):  # test msg length property
        # EXPECTED_RESULT = "b'\\x02\\x00'"
        EXPECTED_RESULT = 2
        res = UBXMessage("CFG", "CFG-MSG", POLL, msgClass=240, msgID=5)
        self.assertEqual(res.length, EXPECTED_RESULT)

    def testVal2Bytes(self):  # test conversion of value to bytes
        INPUTS = [
            (2345, ubt.U2),
            (2345, ubt.E2),
            (1, ubt.L),
            (-2346789, ubt.I4),
            (b"\x44\x55", ubt.X2),
            (23.12345678, ubt.R4),
            (-23.12345678912345, ubt.R8),
            ([1, 2, 3, 4, 5], "A005"),
        ]
        EXPECTED_RESULTS = [
            b"\x29\x09",
            b"\x29\x09",
            b"\x01",
            b"\xdb\x30\xdc\xff",
            b"\x44\x55",
            b"\xd7\xfc\xb8\x41",
            b"\x1f\xc1\x37\xdd\x9a\x1f\x37\xc0",
            b"\x01\x02\x03\x04\x05",
        ]
        for i, inp in enumerate(INPUTS):
            (val, att) = inp
            res = val2bytes(val, att)
            self.assertEqual(res, EXPECTED_RESULTS[i])

    def testBytes2Val(self):  # test conversion of bytes to value
        INPUTS = [
            (b"\x29\x09", ubt.U2),
            (b"\x29\x09", ubt.E2),
            (b"\x01", ubt.L),
            (b"\xdb\x30\xdc\xff", ubt.I4),
            (b"\x44\x55", ubt.X2),
            (b"\xd7\xfc\xb8\x41", ubt.R4),
            (b"\x1f\xc1\x37\xdd\x9a\x1f\x37\xc0", ubt.R8),
            (b"\x01\x02\x03\x04\x05", "A005"),
        ]
        EXPECTED_RESULTS = [
            2345,
            2345,
            1,
            -2346789,
            b"\x44\x55",
            23.12345678,
            -23.12345678912345,
            [1, 2, 3, 4, 5],
        ]
        for i, inp in enumerate(INPUTS):
            (valb, att) = inp
            res = bytes2val(valb, att)
            if att == ubt.R4:
                self.assertAlmostEqual(res, EXPECTED_RESULTS[i], 6)
            elif att == ubt.R8:
                self.assertAlmostEqual(res, EXPECTED_RESULTS[i], 14)
            else:
                self.assertEqual(res, EXPECTED_RESULTS[i])

    def testUBX2Bytes(self):
        res = msgstr2bytes("CFG", "CFG-MSG")
        self.assertEqual(res, (b"\x06", b"\x01"))

    def testKeyfromVal(self):
        res = key_from_val(UBX_CLASSES, "MON")
        self.assertEqual(res, (b"\x0A"))

    def testCalcChecksum(self):
        res = calc_checksum(b"\x06\x01\x02\x00\xf0\x05")
        self.assertEqual(res, b"\xfe\x16")

    def testGoodChecksum(self):
        res = isvalid_checksum(b"\xb5b\x06\x01\x02\x00\xf0\x05\xfe\x16")
        self.assertTrue(res)

    def testBadChecksum(self):
        res = isvalid_checksum(b"\xb5b\x06\x01\x02\x00\xf0\x05\xfe\x15")
        self.assertFalse(res)

    def testitow2utc(self):
        res = str(itow2utc(387092000))
        self.assertEqual(res, "11:31:14")

    def testgnss2str(self):
        GNSS = {
            0: "GPS",
            1: "SBAS",
            2: "Galileo",
            3: "BeiDou",
            4: "IMES",
            5: "QZSS",
            6: "GLONASS",
            7: "7",
        }
        for i in range(0, 8):
            res = gnss2str(i)
            self.assertEqual(res, GNSS[i])

    def testgps2str(self):
        fixs = ["NO FIX", "DR", "2D", "3D", "GPS + DR", "TIME ONLY"]
        for i, fix in enumerate(range(0, 6)):
            res = gpsfix2str(fix)
            self.assertEqual(res, fixs[i])

    def testdop2str(self):
        dops = ["Ideal", "Excellent", "Good", "Moderate", "Fair", "Poor"]
        i = 0
        for dop in (1, 2, 5, 10, 20, 30):
            res = dop2str(dop)
            self.assertEqual(res, dops[i])
            i += 1

    def testcfgname2key(self):
        (key, typ) = cfgname2key("CFG_NMEA_PROTVER")
        self.assertEqual(key, 0x20930001)
        self.assertEqual(typ, ubt.E1)
        (key, typ) = cfgname2key("CFG_UART1_BAUDRATE")
        self.assertEqual(key, 0x40520001)
        self.assertEqual(typ, ubt.U4)

    def testcfgkey2type(self):
        (key, typ) = cfgkey2name(0x20510001)
        self.assertEqual(key, "CFG_I2C_ADDRESS")
        self.assertEqual(typ, ubt.U1)

    def testgetbits(self):
        INPUTS = [
            (b"\x89", 192),
            (b"\xc9", 3),
            (b"\x89", 9),
            (b"\xc9", 9),
            (b"\x18\x18", 8),
            (b"\x18\x20", 8),
        ]
        EXPECTED_RESULTS = [2, 1, 9, 9, 1, 0]
        for i, (vb, mask) in enumerate(INPUTS):
            vi = get_bits(vb, mask)
            self.assertEqual(vi, EXPECTED_RESULTS[i])

    def testgetmsgmode(self):  # test msgmode getter
        EXPECTED_RESULT = 2
        res = UBXMessage("CFG", "CFG-MSG", POLL, msgClass=240, msgID=5)
        self.assertEqual(res.msgmode, EXPECTED_RESULT)

    def testdatastream(self):  # test datastream getter
        EXPECTED_RESULT = "<class '_io.BufferedReader'>"
        res = str(type(UBXReader(self.streamNAV).datastream))
        self.assertEqual(res, EXPECTED_RESULT)

    def testprotocol(self):  # test protocol() method
        res = protocol(b"\xb5b\x06\x01\x02\x00\xf0\x05\xfe\x16")
        self.assertEqual(res, ubt.UBX_PROTOCOL)
        res = protocol(b"$GNGLL,5327.04319,S,00214.41396,E,223232.00,A,A*68\r\n")
        self.assertEqual(res, ubt.NMEA_PROTOCOL)
        res = protocol(b"$PGRMM,WGS84*26\r\n")
        self.assertEqual(res, ubt.NMEA_PROTOCOL)
        res = protocol(b"\xd3\x00\x04L\xe0\x00\x80\xed\xed\xd6")
        self.assertEqual(res, ubt.RTCM3_PROTOCOL)
        res = protocol(b"aPiLeOfGarBage")
        self.assertEqual(res, 0)

    def testhextable(self):  # test hextable*( method)
        EXPECTED_RESULT = "000: 2447 4e47 4c4c 2c35 3332 372e 3034 3331  | b'$GNGLL,5327.0431' |\n016: 392c 532c 3030 3231 342e 3431 3339 362c  | b'9,S,00214.41396,' |\n032: 452c 3232 3332 3332 2e30 302c 412c 412a  | b'E,223232.00,A,A*' |\n048: 3638 0d0a                                | b'68\\r\\n' |\n"
        res = hextable(b"$GNGLL,5327.04319,S,00214.41396,E,223232.00,A,A*68\r\n", 8)
        self.assertEqual(res, EXPECTED_RESULT)

    def testatt2idx(self):  # test att2idx
        EXPECTED_RESULT = [4, 16, 101, 0]
        atts = ["svid_04", "gnssId_16", "cno_101", "gmsLon"]
        for i, att in enumerate(atts):
            res = att2idx(att)
            # print(res)
            self.assertEqual(res, EXPECTED_RESULT[i])

    def testatt2name(self):  # test att2name
        EXPECTED_RESULT = ["svid", "gnssId", "cno", "gmsLon"]
        atts = ["svid_04", "gnssId_16", "cno_101", "gmsLon"]
        for i, att in enumerate(atts):
            res = att2name(att)
            # print(res)
            self.assertEqual(res, EXPECTED_RESULT[i])

    def testdeg2dms(self):
        res = deg2dms(53.346, "LA")
        self.assertEqual(res, ("53°20′45.6″N"))
        res = deg2dms("xxx", "LA")
        self.assertEqual(res, "")

    def testdeg2dmm(self):
        res = deg2dmm(-2.5463, "LN")
        self.assertEqual(res, ("2°32.778′W"))
        res = deg2dmm("xxx", "LN")
        self.assertEqual(res, "")

    def testlatlon2dms(self):
        res = latlon2dms(53.346, -2.5463)
        self.assertEqual(res, ("53°20′45.6″N", "2°32′46.68″W"))

    def testlatlon2dmm(self):
        res = latlon2dmm(53.346, -2.5463)
        self.assertEqual(res, ("53°20.76′N", "2°32.778′W"))

    def testlatlon2dmm(self):
        res = latlon2dmm(53.346, -2.5463)
        self.assertEqual(res, ("53°20.76′N", "2°32.778′W"))

    def testecef2llh(self):
        vals = [
            (3822566.3113, -144427.5123, 5086857.1208),
            (3980570.0700029507, 0.0, 4966833.391498124),
            (10000, 10000, 10000),
        ]
        res = [
            (53.24168283407126, -2.1637695489854565, 214.97854665775156),
            (51.477928, 0, 0),
            (0, 0, -1.0e7),
        ]
        for i, val in enumerate(vals):
            lat, lon, alt = ecef2llh(val[0], val[1], val[2])
            self.assertAlmostEqual(lat, res[i][0], 7)
            self.assertAlmostEqual(lon, res[i][1], 7)
            self.assertAlmostEqual(alt, res[i][2], 7)

    def testllh2ecef(self):
        vals = [
            (53.24168283407126, -2.1637695489854565, 214.97854665775156),
            (51.477928, 0, 0),
        ]
        res = [
            (3822566.3113, -144427.5123, 5086857.1208),
            (3980570.0700029507, 0.0, 4966833.391498124),
        ]
        for i, val in enumerate(vals):
            x, y, z = llh2ecef(val[0], val[1], val[2])
            self.assertAlmostEqual(x, res[i][0], 7)
            self.assertAlmostEqual(y, res[i][1], 7)
            self.assertAlmostEqual(z, res[i][2], 7)

    def testllh2eceftab(self):  # test conversion there and back
        vals = [
            (53.24, -2.16, 214.98),
            (-7.48, 67.87, 43.12),
            (-34.51, -56.09, 1745.98),
            (90, 90, -435184.65),
            (0, 0, 0),
        ]
        for i, val in enumerate(vals):
            x, y, z = llh2ecef(val[0], val[1], val[2])
            lat, lon, alt = ecef2llh(x, y, z)
            self.assertAlmostEqual(lat, val[0], 2)
            self.assertAlmostEqual(lon, val[1], 2)
            self.assertAlmostEqual(alt, val[2], 2)

    def testhaversine(self):
        res = haversine(51.23, -2.41, 34.205, 56.34)
        self.assertAlmostEqual(res, 5010721.853179245, 4)
        res = haversine(-12.645, 34.867, 145.1745, -56.27846)
        self.assertAlmostEqual(res, 10715370.876703888, 4)
        res = haversine(53.45, -2.14, 53.451, -2.141)
        self.assertAlmostEqual(res, 129.56369376761418, 4)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
