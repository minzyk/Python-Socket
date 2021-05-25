import TFRD_RTU_OVER_TCP as Over_tcp
from modbus_tk import modbus_rtu_over_tcp
import modbus_tk.defines as cst
import threading
import pymysql


class Modbus:
    def __init__(self):
        self.connMB = modbus_rtu_over_tcp.RtuOverTcpMaster(host='192.168.0.45', port=502, timeout_in_sec=1)
        #self.connDB = Over_tcp.client()

        self.tableIndex = [
            'analog_input',
            'coil_output',
            'descret_input',
            'holding_input'
        ]

        self.idx_table = list()
        self.idx_column = list()

        for i in range(len(self.tableIndex)):
            self.idx_table.append(self.conv_table_index)
        # END

    def getData(self):
        self.get_data = self.connDB.execute(slave=1, function_code=cst.READ_HOLDING_REGISTERS, starting_address=0,
                                         quantity_of_x=10)
        # self.read_db = Over_tcp.read_input_data()
        print(self.get_data)

    #def setData(self):
    #    self.set_data = self.connDB.excute()


class Database:
    def __init__(self):
        self.connDB = pymysql.connect(
            host='192.168.0.117',
            port=3306,
            database='TFRD_2021_SNBD',
            user='admin',
            password='tf654321',
            charset='utf8'
        )

    def readDB(self, qry):
        read_db = self.connDB.cursor()
        read_db.execute(qry)

    def writeDB(self, qry):
        write_db = self.connDB.cursor()
        write_db.execute(qry)


class Main:
    def __init__(self):
        database = Database()
