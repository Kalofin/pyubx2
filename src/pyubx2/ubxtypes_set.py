"""
UBX Protocol Input payload definitions

THESE ARE THE PAYLOAD DEFINITIONS FOR _SET_ MESSAGES _TO_ THE RECEIVER
(e.g. configuration and calibration commands; AssistNow payloads)

Created on 27 Sep 2020

Information sourced from u-blox Interface Specifications © 2013-2021, u-blox AG

:author: semuadmin
"""
# pylint: disable=too-many-lines, line-too-long

from pyubx2.ubxtypes_core import (
    I1,
    I2,
    I4,
    R4,
    R8,
    SCAL1,
    SCAL2,
    SCAL7,
    U1,
    U2,
    U3,
    U4,
    U5,
    U6,
    U7,
    U11,
    U12,
    U40,
    U64,
    X1,
    X2,
    X4,
    X24,
)
from pyubx2.ubxtypes_get import UBX_PAYLOADS_GET as UBX_GET

UBX_PAYLOADS_SET = {
    # AssistNow Aiding Messages: i.e. Ephemeris, Almanac, other A-GPS data input.
    # Messages in the AID class are used to send GPS aiding data to the receiver
    # AID messages are deprecated in favour of MGA messages in >=Gen8
    "AID-ALM": {"svid": U4, "week": U4, "optBlock": ("None", {"dwrd": U4})},
    "AID-ALP": {
        "group": (
            "None",
            {
                "alpData": U2,
            },
        ),
    },
    "ALP-ALPSRV": {
        "idSize": U1,
        "type": U1,
        "ofs": U2,
        "size": U2,
        "fileId": U2,
        "dataSize": U2,
        "id1": U1,
        "id2": U1,
        "id3": U1,
        "group": (
            "dataSize",
            {
                "data": U1,
            },
        ),
    },
    "AID-AOP": {"gnssId": U1, "svId": U1, "reserved1": U2, "data": U64},
    "AID-EPH": {
        "svid": U4,
        "how": U4,
        "optBlock": (
            "None",
            {
                "sf1d1": U4,
                "sf1d2": U4,
                "sf1d3": U4,
                "sf1d4": U4,
                "sf1d5": U4,
                "sf1d6": U4,
                "sf1d7": U4,
                "sf1d8": U4,
                "sf2d1": U4,
                "sf2d2": U4,
                "sf2d3": U4,
                "sf2d4": U4,
                "sf2d5": U4,
                "sf2d6": U4,
                "sf2d7": U4,
                "sf2d8": U4,
                "sf3d1": U4,
                "sf3d2": U4,
                "sf3d3": U4,
                "sf3d4": U4,
                "sf3d5": U4,
                "sf3d6": U4,
                "sf3d7": U4,
                "sf3d8": U4,
            },
        ),
    },
    "AID-HUI": {
        "health": X4,
        "utcA0": R8,
        "utcA1": R8,
        "utcTOW": I4,
        "utcWNT": I2,
        "utcLS": I2,
        "utcWNF": I2,
        "utcDNs": I2,
        "utcLSF": I2,
        "utcSpare": I2,
        "klobA0": R4,
        "klobA1": R4,
        "klobA2": R4,
        "klobA3": R4,
        "klobB0": R4,
        "klobB1": R4,
        "klobB2": R4,
        "klobB3": R4,
        "flags": X4,
    },
    "AID-INI": {
        "ecefXOrLat": I4,
        "ecefYOrLon": I4,
        "ecefZOrAlt": I4,
        "posAcc": U4,
        "tmCfg": X2,
        "wn": U2,
        "tow": U4,
        "towNs": I4,
        "tAccMs": U4,
        "tAccNs": U4,
        "clkDOrFreq": I4,
        "clkDAccOrFreqAcc": U4,
        "flags": X4,
    },
    # ********************************************************************
    # Configuration Input Messages: i.e. Set Dynamic Model, Set DOP Mask, Set Baud Rate, etc..
    # Messages in the CFG class are used to configure the receiver and read out current configuration values. Any
    # messages in the CFG class sent to the receiver are either acknowledged (with message UBX-ACK-ACK) if
    # processed successfully or rejected (with message UBX-ACK-NAK) if processing unsuccessfully.
    #
    # Most CFG-* GET & SET message payloads are identical, so reference
    # GET definitions here to avoid duplication
    "CFG-ANT": UBX_GET["CFG-ANT"],
    "CFG-BATCH": UBX_GET["CFG-BATCH"],
    "CFG-CFG": UBX_GET["CFG-CFG"],
    "CFG-DAT-NUM": {
        "datumNum": U2,
    },
    "CFG-DAT": {
        "majA": R8,
        "flat": R8,
        "dX": R4,
        "dY": R4,
        "dZ": R4,
        "rotX": R4,
        "rotY": R4,
        "rotZ": R4,
        "scale": R4,
    },
    "CFG-DGNSS": UBX_GET["CFG-DGNSS"],
    "CFG-DOSC": UBX_GET["CFG-DOSC"],
    "CFG-DYNSEED": UBX_GET["CFG-DYNSEED"],
    "CFG-EKF": UBX_GET["CFG-EKF"],
    "CFG-ESFALG": UBX_GET["CFG-ESFALG"],
    "CFG-ESFA": UBX_GET["CFG-ESFA"],
    "CFG-ESFG": UBX_GET["CFG-ESFG"],
    "CFG-ESFWT": UBX_GET["CFG-ESFWT"],
    "CFG-ESFGWT": UBX_GET["CFG-ESFGWT"],
    "CFG-ESRC": UBX_GET["CFG-ESRC"],
    "CFG-FIXSEED": UBX_GET["CFG-FIXSEED"],
    "CFG-FXN": UBX_GET["CFG-FXN"],
    "CFG-GEOFENCE": UBX_GET["CFG-GEOFENCE"],
    "CFG-GNSS": UBX_GET["CFG-GNSS"],
    "CFG-HNR": UBX_GET["CFG-HNR"],
    "CFG-INF": UBX_GET["CFG-INF"],
    "CFG-ITFM": UBX_GET["CFG-ITFM"],
    "CFG-LOGFILTER": UBX_GET["CFG-LOGFILTER"],
    "CFG-MSG": UBX_GET["CFG-MSG"],
    "CFG-NAV5": UBX_GET["CFG-NAV5"],
    "CFG-NAVX5": UBX_GET["CFG-NAVX5"],
    "CFG-NMEA": UBX_GET["CFG-NMEA"],
    "CFG-NMEAv0": UBX_GET["CFG-NMEAv0"],
    "CFG-NMEAvX": UBX_GET["CFG-NMEAvX"],
    "CFG-NVS": {
        "clearMask": (
            X4,
            {
                "reserved0": U12,
                "reserved1": U5,
                "alm": U1,
                "reserved2": U11,
                "aop": U1,
            },
        ),
        "saveMask": (
            X4,
            {
                "reserved3": U12,
                "reserved4": U5,
                "alm": U1,
                "reserved5": U11,
                "aop": U1,
            },
        ),
        "loadMask": (
            X4,
            {
                "reserved6": U12,
                "reserved7": U5,
                "alm": U1,
                "reserved8": U11,
                "aop": U1,
            },
        ),
        "deviceMask": (
            X1,
            {
                "devBBR": U1,
                "devFlash": U1,
                "devEEPROM": U1,
                "reserved9": U1,
                "devSpiFlash": U1,
            },
        ),
    },
    "CFG-ODO": UBX_GET["CFG-ODO"],
    "CFG-PM2": UBX_GET["CFG-PM2"],
    "CFG-PMS": UBX_GET["CFG-PMS"],
    "CFG-PRT": UBX_GET["CFG-PRT"],
    "CFG-PWR": UBX_GET["CFG-PWR"],
    "CFG-RATE": UBX_GET["CFG-RATE"],
    "CFG-RINV": UBX_GET["CFG-RINV"],
    "CFG-RST": {
        "navBbrMask": (
            X2,
            {
                "eph": U1,
                "alm": U1,
                "health": U1,
                "klob": U1,
                "pos": U1,
                "clkd": U1,
                "osc": U1,
                "utc": U1,
                "rtc": U1,
                "reserved2": U6,
                "aop": U1,
            },
        ),
        "resetMode": U1,
        "reserved0": U1,
    },
    "CFG-RXM": UBX_GET["CFG-RXM"],
    "CFG-SBAS": UBX_GET["CFG-SBAS"],
    "CFG-SENIF": UBX_GET["CFG-SENIF"],
    "CFG-SLAS": UBX_GET["CFG-SLAS"],
    "CFG-SMGR": UBX_GET["CFG-SMGR"],
    "CFG-SPT": UBX_GET["CFG-SPT"],
    "CFG-TMODE2": UBX_GET["CFG-TMODE2"],
    "CFG-TMODE3": UBX_GET["CFG-TMODE3"],
    "CFG-TP": UBX_GET["CFG-TP"],
    "CFG-TP5": UBX_GET["CFG-TP5"],
    "CFG-TXSLOT": UBX_GET["CFG-TXSLOT"],
    "CFG-USB": UBX_GET["CFG-USB"],
    "CFG-VALDEL": {
        "version": U1,  # = 0 no transaction, 1 with transaction
        "layers": (
            X1,
            {
                "reserved1": U1,
                "bbr": U1,
                "flash": U1,
            },
        ),
        "transaction": (  # if version = 1, else reserved
            X1,
            {
                "action": U2,
            },
        ),
        "reserved0": U1,
        "group": ("None", {"keys": U4}),  # repeating group
    },
    "CFG-VALSET": {
        "version": U1,  # = 0 no transaction, 1 with transaction
        "layers": (
            X1,
            {
                "ram": U1,
                "bbr": U1,
                "flash": U1,
            },
        ),
        "transaction": (  # if version = 1, else reserved
            X1,
            {
                "action": U2,
            },
        ),
        "reserved0": U1,
        "group": ("None", {"cfgData": U1}),  # repeating group
    },
    # ********************************************************************
    # External Sensor Fusion Messages: i.e. External Sensor Measurements and Status Information.
    # Messages in the ESF class are used to output external sensor fusion information from the receiver.
    # if calibTtagValid = 1; last dataField = calibTtag, numMeas = num of dataFields excluding calibTtag
    "ESF-MEAS": {
        "timeTag": U4,
        "flags": (
            X2,
            {
                "timeMarkSent": U2,
                "timeMarkEdge": U1,
                "calibTtagValid": U1,
                "reserved0": U7,
                "numMeas": U5,
            },
        ),
        "id": U2,
        "group": (
            "numMeas",
            {  # repeating group * numMeas
                "data": (
                    X4,
                    {
                        "dataField": X24,
                        "dataType": U6,
                    },
                ),
            },
        ),
    },
    # ********************************************************************
    # Logging Messages: i.e. Log creation, deletion, info and retrieval.
    # Messages in the LOG class are used to configure and report status information of the logging feature.
    "LOG-CREATE": {
        "version": U1,
        "logCfg": (
            X1,
            {
                "circular": U1,
            },
        ),
        "reserved0": U1,
        "logSize": U1,
        "userDefinedSize": U4,
    },
    "LOG-ERASE": {},
    "LOG-FINDTIME": {
        "version": U1,
        "type": U1,
        "year": U2,
        "month": U1,
        "day": U1,
        "hour": U1,
        "minute": U1,
        "second": U1,
        "reserved1": U1,
    },
    "LOG-RETRIEVE": {
        "startNumber": U4,
        "entryCount": U4,
        "version": U1,
        "reserved0": U3,
    },
    "LOG-RETRIEVEBATCH": {
        "version": U1,
        "flags": (
            X1,
            {
                "sendMonFirst": U1,
            },
        ),
        "reserved0": U2,
    },
    "LOG-STRING": {"group": ("None", {"bytes": U1})},  # repeating group
    # ********************************************************************
    # Multiple GNSS Assistance Messages: i.e. Assistance data for various GNSS.
    # Messages in the MGA class are used for GNSS aiding information from and to the receiver.
    "MGA-ANO": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "gnssId": U1,
        "year": U1,
        "month": U1,
        "day": U1,
        "reserved0": U1,
        "data": U64,
        "reserved1": U4,
    },
    "MGA-BDS-ALM": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved0": U1,
        "Wna": U1,
        "toa": [U1, 2**12],
        "deltaI": [I2, 2**-19],
        "sqrtA": [U4, 2**-11],
        "e": [U4, 2**-21],
        "omega": [I4, 2**-23],
        "M0": [I4, 2**-23],
        "Omega0": [I4, 2**-23],
        "omegaDot": [I4, 2**-38],
        "a0": [I2, 2**-20],
        "a1": [I2, 2**-38],
        "reserved1": U4,
    },
    "MGA-DBD": UBX_GET["MGA-DBD"],
    "MGA-BDS-EPH": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved0": U1,
        "SatH1": U1,
        "IODC": U1,
        "a2": [I2, 2**-66],
        "a1": [I4, 2**-50],
        "a0": [I4, 2**-33],
        "toc": [U4, 2**3],
        "TGD1": [I2, SCAL1],
        "URAI": U1,
        "IODE": U1,
        "toe": [U4, 2**3],
        "sqrtA": [U4, 2**-19],
        "e": [U4, 2**-33],
        "omega": [I4, 2**-31],
        "Deltan": [I2, 2**-43],
        "IDOT": [I2, 2**-43],
        "M0": [I4, 2**-31],
        "Omega0": [I4, 2**-31],
        "OmegaDot": [I4, 2**-43],
        "i0": [I4, 2**-31],
        "Cuc": [I4, 2**-31],
        "Cus": [I4, 2**-31],
        "Crc": [I4, 2**-6],
        "Crs": [I4, 2**-6],
        "Cic": [I4, 2**-31],
        "Cis": [I4, 2**-31],
        "reserved1": U4,
    },
    "MGA-BDS-HEALTH": {
        "type": U1,  # 0x04
        "version": U1,
        "reserved0": U2,
        "grouphealthcode": (
            30,
            {
                "healthCode": U2,
            },
        ),  # repeating group * 30
        "reserved1": U4,
    },
    "MGA-BDS-IONO": {
        "type": U1,  # 0x06
        "version": U1,
        "reserved0": U2,
        "alpha0": [I1, 2**-30],
        "alpha1": [I1, 2**-27],
        "alpha2": [I1, 2**-24],
        "alpha3": [I1, 2**-24],
        "beta0": [I1, 2**11],
        "beta1": [I1, 2**14],
        "beta2": [I1, 2**16],
        "beta3": [I1, 2**16],
        "reserved1": U4,
    },
    "MGA-BDS-UTC": {
        "type": U1,  # 0x05
        "version": U1,
        "reserved0": U2,
        "a0UTC": [I4, 2**-30],
        "a1UTC": [I4, 2**-50],
        "dtLS": I1,
        "reserved1": U1,
        "wnRec": U1,
        "wnLSF": U1,
        "dN": U1,
        "dtLSF": I1,
        "reserved2": U2,
    },
    "MGA-FLASH-DATA": {
        "type": U1,
        "version": U1,
        "sequence": U2,
        "size": U2,
        "group": ("size", {"data": U1}),  # repeating group * size
    },
    "MGA-FLASH-STOP": {"type": U1, "version": U1},
    "MGA-GAL-ALM": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved0": U1,
        "ioda": U1,
        "almWNa": U1,
        "toa": [U2, 600],
        "deltaSqrtA": [I2, 2**-9],
        "e": [U2, 2**-16],
        "deltaI": [I2, 2**-14],
        "omega0": [I2, 2**-15],
        "omegaDot": [I2, 2**-33],
        "omega": [I2, 2**-15],
        "m0": [I2, 2**-15],
        "af0": [I2, 2**-19],
        "af1": [I2, 2**-38],
        "healthE1B": U1,
        "healthE5b": U1,
        "reserved1": U4,
    },
    "MGA-GAL-EPH": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved0": U1,
        "iodNav": U2,
        "deltaN": [I2, 2**-43],
        "m0": [I4, 2**-31],
        "e": [U4, 2**-33],
        "sqrtA": [U4, 2**-19],
        "omega0": [I4, 2**-31],
        "i0": [I4, 2**-31],
        "omega": [I4, 2**-31],
        "omegaDot": [I4, 2**-43],
        "iDot": [I2, 2**-43],
        "cuc": [I2, 2**-29],
        "cus": [I2, 2**-29],
        "crc": [I2, 2**-5],
        "crs": [I2, 2**-5],
        "cic": [I2, 2**-29],
        "cis": [I2, 2**-29],
        "toe": [U2, 60],
        "af0": [I4, 2**-34],
        "af1": [I4, 2**-46],
        "af2": [I1, 2**-59],
        "sisaIndexE1E5b": U1,
        "toc": [U2, 60],
        "bgdE1E5b": I2,
        "reserved1": U2,
        "healthE1B": U1,
        "dataValidityE1B": U1,
        "healthE5b": U1,
        "dataValidityE5b": U1,
        "reserved2": U4,
    },
    "MGA-GAL-TIMEOFFSET": {
        "type": U1,
        "version": U1,
        "reserved0": U2,
        "a0G": [I2, 2**-35],
        "a1G": [I2, 2**-51],
        "t0G": [U1, 3600],
        "wn0G": U1,
        "reserved1": U2,
    },
    "MGA-GAL-UTC": {
        "type": U1,
        "version": U1,
        "reserved0": U2,
        "a0": [I4, 2**-30],
        "a1": [I4, 2**-50],
        "dtLS": I1,
        "tot": [U1, 3600],
        "wnt": U1,
        "wnLSF": U1,
        "dN": U1,
        "dTLSF": I1,
        "reserved1": U2,
    },
    "MGA-GLO-ALM": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved0": U1,
        "N": U2,
        "M": U1,
        "C": U1,
        "tau": [I2, 2**-18],
        "epsilon": [U2, 2**-20],
        "lambda": [I4, 2**-20],
        "deltaI": [I4, 2**-20],
        "tLambda": [U4, 2**-5],
        "deltaT": [I4, 2**-9],
        "deltaDT": [I1, 2**-14],
        "H": I1,
        "omega": I2,
        "reserved1": U4,
    },
    "MGA-GLO-EPH": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved0": U1,
        "FT": U1,
        "B": U1,
        "M": U1,
        "H": I1,
        "x": [I4, 2**-11],
        "y": [I4, 2**-11],
        "z": [I4, 2**-11],
        "dx": [I4, 2**-20],
        "dy": [I4, 2**-20],
        "dz": [I4, 2**-20],
        "ddx": [I1, 2**-30],
        "ddy": [I1, 2**-30],
        "ddz": [I1, 2**-30],
        "tb": [U1, 15],
        "gamma": [I2, 2**-40],
        "E": U1,
        "deltaTau": [I1, 2**-30],
        "tau": [I4, 2**-30],
        "reserved1": U4,
    },
    "MGA-GLO-TIMEOFFSET": {
        "type": U1,
        "version": U1,
        "N": U2,
        "tauC": [I4, 2**-27],
        "tauGps": [I4, 2**-31],
        "B1": [I2, 2**-10],
        "B2": [I2, 2**-16],
        "reserved0": U4,
    },
    "MGA-GPS-ALM": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "svHealth": U1,
        "e": [U2, 2**-21],
        "almWNa": U1,
        "toa": [U1, 2**12],
        "deltaI": [I2, 2**-19],
        "omegaDot": [I2, 2**-38],
        "sqrtA": [U4, 2**-11],
        "omega0": [I4, 2**-23],
        "omega": [I4, 2**-23],
        "m0": [I4, 2**-23],
        "af0": [I2, 2**-20],
        "af1": [I2, 2**-38],
        "reserved0": U4,
    },
    "MGA-GPS-EPH": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved0": U1,
        "fitInterval": U1,
        "uraIndex": U1,
        "svHealth": U1,
        "tgd": [I1, 2**-31],
        "iodc": U2,
        "toc": [U2, 2**4],
        "reserved1": U1,
        "af2": [I1, 2**-55],
        "af1": [I2, 2**-43],
        "af0": [I4, 2**-31],
        "crs": [I2, 2**-5],
        "deltaN": [I2, 2**-43],
        "m0": [I4, 2**-31],
        "cuc": [I2, 2**-29],
        "cus": [I2, 2**-29],
        "e": [U4, 2**-33],
        "sqrtA": [U4, 2**-19],
        "toe": [U2, 2**4],
        "cic": [I2, 2**-29],
        "omega0": [I4, 2**-31],
        "cis": [I2, 2**-29],
        "crc": [I2, 2**-5],
        "i0": [I4, 2**-31],
        "omega": [I4, 2**-31],
        "omegaDot": [I4, 2**-43],
        "idot": [I2, 2**-43],
        "reserved2": U4,
    },
    "MGA-GPS-HEALTH": {
        "type": U1,
        "version": U1,
        "reserved0": U2,
        "grouphealthcode": (
            32,
            {
                "healthCode": U1,
            },
        ),  # repeating group * 32
        "reserved1": U4,
    },
    "MGA-GPS-IONO": {
        "type": U1,
        "version": U1,
        "reserved0": U2,
        "ionoAlpha0": [I1, 2**-30],
        "ionoAlpha1": [I1, 2**-27],
        "ionoAlpha2": [I1, 2**-24],
        "ionoAlpha3": [I1, 2**-24],
        "ionoBeta0": [I1, 2**11],
        "ionoBeta1": [I1, 2**14],
        "ionoBeta2": [I1, 2**16],
        "ionoBeta3": [I1, 2**16],
        "reserved1": U4,
    },
    "MGA-GPS-UTC": {
        "type": U1,
        "version": U1,
        "reserved0": U2,
        "utcA0": [I4, 2**-30],
        "utcA1": [I4, 2**-50],
        "utcDtLS": I1,
        "utcTot": [U1, 2**12],
        "utcWNt": U1,
        "utcWNlsf": U1,
        "utcDn": U1,
        "utcDtLSF": I1,
        "reserved1": U2,
    },
    "MGA-INI-CLKD": {
        "type": U1,
        "version": U1,
        "reserved0": U2,
        "clkD": I4,
        "clkDAcc": U4,
    },
    "MGA-INI-EOP": {
        "type": U1,
        "version": U1,
        "reserved0": U2,
        "d2kRef": U2,
        "d2kMax": U2,
        "xpP0": [I4, 2**-30],
        "xpP1": [I4, 2**-30],
        "ypP0": [I4, 2**-30],
        "ypP1": [I4, 2**-30],
        "dUT1": [I4, 2**-25],
        "ddUT1": [I4, 2**-30],
        "reserved1": U40,
    },
    "MGA-INI-FREQ": {
        "type": U1,
        "version": U1,
        "reserved0": U1,
        "flags": (
            X1,
            {
                "source": U4,
                "fall": U1,
            },
        ),
        "freq": [I4, SCAL2],
        "freqAcc": U4,
    },
    "MGA-INI-POS-LLH": {
        "type": U1,
        "version": U1,
        "reserved0": U2,
        "lat": [I4, SCAL7],
        "lon": [I4, SCAL7],
        "alt": I4,
        "posAcc": U4,
    },
    "MGA-INI-POS-XYZ": {
        "type": U1,
        "version": U1,
        "reserved0": U2,
        "ecefX": I4,
        "ecefY": I4,
        "ecefZ": I4,
        "posAcc": U4,
    },
    "MGA-INI-TIME-GNSS": {
        "type": U1,
        "version": U1,
        "ref": (
            X1,
            {
                "source": U4,
                "fall": U1,
                "last": U1,
            },
        ),
        "gnssId": U1,
        "reserved0": U2,
        "week": U2,
        "tow": U4,
        "ns": U4,
        "tAccS": U2,
        "reserved1": U2,
        "tAccNs": U4,
    },
    "MGA-INI-TIME-UTC": {
        "type": U1,
        "version": U1,
        "ref": (
            X1,
            {
                "source": U4,
                "fall": U1,
                "last": U1,
            },
        ),
        "leapSecs": I1,
        "year": U2,
        "month": U1,
        "day": U1,
        "hour": U1,
        "minute": U1,
        "second": U1,
        "reserved0": U1,
        "ns": U4,
        "tAccS": U2,
        "reserved1": U2,
        "tAccNs": U4,
    },
    "MGA-QZSS-ALM": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "svHealth": U1,
        "e": [U2, 2**-21],
        "almWNa": U1,
        "toa": [U1, 2**12],
        "deltaI": [I2, 2**-19],
        "omegaDot": [I2, 2**-38],
        "sqrtA": [U4, 2**-11],
        "omega0": [I4, 2**-23],
        "omega": [I4, 2**-23],
        "m0": [I4, 2**-23],
        "af0": [I2, 2**-20],
        "af1": [I2, 2**-38],
        "reserved0": U4,
    },
    "MGA-QZSS-EPH": {
        "type": U1,
        "version": U1,
        "svId": U1,
        "reserved0": U1,
        "fitInterval": U1,
        "uraIndex": U1,
        "svHealth": U1,
        "tgd": [I1, 2**-31],
        "iodc": U2,
        "toc": [U2, 2**4],
        "reserved1": U1,
        "af2": [I1, 2**-55],
        "af1": [I2, 2**-43],
        "af0": [I4, 2**-31],
        "crs": [I2, 2**-5],
        "deltaN": [I2, 2**-43],
        "m0": [I4, 2**-31],
        "cuc": [I2, 2**-29],
        "cus": [I2, 2**-29],
        "e": [U4, 2**-33],
        "sqrtA": [U4, 2**-19],
        "toe": [U2, 2**4],
        "cic": [I2, 2**-29],
        "omega0": [I4, 2**-31],
        "cis": [I2, 2**-29],
        "crc": [I2, 2**-5],
        "i0": [I4, 2**-31],
        "omega": [I4, 2**-31],
        "omegaDot": [I4, 2**-43],
        "idot": [I2, 2**-43],
        "reserved2": U2,
    },
    "MGA-QZSS-HEALTH": {
        "type": U1,
        "version": U1,
        "reserved0": U2,
        "grouphealthcode": (
            5,
            {
                "healthCode": U1,
            },
        ),  # repeating group * 5
        "reserved1": U3,
    },
    # ********************************************************************
    # Navigation Results Messages: i.e. Position, Speed, Time, Acceleration, Heading, DOP, SVs used.
    # Messages in the NAV class are used to output navigation data such as position, altitude and velocity in a
    # number of formats. Additionally, status flags and accuracy figures are output. The messages are generated with
    # the configured navigation/measurement rate.
    "NAV-RESETODO": {},
    # ********************************************************************
    # Receiver Manager Messages: i.e. Satellite Status, RTC Status.
    # Messages in the RXM class are used to output status and result data from the Receiver Manager. The output
    # rate is not bound to the navigation/measurement rate and messages can also be generated on events.
    "RXM-PMP-V0": UBX_GET["RXM-PMP-V0"],
    "RXM-PMP-V1": UBX_GET["RXM-PMP-V1"],
    "RXM-PMREQ-S": {
        "duration": U4,
        "flags": (
            X4,
            {
                "reserved1": U1,
                "backup": U1,
            },
        ),
    },  # this appears to be a deprecated version
    "RXM-PMREQ": {
        "version": U1,  # 0x00
        "reserved0": U3,
        "duration": U4,
        "flags": (
            X4,
            {
                "reserved1": U1,
                "backup": U1,
                "force": U1,
            },
        ),
        "wakeupSources": (
            X4,
            {
                "reserved2": U3,
                "uartrx": U1,
                "reserved3": U1,
                "extint0": U1,
                "extint1": U1,
                "spics": U1,
            },
        ),
    },
    "RXM-QZSSL6": UBX_GET["RXM-QZSSL6"],
    "RXM-SPARTN-KEY": UBX_GET["RXM-SPARTN-KEY"],
    # ********************************************************************
    # Timing Messages: i.e. Time Pulse Output, Time Mark Results.
    # Messages in the TIM class are used to output timing information from the receiver, like Time Pulse and Time
    # Mark measurements.
    "TIM-HOC": {
        "version": U1,  # 0x00
        "oscId": U1,
        "flags": U1,
        "reserved1": U1,
        "value": [I4, 2**-8],
    },
    "TIM-SMEAS": UBX_GET["TIM-SMEAS"],
    "TIM-VCOCAL-V0": {  # stop calibration
        "type": U1,  # 0x00
    },
    "TIM-VCOCAL": {
        "type": U1,  # 0x02
        "version": U1,  # 0x00
        "oscId": U1,
        "srcId": U1,
        "reserved1": U2,
        "raw0": U2,
        "raw1": U2,
        "maxStepSize": U2,
    },
    # ********************************************************************
    # Firmware Update Messages: i.e. Memory/Flash erase/write, Reboot, Flash identification, etc..
    # Messages in the UPD class are used to update the firmware and identify any attached flash device.
    "UPD-SOS": {
        "cmd": U1,  # 0x00 to create backup in flash, 0x01 to clear backup
        "reserved0": U3,
    },
}
